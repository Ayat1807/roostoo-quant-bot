"""Block 7 (combinations): report with margin-vs-luck statistics, sweep resolver. Rules: variants_b7_combo.yaml.

    python -m lab.b7 --resolve-sweep
    python -m lab.b7          # leaderboard_b7.md (b5 tables + margin vs luck)
"""

from __future__ import annotations

import argparse
import sys

import numpy as np
import pandas as pd
import yaml

from lab import ROOT
from lab.b3 import windows
from lab.b5 import HALVES, LIVE, REF, judge, rank, report
from lab.b6 import append, doc
from lab.leaderboard import N01, declared_total
from lab.runner import load_hourly

FILE = "variants_b7_combo.yaml"
REF_RUN = "b3_s3v2e_core10"


def margins(name: str) -> dict:
    """Per half: margin and t vs the reference for mean 14d return (paired, overlap-corrected) and median composite
    (14-day moving-block bootstrap, 2000 draws)."""
    out = {}
    rng = np.random.default_rng(0)
    for k in ("IS", "OOS"):
        a, b = HALVES[k]
        wc, wr = windows(load_hourly(name), a, b), windows(load_hourly(REF_RUN), a, b)
        m = wc.merge(wr, on="start", suffixes=("", "_r"))
        d = (m["ret"] - m["ret_r"]).values
        n = len(d)
        se_mean = d.std(ddof=1) / np.sqrt(n / 14) if n > 28 else np.nan
        c1, c0 = m["comp"].values, m["comp_r"].values
        med_diff = float(np.median(c1) - np.median(c0))
        nb = int(np.ceil(n / 14))
        boots = []
        for _ in range(2000):
            starts = rng.integers(0, n - 14, nb)
            ix = np.concatenate([np.arange(s, s + 14) for s in starts])[:n]
            boots.append(np.median(c1[ix]) - np.median(c0[ix]))
        se_med = float(np.std(boots, ddof=1))
        out[k] = {"mean_diff": float(d.mean()), "t_mean": float(d.mean() / se_mean) if se_mean else np.nan,
                  "med_diff": med_diff, "t_med": med_diff / se_med if se_med > 0 else np.nan, "n": n}
    return out


def resolve_sweep() -> int:
    if "trial: 487," in (ROOT / FILE).read_text(encoding="utf-8"):
        print("already resolved")
        return 0
    names = [r["name"] for r in doc(FILE)["runs"] if r.get("group") != "sweep"]
    J = {n: judge(n) for n in names}
    best2 = rank(names, J)[:2]
    L = [f"  # resolved {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by lab/b7.py --resolve-sweep: best 2 = {best2}"]
    t = 487
    for n in best2:
        for e in (1, 2, 4, 6, 12):
            L.append(f"  - {{name: b7s_{n}_r{e}h, trial: {t}, group: sweep, base: {n}, rebalance_every_h: {e}}}")
            t += 1
    append(FILE, L)
    return 0


def main_report() -> int:
    runs = [r["name"] for r in doc(FILE)["runs"]]
    names = [LIVE, REF] + ["b6b_hmm2", "b6c_erc", "b6a_A3_cusum4_c50"] + runs
    report(names, "leaderboard_b7.md")
    lt = N01.inv_cdf(1 - 1 / declared_total())
    have = [n for n in ["b6b_hmm2", "b6c_erc", "b6a_A3_cusum4_c50"] + runs if load_hourly(n) is not None]
    L = ["\n## Margin vs the reference (b3_s3v2e_core10) and the luck threshold\n",
         f"t = margin / standard error (see variants_b7_combo.yaml). Luck threshold for {declared_total()} declared trials: "
         f"about {lt:.1f} SE. A margin is distinguishable from selection luck only if t exceeds it.\n",
         "| run | half | mean 14d diff | t | median composite diff | t | beats on both (sign) | clears luck threshold on both |",
         "|---|---|---|---|---|---|---|---|"]
    for n in have:
        mg = margins(n)
        for k, v in mg.items():
            both = v["mean_diff"] > 0 and v["med_diff"] > 0
            clear = both and v["t_mean"] > lt and v["t_med"] > lt
            L.append(f"| {n} | {k} | {v['mean_diff']:+.2%} | {v['t_mean']:+.2f} | {v['med_diff']:+.2f} | {v['t_med']:+.2f} | "
                     f"{'yes' if both else 'no'} | {'yes' if clear else 'no'} |")
    p = ROOT / "leaderboard_b7.md"
    p.write_text(p.read_text(encoding="utf-8") + "\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--resolve-sweep", action="store_true")
    a = ap.parse_args()
    sys.exit(resolve_sweep() if a.resolve_sweep else main_report())
