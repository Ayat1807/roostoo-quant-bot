"""Block 12 comparison of the aggressive options (variants_b12_aggr.yaml): reports/aggr_comparison.md.

    python -m lab.b12
"""

from __future__ import annotations

import sys

import numpy as np
import pandas as pd

from lab import ROOT
from lab.b3 import OOS_END, fwd
from lab.b5 import judge, three_day
from lab.b8 import broad_down, broad_down_starts
from lab.leaderboard import N01, declared_total
from lab.runner import load_hourly

RUNS = {"live (s3v2e tv0.4)": "b3_s3v2e_core10", "OPTION A (s3v2e tv0.6)": "b3_s3v2e_tv06_core10",
        "s3v2e tv0.8 w0.4 (deployed 2026-10-12)": "b3_s3v2e_tv08_w04_core10",
        "OPTION B (hmm_cusum_aggr)": "b12_hmm_cusum_aggr", "aggr_mid": "b12_aggr_mid", "aggr_15": "b12_aggr_15"}


def main() -> int:
    from lab.analogs import features, find_analogs
    have = {k: n for k, n in RUNS.items() if load_hourly(n) is not None}
    J = {k: judge(n) for k, n in have.items()}
    f = features()
    today = f[["btc_ret_30d"]].dropna().index[-1]
    f2 = f[(f.index <= OOS_END - pd.Timedelta(days=14)) | (f.index == today)]
    analog_days = [d + pd.Timedelta(hours=23) for d in find_analogs(f2, today, k=30)[0].index]
    starts = broad_down_starts()
    pct = lambda v: "" if v is None or (isinstance(v, float) and np.isnan(v)) else f"{v:+.1%}"
    pr = lambda v: "" if v is None or (isinstance(v, float) and np.isnan(v)) else f"{v:.0%}"
    cols = list(have)
    L = ["# Aggressive options for the competition bot: side-by-side comparison\n",
         f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by `python -m lab.b12`. Rules: `variants_b12_aggr.yaml` "
         f"(declared before the runs). Data to 2026-06-30, both halves; Jul-Oct informational. Trials: {declared_total()} declared, "
         f"luck threshold about {N01.inv_cdf(1 - 1 / declared_total()):.1f} SE. Full stats cards: "
         "`reports/stats_card_aggr_options.md`._\n",
         "| | " + " | ".join(cols) + " |", "|---|" + "---|" * len(cols)]
    row = lambda label, fn: L.append(f"| {label} | " + " | ".join(fn(k) for k in cols) + " |")
    for h in ("IS", "OOS"):
        row(f"{h} Sharpe", lambda k: f"{J[k][h]['sharpe']:.2f}")
        row(f"{h} max drawdown", lambda k: pct(J[k][h]["mdd"]))
        row(f"{h} median 14d composite", lambda k: f"{J[k][h]['comp']:.2f}")
        row(f"{h} mean / median 14d", lambda k: f"{pct(J[k][h]['mean'])} / {pct(J[k][h]['median'])}")
        row(f"{h} worst 14d", lambda k: pct(J[k][h]["worst"]))
        row(f"{h} P(14d <= -10%)", lambda k: pr(J[k][h]["pm10"]))
        row(f"{h} P(14d >= +10%)", lambda k: pr(J[k][h]["p10"]))
        row(f"{h} down windows (BTC 14d < -5%) mean", lambda k: pct(J[k][h]["down"]))
        row(f"{h} fees / yr, trades / day", lambda k: f"{J[k][h]['fees_yr']:.1%}, {J[k][h]['trades_day']:.1f}")
    row("meets the block-5 requirements (both halves)", lambda k: "yes" if J[k]["meets"] else "**no**")
    BD = {k: broad_down(n, starts) for k, n in have.items()}
    row("broad-down windows mean IS / OOS (n)", lambda k: f"{pct(BD[k].get('IS', {}).get('mean'))} / "
        f"{pct(BD[k].get('OOS', {}).get('mean'))} ({BD[k].get('OOS', {}).get('n', 0)})")
    TD = {k: three_day(load_hourly(n), analog_days) for k, n in have.items()}
    for h in ("IS", "OOS"):
        row(f"3-day {h}: mean / median / P(>0) / worst", lambda k: (f"{pct(TD[k][h]['mean'])} / {pct(TD[k][h]['median'])} / "
                                                                    f"{pr(TD[k][h]['pos'])} / {pct(TD[k][h]['worst'])}"))
    row("3-day after the 30 analogs: mean / median / P(>0) / worst",
        lambda k: (f"{pct(TD[k]['analogs']['mean'])} / {pct(TD[k]['analogs']['median'])} / {pr(TD[k]['analogs']['pos'])} / "
                   f"{pct(TD[k]['analogs']['worst'])}") if "analogs" in TD[k] else "")
    AN = {k: fwd(load_hourly(n), analog_days) for k, n in have.items()}
    row("14-day after the 30 analogs: mean / P(>= +10%)", lambda k: f"{pct(AN[k].get('mean'))} / {pr(AN[k].get('p10'))}")
    row("Jul-Oct 2026 (info only): mean 14d / worst 14d", lambda k: f"{pct(J[k]['INFO'].get('mean'))} / {pct(J[k]['INFO'].get('worst'))}")
    (ROOT / "reports" / "aggr_comparison.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
