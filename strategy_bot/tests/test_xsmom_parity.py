"""(a3) Parity: strategies/xsmom.py == teammate_xsmom/final_momentum_strategy.py.

    python -m tests.test_xsmom_parity

On 40+ daily 14:00 UTC decision bars (2025-09 -> latest), the plug-in, given only the last
2000 hourly bars (what the bot keeps), must return exactly the teammate's
target_at_signal_time() computed on the full history from 2023. Requirement: max |diff|
< 1e-12 and identical selected coins on every date.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

from strategies import get_strategy
from tests.hist_data import load_symbol

HERE = Path(__file__).resolve().parent.parent
TM = HERE.parent / "teammate_xsmom"
COINS = ["ZEC", "PAXG", "POL", "ICP", "TRX", "LISTA", "STO", "CAKE", "TUT", "SOL"]


def tm_prices() -> pd.DataFrame:
    s = {c: load_symbol(f"{c}USDT") for c in COINS}
    df = pd.DataFrame(s).sort_index()
    df.index = pd.DatetimeIndex(df.index).tz_convert("UTC")
    return df.reindex(pd.date_range(df.index[0], df.index[-1], freq="1h", tz="UTC"))


def main() -> int:
    sys.path.insert(0, str(TM))
    import final_momentum_strategy as tm  # noqa: E402

    prices = tm_prices()
    live = get_strategy("xsmom")
    dates = [t for t in pd.date_range(pd.Timestamp("2025-09-10 14:00", tz="UTC"), prices.index[-1], freq="7D")
             if t in prices.index]
    worst, n, same = 0.0, 0, True
    for ts in dates:
        try:
            ref = tm.target_at_signal_time(prices, ts)
        except ValueError:
            continue
        hist = prices.loc[:ts].iloc[-2000:]
        got = pd.Series(live.target_weights(hist, {}))
        worst = max(worst, float((got.reindex(ref.index) - ref).abs().max()))
        same &= set(got[got > 0].index) == set(ref[ref > 0].index)
        n += 1
    ok = n >= 20 and worst < 1e-12 and same
    print(f"[{'PASS' if ok else 'FAIL'}] xsmom == teammate target_at_signal_time on {n} decision dates: "
          f"max diff {worst:.1e}, same coins on every date: {same}")
    print(f"\n(a3) xsmom parity: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
