"""s3v2x_regime: s3v2x (s3v2e) with point-in-time regime scaling (block 6 track B, variants_b6b_regime.yaml).

Regime inputs (lab/regime_hmm.py, walk-forward, data/regime/): for a target computed on the bar opening at day D hour h,
the HMM row of day D - 1 (complete daily data) and the correlation row of day D (window ending D - 1h) are used.
Declared mapping:
  short_scale_bull_eff = short_scale_bull + (1 - short_scale_bull) x p_crisis    (full shorts in a crisis, even in a bull)
  gross multiplier     = (1 - crisis_cut x p_crisis) x (1 + trend_boost x p_trend) x (corr_mult if the correlation state
                         is high and corr_filter)                               crisis_cut 0.5, trend_boost 0.25, corr_mult 0.7
  then gross > 1 is scaled to 1. Days before the first walk-forward fit (2020-08) use p = 0 (no change).
regime_hmm 0 (none), 2 or 3 states; corr_filter true / false.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from lab import ROOT
from lab.strategies import Strategy

_CACHE: dict[str, pd.DataFrame] = {}


def _load(name: str) -> pd.DataFrame:
    if name not in _CACHE:
        d = pd.read_csv(ROOT / "data" / "regime" / f"{name}.csv", index_col=0)
        d.index = pd.to_datetime(d.index, utc=True)
        _CACHE[name] = d
    return _CACHE[name]


class S3v2xRegime(Strategy):
    name = "s3v2x_regime"
    DEF = {"regime_hmm": 0, "corr_filter": False, "crisis_cut": 0.5, "trend_boost": 0.25, "corr_mult": 0.7}

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        from lab.strategies import get_strategy
        p = {**self.DEF, **(cfg or {})}
        day = closes.index[-1].floor("D")
        pc = pt = 0.0
        if int(p["regime_hmm"]):
            h = _load(f"hmm{int(p['regime_hmm'])}")
            prev = day - pd.Timedelta(days=1)
            if prev in h.index:
                pc, pt = float(h.at[prev, "p_crisis"]), float(h.at[prev, "p_trend"])
        base = {k: v for k, v in p.items() if k not in self.DEF}
        ssb = float(base.get("short_scale_bull", 0.5))
        base["short_scale_bull"] = ssb + (1 - ssb) * pc
        w = get_strategy("s3v2x").target_weights(closes, base)
        mult = (1 - float(p["crisis_cut"]) * pc) * (1 + float(p["trend_boost"]) * pt)
        if p["corr_filter"]:
            c = _load("corr")
            if day in c.index and bool(c.at[day, "high"]):
                mult *= float(p["corr_mult"])
        out = {a: v * mult for a, v in w.items()}
        g = sum(abs(v) for v in out.values())
        if g > 1:
            out = {a: v / g for a, v in out.items()}
        st = self.__dict__.setdefault("stats", {"decisions": 0, "mult_sum": 0.0, "corr_high": 0})
        st["decisions"] += 1
        st["mult_sum"] += mult
        return self.check(out)
