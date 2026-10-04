"""Strategy plug-in interface.

A strategy is a pure function of hourly closes -> signed target weights. It must not
touch the exchange, the clock or the filesystem, so it can be backtested, replayed and
unit-tested exactly as it runs live.

To add a strategy:
  1. create strategies/<name>.py with a subclass of Strategy,
  2. register it in strategies/__init__.py (STRATEGIES dict),
  3. set `strategy.name: <name>` and its params in config.yaml.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

import pandas as pd


class Strategy(ABC):
    """Base class for all strategies."""

    name: str = "base"

    @abstractmethod
    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        """Return {pair: signed weight} for the latest bar.

        closes: completed hourly closes, rows = hours (ascending, contiguous), cols = pairs.
        cfg:    the `strategy` section of config.yaml (strategy-specific params).
        Contract: weights are fractions of (capped) equity; negative = short;
        sum(|w|) <= 1; every column of `closes` appears in the result.
        """

    @staticmethod
    def check(weights: dict[str, float], tol: float = 1e-9) -> dict[str, float]:
        """Validate the contract above; raises ValueError on violation."""
        gross = sum(abs(w) for w in weights.values())
        if gross > 1 + tol:
            raise ValueError(f"gross exposure {gross:.6f} > 1")
        if any(pd.isna(w) for w in weights.values()):
            raise ValueError("NaN weight")
        return weights
