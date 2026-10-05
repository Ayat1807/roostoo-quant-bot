"""Final exam for research block 2: the holdout 2026-07-01 -> latest data, used ONCE.

    python -m lab.final_exam                 # candidates = "beats live" runs in reports/block2_runs.csv
    python -m lab.final_exam --runs a,b      # explicit candidates (still only once)

Re-runs each candidate and the baseline (b2_core) with the same spec but no end date (core and
satellite books are re-run for a combo), then scores only the exam period. Pass rule (declared
in variants_b2.yaml before any run): exam return >= baseline exam return AND exam max drawdown
no worse than the baseline's by more than 5pp. Writes reports/final_exam.md and
runs/final_exam.lock; refuses to run again while the lock exists.
"""

from __future__ import annotations

import argparse
import json
import sys

import pandas as pd
import yaml

from lab import ROOT
from lab.backtest import run
from lab.combine import combine_hourly
from lab.scorecard import metrics, rolling_14d, summarize_windows

EXAM0 = pd.Timestamp("2026-07-01", tz="UTC")
LOCK = ROOT / "runs" / "final_exam.lock"
FILE = "variants_b2.yaml"


def spec_of(name: str, doc: dict) -> dict:
    df = doc["defaults"]
    r = next(x for x in doc["runs"] if x["name"] == name)
    s = {**df, **{k: v for k, v in r.items() if k not in ("name", "trial", "group", "note")}}
    s["params"] = {**df.get("params", {}), **r.get("params", {})}
    s["name"] = name
    s["end"] = None
    return s


def full_curve(name: str, doc: dict, memo: dict) -> pd.DataFrame:
    if name in memo:
        return memo[name]
    r = next(x for x in doc["runs"] if x["name"] == name)
    if "combo" in r:
        cb = r["combo"]
        h = combine_hourly(full_curve(cb["core"], doc, memo), full_curve(cb["satellite"], doc, memo),
                           float(cb["sat_share"]))
    else:
        h = run(spec_of(name, doc))["hourly"]
    memo[name] = h
    return h


def exam_stats(h: pd.DataFrame) -> dict:
    x = h.loc[EXAM0:]
    m = metrics(x["equity"].values)
    w = summarize_windows(rolling_14d(x))
    return {"return": m["return"], "sharpe": m["sharpe"], "mdd": m["mdd"], "w_median": w.get("median_return"),
            "w_pct_pos": w.get("pct_positive"), "w_worst": w.get("worst_return"), "n_windows": w.get("n_windows"),
            "start": str(x.index[0]), "end": str(x.index[-1])}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs")
    a = ap.parse_args()
    if LOCK.exists():
        print(f"final exam already taken ({LOCK.read_text().strip()}); see reports/final_exam.md")
        return 1
    doc = yaml.safe_load((ROOT / FILE).read_text(encoding="utf-8"))
    if a.runs:
        cands = a.runs.split(",")
    else:
        t = pd.read_csv(ROOT / "reports" / "block2_runs.csv", index_col=0)
        cands = list(t.index[t.beats_live.astype(bool)])
    LOCK.write_text(json.dumps({"taken": str(pd.Timestamp.now(tz="UTC")), "candidates": cands}))
    memo: dict = {}
    base = exam_stats(full_curve("b2_core", doc, memo))
    res = {n: exam_stats(full_curve(n, doc, memo)) for n in cands}
    L = ["# Final exam (holdout 2026-07-01 -> latest), taken once\n",
         f"Candidates: {', '.join(cands) if cands else 'none'}. Pass = exam return >= baseline AND exam max "
         f"drawdown no worse than baseline by more than 5pp.\n",
         "| run | exam return | exam Sharpe | exam maxDD | 14d median | 14d % pos | 14d worst | windows | pass |",
         "|---|---|---|---|---|---|---|---|---|"]
    for n, s in [("b2_core (live)", base)] + list(res.items()):
        ok = "" if n.startswith("b2_core") else (
            "**PASS**" if s["return"] >= base["return"] and s["mdd"] >= base["mdd"] - 0.05 else "fail")
        L.append(f"| {n} | {s['return']:+.2%} | {s['sharpe']:.2f} | {s['mdd']:+.2%} | {s['w_median']:+.2%} | "
                 f"{s['w_pct_pos']:.0%} | {s['w_worst']:+.2%} | {s['n_windows']} | {ok} |")
    L.append(f"\nExam window: {base['start'][:16]} -> {base['end'][:16]} UTC.")
    (ROOT / "reports" / "final_exam.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
