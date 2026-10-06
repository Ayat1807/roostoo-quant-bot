"""Resolve the block-3 addendum's sweep slots b and c (rule declared in variants_b3_addendum.yaml).

    python -m lab.b3_sweep          # after all block-3 runs; appends runs 253-267 to the addendum

Uses data to 2026-06-30 only (the same windows as lab/b3.py):
  b: the "best of i" xsmom universe (core10 / alt10 / R1) by OOS P(>= +10%), ties IS
  c: the top 2 block-3 runs under the selection rule (meeting both constraints in both halves,
     by OOS P(>= +10%), ties IS; topped up by OOS P(>= +10%) if fewer than 2 qualify), excluding
     xsmom runs, combos and sweep runs
Each gets the 5 refreshes in sweep_refresh_h other than its own (253-257 for b, 258-262 and
263-267 for c).
"""

from __future__ import annotations

import sys

import yaml

from lab import ROOT
from lab.b3 import IS_END, OOS0, OOS_END, windows, wstats
from lab.runner import load_hourly, resolve_base

ADD = ROOT / "variants_b3_addendum.yaml"


def scores(name: str) -> tuple[dict, dict]:
    h = load_hourly(name)
    if h is None:
        raise RuntimeError(f"run {name} first")
    return wstats(windows(h, None, IS_END)), wstats(windows(h, OOS0, OOS_END))


def meets(s: dict) -> bool:
    return s.get("n", 0) > 0 and s["pm10"] <= 0.10 and s["worst"] >= -0.20


def main() -> int:
    add = yaml.safe_load(ADD.read_text(encoding="utf-8"))
    if any(r.get("trial", 0) >= 253 for r in add["runs"]):
        print("already resolved")
        return 0
    b3 = yaml.safe_load((ROOT / "variants_b3.yaml").read_text(encoding="utf-8"))
    refresh = add["sweep_refresh_h"]
    # b
    i_runs = ["b3_xsmom_core10", "b3_xsmom_alt10", "b3_xsmom_r1"]
    sc = {n: scores(n) for n in i_runs}
    best_i = max(i_runs, key=lambda n: (sc[n][1].get("p10", -1), sc[n][0].get("p10", -1)))
    # c
    cands = [r["name"] for r in b3["runs"] if "combo" not in r and not r["name"].startswith("b3_xsmom")]
    allsc = {n: scores(n) for n in cands}
    key = lambda n: (allsc[n][1].get("p10", -1), allsc[n][0].get("p10", -1))
    q = sorted([n for n in cands if meets(allsc[n][0]) and meets(allsc[n][1])], key=key, reverse=True)
    rest = sorted([n for n in cands if n not in q], key=key, reverse=True)
    top2 = (q + rest)[:2]
    lines: list[str] = []

    def emit(base: str, first_trial: int, label: str) -> None:
        own = float(resolve_base(base).get("rebalance_every_h", 24))
        lines.append(f"  # {label}: {base} (own refresh {own:g}h, skipped)")
        for t, r in zip(range(first_trial, first_trial + 5), [r for r in refresh if float(r) != own][:5]):
            lines.append(f"  - {{name: b3s_{base[3:]}_r{r}h, trial: {t}, group: sweep, base: {base}, "
                         f"rebalance_every_h: {r}}}")

    emit(best_i, 253, "b, best of i by OOS P(>=+10%): "
         + ", ".join(f"{n} {sc[n][1].get('p10', 0):.0%}" for n in i_runs))
    for k, (n, first) in enumerate(zip(top2, (258, 263))):
        emit(n, first, f"c{k + 1}, OOS P(>=+10%) {allsc[n][1].get('p10', 0):.0%}, meets both halves: "
                       f"{meets(allsc[n][0]) and meets(allsc[n][1])}")
    txt = ADD.read_text(encoding="utf-8").rstrip("\n") + "\n" + "\n".join(lines) + "\n"
    ADD.write_text(txt, encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
