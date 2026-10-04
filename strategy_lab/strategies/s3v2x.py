"""s3v2x: S3v2 with two research knobs (lab only; identical to live s3v2 by default).

  n_divisor: null -> divide by N = number of pairs (live s3v2); an int (e.g. 10) keeps
             per-coin sizing fixed as the universe widens (20-30 coins).
  parking_asset: e.g. PAXGUSDT. Capital not allocated by the signal (1 - gross) is put
             into this asset (x parking_frac) instead of USD. It is excluded from the
             signal and the vol/N computation. PAXG = tokenised gold, listed on Roostoo.
Verified equal to s3v2 with defaults by tests/test_strategies.py.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from lab.strategies import Strategy, live

DEFAULTS = {**live.s3v2.DEFAULTS, "n_divisor": None, "parking_asset": None, "parking_frac": 1.0}


class S3v2x(Strategy):
    name = "s3v2x"

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        p = {**DEFAULTS, **(cfg or {})}
        park = p["parking_asset"]
        sig_cols = [c for c in closes.columns if c != park]
        c = closes[sig_cols].dropna(axis=1, how="any")
        horizons = tuple(p["horizons"])
        need = max(max(horizons), int(p["vol_win"]), int(p["regime_win"])) + 1
        if len(c) < need:
            raise ValueError(f"need {need} hourly bars, have {len(c)}")
        last = c.iloc[-1]
        sig = sum(np.sign(last / c.iloc[-1 - h] - 1) for h in horizons) / len(horizons)
        rv = c.pct_change().iloc[-int(p["vol_win"]):].std() * np.sqrt(24 * 365)
        n = int(p["n_divisor"]) if p["n_divisor"] else len(c.columns)
        raw = sig * (float(p["target_vol"]) / rv) / n
        btc = c[p["btc_pair"]]
        bull = btc.iloc[-1] > btc.iloc[-int(p["regime_win"]):].mean()
        raw = raw.where(raw >= 0, raw * (float(p["short_scale_bull"]) if bull else 1.0))
        raw = raw.clip(-float(p["max_w"]), float(p["max_w"]))
        g = raw.abs().sum()
        if g > 1:
            raw = raw / g
        w = raw.reindex(closes.columns).fillna(0.0)
        if park and park in closes.columns and pd.notna(closes[park].iloc[-1]):
            w[park] = float(p["parking_frac"]) * max(0.0, 1.0 - float(raw.abs().sum()))
        return self.check({k: float(v) for k, v in w.items()})
