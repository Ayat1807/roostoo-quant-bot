"""Universe selection for backtests. Asset names are Binance symbols ('BTCUSDT').

Spec (run config `universe:`):
  {type: list, assets: [BTCUSDT, ETHUSDT, ...]}
  {type: roostoo_all}           all Roostoo crypto pairs that have Binance history
  {type: top_volume, n: 20, lookback_days: 30, rank_pool: all|roostoo, trade: all|roostoo,
   reselect: daily|monthly, min_history_days: 60, min_quote_volume_usd: 5e6}
      On each selection day (every day, or the first day of each month), rank assets by
      mean daily quote volume over the previous `lookback_days` complete days (point in
      time, no look-ahead) among `rank_pool`, after the liquidity filter (mean daily
      volume >= min_quote_volume_usd; klines carry no spread, so volume is the liquidity
      proxy) and history filter; take the top n, then keep only those in `trade`.
      rank_pool=all, trade=roostoo is kadoo69's "rank on all Binance pairs, trade the
      Roostoo intersection".
  {type: satellite, rule: R1|R2|R3|R4, n_liquid: 15, k: 5, crash_guard: true, ...}
      Research block 2 satellite rules (team spec). Pool: Roostoo crypto pairs with Binance
      history, minus the 10 core coins and tokenised stocks. Re-selected on the 1st of each
      month from data up to the previous day:
        R1 top `n_liquid` by 30d mean daily dollar volume, >= `min_history_days` (90) of
           history, 30d mean volume >= min_quote_volume_usd (spread proxy: Binance klines
           carry no spread, so "spread <= 5 bps" is approximated by liquidity)
        R2 R1, then 30d annualised vol (daily returns) within vol_band [0.5, 1.3]
        R3 R1, then top k by 30d vol-adjusted return (ret30 / (daily std x sqrt(30)))
        R4 R1, then the k with the lowest 90d daily-return correlation to the core
           portfolio (equity of run `core_run`; >= 60 overlapping days required)
      R5 crash guard (crash_guard: true), checked daily from data up to the previous day:
        drop a coin > 40% below its 30d high, or with a pump signature in the last 7 days
        (day volume > 3x its prior 30d mean AND 3-day return > 30%), or < 90 days listed.
Always excluded from top_volume: tokenised stocks / non-crypto (config `exclude_assets`),
and assets with fewer than `min_history_days` of history (default 30).
"""

from __future__ import annotations

import re
from functools import lru_cache
from typing import Any

import numpy as np
import pandas as pd

from lab import load_config
from lab.data import load_close, load_daily
from lab.roostoo import binance_to_roostoo

ROOSTOO_10 = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT",
              "ADAUSDT", "DOGEUSDT", "AVAXUSDT", "LINKUSDT", "DOTUSDT"]
CFG = load_config()


@lru_cache(maxsize=1)
def _daily() -> dict[str, pd.DataFrame]:
    return load_daily()


@lru_cache(maxsize=1)
def stock_tokens() -> tuple[str, ...]:
    """Binance tokenised stocks/ETFs per config data.stock_tokens (not crypto)."""
    rule = CFG["data"].get("stock_tokens")
    if not rule:
        return ()
    close = _daily()["close"]
    first = close.apply(lambda s: s.first_valid_index())
    after = pd.Timestamp(rule["first_listed_after"], tz="UTC")
    return tuple(a for a in close.columns
                 if a.split("~")[0][:-4].endswith(rule["base_suffix"]) and first[a] >= after)


class Universe:
    def __init__(self, spec: dict[str, Any]) -> None:
        self.spec = dict(spec)
        self.type = spec.get("type", "list")
        self.btc_asset = "BTCUSDT"
        self._roostoo = binance_to_roostoo()
        excl = CFG["data"].get("exclude_assets_regex")
        self._excl = re.compile(excl) if excl else None
        self._daily_members: pd.Series | None = None
        if self.type == "satellite" and self.spec.get("rule") not in ("R1", "R2", "R3", "R4"):
            raise ValueError(f"satellite rule must be R1-R4, got {self.spec.get('rule')!r}")
        if self.type == "roostoo_all":
            have = set(_daily()["close"].columns)
            self._list = sorted(a for a in self._roostoo if a in have)
        else:
            self._list = list(spec.get("assets", []))

    def specs(self) -> dict[str, dict]:
        return self._roostoo

    # ----- membership --------------------------------------------------- #
    def _rank_table(self, start: pd.Timestamp, end: pd.Timestamp | None) -> pd.Series:
        """Day -> list of members, for top_volume universes."""
        s = self.spec
        d = _daily()
        qv, close = d["quote_volume"], d["close"]
        stocks = set(stock_tokens())
        cols = [a for a in qv.columns if a not in stocks and not (self._excl and self._excl.search(a))]
        if s.get("rank_pool", "all") == "roostoo":
            cols = [a for a in cols if a.split("~")[0] in self._roostoo and "~" not in a]
        qv = qv[cols]
        hist = close[cols].notna().cumsum()
        mean_qv = qv.rolling(int(s.get("lookback_days", 30)), min_periods=1).mean().shift(1)
        ok = (hist.shift(1) >= int(s.get("min_history_days", 30))) & close[cols].notna()
        ok &= mean_qv >= float(s.get("min_quote_volume_usd", 0))
        days = mean_qv.loc[start.floor("D") - pd.Timedelta(days=1):end.floor("D") if end else None].index
        out = {}
        monthly = s.get("reselect", "daily") == "monthly"
        cur_month, cur = None, []
        for day in days:
            if monthly and (day.year, day.month) == cur_month:
                out[day] = cur
                continue
            row = mean_qv.loc[day].where(ok.loc[day])
            top = list(row.dropna().sort_values(ascending=False).index[: int(s["n"])])
            if s.get("trade", "all") == "roostoo":
                top = [a for a in top if "~" not in a and a in self._roostoo]
            out[day] = top
            cur_month, cur = (day.year, day.month), top
        return pd.Series(out)

    def _sat_table(self, start: pd.Timestamp, end: pd.Timestamp | None) -> pd.Series:
        """Day -> satellite members (monthly selection minus daily crash-guard exclusions)."""
        s = self.spec
        d = _daily()
        close, qv = d["close"], d["quote_volume"]
        stocks = set(stock_tokens())
        core = set(ROOSTOO_10) if s.get("exclude_core", True) else set()
        pool = [a for a in close.columns if "~" not in a and a in self._roostoo
                and a not in core and a not in stocks]
        close, qv = close[pool], qv[pool]
        min_hist = int(s.get("min_history_days", 90))
        hist = close.notna().cumsum()
        mqv = qv.rolling(30, min_periods=30).mean()
        r1 = close.pct_change()
        vol30 = r1.rolling(30, min_periods=25).std()
        ret30 = close / close.shift(30) - 1
        core = None
        if s["rule"] == "R4":
            from lab.runner import load_hourly
            h = load_hourly(s.get("core_run", "b2_core"))
            if h is None:
                raise RuntimeError("R4 needs the core run's equity: run b2_core first")
            core = h["equity"].resample("1D").last().pct_change()
        # R5 inputs
        dd30 = close / close.rolling(30, min_periods=1).max() - 1
        pump = (qv > 3 * qv.shift(1).rolling(30, min_periods=20).mean()) & (close / close.shift(3) - 1 > 0.30)
        pump7 = pump.rolling(7, min_periods=1).max().astype(bool)
        days = close.loc[start.floor("D") - pd.Timedelta(days=1):end.floor("D") if end else None].index
        out, cur_month, sel = {}, None, []
        for day in days:
            prev = day - pd.Timedelta(days=1)
            if prev not in close.index:
                out[day] = []
                continue
            if (day.year, day.month) != cur_month:
                cur_month = (day.year, day.month)
                ok = (hist.loc[prev] >= min_hist) & mqv.loc[prev].notna()
                ok &= mqv.loc[prev] >= float(s.get("min_quote_volume_usd", 10e6))
                liq = list(mqv.loc[prev][ok].sort_values(ascending=False).index[: int(s.get("n_liquid", 15))])
                k = int(s.get("k", 5))
                if s["rule"] == "R1":
                    sel = liq
                elif s["rule"] == "R2":
                    lo, hi = s.get("vol_band", [0.5, 1.3])
                    v = vol30.loc[prev, liq] * np.sqrt(365)
                    sel = [a for a in liq if lo <= v[a] <= hi]
                elif s["rule"] == "R3":
                    score = (ret30.loc[prev, liq] / (vol30.loc[prev, liq] * np.sqrt(30))).dropna()
                    sel = list(score.sort_values(ascending=False).index[:k])
                else:
                    win = r1.loc[prev - pd.Timedelta(days=89):prev, liq]
                    cr = core.reindex(win.index)
                    corr = {a: win[a].corr(cr) for a in liq
                            if pd.concat([win[a], cr], axis=1).dropna().shape[0] >= 60}
                    sel = list(pd.Series(corr, dtype=float).dropna().sort_values().index[:k])
            m = sel
            if s.get("crash_guard", True):
                m = [a for a in sel if not (dd30.loc[prev, a] < -0.40 or pump7.loc[prev, a]
                                           or hist.loc[prev, a] < min_hist)]
            out[day] = m
        return pd.Series(out, dtype=object)

    def members(self, ts: pd.Timestamp, assets: list[str], alive) -> list[str]:
        if self.type in ("list", "roostoo_all"):
            return [a for a, ok in zip(assets, alive) if ok and a in self._list]
        day = ts.floor("D")
        mem = self._daily_members.get(day, []) if self._daily_members is not None else []
        alive_set = {a for a, ok in zip(assets, alive) if ok}
        m = [a for a in mem if a in alive_set]
        # BTC is always passed for the regime filter (s3v2 needs it); it trades only if a member
        if self.btc_asset not in m and self.btc_asset in alive_set:
            m = m + [self.btc_asset] if self.spec.get("always_include_btc", self.type != "satellite") else m
        return m

    # ----- data --------------------------------------------------------- #
    def load_closes(self, start: pd.Timestamp, end: pd.Timestamp | None,
                    interval: str = "1h", field: str = "close") -> pd.DataFrame:
        if self.type in ("list", "roostoo_all"):
            assets = list(self._list)
        else:
            self._daily_members = (self._sat_table(start, end) if self.type == "satellite"
                                   else self._rank_table(start, end))
            assets = sorted({a for m in self._daily_members for a in m} | {self.btc_asset})
        return load_close(assets, str(start), str(end) if end else None, interval, field)
