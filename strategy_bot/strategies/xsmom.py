"""xsmom: fixed-clock 24h cross-sectional momentum (teammate's final strategy, ported exactly
from teammate_xsmom/final_momentum_strategy.py; verified by tests/test_xsmom_parity.py).

Decision once a day on the hourly bar that opens at `decision_hour_utc` (14:00 UTC; the bot
decides when that bar completes, i.e. at the first poll after 15:00 UTC, and trades on that
poll). From hourly closes (oldest first):
  fast  = EMA(span 24, adjust=False, min_periods 24), slow = EMA(span 168, ...)
  mom   = close / close 72 bars ago - 1
  vol   = std of the last 72 hourly returns
  ready = 168 non-missing closes in the last 168 bars
  eligible = fast > slow AND mom > 2% AND ready
  rank eligible coins by mom / vol (descending, ties by column order); top 5 get 15% each
  (max risky exposure 75%, the rest stays in cash). Long only.
The EMAs are recursive over the whole history passed in; the bot keeps 2000 bars, enough for
the start-up effect to vanish (0.988^2000 ~ 1e-11), so results equal the teammate's script.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from .base import Strategy

DEFAULTS: dict[str, Any] = {
    "fast_ema": 24,
    "slow_ema": 168,
    "momentum_hours": 72,
    "momentum_threshold": 0.02,
    "volatility_hours": 72,
    "top_n": 5,
    "max_asset_weight": 0.15,
    "max_risky_exposure": 0.75,
    "decision_hour_utc": 14,
}


def xsmom_weights(prices: pd.DataFrame, p: dict[str, Any]) -> pd.Series:
    """Target weights at the last row of `prices` (same maths as the teammate's
    build_momentum_targets / target_at_signal_time)."""
    returns = prices.pct_change(fill_method=None)
    fast = prices.ewm(span=int(p["fast_ema"]), adjust=False, min_periods=int(p["fast_ema"])).mean()
    slow = prices.ewm(span=int(p["slow_ema"]), adjust=False, min_periods=int(p["slow_ema"])).mean()
    mh = int(p["momentum_hours"])
    momentum = prices / prices.shift(mh) - 1.0
    volatility = returns.rolling(int(p["volatility_hours"])).std()
    ready = prices.rolling(int(p["slow_ema"])).count().eq(int(p["slow_ema"]))
    score = momentum / volatility.replace(0.0, np.nan)
    last = prices.index[-1]
    eligible = (fast.loc[last] > slow.loc[last]) & (momentum.loc[last] > float(p["momentum_threshold"])) \
        & ready.loc[last]
    ranked = score.loc[last].where(eligible).rank(ascending=False, method="first")
    w = (ranked <= int(p["top_n"])).astype(float) * float(p["max_asset_weight"])
    w = w.reindex(prices.columns).fillna(0.0)
    if w.sum() > float(p["max_risky_exposure"]) + 1e-12:
        raise ValueError("xsmom: risky exposure cap exceeded")
    return w


class XSMom(Strategy):
    name = "xsmom"

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        p = {**DEFAULTS, **(cfg or {})}
        need = max(int(p["slow_ema"]), int(p["momentum_hours"]) + 1, int(p["volatility_hours"]) + 1)
        if len(closes) < need:
            raise ValueError(f"xsmom needs {need} hourly bars, have {len(closes)}")
        w = xsmom_weights(closes, p)
        return self.check({k: float(v) for k, v in w.items()})
