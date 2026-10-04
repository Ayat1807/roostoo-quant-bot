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
Always excluded from top_volume: tokenised stocks / non-crypto (config `exclude_assets`),
and assets with fewer than `min_history_days` of history (default 30).
"""

from __future__ import annotations

import re
from functools import lru_cache
from typing import Any

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

    def members(self, ts: pd.Timestamp, assets: list[str], alive) -> list[str]:
        if self.type in ("list", "roostoo_all"):
            return [a for a, ok in zip(assets, alive) if ok and a in self._list]
        day = ts.floor("D")
        mem = self._daily_members.get(day, []) if self._daily_members is not None else []
        alive_set = {a for a, ok in zip(assets, alive) if ok}
        m = [a for a in mem if a in alive_set]
        # BTC is always passed for the regime filter (s3v2 needs it); it trades only if a member
        if self.btc_asset not in m and self.btc_asset in alive_set:
            m = m + [self.btc_asset] if self.spec.get("always_include_btc", True) else m
        return m

    # ----- data --------------------------------------------------------- #
    def load_closes(self, start: pd.Timestamp, end: pd.Timestamp | None) -> pd.DataFrame:
        if self.type in ("list", "roostoo_all"):
            assets = list(self._list)
        else:
            self._daily_members = self._rank_table(start, end)
            assets = sorted({a for m in self._daily_members for a in m} | {self.btc_asset})
        return load_close(assets, str(start), str(end) if end else None)
