"""Benchmarks: buy-and-hold BTC and equal-weight hold of the universe.

They go through the same backtester (costs, band, guard), so they are directly
comparable with real strategies.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from lab.strategies import Strategy


class HoldBTC(Strategy):
    name = "hold_btc"

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        btc = (cfg or {}).get("btc_pair", "BTCUSDT")
        return {c: (1.0 if c == btc else 0.0) for c in closes.columns}


class HoldEqualWeight(Strategy):
    name = "hold_ew"

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        live = [c for c in closes.columns if pd.notna(closes[c].iloc[-1])]
        return {c: (1.0 / len(live) if c in live else 0.0) for c in closes.columns}
