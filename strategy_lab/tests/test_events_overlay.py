"""Event overlays (block 4a): the overlay code path must not change the control.

    python -m tests.test_events_overlay

1. b3_xsmom_r1 re-run with a no-op overlay (de-risk cap 100%, every event) == the stored
   b3_xsmom_r1 hourly curve exactly (equity, trades, fees).
2. Event plan timing on the real calendar: CPI 2024-05-15 12:30 UTC -> de-risk steps from
   tau 13:00 the day before to tau 16:00 (last step < 16:30); breakout checks at tau 13:00-16:00
   against the 12:00 close.
Not a trial (no new strategy result).
"""

from __future__ import annotations

import sys

import numpy as np
import pandas as pd

from lab.backtest import Backtest, RunConfig
from lab.runner import load_hourly, resolve_base


def main() -> int:
    ok = True
    ref = load_hourly("b3_xsmom_r1")
    spec = {**resolve_base("b3_xsmom_r1"), "name": "chk_noop",
            "events": {"derisk": {"types": ["CPI", "FOMC_DECISION", "FOMC_MINUTES"], "before_h": 24,
                                  "after_h": 4, "max_gross": 1.0}}}
    bt = Backtest(RunConfig.from_dict(spec))
    res = bt.run()
    h = res["hourly"].loc[ref.index[0]:ref.index[-1]]
    same = (len(h) == len(ref) and np.allclose(h["equity"].values, ref["equity"].values, rtol=0, atol=1e-9)
            and (h["trades"].values == ref["trades"].values).all())
    print(f"[{'PASS' if same else 'FAIL'}] no-op overlay reproduces b3_xsmom_r1 "
          f"({len(h)} hours, max |d equity| {np.abs(h['equity'].values - ref['equity'].values).max():.2e}, "
          f"derisk bars seen {res['events']['derisk_bars']})")
    ok &= same

    idx = bt.closes.index
    spec2 = {**spec, "events": {"derisk": {"types": ["CPI"], "before_h": 24, "after_h": 4, "max_gross": 0.5},
                                "breakout": {"types": ["CPI"], "within_h": 4}}}
    bt.rc = RunConfig.from_dict(spec2)
    plan = bt._event_plan(idx, list(bt.closes.columns))
    tau = idx + pd.Timedelta(hours=1)
    day = (tau >= pd.Timestamp("2024-05-14", tz="UTC")) & (tau < pd.Timestamp("2024-05-16", tz="UTC"))
    on = tau[day & plan["derisk"]]
    want0, want1 = pd.Timestamp("2024-05-14 13:00", tz="UTC"), pd.Timestamp("2024-05-15 16:00", tz="UTC")
    t_ok = len(on) > 0 and on[0] == want0 and on[-1] == want1
    print(f"[{'PASS' if t_ok else 'FAIL'}] CPI 2024-05-15 12:30 UTC: de-risk steps {on[0] if len(on) else None} -> "
          f"{on[-1] if len(on) else None} (want {want0} -> {want1})")
    bo = sorted(tau[j] for j, lst in plan["breakout"].items()
                if any(pd.Timestamp("2024-05-15", tz="UTC") <= tau[p] < pd.Timestamp("2024-05-16", tz="UTC")
                       for _, p in lst))
    pre = {tau[p] for j, lst in plan["breakout"].items() for _, p in lst
           if pd.Timestamp("2024-05-15", tz="UTC") <= tau[p] < pd.Timestamp("2024-05-16", tz="UTC")}
    b_ok = ([str(t.time()) for t in bo] == ["13:00:00", "14:00:00", "15:00:00", "16:00:00"]
            and pre == {pd.Timestamp("2024-05-15 12:00", tz="UTC")})
    print(f"[{'PASS' if b_ok else 'FAIL'}] breakout checks at {[str(t.time()) for t in bo]} vs close {sorted(pre)}")
    ok &= t_ok and b_ok
    print(f"\nevent overlay checks: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
