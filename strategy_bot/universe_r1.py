"""R1 universe for a sleeve: the strategy_lab rule of trial b3_xsmom_r1, live and point-in-time.

On the first step of each UTC month (or at a start with no selection for the current month),
from data up to the last day of the previous month (`as_of`):
  pool      Roostoo crypto pairs that can trade (exchangeInfo), mapped to Binance COINUSDT
  history   >= min_history_days daily closes on Binance up to as_of
  liquidity mean daily quote volume over the last 30 days (Binance 1d klines, as_of inclusive)
            >= min_quote_volume_usd  (the lab's spread proxy)
  spread    live Roostoo spread <= max_spread_bps at selection time (live-only addition: no
            history exists, so the lab cannot apply it; set max_spread_bps: null to disable)
  select    the top n eligible pairs by that 30-day mean volume
The list is fixed for the month, saved to state/universe_r1.json with its dates, and every
selection is logged (decisions.jsonl "universe_reselect"). Verified against the lab's
Universe(rule R1) by tests/test_competition.py.
"""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any, Callable

import pandas as pd
import requests

from infra import append_log, write_json_atomic
from market_data import BINANCE_HOSTS, to_binance
from roostoo_client import num

log = logging.getLogger("strategy_bot.r1")
DAY_MS = 86_400_000

DEFAULTS = {"n": 15, "min_history_days": 90, "min_quote_volume_usd": 1.0e7, "max_spread_bps": 5.0,
            "lookback_days": 120}


def fetch_binance_daily(pair: str, end: pd.Timestamp, days: int = 120,
                        api_log: Path | None = None) -> pd.DataFrame | None:
    """Daily [close, quote_volume] from Binance 1d klines for the `days` UTC days before `end`
    (exclusive). None if the symbol is unknown or every host fails."""
    end_ms = int(end.timestamp() * 1000)
    params = {"symbol": to_binance(pair), "interval": "1d", "startTime": end_ms - days * DAY_MS,
              "endTime": end_ms - 1, "limit": 1000}
    for host in BINANCE_HOSTS:
        try:
            t0 = time.perf_counter()
            r = requests.get(f"{host}/api/v3/klines", params=params, timeout=10)
            if api_log:
                append_log({"ts": int(time.time() * 1000), "method": "GET",
                            "endpoint": f"{host.split('//')[1]}/api/v3/klines", "params": params,
                            "http_status": r.status_code,
                            "latency_ms": round((time.perf_counter() - t0) * 1000, 1)}, api_log)
            if r.status_code == 400:            # unknown symbol on Binance
                return None
            r.raise_for_status()
            k = r.json()
            if not k:
                return None
            idx = pd.to_datetime([x[0] for x in k], unit="ms", utc=True)
            df = pd.DataFrame({"close": [float(x[4]) for x in k],
                               "quote_volume": [float(x[7]) for x in k]}, index=idx)
            return df[~df.index.duplicated(keep="last")]
        except (requests.RequestException, ValueError) as exc:
            log.warning("binance daily %s %s failed: %s", host, pair, exc)
    return None


def select_r1(daily: dict[str, pd.DataFrame | None], as_of: pd.Timestamp, p: dict[str, Any],
              spread_bps: dict[str, float] | None = None) -> tuple[list[str], list[dict]]:
    """Pure selection (same rule as strategy_lab Universe type satellite, rule R1, crash_guard
    off, exclude_core off). Returns (selected pairs, table of every pool pair)."""
    rows = []
    for pair, d in daily.items():
        row: dict[str, Any] = {"pair": pair, "eligible": False}
        if d is None or d.empty:
            rows.append({**row, "why": "no Binance daily data"})
            continue
        d = d.loc[:as_of]
        if d.empty or d.index[-1] != as_of:
            rows.append({**row, "why": f"no Binance bar on {as_of:%Y-%m-%d}"})
            continue
        hist = int(d["close"].notna().sum())
        qv = d["quote_volume"].iloc[-30:]
        mqv = float(qv.mean()) if len(qv) == 30 and qv.notna().all() else float("nan")
        row.update(history_days=hist, mean_qv_30d=mqv)
        if hist < int(p["min_history_days"]):
            row["why"] = f"history {hist}d < {p['min_history_days']}d"
        elif not mqv == mqv:                     # NaN: fewer than 30 complete days
            row["why"] = "fewer than 30 days of volume"
        elif mqv < float(p["min_quote_volume_usd"]):
            row["why"] = f"30d volume ${mqv:,.0f} < ${float(p['min_quote_volume_usd']):,.0f}"
        elif spread_bps is not None and p.get("max_spread_bps") is not None \
                and spread_bps.get(pair, float("inf")) > float(p["max_spread_bps"]):
            row["why"] = f"Roostoo spread {spread_bps.get(pair, float('inf')):.1f} bps > {p['max_spread_bps']}"
        else:
            row["eligible"] = True
        rows.append(row)
    ok = sorted((r for r in rows if r["eligible"]), key=lambda r: r["mean_qv_30d"], reverse=True)
    selected = [r["pair"] for r in ok[: int(p["n"])]]
    for r in rows:
        r["selected"] = r["pair"] in selected
    return selected, rows


def spreads_from_ticker(tick: dict[str, Any], pairs: list[str]) -> dict[str, float]:
    out = {}
    for p in pairs:
        t = tick.get(p, {})
        bid, ask = num(t, "MaxBid"), num(t, "MinAsk")
        out[p] = (ask - bid) / ((ask + bid) / 2) * 1e4 if bid > 0 and ask > 0 else float("inf")
    return out


class R1Universe:
    """Monthly R1 selection with persistence; `members(now, tick)` returns the current list."""

    def __init__(self, pool: list[str], params: dict[str, Any], state_file: Path, logs: Any,
                 api_log: Path | None = None,
                 fetch: Callable[[str, pd.Timestamp, int], pd.DataFrame | None] | None = None) -> None:
        self.pool, self.p = list(pool), {**DEFAULTS, **(params or {})}
        self.state_file, self.logs, self.api_log = Path(state_file), logs, api_log
        self.fetch = fetch or (lambda pair, end, days: fetch_binance_daily(pair, end, days, api_log))
        self.state: dict[str, Any] = {}
        if self.state_file.exists():
            try:
                self.state = json.loads(self.state_file.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                self.state = {}

    def rule(self) -> dict[str, Any]:
        return {"type": "R1", **{k: self.p[k] for k in ("n", "min_history_days", "min_quote_volume_usd",
                                                         "max_spread_bps")}}

    def members(self, now: pd.Timestamp, tick: dict[str, Any] | None) -> list[str]:
        month = f"{now:%Y-%m}"
        if self.state.get("month") == month and self.state.get("rule") == self.rule() and self.state.get("selected"):
            return list(self.state["selected"])
        try:
            return self.reselect(now, tick)
        except Exception as exc:                 # keep the previous list; retry next step
            self.logs.error("universe_r1", exc)
            log.error("R1 re-selection failed (%s); keeping %s", exc, self.state.get("selected"))
            return list(self.state.get("selected") or [])

    def reselect(self, now: pd.Timestamp, tick: dict[str, Any] | None) -> list[str]:
        month_start = now.floor("D").replace(day=1)
        as_of = month_start - pd.Timedelta(days=1)
        daily = {p: self.fetch(p, month_start, int(self.p["lookback_days"])) for p in self.pool}
        if sum(d is not None for d in daily.values()) < 0.5 * len(self.pool):
            raise RuntimeError("Binance daily data missing for most of the pool")
        spreads = spreads_from_ticker(tick, self.pool) if tick and self.p.get("max_spread_bps") is not None else None
        selected, rows = select_r1(daily, as_of, self.p, spreads)
        prev = self.state.get("selected")
        self.state = {"month": f"{now:%Y-%m}", "as_of": str(as_of.date()), "selected_at": str(now),
                      "rule": self.rule(), "selected": selected,
                      "spread_bps": {p: round(v, 2) for p, v in (spreads or {}).items() if p in selected}}
        write_json_atomic(self.state_file, self.state)
        self.logs.write("decisions", {"event": "universe_reselect", "rule": self.rule(), "as_of": str(as_of.date()),
                                      "selected": selected, "previous": prev,
                                      "added": sorted(set(selected) - set(prev or [])),
                                      "removed": sorted(set(prev or []) - set(selected)),
                                      "table": [{k: (round(v, 2) if isinstance(v, float) else v) for k, v in r.items()}
                                                for r in rows]})
        log.info("R1 universe for %s (as of %s): %s", self.state["month"], as_of.date(), selected)
        return list(selected)
