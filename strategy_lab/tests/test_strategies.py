"""Strategy plug-in checks (offline, uses the lab cache).

    python -m tests.test_strategies

* every registered strategy returns a valid weight dict on real data (gross <= 1)
* s3v2x with default knobs == live s3v2 exactly (max diff < 1e-12)
* breakout enters on a new 96-bar high and exits on a new 48-bar low (synthetic path)
"""

from __future__ import annotations

import sys

import numpy as np
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
    # breakout on a synthetic path: flat noise, rally (new highs), then a drop (new lows)
    rng = np.random.default_rng(0)
    base = 100 + rng.normal(0, 0.05, 900).cumsum()
    up = base.copy()
    up[500:] += np.linspace(0, 20, 400)                 # breaks out above the 96-bar high
    down = up.copy()
    down[850:] -= np.linspace(0, 40, 50)               # falls below the 48-bar low
    idx = pd.date_range("2025-01-01", periods=900, freq="30min", tz="UTC")
    bo = get_strategy("breakout")
    w_up = bo.target_weights(pd.DataFrame({"AUSDT": up, "BUSDT": base}, index=idx).iloc[-800:], {})
    w_dn = bo.target_weights(pd.DataFrame({"AUSDT": down, "BUSDT": base}, index=idx).iloc[-800:], {})
    good = 0 < w_up["AUSDT"] <= 0.03 + 1e-12 and w_dn["AUSDT"] == 0
    ok &= good
    print(f"[{'PASS' if good else 'FAIL'}] breakout: long after breakout ({w_up['AUSDT']:.3f}, <= 0.30/10), "
          f"flat after breakdown ({w_dn['AUSDT']:.3f})")
    print(f"\nstrategy tests: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
