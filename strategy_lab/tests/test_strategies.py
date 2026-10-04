"""Strategy plug-in checks (offline, uses the lab cache).

    python -m tests.test_strategies

* every registered strategy returns a valid weight dict on real data (gross <= 1)
* s3v2x with default knobs == live s3v2 exactly (max diff < 1e-12)
"""

from __future__ import annotations

import sys

import pandas as pd

from lab.data import load_close
from lab.strategies import get_strategy, registry
from lab.universe import ROOSTOO_10


def main() -> int:
    c = load_close(ROOSTOO_10 + ["PAXGUSDT"], "2025-01-01")
    ok = True
    params = {"btc_pair": "BTCUSDT"}
    for name, (cls, origin) in sorted(registry().items()):
        w = get_strategy(name).target_weights(c[ROOSTOO_10].iloc[-800:], params)
        g = sum(abs(v) for v in w.values())
        good = g <= 1 + 1e-9 and set(w) == set(ROOSTOO_10)
        ok &= good
        print(f"[{'PASS' if good else 'FAIL'}] {name:<18} ({origin}) gross {g:.3f}")
    worst = 0.0
    for ts in pd.date_range("2025-03-01", "2026-09-30", freq="11D", tz="UTC"):
        win = c[ROOSTOO_10].loc[:ts].iloc[-800:]
        a = pd.Series(get_strategy("s3v2").target_weights(win, params))
        b = pd.Series(get_strategy("s3v2x").target_weights(win, params))
        worst = max(worst, float((a - b).abs().max()))
    good = worst < 1e-12
    ok &= good
    print(f"[{'PASS' if good else 'FAIL'}] s3v2x(defaults) == s3v2 on 53 dates (max diff {worst:.1e})")
    w = get_strategy("s3v2x").target_weights(c.iloc[-800:], {**params, "parking_asset": "PAXGUSDT"})
    print(f"[info] s3v2x with PAXG parking now: PAXG {w['PAXGUSDT']:.3f}, gross {sum(abs(v) for v in w.values()):.3f}")
    print(f"\nstrategy tests: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
