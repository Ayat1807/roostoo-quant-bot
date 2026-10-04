"""S3v2: low-turnover, volatility-targeted, multi-horizon time-series momentum.

Exact port of the reference prototype (`roostoo-bot/bot/strategy.py`), which is verified
against `research/strategies.py::tsmom_lt` by tests/test_parity.py:

  score  = mean over horizons h of sign(close_t / close_{t-h} - 1)   (numpy sign: sign(0)=0)
  vol    = std of hourly pct returns over the last `vol_win` bars x sqrt(24*365)
  raw    = score x (target_vol / vol) / N            (N = number of pairs in the universe)
  bull   = BTC close > mean of its last `regime_win` closes
  shorts (raw < 0) x short_scale_bull while bull     (applied BEFORE clipping)
  clip to +-max_w, then scale so that sum(|w|) <= 1

Only the function signature changed (config dict instead of keyword args); the math is
line-for-line the reference.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from .base import Strategy

DEFAULTS: dict[str, Any] = {
    "horizons": [24, 72, 168, 336],
    "vol_win": 336,
    "target_vol": 0.40,
    "short_scale_bull": 0.5,
    "max_w": 0.30,
    "btc_pair": "BTC/USD",
    "regime_win": 336,
}


def target_weights_series(close: pd.DataFrame, horizons=(24, 72, 168, 336), vol_win=336,
                          target_vol=0.40, short_scale_bull=0.5, max_w=0.30,
                          btc_col="BTC/USD", regime_win=336) -> pd.Series:
    """Reference implementation (unchanged). close: completed hourly closes."""
    c = close.dropna(axis=1, how="any")
    need = max(max(horizons), vol_win, regime_win) + 1
    if len(c) < need:
        raise ValueError(f"need {need} hourly bars, have {len(c)}")
    last = c.iloc[-1]
    sig = sum(np.sign(last / c.iloc[-1 - h] - 1) for h in horizons) / len(horizons)
    rv = c.pct_change().iloc[-vol_win:].std() * np.sqrt(24 * 365)
    raw = sig * (target_vol / rv) / len(c.columns)
    btc = c[btc_col]
    bull = btc.iloc[-1] > btc.iloc[-regime_win:].mean()
    raw = raw.where(raw >= 0, raw * (short_scale_bull if bull else 1.0))
    raw = raw.clip(-max_w, max_w)
    g = raw.abs().sum()
    if g > 1:
        raw = raw / g
    return raw.reindex(close.columns).fillna(0.0)


class S3v2(Strategy):
    name = "s3v2"

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        p = {**DEFAULTS, **(cfg or {})}
        w = target_weights_series(
            closes, horizons=tuple(p["horizons"]), vol_win=int(p["vol_win"]),
            target_vol=float(p["target_vol"]), short_scale_bull=float(p["short_scale_bull"]),
            max_w=float(p["max_w"]), btc_col=p["btc_pair"], regime_win=int(p["regime_win"]))
        return self.check({k: float(v) for k, v in w.items()})
