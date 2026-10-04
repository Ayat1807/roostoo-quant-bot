"""Verify the lab backtester against strategy_bot's S3v2 reference backtest.

    python -m tests.test_reproduce

Step 1 (engine mode): lab backtester with the reference research engine's
simplifications vs research/engine.py simulate() on the same lab data, same window.
They must agree closely (different code, same rules).
Step 2 (realistic mode): Roostoo rules on top (AmountPrecision rounding, $1 MiniOrder,
per-leg books, taker 0.10% + 2 bps). Expect about +19-21% on the reference OOS window
(Oct 2025 -> Oct 2026), brake on and off. The reference result has no activity guard,
so the check runs with it off; the guard's effect is printed separately (informational:
it adds large path variance, e.g. -24pp in 2025 but +7pp in 2022).
"""

from __future__ import annotations

import importlib.util
import sys

import pandas as pd

from lab import REPO
from lab.backtest import run
from lab.data import load_close
from lab.universe import ROOSTOO_10

RESEARCH = REPO / "_reference" / "roostoo-bot" / "research"
START, END = "2025-10-01", "2026-10-01"


def _ref(name: str, file: str):
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, RESEARCH / file)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def stats(eq: pd.Series) -> tuple[float, float, float]:
    r = eq.pct_change().dropna()
    sharpe = r.mean() / r.std() * (24 * 365) ** 0.5
    return eq.iloc[-1] / eq.iloc[0] - 1, sharpe, (eq / eq.cummax() - 1).min()


def main() -> int:
    engine = _ref("engine", "engine.py")
    ref_strat = _ref("ref_strategies", "strategies.py")
    closes = load_close(ROOSTOO_10, "2023-01-01")
    W = ref_strat.tsmom_lt({"close": closes}, horizons=(24, 72, 168, 336), reb=24,
                           short_scale_bull=0.5, target_vol=0.4)
    base = {"strategy": "s3v2", "universe": {"type": "list", "assets": ROOSTOO_10},
            "start": START, "end": END, "band": 0.06,
            "params": {"horizons": [24, 72, 168, 336], "vol_win": 336, "target_vol": 0.4,
                       "short_scale_bull": 0.5, "max_w": 0.3, "regime_win": 336}}
    print(f"window {START} -> {END}, 10 coins, data: lab Binance cache\n")
    print(f"{'run':<44}{'return':>9}{'sharpe':>8}{'maxDD':>9}{'trades':>8}{'fees $':>9}")
    ok = True
    for brake in (False, True):
        kw = dict(dd_soft=-0.04, dd_hard=-0.07) if brake else {}
        ref = engine.simulate(closes, W, fee=0.001, slip=0.0002, band=0.06, start=START, end=END, **kw)
        r_ret, r_sr, r_dd = stats(ref["equity"])
        eng = run({**base, "name": "engine_mode", "brake": brake, "engine_mode": True}, closes)
        e_ret, e_sr, e_dd = stats(eng["hourly"]["equity"])
        real = run({**base, "name": "realistic", "brake": brake, "activity_guard": False}, closes)
        guard = run({**base, "name": "realistic_guard", "brake": brake}, closes)
        g_ret, g_sr, g_dd = stats(guard["hourly"]["equity"])
        h = real["hourly"]
        x_ret, x_sr, x_dd = stats(h["equity"])
        tag = "on " if brake else "off"
        print(f"{'reference research/engine.py   brake ' + tag:<44}{r_ret:>+8.2%}{r_sr:>8.2f}{r_dd:>+9.2%}"
              f"{int(ref['trades'].sum()):>8}{'':>9}")
        print(f"{'lab engine_mode                 brake ' + tag:<44}{e_ret:>+8.2%}{e_sr:>8.2f}{e_dd:>+9.2%}"
              f"{eng['trades_total']:>8}{eng['hourly']['fees'].sum():>9,.0f}")
        print(f"{'lab realistic (Roostoo rules)   brake ' + tag:<44}{x_ret:>+8.2%}{x_sr:>8.2f}{x_dd:>+9.2%}"
              f"{real['trades_total']:>8}{h['fees'].sum():>9,.0f}   ({real['runtime_s']}s)")
        print(f"{'  + activity guard 1pp @20:00 (live bot)  ' + tag:<44}{g_ret:>+8.2%}{g_sr:>8.2f}"
              f"{g_dd:>+9.2%}{guard['trades_total']:>8}{guard['hourly']['fees'].sum():>9,.0f}   (info)")
        corr = ref["equity"].pct_change().corr(eng["hourly"]["equity"].pct_change())
        gap = abs(e_ret - r_ret)
        m_ok = gap < 0.005 and corr > 0.999
        x_ok = 0.17 <= x_ret <= 0.23
        ok &= m_ok and x_ok
        print(f"   engine-mode vs reference: |return gap| {gap:.4%}, hourly-return corr {corr:.6f} "
              f"-> {'PASS' if m_ok else 'FAIL'}; realistic in ~19-21% band -> "
              f"{'PASS' if x_ok else 'CHECK'}\n")
    print(f"reproduction: {'PASS' if ok else 'CHECK'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
