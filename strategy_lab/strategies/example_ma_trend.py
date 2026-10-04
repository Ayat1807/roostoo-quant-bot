"""EXAMPLE strategy for teammates: copy this file, rename the class and `name`, edit.

Long each coin whose price is above its N-hour moving average, flat otherwise,
equal weight across the coins that qualify. About as simple as a strategy gets.

Rules every strategy follows (see README "Add a strategy in 5 minutes"):
  * input: `closes`, hourly closes (rows = completed hours, oldest first, columns =
    asset names like 'BTCUSDT'); `cfg`: the run's `params` dict.
  * output: {asset: signed weight}; negative = short; sum(|w|) <= 1.
  * use only the data you are given (it already ends at the decision time: no look-ahead).
  * raise ValueError if there is not enough history yet (the backtester then stays flat).
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from lab.strategies import Strategy


class ExampleMATrend(Strategy):
    name = "example_ma_trend"

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        n = int((cfg or {}).get("ma_hours", 24 * 7))
        if len(closes) < n:
            raise ValueError(f"need {n} bars")
        c = closes.dropna(axis=1)                     # coins with a full window only
        above = c.iloc[-1] > c.iloc[-n:].mean()       # True/False per coin
        k = int(above.sum())
        w = {col: (1.0 / k if (k and above.get(col, False)) else 0.0) for col in closes.columns}
        return self.check(w)
