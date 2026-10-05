"""Run a backtest spec, score it and store the results.

    python -m lab.runner variants.yaml                   # every declared run
    python -m lab.runner variants.yaml --only s3v2_base,guard_off
    python -m lab.runner variants_b2.yaml --group D,E      # research block 2 (baseline b2_core)

Outputs per run (runs/<name>/, committed): result.json (spec + scorecard), summary.md,
equity_daily.csv. The hourly curve is kept in .cache/runs/<name>.pkl (git-ignored) for
analogs and correlations. Each executed run increments the trial ledger
(runs/trials.json) used by the leaderboard's overfitting flags.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any

import pandas as pd
import yaml

from lab import ROOT
from lab.backtest import run
from lab.combine import combine_hourly
from lab.data import load_close
from lab.scorecard import scorecard, to_markdown

RUNS = ROOT / "runs"
HCACHE = ROOT / ".cache" / "runs"
BASELINE = "s3v2_base"


def load_hourly(name: str) -> pd.DataFrame | None:
    p = HCACHE / f"{name}.pkl"
    return pd.read_pickle(p) if p.exists() else None


def bump_trials(names: list[str]) -> dict[str, Any]:
    path = RUNS / "trials.json"
    led = json.loads(path.read_text()) if path.exists() else {"total_runs": 0, "distinct": []}
    led["total_runs"] += len(names)
    led["distinct"] = sorted(set(led["distinct"]) | set(names))
    led["updated"] = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())
    RUNS.mkdir(exist_ok=True)
    path.write_text(json.dumps(led, indent=1))
    return led


def execute(name: str, spec: dict[str, Any], btc: pd.Series, closes_cache: dict,
            baseline: str = BASELINE) -> dict[str, Any]:
    t0 = time.time()
    s = {k: v for k, v in spec.items() if k not in ("trial", "note", "group")}
    s["name"] = name
    if "combo" in s:     # core + satellite sub-books (lab/combine.py)
        cb = s["combo"]
        core, sat = load_hourly(cb["core"]), load_hourly(cb["satellite"])
        if core is None or sat is None:
            raise RuntimeError(f"{name}: run {cb['core']} and {cb['satellite']} first")
        s = {"name": name, "combo": cb}
        h = combine_hourly(core, sat, float(cb["sat_share"]))
        res = {"assets": [], "targets": []}
    else:
        res = run(s, closes_cache.get(None))
        h = res["hourly"]
    HCACHE.mkdir(parents=True, exist_ok=True)
    h.to_pickle(HCACHE / f"{name}.pkl")
    base = load_hourly(baseline) if name != baseline else None
    sc = scorecard(h, btc, base)
    out_dir = RUNS / name
    out_dir.mkdir(parents=True, exist_ok=True)
    meta = {"name": name, "group": spec.get("group"), "note": spec.get("note"),
            "trial": spec.get("trial"), "spec": s, "runtime_s": round(time.time() - t0, 1),
            "assets_loaded": len(res["assets"]), "scorecard": sc,
            "last_targets": res["targets"][-1] if res["targets"] else None}
    (out_dir / "result.json").write_text(json.dumps(meta, indent=1, default=str))
    (out_dir / "summary.md").write_text(to_markdown(name, s, sc), encoding="utf-8")
    h["equity"].resample("1D").last().to_csv(out_dir / "equity_daily.csv", header=["equity"])
    return meta


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("file", type=Path)
    ap.add_argument("--only", help="comma-separated run names")
    ap.add_argument("--group", help="comma-separated groups (e.g. D,E)")
    a = ap.parse_args()
    doc = yaml.safe_load(a.file.read_text(encoding="utf-8"))
    defaults = doc.get("defaults", {})
    baseline = doc.get("baseline", BASELINE)
    runs = doc["runs"]
    names = [r["name"] for r in runs]
    if a.only:
        want = a.only.split(",")
        runs = [r for r in runs if r["name"] in want]
    if a.group:
        groups = a.group.split(",")
        runs = [r for r in runs if r.get("group") in groups]
    # baseline first (correlations, R4), then strategies, then combos (need both books)
    runs.sort(key=lambda r: (r["name"] != baseline, "combo" in r))
    btc = load_close(["BTCUSDT"])["BTCUSDT"]
    led = bump_trials([r["name"] for r in runs if r.get("trial") is not None])
    print(f"{len(runs)} runs ({len(names)} declared; trial ledger total {led['total_runs']})")
    cache: dict = {}
    for r in runs:
        spec = {**defaults, **{k: v for k, v in r.items() if k != "name"}}
        if "params" in defaults and "params" in r:
            spec["params"] = {**defaults["params"], **r["params"]}
        if "combo" in r:
            spec = {k: v for k, v in r.items() if k != "name"}
        m = execute(r["name"], spec, btc, cache, baseline)
        sc = m["scorecard"]
        oos, w = sc["periods"].get("out_of_sample", {}), sc["rolling_14d"].get("out_of_sample", {})
        print(f"  {r['name']:<32} OOS {oos.get('return', 0):+7.2%} SR {oos.get('sharpe', 0):5.2f} "
              f"DD {oos.get('mdd', 0):+7.2%} | 14d med {w.get('median_return', 0):+6.2%} "
              f"pos {w.get('pct_positive', 0):4.0%} comp {w.get('median_composite', 0):6.2f} "
              f"act {w.get('median_active_days', 0):4.1f}/14  [{m['runtime_s']}s]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
