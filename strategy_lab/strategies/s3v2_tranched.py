"""s3v2_tranched: four S3v2 sub-books, each refreshed once a day at a different hour.

The book is the average of `tranches` sub-targets; sub-book i was last refreshed
i * spacing_bars ago (00/06/12/18 UTC with 4 x 6h on hourly bars). Run it with
rebalance_every_h = spacing (6): at every refresh the newest sub-book uses the current
closes, the others keep the targets of their own last refresh. Stateless: each sub-target
is recomputed from the closes as they were at its refresh time (window truncated).
Same maths per sub-book as s3v2x (params passed through).
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from lab.strategies import Strategy, get_strategy


class S3v2Tranched(Strategy):
    name = "s3v2_tranched"

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        p = dict(cfg or {})
        n, gap = int(p.pop("tranches", 4)), int(p.pop("spacing_bars", 6))
        base = get_strategy("s3v2x")
        acc = pd.Series(0.0, index=closes.columns)
        for i in range(n):
            win = closes.iloc[: len(closes) - i * gap] if i else closes
            acc = acc.add(pd.Series(base.target_weights(win, p)), fill_value=0.0)
        w = acc / n
        return self.check({k: float(v) for k, v in w.items()})
