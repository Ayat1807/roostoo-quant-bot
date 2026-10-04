"""(a) Parity: live strategies/s3v2.py == reference research tsmom_lt on many dates.

    python -m tests.test_parity

The live strategy sees only the last 800 completed bars (what the bot holds); the
research version is computed on the full history with reb=1 (a fresh target every
hour). Requirement: max |diff| < 1e-9 on every date.
"""

from __future__ import annotations

import sys

import numpy as np
import pandas as pd

from strategies import get_strategy
from tests.hist_data import load_closes
from tests.reference import ref_strategies

CFG = {"horizons": [24, 72, 168, 336], "vol_win": 336, "target_vol": 0.40,
       "short_scale_bull": 0.5, "max_w": 0.30, "btc_pair": "BTC/USD", "regime_win": 336}


def main() -> int:
    c = load_closes()
    usdt = c.rename(columns=lambda x: x.replace("/USD", "USDT"))
    Wbt = ref_strategies.tsmom_lt({"close": usdt}, horizons=(24, 72, 168, 336), reb=1,
                                  short_scale_bull=0.5, target_vol=0.4)
    Wbt.columns = c.columns
    s3 = get_strategy("s3v2")

    # 40 monthly dates (00:00 UTC, as the live daily rebalance) + 12 random hours.
    dates = list(pd.date_range(pd.Timestamp("2023-03-01", tz="UTC"), c.index[-1], freq="30D"))
    rng = np.random.default_rng(7)
    dates += list(c.index[rng.integers(900, len(c), 12)])
    rows, worst = [], 0.0
    for ts in sorted(dates):
        live = pd.Series(s3.target_weights(c.loc[:ts].iloc[-800:], CFG))
        diff = float((live - Wbt.loc[ts]).abs().max())
        worst = max(worst, diff)
        rows.append((ts, diff, live.abs().sum(), int((live < 0).sum())))
    print(f"{'date (UTC)':<22}{'max|diff|':>11}{'gross':>8}{'shorts':>8}")
    for ts, d, g, ns in rows[:8] + [("...", np.nan, np.nan, 0)] + rows[-4:]:
        print(f"{str(ts)[:19]:<22}{d:>11.1e}{g:>8.3f}{ns:>8}")
    ok = worst < 1e-9
    print(f"\n(a) parity on {len(rows)} dates: max |live - reference| = {worst:.2e} "
          f"-> {'PASS' if ok else 'FAIL'} (< 1e-9)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
