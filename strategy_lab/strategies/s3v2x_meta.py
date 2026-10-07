"""s3v2x_meta: s3v2e targets sized by the meta-label probability (block 6 track D, variants_b6d_meta.yaml).

At a daily decision (bar opening 00:00 UTC) each coin's s3v2e target is multiplied by m(p), p = the walk-forward,
out-of-sample calibrated probability that the position is profitable over the next 3 days net of costs (lab/meta.py,
data/meta/preds.csv). Coins / days without a prediction (before the first fit) keep m = 1.
  size_map p     m = p
  size_map edge  m = clip(2p - 1, 0, 1)   (no position unless p > 0.5)
Targets computed at other hours (frequency sweep) use the prediction of that day's 00:00 decision.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from lab import ROOT
from lab.strategies import Strategy

_P: dict = {}


def _preds() -> dict:
    if not _P:
        d = pd.read_csv(ROOT / "data" / "meta" / "preds.csv")
        d["time"] = pd.to_datetime(d["time"], utc=True)
        _P.update({(t, a): p for t, a, p in zip(d["time"], d["asset"], d["p"])})
    return _P


class S3v2xMeta(Strategy):
    name = "s3v2x_meta"
    DEF = {"size_map": "p"}

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        from lab.strategies import get_strategy
        p = {**self.DEF, **(cfg or {})}
        base = {k: v for k, v in p.items() if k not in self.DEF}
        w = get_strategy("s3v2x").target_weights(closes, base)
        day = closes.index[-1].floor("D")
        P = _preds()
        out = {}
        for a, v in w.items():
            pr = P.get((day, a))
            if v == 0 or pr is None:
                out[a] = v
                continue
            m = float(pr) if p["size_map"] == "p" else float(np.clip(2 * pr - 1, 0, 1))
            out[a] = v * m
        return self.check(out)
