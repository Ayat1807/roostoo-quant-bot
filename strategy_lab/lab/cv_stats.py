"""CV stats (reports/cv_stats.md) from EXISTING runs only (no new trials). Live rows come from strategy_bot/cv_live_stats.py
on the machine that holds the live logs; anything that does not exist is written as "not computed".

    python -m lab.cv_stats [--live live_stats.json]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

from lab import ROOT, load_config
from lab.b3 import IS_END, OOS0, OOS_END
from lab.b5 import judge
from lab.runner import HCACHE, load_hourly
from lab.scorecard import metrics

RUNS = {"s3v2e_core10 (live)": "b3_s3v2e_core10", "HMM2 + CUSUM (forward test)": "b7_hmm2_cusum"}
NC = "not computed"


def period(h: pd.DataFrame, a, b) -> tuple[pd.DataFrame, str]:
    x = h.loc[a:b]
    days = (x.index[-1] - x.index[0]) / pd.Timedelta(days=1)
    return x, f"{x.index[0]:%Y-%m-%d} to {x.index[-1]:%Y-%m-%d} ({days:.0f} days)"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", type=Path, help="JSON written by strategy_bot/cv_live_stats.py --json")
    a = ap.parse_args()
    live = json.loads(a.live.read_text()) if a.live and a.live.exists() else {}
    costs = load_config()["costs"]
    cols = list(RUNS)
    rows: dict[str, list[str]] = {}
    cv: dict[str, dict] = {}

    def add(label: str, vals: list[str]) -> None:
        rows[label] = vals

    for half, (lo, hi) in (("IS", (None, IS_END)), ("OOS", (OOS0, OOS_END))):
        per, met, jj, st = [], [], [], []
        for c in cols:
            n = RUNS[c]
            h = load_hourly(n)
            x, lab = period(h, lo, hi)
            per.append(lab)
            met.append(metrics(x["equity"].values))
            jj.append(judge(n)[half])
            sp = HCACHE / f"{n}__stress.pkl"
            st.append(metrics(pd.read_pickle(sp).loc[lo:hi]["equity"].values) if sp.exists() else None)
        add(f"**{half}** period", per)
        add(f"{half} Sharpe", [f"{m['sharpe']:.2f}" for m in met])
        add(f"{half} Sortino", [f"{m['sortino']:.2f}" for m in met])
        add(f"{half} Calmar", [f"{m['calmar']:.2f}" for m in met])
        add(f"{half} max drawdown", [f"{m['mdd']:.1%}" for m in met])
        add(f"{half} total return", [f"{m['return']:+.1%}" for m in met])
        add(f"{half} annualised return (CAGR)", [f"{m['ann_ret']:+.1%}" for m in met])
        add(f"{half} trades per day", [f"{j['trades_day']:.1f}" for j in jj])
        add(f"{half} fees per year (share of mean equity)", [f"{j['fees_yr']:.1%}" for j in jj])
        add(f"{half} stress (100% taker + 7 bps): return / Sharpe / max drawdown",
            [f"{s['return']:+.1%} / {s['sharpe']:.2f} / {s['mdd']:.1%}" if s else NC for s in st])
        for c, m in zip(cols, met):
            cv.setdefault(c, {})[half] = m
    cost_txt = (f"taker {costs['taker']:.2%} per fill (100% of spot fills assumed taker) + {costs['slippage'] * 1e4:.0f} bps "
                f"slippage per fill; shorts {costs['short']:.2%} on open AND on close + slippage")
    add("cost assumptions (backtest)", [cost_txt, cost_txt])

    def live_cell(key: str) -> str:
        d = live.get(key)
        if not d:
            return NC
        return (f"{d['from']} to {d['to']} UTC ({d['days']:.1f} days): return {d['return']:+.2%}, max drawdown "
                f"{d['mdd']:.2%}, trades {d['trades']} (start equity ${d['start_equity']:,.2f}, end ${d['end_equity']:,.2f})")

    L = ["# CV statistics: s3v2e_core10 (live) and HMM2 + CUSUM (forward test)\n",
         f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by `python -m lab.cv_stats` from existing strategy_lab runs "
         "(`b3_s3v2e_core10`, `b7_hmm2_cusum`) and, for the live rows, `strategy_bot/cv_live_stats.py` output. No new trials, "
         "no estimates; \"not computed\" = the source does not exist here._\n",
         "## Backtest (simulated, hourly, Roostoo costs)\n",
         "| | " + " | ".join(cols) + " |", "|---|" + "---|" * len(cols)]
    for k, v in rows.items():
        L.append(f"| {k} | " + " | ".join(v) + " |")
    L += ["\n## LIVE (real exchange, Roostoo; label: live)\n",
          "| | " + " | ".join(cols) + " |", "|---|" + "---|" * len(cols),
          f"| live on its own key | {live_cell('s3v2e_competition')} | {live_cell('hmm_testing')} |",
          f"\n**Whole competition account since 2026-10-06 15:30 UTC** (xsmom on R1 ran until 2026-10-07 10:00 UTC, then "
          f"s3v2e_core10 from 10:04 UTC): {live_cell('competition_account')}\n"]
    if not live:
        L.append("_Live rows are \"not computed\" here: the live logs exist only on the EC2 machine "
                 "(`logs_competition/`, `logs_competition_s3v2e/`, `logs_testing_hmm/`). To fill them from source: on EC2 run "
                 "`.venv/bin/python cv_live_stats.py --json live_stats.json`, copy the file here and run "
                 "`python -m lab.cv_stats --live live_stats.json`._\n")
    o = {c: cv[c]["OOS"] for c in cols}
    i = {c: cv[c]["IS"] for c in cols}
    L += ["## CV-ready lines (built only from the numbers above)\n"]
    for c in cols:
        ls = live.get("s3v2e_competition" if c.startswith("s3v2e") else "hmm_testing")
        live_txt = (f"; live {ls['days']:.0f} days on Roostoo: {ls['return']:+.1%}, max drawdown {ls['mdd']:.1%}"
                    if ls else "")
        L.append(f"- **{c}:** out-of-sample backtest 2025-01 to 2026-06 with taker fees and slippage: Sharpe {o[c]['sharpe']:.2f}, "
                 f"Sortino {o[c]['sortino']:.2f}, CAGR {o[c]['ann_ret']:+.1%}, max drawdown {o[c]['mdd']:.1%} "
                 f"(in-sample 2020-2024: Sharpe {i[c]['sharpe']:.2f}, max drawdown {i[c]['mdd']:.1%}){live_txt}.")
    (ROOT / "reports" / "cv_stats.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
