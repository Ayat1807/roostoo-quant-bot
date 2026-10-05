"""donchian_long: Zarattini-style Donchian channel ensemble, long-only, vol-scaled (lab only;
research block 3, definition fixed before running).

Daily closes = last hourly close of each complete UTC day in the window. For each lookback n in
`lookbacks` (days): enter when the close breaks above the highest close of the previous n days;
exit when it falls below the mid-channel ((max + min) / 2 of the previous n days), a trailing
stop. State is rebuilt by simulating over the window (stateless).
  signal_i = mean over lookbacks of state_n  (0..1)
  w_i      = signal_i * min(max_w, target_vol / vol_i) / n_divisor,
             vol_i = std of the last 90 daily returns x sqrt(365)
  sum(w) <= 1; columns in `no_trade` (e.g. BTCUSDT as a pure input) get weight 0.
Needs ~ max(lookbacks) + 1 days of history: lookback_bars 10000.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from lab.strategies import Strategy

DEFAULTS = {"lookbacks": [5, 10, 20, 30, 60, 90, 150, 250, 360], "target_vol": 0.5, "max_w": 0.30,
            "n_divisor": 10, "vol_days": 90, "no_trade": []}


def _states(x: np.ndarray, n: int) -> np.ndarray:
    """Long/flat state per column at the last day for lookback n (x: days x coins)."""
    T, A = x.shape
    st = np.zeros(A, dtype=bool)
    for t in range(n, T):
        win = x[t - n:t]
        hi, lo = np.nanmax(win, axis=0), np.nanmin(win, axis=0)
        px = x[t]
        st = np.where(st, ~(px < (hi + lo) / 2), px > hi)
        st &= ~np.isnan(px)
    return st


class DonchianLong(Strategy):
    name = "donchian_long"

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        p = {**DEFAULTS, **(cfg or {})}
        d = closes.resample("1D").last()
        if closes.index[-1].hour != 23:          # drop the current, incomplete day
            d = d.iloc[:-1]
        lbs = [int(n) for n in p["lookbacks"]]
        if len(d) < min(lbs) + 2:
            raise ValueError("not enough daily history")
        x = d.values.astype(float)
        sig = np.mean([_states(x, n) if len(d) > n else np.zeros(x.shape[1], bool) for n in lbs], axis=0)
        r = d.pct_change().iloc[-int(p["vol_days"]):]
        vol = (r.std() * np.sqrt(365)).values
        w = np.where(vol > 0, sig * np.minimum(float(p["max_w"]), float(p["target_vol"]) / vol), 0.0)
        w = np.nan_to_num(w) / float(p["n_divisor"])
        out = pd.Series(w, index=closes.columns)
        for a in p["no_trade"] or []:
            if a in out.index:
                out[a] = 0.0
        if out.sum() > 1:
            out = out / out.sum()
        return self.check({k: float(v) for k, v in out.items()})
