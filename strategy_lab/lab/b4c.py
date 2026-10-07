"""Block 4c (long/short xsmom with intraday re-evaluation): resolvers and report (leaderboard_b4c_lsx.md).

    python -m lab.b4c --resolve-a1     # trial 299: best of stage A (291-298) with min_positions 1
    python -m lab.b4c --resolve-b      # trials 300-326 on the stage A winner
    python -m lab.b4c --resolve-c      # trials 327-333: neighbours of the stage B winner
    python -m lab.b4c --resolve-sweep  # trials 334-343: best 2 stage A runs at 1h-12h full re-selection
    python -m lab.b4c                  # report

Rules in variants_b4c_lsx.yaml (declared before any run). Each resolver appends run specs to that file;
they are committed before the runs.
"""

from __future__ import annotations

import argparse
import json
import sys

import numpy as np
import pandas as pd
import yaml

from lab import ROOT
from lab.b4e import CONTROL, HALVES
from lab.b4x import half_stats
from lab.events import load_events
from lab.leaderboard import N01, declared_total
from lab.runner import HCACHE, load_hourly, resolve_base

FILE = "variants_b4c_lsx.yaml"
LADDER = [1, 2, 4, 6, 8]


def runs() -> list[dict]:
    return yaml.safe_load((ROOT / FILE).read_text(encoding="utf-8"))["runs"]


def text() -> str:
    return (ROOT / FILE).read_text(encoding="utf-8")


def append(lines: list[str]) -> None:
    (ROOT / FILE).write_text(text().rstrip("\n") + "\n" + "\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


_EV = None


def stats(n: str) -> dict:
    global _EV
    if _EV is None:
        _EV = pd.DatetimeIndex(load_events(("CPI", "FOMC_DECISION"))["time"]).sort_values()
    h = load_hourly(n)
    if h is None:
        raise SystemExit(f"run {n} first")
    return half_stats(h, _EV)


def meets(s: dict) -> bool:
    return s["IS"]["meets"] and s["OOS"]["meets"]


def select(names: list[str]) -> tuple[str, dict]:
    """Declared selection rule: highest OOS P(>= +10%) among runs meeting both constraints in both halves,
    ties -> higher OOS median 14d; none meets -> highest OOS P(>= +10%) regardless."""
    st = {n: stats(n) for n in names}
    key = lambda n: (st[n]["OOS"]["p10"], st[n]["OOS"]["median"])
    q = [n for n in names if meets(st[n])] or names
    return max(q, key=key), st


def beats(s: dict, c: dict) -> bool:
    return all(s[k]["p10"] > c[k]["p10"] and s[k]["p8"] >= c[k]["p8"] and s[k]["meets"] for k in ("IS", "OOS"))


def spec_line(name: str, trial: int, group: str, params: dict, every: float | None = None) -> str:
    ps = ", ".join(f"{k}: {v}" for k, v in params.items())
    return (f"  - {{name: {name}, trial: {trial}, group: {group}, params: {{{ps}}}"
            f"{f', rebalance_every_h: {every:g}' if every else ''}}}")


def params_of(name: str) -> dict:
    r = next(r for r in runs() if r["name"] == name)
    return dict(r.get("params") or {})


def stage(g: str) -> list[str]:
    return [r["name"] for r in runs() if r.get("group") == g]


def resolve_a1() -> int:
    if "trial: 299," in text():
        print("already resolved")
        return 0
    a = stage("A")
    best, st = select(a)
    p = {**params_of(best), "min_positions": 1}
    append([f"  # resolved {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by lab/b4c.py --resolve-a1: best of 291-298 = {best} "
            f"(OOS P>=10% {st[best]['OOS']['p10']:.1%}, OOS median {st[best]['OOS']['median']:+.2%}, "
            f"meets {meets(st[best])})", spec_line("b4c_A1_minpos", 299, "A", p)])
    return 0


def resolve_b() -> int:
    if "trial: 300," in text():
        print("already resolved")
        return 0
    a = stage("A")
    if "b4c_A1_minpos" not in a:
        raise SystemExit("resolve and run 299 first")
    win, st = select(a)
    base = params_of(win)
    L = [f"  # resolved {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by lab/b4c.py --resolve-b: stage A winner = {win} "
         f"(OOS P>=10% {st[win]['OOS']['p10']:.1%}, OOS median {st[win]['OOS']['median']:+.2%}, meets {meets(st[win])})"]
    t = 300
    for c in (2, 4, 6):
        for w in (0.0, 0.3, 0.5):
            for m in (1.25, 1.5, 2.0):
                p = {**base, "check_h": c, "w": w, "swap_m": m, "min_hold_h": 6}
                L.append(spec_line(f"b4c_B_c{c}_w{int(w * 10):02d}_m{int(m * 100)}", t, "B", p, c))
                t += 1
    append(L)
    return 0


def resolve_c() -> int:
    if "trial: 327," in text():
        print("already resolved")
        return 0
    b = stage("B")
    win, st = select(b)
    p0 = params_of(win)
    c, w, m = int(p0["check_h"]), float(p0["w"]), float(p0["swap_m"])
    i = LADDER.index(c)
    nb = []
    for c2 in [LADDER[j] for j in (i - 1, i + 1) if 0 <= j < len(LADDER)]:
        nb.append(("c", {**p0, "check_h": c2}, c2))
    for w2 in (round(w - 0.2, 2), round(w + 0.2, 2)):
        if 0 <= w2 <= 1:
            nb.append(("w", {**p0, "w": w2}, c))
    for m2 in (m - 0.25, m + 0.25):
        nb.append(("m", {**p0, "swap_m": m2}, c))
    nb.append(("h", {**p0, "min_hold_h": 12}, c))
    existing = {json.dumps({k: v for k, v in params_of(n).items()}, sort_keys=True): n for n in b}
    L = [f"  # resolved {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by lab/b4c.py --resolve-c: stage B winner = {win} "
         f"(OOS P>=10% {st[win]['OOS']['p10']:.1%}, meets {meets(st[win])}); neighbours below"]
    t = 327
    for tag, p, every in nb:
        key = json.dumps(p, sort_keys=True)
        if key in existing:
            L.append(f"  # neighbour {tag}: same as stage B run {existing[key]} (re-used; slot {t} unused)")
        else:
            nm = f"b4c_C_{tag}_c{p['check_h']}_w{int(round(p['w'] * 10)):02d}_m{int(round(p['swap_m'] * 100))}_h{p['min_hold_h']}"
            L.append(spec_line(nm, t, "C", p, p["check_h"]))
        t += 1
    L.append(f"  # stage C winner under test: {win}; neighbour slots {327}-{t - 1} of 327-333 used")
    append(L)
    return 0


def neighbours() -> tuple[str | None, list[str]]:
    txt = text()
    if "--resolve-c: stage B winner = " not in txt:
        return None, []
    win = txt.split("--resolve-c: stage B winner = ")[1].split(" ")[0]
    nb = stage("C")
    nb += [ln.split("same as stage B run ")[1].split(" ")[0] for ln in txt.splitlines() if "same as stage B run" in ln]
    return win, nb


def resolve_sweep() -> int:
    if "trial: 334," in text():
        print("already resolved")
        return 0
    a = stage("A")
    st = {n: stats(n) for n in a}
    key = lambda n: (st[n]["OOS"]["p10"], st[n]["OOS"]["median"])
    q = sorted([n for n in a if meets(st[n])], key=key, reverse=True)
    best2 = (q + sorted([n for n in a if n not in q], key=key, reverse=True))[:2]
    L = [f"  # resolved {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by lab/b4c.py --resolve-sweep: best 2 stage A = {best2}"]
    t = 334
    for n in best2:
        for e in (1, 2, 4, 6, 12):
            L.append(spec_line(f"b4s_{n}_r{e}h", t, "sweep", params_of(n), e))
            t += 1
    append(L)
    return 0


def ls_detail(name: str) -> dict:
    p = HCACHE / f"{name}_pos.pkl"
    h = load_hourly(name)
    if not p.exists() or h is None:
        return {}
    pos = pd.read_pickle(p)
    out = {}
    for k, (a, b) in HALVES.items():
        x = pos[(pos["time"] >= (a or pos["time"].min())) & (pos["time"] <= (b or pos["time"].max()))]
        hj = h.loc[a:b]
        net = x.groupby("time")["w"].sum().reindex(hj.index, fill_value=0.0)
        eqm = float(hj["equity"].mean())
        n_ep = win = 0
        for _, g in x[x["w"] < -1e-9].sort_values("time").groupby("asset"):
            t = g["time"].values
            br = np.where(np.diff(t) > np.timedelta64(1, "h"))[0]
            edges = [0, *(br + 1), len(g)]
            for s0, s1 in zip(edges[:-1], edges[1:]):
                n_ep += 1
                win += float(g["ps"].iloc[s0:s1].sum()) > 0
        held = x[x["w"].abs() > 1e-6]
        out[k] = {"net_short": float((net < -1e-9).mean()), "eps": n_ep, "hit": win / n_ep if n_ep else None,
                  "long_pnl": float(x["pl"].sum()) / eqm, "short_pnl": float(x["ps"].sum()) / eqm,
                  "coins": float(held.groupby("time").size().reindex(hj.index, fill_value=0).mean()),
                  "max_w": float(x["w"].abs().max()) if len(x) else 0.0}
    return out


def corr_live(n: str) -> float | None:
    a, b = load_hourly(n), load_hourly(CONTROL)
    if a is None or b is None:
        return None
    da = a["equity"].loc[:HALVES["OOS"][1]].resample("1D").last().pct_change()
    db = b["equity"].loc[:HALVES["OOS"][1]].resample("1D").last().pct_change()
    j = pd.concat([da, db], axis=1).dropna()
    return float(j.iloc[:, 0].corr(j.iloc[:, 1]))


def report() -> int:
    have = [r["name"] for r in runs() if load_hourly(r["name"]) is not None]
    st = {n: stats(n) for n in [CONTROL] + have}
    c = st[CONTROL]
    pct = lambda x: "" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:+.1%}"
    pr = lambda x: "" if x is None else f"{x:.0%}"
    n_tr = declared_total()
    out = ["# Block 4c: long/short xsmom with intraday re-evaluation (live strategy = control)\n",
           f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC. Rules: `{FILE}` (declared before any run). Data to "
           "2026-06-30, both halves; Jul-Oct 2026 informational only._\n",
           f"**Trials:** {n_tr} declared across all blocks; luck threshold about {N01.inv_cdf(1 - 1 / n_tr):.1f} standard errors.\n"]
    winners = {}
    for g in ("A", "B", "C", "sweep"):
        names = [n for n in stage(g) if n in have]
        if not names:
            continue
        if g in ("A", "B") and len(names) == len(stage(g)):
            winners[g] = select(names)[0]
        out += [f"\n## Stage {g}{' (frequency sweep, not adoptable)' if g == 'sweep' else ''}"
                f"{': winner `' + winners[g] + '`' if g in winners else ''}\n",
                "| run | IS P>=10% / P>=8% / P<=-10% / worst / median | OOS P>=10% / P>=8% / P<=-10% / worst / median | meets | "
                "beats control | fees/yr OOS | trades/day OOS | INFO P>=10% / median |", "|---|---|---|---|---|---|---|---|"]
        cell = lambda s: f"{pr(s['p10'])} / {pr(s['p8'])} / {pr(s['pm10'])} / {pct(s['worst'])} / {pct(s['median'])}"
        for n in [CONTROL] + names:
            s = st[n]
            out.append(f"| {n}{' (control)' if n == CONTROL else ''} | {cell(s['IS'])} | {cell(s['OOS'])} | "
                       f"{'yes' if meets(s) else '**no**'} | {'' if n == CONTROL else ('**yes**' if beats(s, c) else 'no')} | "
                       f"{s['OOS']['fees_yr']:.1%} | {s['OOS']['trades_day']:.1f} | {pr(s['INFO'].get('p10'))} / "
                       f"{pct(s['INFO'].get('median'))} |")
    win, nb = neighbours()
    if win and all(n in have for n in nb):
        ok_w = beats(st[win], c)
        ok_nb = [n for n in nb if beats(st[n], c)]
        plateau = len(ok_nb) * 2 >= len(nb)
        verdict = ok_w and plateau
        out += ["\n## Adopt decision (stage C plateau test)\n",
                f"Final candidate `{win}`: beats the control in both halves: **{'yes' if ok_w else 'no'}**. Neighbours beating the "
                f"control: {len(ok_nb)} of {len(nb)} ({', '.join(ok_nb) or 'none'}): plateau **{'yes' if plateau else 'no'}**.\n",
                f"**Verdict: {'ADOPT (implement behind flags, testing key only)' if verdict else 'NOT ADOPTED'}**\n"]
    out += ["\n## Long/short detail, rule firing, correlation with live\n",
            "Net short = share of hours with a negative net book. Short episode = continuous short holding of one coin; hit = its "
            "P&L > 0. P&L = sum over the half / mean equity. Counters over the whole run (lab/backtest extra.strategy_stats).\n",
            "| run | period | net short | short episodes / hit | long P&L | short P&L | avg coins | max coin weight | "
            "exits / swaps / flips / fallback | corr. daily ret. with live (to 2026-06) |", "|---|---|---|---|---|---|---|---|---|---|"]
    for n in have:
        d = ls_detail(n)
        m = json.loads((ROOT / "runs" / n / "result.json").read_text())
        ss = (m.get("extra") or {}).get("strategy_stats") or {}
        cr = corr_live(n)
        for k, v in d.items():
            out.append(f"| {n} | {k} | {pr(v['net_short'])} | {v['eps']} / {pr(v['hit'])} | {pct(v['long_pnl'])} | "
                       f"{pct(v['short_pnl'])} | {v['coins']:.1f} | {v['max_w']:.0%} | {ss.get('exits', 0)} / "
                       f"{ss.get('swaps', 0)} / {ss.get('flips', 0)} / {ss.get('fallback_min_pos', 0)} | "
                       f"{'' if cr is None or k != 'IS' else format(cr, '.2f')} |")
    (ROOT / "leaderboard_b4c_lsx.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"winners: {winners}; stage C: {win} neighbours {nb}")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    for f in ("resolve-a1", "resolve-b", "resolve-c", "resolve-sweep"):
        ap.add_argument(f"--{f}", action="store_true")
    a = ap.parse_args()
    if a.resolve_a1:
        sys.exit(resolve_a1())
    if a.resolve_b:
        sys.exit(resolve_b())
    if a.resolve_c:
        sys.exit(resolve_c())
    if a.resolve_sweep:
        sys.exit(resolve_sweep())
    sys.exit(report())
