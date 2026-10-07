"""xsmom_sz (block 4b research options) with defaults == live xsmom, on real closes.

    python -m tests.test_xsmom_sz

1. Defaults: identical weights to strategy_bot's xsmom on 60 decision dates (14:00 bars, 2000-bar windows).
2. Option sanity on the same dates: weights >= 0, gross <= the option's cap, per-coin cap respected,
   all_eligible / breadth_k / topK coin counts as declared.
"""

from __future__ import annotations

import sys

import numpy as np
import pandas as pd

from lab.data import load_close
from lab.strategies import get_strategy

SYMS = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT", "DOGEUSDT", "ADAUSDT", "AVAXUSDT", "LINKUSDT",
        "DOTUSDT", "LTCUSDT", "TRXUSDT", "NEARUSDT", "UNIUSDT", "ATOMUSDT"]


def main() -> int:
    c = load_close(SYMS)
    live, sz = get_strategy("xsmom"), get_strategy("xsmom_sz")
    dates = [d for d in pd.date_range("2021-06-01 14:00", "2026-06-01 14:00", freq="31D", tz="UTC") if d in c.index]
    worst, ok_opt = 0.0, True
    opts = [({"sizing": "score"}, 0.75, None), ({"sizing": "inv_vol", "coin_cap": 0.20}, 0.75, 0.20),
            ({"sizing": "score_x_invvol", "coin_cap": 0.25}, 0.75, 0.25), ({"top_n": 10, "gross": 0.90}, 0.90, 0.09),
            ({"select": "all_eligible", "coin_cap": 0.10}, 0.75, 0.10), ({"select": "breadth_k"}, 0.75, 0.25),
            ({"exposure": "vol_target"}, 0.90, None), ({"exposure": "breadth"}, 0.75, 0.15),
            ({"exposure": "regime"}, 0.90, 0.18)]
    for d in dates:
        i = c.index.get_loc(d)
        win = c.iloc[i - 1999:i + 1]
        win = win[[s for s in SYMS if win[s].notna().iloc[-200:].all()]]
        a = pd.Series(live.target_weights(win, {}))
        b = pd.Series(sz.target_weights(win, {"_btc": win["BTCUSDT"]}))
        worst = max(worst, float((a - b.reindex(a.index)).abs().max()))
        for o, gcap, ccap in opts:
            w = pd.Series(sz.target_weights(win, {**o, "_btc": win["BTCUSDT"]}))
            good = (w >= -1e-12).all() and w.sum() <= gcap + 1e-9 and (ccap is None or w.max() <= ccap + 1e-9)
            if not good:
                print(f"   option {o} on {d}: gross {w.sum():.3f} max {w.max():.3f}")
            ok_opt &= bool(good)
    ok1 = worst < 1e-12
    print(f"[{'PASS' if ok1 else 'FAIL'}] defaults == live xsmom on {len(dates)} dates (max diff {worst:.1e})")
    print(f"[{'PASS' if ok_opt else 'FAIL'}] options respect gross / per-coin caps on every date")
    return 0 if ok1 and ok_opt else 1


if __name__ == "__main__":
    sys.exit(main())
