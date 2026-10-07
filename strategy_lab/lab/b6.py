"""Block 6 (upgrades of s3v2e_core10): resolvers and reports per track; judging = lab/b5.py (team objective).

    python -m lab.b6 a --resolve-a4      # trial 419: A1 + best A3
    python -m lab.b6 <track> --resolve-sweep
    python -m lab.b6 <track>             # report: leaderboard_b6<track>.md (+ references)
"""

from __future__ import annotations

import argparse
import json
import sys

import pandas as pd
import yaml

from lab import ROOT
from lab.b5 import LIVE, REF, judge, rank, report

TRACKS = {"a": ("variants_b6a_signal.yaml", 420), "b": ("variants_b6b_regime.yaml", 435),
          "c": ("variants_b6c_alloc.yaml", 448), "e": ("variants_b6e_universe.yaml", 461),
          "d": ("variants_b6d_meta.yaml", None)}


def doc(f: str) -> dict:
    return yaml.safe_load((ROOT / f).read_text(encoding="utf-8"))


def append(f: str, lines: list[str]) -> None:
    p = ROOT / f
    p.write_text(p.read_text(encoding="utf-8").rstrip("\n") + "\n" + "\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


def flow(d: dict) -> str:
    return json.dumps(d).replace('"', "")


def resolve_a4() -> int:
    f = TRACKS["a"][0]
    if "trial: 419," in (ROOT / f).read_text(encoding="utf-8"):
        print("already resolved")
        return 0
    runs = doc(f)["runs"]
    a3 = [r["name"] for r in runs if r.get("group") == "A3"]
    J = {n: judge(n) for n in a3}
    best = rank(a3, J)[0]
    cp = next(r for r in runs if r["name"] == best)["changepoint"]
    append(f, [f"  # resolved {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by lab/b6.py a --resolve-a4: best A3 = {best}",
               f"  - {{name: b6a_A4_tstat_{best.split('A3_')[1]}, trial: 419, group: A4, params: {{signal: tstat, tstat_cap: 2.0}}, "
               f"changepoint: {flow(cp)}}}"])
    return 0


def resolve_sweep(track: str, t0: int) -> int:
    f = TRACKS[track][0]
    if f"trial: {t0}," in (ROOT / f).read_text(encoding="utf-8"):
        print("already resolved")
        return 0
    names = [r["name"] for r in doc(f)["runs"] if r.get("group") != "sweep"]
    J = {n: judge(n) for n in names}
    best2 = rank(names, J)[:2]
    L = [f"  # resolved {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by lab/b6.py {track} --resolve-sweep: best 2 = {best2}"]
    t = t0
    for n in best2:
        for e in (1, 2, 4, 6, 12):
            L.append(f"  - {{name: b6s_{n}_r{e}h, trial: {t}, group: sweep, base: {n}, rebalance_every_h: {e}}}")
            t += 1
    append(f, L)
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("track", choices=sorted(TRACKS))
    ap.add_argument("--resolve-a4", action="store_true")
    ap.add_argument("--resolve-sweep", action="store_true")
    ap.add_argument("--sweep-start", type=int)
    a = ap.parse_args()
    if a.resolve_a4:
        sys.exit(resolve_a4())
    if a.resolve_sweep:
        sys.exit(resolve_sweep(a.track, a.sweep_start or TRACKS[a.track][1]))
    f = TRACKS[a.track][0]
    names = [LIVE, REF] + [r["name"] for r in doc(f)["runs"]]
    sys.exit(report(names, f"leaderboard_b6{a.track}.md"))
