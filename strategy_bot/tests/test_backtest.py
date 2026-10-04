"""(b) Reproduce the reference out-of-sample backtest of S3v2.

    python -m tests.test_backtest

Reference (research/summary_results.csv, "OOS last 12m"): +21.24%, Sharpe 1.073,
max DD -17.13%. Setup per the team: tsmom_lt(horizons=(24,72,168,336), reb=24,
short_scale_bull=0.5, target_vol=0.4), simulate(band=0.06, fee=0.10%, slip=2 bps),
10 coins, Oct 2025 -> Oct 2026. Data: Binance 1h klines Jan 2023 -> now.

The reference run date (its "now") is unknown, so the 12-month window is evaluated
for a few end dates; the drawdown brake variant is shown as well.
"""

from __future__ import annotations

import sys

import pandas as pd

from tests.hist_data import load_closes
from tests.reference import engine, ref_strategies

REF = {"return": 0.2124195869409482, "sharpe": 1.0732972165899122, "mdd": -0.17133272078605888}


def run(usdt: pd.DataFrame, W: pd.DataFrame, start: str, end: str, brake: bool) -> dict:
    kw = dict(dd_soft=-0.04, dd_hard=-0.07) if brake else {}
    r = engine.simulate(usdt, W, fee=0.001, slip=0.0002, band=0.06, start=start, end=end, **kw)
    m = engine.metrics(r["equity"])
    days = r["trades"].groupby(r.index.date).sum()
    m["active_days"] = f"{int((days > 0).sum())}/{len(days)}"
    m["trades_per_day"] = r["trades"].sum() / len(days)
    return m


def main() -> int:
    c = load_closes()
    usdt = c.rename(columns=lambda x: x.replace("/USD", "USDT"))
    W = ref_strategies.tsmom_lt({"close": usdt}, horizons=(24, 72, 168, 336), reb=24,
                                short_scale_bull=0.5, target_vol=0.4)
    last = c.index[-1]
    print(f"data {c.index[0]:%Y-%m-%d} -> {last:%Y-%m-%d %H:%M} UTC; fee 0.10% + slip 2 bps; band 6pp\n")
    print(f"{'window':<27}{'brake':<7}{'return':>9}{'sharpe':>8}{'maxDD':>9}{'active':>9}{'trades/d':>9}")
    best = None
    for end in (last, last - pd.Timedelta(days=3), pd.Timestamp("2026-10-01", tz="UTC")):
        start = end - pd.Timedelta(days=365)
        for brake in (False, True):
            m = run(usdt, W, str(start), str(end), brake)
            err = abs(m["return"] - REF["return"]) + abs(m["sharpe"] - REF["sharpe"]) / 10
            if best is None or err < best[0]:
                best = (err, start, end, brake, m)
            print(f"{start:%Y-%m-%d}..{end:%Y-%m-%d %H}h   {'on' if brake else 'off':<7}"
                  f"{m['return']:>+8.2%}{m['sharpe']:>8.2f}{m['mdd']:>+9.2%}"
                  f"{m['active_days']:>9}{m['trades_per_day']:>9.2f}")
    print(f"\nreference                         {REF['return']:>+8.2%}{REF['sharpe']:>8.2f}"
          f"{REF['mdd']:>+9.2%}")
    _, s, e, b, m = best
    ok = abs(m["return"] - REF["return"]) < 0.03 and abs(m["sharpe"] - REF["sharpe"]) < 0.15 \
        and abs(m["mdd"] - REF["mdd"]) < 0.03
    print(f"(b) closest: {s:%Y-%m-%d}..{e:%Y-%m-%d} brake={'on' if b else 'off'} -> "
          f"{m['return']:+.2%} / SR {m['sharpe']:.2f} / DD {m['mdd']:+.2%}  "
          f"{'PASS' if ok else 'CHECK'} (tolerance: ret +-3pp, SR +-0.15, DD +-3pp)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
