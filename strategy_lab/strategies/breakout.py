"""breakout: long-only Donchian channel breakout on closes (lab only; MFT, meant for 30m bars).

Per coin, from its closes (state rebuilt from the window each call, so it is stateless):
  entry  when close > highest close of the previous `entry_bars` bars
  exit   when close < lowest close of the previous `exit_bars` bars
  long   if the latest entry signal is more recent than the latest exit signal
Size, top_k set (team spec, like kadoo69's live design): of the coins in breakout state,
  hold the `top_k` with the highest return over the last `entry_bars` bars, equal weight
  1/top_k each (top_k=3 -> ~33% per position, gross <= 1).
Size, top_k null (trials 28-30 only, superseded): S3v2-style vol targeting,
  w = min(max_w, target_vol / vol) / n_divisor (max 3% per coin), then sum(w) <= 1.
Defaults on 30m bars: entry 96 bars (48h), exit 48 bars (24h), vol 336 bars (7d).
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from lab.strategies import Strategy

DEFAULTS = {"entry_bars": 96, "exit_bars": 48, "vol_win": 336, "target_vol": 0.40, "max_w": 0.30,
            "n_divisor": 10, "bars_per_year": 2 * 24 * 365, "top_k": None}


def _last_true(m: np.ndarray) -> np.ndarray:
    """Per column: index of the last True row, -1 if none."""
    n = m.shape[0]
    rev = np.argmax(m[::-1], axis=0)
    return np.where(m.any(axis=0), n - 1 - rev, -1)


class Breakout(Strategy):
    name = "breakout"

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        p = {**DEFAULTS, **(cfg or {})}
        ent, ext, vw = int(p["entry_bars"]), int(p["exit_bars"]), int(p["vol_win"])
        c = closes.dropna(axis=1, how="any")
        need = max(ent, ext, vw) + 2
        if len(c) < need:
            raise ValueError(f"need {need} bars, have {len(c)}")
        x = c.values
        hi = pd.DataFrame(x).rolling(ent).max().shift(1).values
        lo = pd.DataFrame(x).rolling(ext).min().shift(1).values
        long_ = _last_true(x > hi) > _last_true(x < lo)
        if p["top_k"]:
            k = int(p["top_k"])
            mom = np.where(long_, x[-1] / x[-1 - ent] - 1, -np.inf)
            pick = [j for j in np.argsort(-mom)[:k] if long_[j]]
            w = np.zeros(len(c.columns))
            w[pick] = 1.0 / k
            out = pd.Series(w, index=c.columns).reindex(closes.columns).fillna(0.0)
            return self.check({kk: float(v) for kk, v in out.items()})
        vol = c.pct_change().iloc[-vw:].std().values * np.sqrt(float(p["bars_per_year"]))
        w = np.where(long_, np.minimum(float(p["max_w"]), float(p["target_vol"]) / vol), 0.0)
        w = np.nan_to_num(w) / float(p["n_divisor"])
        if w.sum() > 1:
            w = w / w.sum()
        out = pd.Series(w, index=c.columns).reindex(closes.columns).fillna(0.0)
        return self.check({k: float(v) for k, v in out.items()})
