"""s3v2x_fng: s3v2x (s3v2e) with the news layer's Fear & Greed rule (block 11): when the Crypto Fear & Greed value of the
target's day (alternative.me daily history, data/fng.csv; published at 00:00 UTC) is >= fng_high or <= fng_low, all
targets x fng_mult. Defaults off (fng_mult 1)."""

from __future__ import annotations

from typing import Any

import pandas as pd

from lab import ROOT
from lab.strategies import Strategy

_F: dict = {}


def _fng() -> pd.Series:
    if "s" not in _F:
        d = pd.read_csv(ROOT / "data" / "fng.csv")
        _F["s"] = pd.Series(d["value"].values, index=pd.to_datetime(d["date"], utc=True))
    return _F["s"]


class S3v2xFng(Strategy):
    name = "s3v2x_fng"
    DEF = {"fng_high": 85, "fng_low": 10, "fng_mult": 1.0}

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        from lab.strategies import get_strategy
        p = {**self.DEF, **(cfg or {})}
        w = get_strategy("s3v2x").target_weights(closes, {k: v for k, v in p.items() if k not in self.DEF})
        day = closes.index[-1].floor("D")
        v = _fng().get(day)
        st = self.__dict__.setdefault("stats", {"decisions": 0, "fng_fired": 0})
        st["decisions"] += 1
        if v is not None and (v >= p["fng_high"] or v <= p["fng_low"]):
            st["fng_fired"] += 1
            w = {a: x * float(p["fng_mult"]) for a, x in w.items()}
        return self.check(w)
