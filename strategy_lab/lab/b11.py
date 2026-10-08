"""Block 11 report: historical dry run of the news layer's calendar and Fear & Greed rules (variants_b11_news.yaml).

    python -m lab.b11        # reports/news_rules_dry_run.md
"""

from __future__ import annotations

import json
import sys

import numpy as np
import pandas as pd

from lab import ROOT
from lab.b5 import HALVES, beats_ref, judge
from lab.events import load_events
from lab.leaderboard import N01, declared_total
from lab.runner import load_hourly
from lab.scorecard import metrics

RUN, REF = "b11_news_rules", "b3_s3v2e_core10"
WINDOW = (pd.Timestamp("2025-01-01", tz="UTC"), pd.Timestamp("2026-06-30 23:00", tz="UTC"))


def main() -> int:
    h, r = load_hourly(RUN), load_hourly(REF)
    J, Jr = judge(RUN), judge(REF)
    ev = pd.DatetimeIndex(load_events(("CPI", "FOMC_DECISION"))["time"])
    fng = pd.read_csv(ROOT / "data" / "fng.csv")
    fng = pd.Series(fng["value"].values, index=pd.to_datetime(fng["date"], utc=True))
    pct = lambda v: "" if v is None or (isinstance(v, float) and np.isnan(v)) else f"{v:+.1%}"
    L = ["# News risk layer: historical dry run of the deterministic rules (block 11)\n",
         f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by `python -m lab.b11`. Rules declared in "
         "`variants_b11_news.yaml` before the run. **Not hindsight-contaminated**: the calendar and Fear & Greed rules use no LLM. "
         "**The headline veto rule is NOT evaluated here**: there is no free archive of timestamped headlines, and LLM recall "
         "of past events would be hindsight-contaminated; it is judged on the forward shadow log only._\n",
         f"Trials: {declared_total()} declared; luck threshold about {N01.inv_cdf(1 - 1 / declared_total()):.1f} SE.\n",
         "## How often the rules fire\n", "| period | calendar rule active (share of hours) | Fear & Greed rule (share of days) |",
         "|---|---|---|"]
    for k, (a, b) in list(HALVES.items())[:2] + [("Jan 2025 - Jun 2026", WINDOW)]:
        idx = h.loc[a:b].index
        tau = idx + pd.Timedelta(hours=1)
        on = np.zeros(len(idx), dtype=bool)
        for t in ev:
            on |= (tau >= t - pd.Timedelta(hours=24)) & (tau < t + pd.Timedelta(hours=4))
        f = fng.loc[(a or fng.index[0]):(b or fng.index[-1])]
        L.append(f"| {k} | {on.mean():.1%} | {((f >= 85) | (f <= 10)).mean():.1%} |")
    L += ["\n## Return and drawdown, with vs without the layer\n",
          "| period | return without / with | max drawdown without / with | Sharpe without / with | worst 14d without / with |",
          "|---|---|---|---|---|"]
    for k, (a, b) in list(HALVES.items())[:2] + [("Jan 2025 - Jun 2026 (team window)", WINDOW)]:
        m0, m1 = metrics(r.loc[a:b]["equity"].values), metrics(h.loc[a:b]["equity"].values)
        w0 = Jr[k]["worst"] if k in Jr else Jr["OOS"]["worst"]
        w1 = J[k]["worst"] if k in J else J["OOS"]["worst"]
        L.append(f"| {k} | {pct(m0['return'])} / {pct(m1['return'])} | {pct(m0['mdd'])} / {pct(m1['mdd'])} | "
                 f"{m0['sharpe']:.2f} / {m1['sharpe']:.2f} | {pct(w0)} / {pct(w1)} |")
    L += ["\n## Team objective (lab/b5.py)\n", "| | median 14d composite IS / OOS | mean 14d IS / OOS | down-window mean IS / OOS | "
          "OOS Sharpe | meets all | beats s3v2e_core10 |", "|---|---|---|---|---|---|---|"]
    for n, j in ((REF, Jr), (RUN, J)):
        L.append(f"| {n} | {j['IS']['comp']:.2f} / {j['OOS']['comp']:.2f} | {pct(j['IS']['mean'])} / {pct(j['OOS']['mean'])} | "
                 f"{pct(j['IS']['down'])} / {pct(j['OOS']['down'])} | {j['OOS']['sharpe']:.2f} | {'yes' if j['meets'] else 'no'} | "
                 f"{'' if n == REF else ('yes' if beats_ref(J, Jr) else 'no')} |")
    m = json.loads((ROOT / "runs" / RUN / "result.json").read_text())
    st = (m.get("extra") or {}).get("strategy_stats") or {}
    L.append(f"\nFear & Greed rule fired at {st.get('fng_fired', '?')} of {st.get('decisions', '?')} daily target computations; "
             f"calendar overlay active in {(m.get('events_log') or {}).get('derisk_bars', '?')} hourly bars.")
    (ROOT / "reports" / "news_rules_dry_run.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
