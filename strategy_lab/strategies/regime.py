"""regime_switch / regime_switch_cons (lab only; research block 3; thresholds FROZEN 2026-10-06
before any run). Mode set daily at the 00:00 UTC target refresh from data up to that bar:

  BTC above   = BTC close > mean of the last 720 hourly closes (30 days)
  BTC r14     = BTC close / close 336 bars ago - 1
  vol30       = std of the last 720 hourly BTC returns; its percentile vs the 365 daily
                samples before (the same quantity measured 24, 48, ... 8760 bars earlier)
  breadth     = alt_rally share (fraction of the top-50 liquid alts beating BTC over 30 days,
                lab/alt_rally.py) at the previous UTC day's close
  ATTACK  if BTC above AND r14 > +5% AND breadth > 60% AND vol30 below its 80th percentile:
          the top 3 tradable coins by vol-adjusted 14-day momentum (return over 336 bars /
          (hourly std over 336 bars x sqrt(336))), positive only, 0.30 each (gross 0.9)
  DEFEND  if BTC not above AND r14 < -5%: s3v2e (EWMA vol) at target_vol 0.6 with full shorts
          (short_scale_bull 1.0)
  BASE    otherwise: s3v2e at target_vol `base_tv` (0.6 regime_switch, 0.4 regime_switch_cons)
s3v2e components get the last 800 bars (same as the live bot). `no_trade` columns (BTCUSDT on
the alt10 universe) are inputs only. Needs lookback_bars >= 9500.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any

import numpy as np
import pandas as pd

from lab.strategies import Strategy, get_strategy

DEFAULTS = {"base_tv": 0.6, "defend_tv": 0.6, "attack_gross": 0.9, "attack_k": 3, "btc_pair": "BTCUSDT",
            "no_trade": [], "s3v2": {"horizons": [24, 72, 168, 336], "vol_win": 336, "regime_win": 336,
                                     "short_scale_bull": 0.5, "max_w": 0.30, "vol_method": "ewma",
                                     "ewma_halflife": 168}}


@lru_cache(maxsize=1)
def _breadth() -> pd.Series:
    from lab import ROOT
    f = pd.read_csv(ROOT / "reports" / "alt_rally.csv", index_col=0, parse_dates=True)["share"]
    f.index = pd.DatetimeIndex(f.index).tz_convert("UTC") if f.index.tz else pd.DatetimeIndex(f.index).tz_localize("UTC")
    return f


def mode_at(btc: pd.Series, ts: pd.Timestamp) -> str:
    """Regime mode from BTC hourly closes up to ts (inclusive) and the frozen breadth series."""
    b = btc.loc[:ts].dropna()
    if len(b) < 720 + 24 * 365 + 1:
        return "BASE"
    above = b.iloc[-1] > b.iloc[-720:].mean()
    r14 = b.iloc[-1] / b.iloc[-337] - 1
    r = b.pct_change()
    samples = [r.iloc[len(r) - 720 - 24 * k:len(r) - 24 * k].std() for k in range(0, 366)]
    now, past = samples[0], np.array(samples[1:])
    vol_ok = now < np.quantile(past, 0.80)
    br = _breadth().get(ts.floor("D") - pd.Timedelta(days=1), np.nan)
    if above and r14 > 0.05 and br > 0.60 and vol_ok:
        return "ATTACK"
    if (not above) and r14 < -0.05:
        return "DEFEND"
    return "BASE"


class RegimeSwitch(Strategy):
    name = "regime_switch"

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        p = {**DEFAULTS, **(cfg or {})}
        btc_col = p["btc_pair"]
        ts = closes.index[-1]
        mode = mode_at(closes[btc_col], ts)
        tradable = [c for c in closes.columns if c not in set(p["no_trade"] or [])]
        out = pd.Series(0.0, index=closes.columns)
        if mode == "ATTACK":
            c = closes[tradable].iloc[-337:].dropna(axis=1, how="any")
            score = (c.iloc[-1] / c.iloc[0] - 1) / (c.pct_change().std() * np.sqrt(336))
            top = score[score > 0].sort_values(ascending=False).index[: int(p["attack_k"])]
            out[list(top)] = float(p["attack_gross"]) / int(p["attack_k"])
        else:
            tv = float(p["defend_tv"] if mode == "DEFEND" else p["base_tv"])
            sp = {**p["s3v2"], "target_vol": tv, "btc_pair": btc_col, "no_trade": p["no_trade"],
                  "n_divisor": p.get("n_divisor")}
            if mode == "DEFEND":
                sp["short_scale_bull"] = 1.0
            w = get_strategy("s3v2x").target_weights(closes.iloc[-800:], sp)
            out = pd.Series(w).reindex(closes.columns).fillna(0.0)
        return self.check({k: float(v) for k, v in out.items()})
