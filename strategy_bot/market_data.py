"""Hourly bar store (port of the reference bot/market_data.py).

Bootstraps `bootstrap_hours` of 1h closes per pair from Binance klines (USDT pairs as a
proxy for Roostoo USD pairs; live checks showed the prices match to <0.001%), then
appends one close per completed hour built from Roostoo ticker snapshots (last price
seen inside the hour). Bars are persisted to state/bars.csv so restarts are fast.

Changes vs the reference (behaviour-preserving):
* CSV instead of parquet (no pyarrow dependency on EC2; full float precision kept).
* The index is kept contiguous: if the bot misses whole hours (restart, network outage)
  the gap is forward-filled and logged. The strategy indexes bars by position
  (`iloc[-1 - h]`), so a gap would otherwise silently shift every horizon.
* Every Binance request is appended to logs/api_log.jsonl like Roostoo calls.
"""

from __future__ import annotations

import logging
import time
from pathlib import Path
from typing import Any

import pandas as pd
import requests

from infra import replace_with_retry
from roostoo_client import append_log

log = logging.getLogger("strategy_bot.data")
BINANCE_HOSTS = ["https://api.binance.com", "https://data-api.binance.vision"]
HOUR = pd.Timedelta(hours=1)
KEEP_ROWS = 2000  # reference keeps the last 2000 hourly bars


def to_binance(pair: str) -> str:
    """'BTC/USD' -> 'BTCUSDT'."""
    return pair.split("/")[0] + "USDT"


def fetch_binance_hourly(pair: str, hours: int = 800, api_log: Path | None = None,
                         now: pd.Timestamp | None = None) -> pd.Series | None:
    """Last `hours` completed 1h closes for `pair`, or None if every host fails."""
    now = now or pd.Timestamp.now(tz="UTC")
    end = int(now.timestamp() * 1000)
    start = end - hours * 3600 * 1000
    for host in BINANCE_HOSTS:
        try:
            rows: list[list[Any]] = []
            s = start
            while s < end:
                params = {"symbol": to_binance(pair), "interval": "1h", "startTime": s, "limit": 1000}
                t0 = time.perf_counter()
                r = requests.get(f"{host}/api/v3/klines", params=params, timeout=10)
                if api_log:
                    append_log({"ts": int(time.time() * 1000), "method": "GET",
                                "endpoint": f"{host.split('//')[1]}/api/v3/klines", "params": params,
                                "http_status": r.status_code,
                                "latency_ms": round((time.perf_counter() - t0) * 1000, 1)}, api_log)
                r.raise_for_status()
                k = r.json()
                if not k:
                    break
                rows += k
                s = k[-1][0] + 3600 * 1000
            idx = pd.to_datetime([x[0] for x in rows], unit="ms", utc=True)
            ser = pd.Series([float(x[4]) for x in rows], index=idx, name=pair)
            ser = ser[~ser.index.duplicated(keep="last")]
            return ser[ser.index < now.floor("h")]  # drop the still-forming candle
        except (requests.RequestException, ValueError) as exc:
            log.warning("binance %s %s failed: %s", host, pair, exc)
    return None


class BarStore:
    def __init__(self, pairs: list[str], path: Path, api_log: Path | None = None) -> None:
        self.pairs, self.path, self.api_log = list(pairs), Path(path), api_log
        self.close = pd.DataFrame(columns=self.pairs, dtype=float)
        self._hour_last: dict[str, float] = {}  # last ticker price seen within the current hour
        self._cur_hour: pd.Timestamp | None = None

    # ----- bootstrap ------------------------------------------------------- #

    def load_or_bootstrap(self, hours: int = 800, now: pd.Timestamp | None = None) -> None:
        if self.path.exists():
            df = pd.read_csv(self.path, index_col=0)
            df.index = pd.to_datetime(df.index, utc=True)
            self.close = df.astype(float)
        missing = [p for p in self.pairs
                   if p not in self.close.columns or self.close[p].dropna().shape[0] < hours // 2]
        for p in missing:
            s = fetch_binance_hourly(p, hours, self.api_log, now)
            if s is not None:
                self.close = self.close.reindex(self.close.index.union(s.index))
                self.close[p] = self.close.get(p, pd.Series(dtype=float)).combine_first(s)
            else:
                log.error("no history for %s from any Binance host", p)
        # If stored bars are stale (bot was down), top up recent hours for every pair.
        now = now or pd.Timestamp.now(tz="UTC")
        if len(self.close) and self.close.index[-1] < now.floor("h") - HOUR:
            gap_h = int((now.floor("h") - self.close.index[-1]) / HOUR) + 2
            log.info("stored bars end %s; topping up %d hours", self.close.index[-1], gap_h)
            for p in self.pairs:
                s = fetch_binance_hourly(p, gap_h, self.api_log, now)
                if s is not None:
                    self.close = self.close.reindex(self.close.index.union(s.index))
                    self.close[p] = s.combine_first(self.close[p])
        self.close = self._contiguous(self.close[self.pairs].sort_index()).iloc[-KEEP_ROWS:]
        self.save()
        log.info("bars loaded: %d rows x %d pairs, last bar %s", *self.close.shape,
                 self.close.index[-1] if len(self.close) else None)

    # ----- live updates ---------------------------------------------------- #

    def on_ticker(self, now: pd.Timestamp, prices: dict[str, float]) -> bool:
        """Call every poll with Roostoo LastPrice per pair. Returns True when an hour completed."""
        hour = now.floor("h")
        closed = False
        if self._cur_hour is not None and hour > self._cur_hour and self._hour_last:
            row = pd.DataFrame([self._hour_last], index=[self._cur_hour])
            self.close = pd.concat([self.close[~self.close.index.isin(row.index)], row]).sort_index()
            self.close = self._contiguous(self.close).iloc[-KEEP_ROWS:]
            self.save()
            closed = True
        if self._cur_hour is None or hour > self._cur_hour:
            self._cur_hour, self._hour_last = hour, {}
        self._hour_last.update({p: v for p, v in prices.items() if p in self.pairs})
        return closed

    def _contiguous(self, df: pd.DataFrame) -> pd.DataFrame:
        if df.empty:
            return df
        full = pd.date_range(df.index[0], df.index[-1], freq="1h", tz="UTC")
        if len(full) != len(df):
            log.warning("bar gap: %d missing hours forward-filled", len(full) - len(df))
            df = df.reindex(full).ffill()
        return df

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        self.close.to_csv(tmp)
        replace_with_retry(tmp, self.path)
