"""Shared report / resolvers for blocks 4d (entry timing) and 4b (sizing / exposure / coins).

    python -m lab.b4gen 4d [--resolve-sweep]
    python -m lab.b4gen 4b [--resolve-best-sizing | --resolve-sweep]

Selection rule (both blocks, declared): highest OOS P(14d >= +10%) among runs meeting both constraints in both halves,
ties higher OOS median 14d. Adopt: P(>= +10%) strictly above the control and P(>= +8%) not below in both halves,
constraints met in both halves; sweep runs are not adoptable.
"""

from __future__ import annotations

import argparse
import json
import sys

import numpy as np
import pandas as pd
import yaml

from lab import ROOT
from lab.b3 import windows
from lab.b4c import beats, meets, spec_line, stats
from lab.b4e import CONTROL, HALVES
from lab.data import load_close
from lab.leaderboard import N01, declared_total
from lab.runner import HCACHE, load_hourly

BLOCKS = {"4d": ("variants_b4d_entry.yaml", "leaderboard_b4d_entry.md", "Entry timing", 349),
          "4b": ("variants_b4b_sizing.yaml", "leaderboard_b4b_sizing.md", "Sizing, exposure, number of coins", 384)}


def doc(f: str) -> dict:
    return yaml.safe_load((ROOT / f).read_text(encoding="utf-8"))


def append(f: str, lines: list[str]) -> None:
    p = ROOT / f
    p.write_text(p.read_text(encoding="utf-8").rstrip("\n") + "\n" + "\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


def select(names: list[str]) -> str:
    st = {n: stats(n) for n in names}
    q = [n for n in names if meets(st[n])] or names
    return max(q, key=lambda n: (st[n]["OOS"]["p10"], st[n]["OOS"]["median"]))


def resolve_sweep(block: str) -> int:
    f, _, _, t0 = BLOCKS[block]
    if f"trial: {t0}," in (ROOT / f).read_text(encoding="utf-8"):
        print("already resolved")
        return 0
    runs = [r for r in doc(f)["runs"] if r.get("group") != "sweep"]
    names = [r["name"] for r in runs]
    st = {n: stats(n) for n in names}
    key = lambda n: (st[n]["OOS"]["p10"], st[n]["OOS"]["median"])
    q = sorted([n for n in names if meets(st[n])], key=key, reverse=True)
    best2 = (q + sorted([n for n in names if n not in q], key=key, reverse=True))[:2]
    L = [f"  # resolved {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by lab/b4gen.py {block} --resolve-sweep: best 2 = {best2}"]
    t = t0
    for n in best2:
        for e in (1, 2, 4, 6, 12):
            L.append(f"  - {{name: b4s_{n}_r{e}h, trial: {t}, group: sweep, base: {n}, rebalance_every_h: {e}}}")
            t += 1
    append(f, L)
    return 0


def resolve_best_sizing() -> int:
    f = BLOCKS["4b"][0]
    if "trial: 372," in (ROOT / f).read_text(encoding="utf-8"):
        print("already resolved")
        return 0
    runs = doc(f)["runs"]
    sz = [r["name"] for r in runs if r.get("group") == "sizing"]
    best = select(sz)
    bp = next(r for r in runs if r["name"] == best)["params"]
    L = [f"  # resolved {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by lab/b4gen.py 4b --resolve-best-sizing: best sizing = {best}"]
    t = 372
    for ex in ("breadth", "vol_target", "regime", "conviction"):
        line = spec_line(f"b4b_best_{ex}", t, "exposure_best", {**bp, "exposure": ex})
        if ex == "conviction":
            line = line[:-1] + ", lookback_bars: 10760}"
        L.append(line)
        t += 1
    append(f, L)
    return 0


def pos_detail(name: str) -> dict:
    """avg coins held, max single-coin weight, worst single-coin contribution in the 5 worst 14d windows (per half)."""
    p = HCACHE / f"{name}_pos.pkl"
    h = load_hourly(name)
    if not p.exists() or h is None:
        return {}
    pos = pd.read_pickle(p)
    out = {}
    for k, (a, b) in HALVES.items():
        x = pos[(pos["time"] >= (a or pos["time"].min())) & (pos["time"] <= (b or pos["time"].max()))]
        hj = h.loc[a:b]
        held = x[x["w"].abs() > 1e-6]
        w = windows(h, a, b)
        worst = None
        if not w.empty:
            for s in w.nsmallest(5, "ret")["start"]:
                e0 = float(h["equity"].asof(s))
                y = x[(x["time"] > s) & (x["time"] <= s + pd.Timedelta(days=14))]
                c = (y.groupby("asset")["pl"].sum() + y.groupby("asset")["ps"].sum()) / e0
                if len(c) and (worst is None or c.min() < worst[1]):
                    worst = (c.idxmin(), float(c.min()), str(s.date()))
        out[k] = {"coins": float(held.groupby("time").size().reindex(hj.index, fill_value=0).mean()),
                  "max_w": float(held["w"].abs().max()) if len(held) else 0.0, "worst_coin": worst}
    return out


def entry_detail(name: str, ctrl_entries: pd.DataFrame | None) -> dict:
    """New entries: mean (entry close / highest close of the previous 72h - 1); big winning trends missed vs the control."""
    p = HCACHE / f"{name}_pos.pkl"
    if not p.exists():
        return {}
    pos = pd.read_pickle(p)
    ent = new_entries(pos)
    closes = _closes(sorted(ent["asset"].unique()) + (sorted(ctrl_entries["asset"].unique()) if ctrl_entries is not None else []))
    out = {}
    for k, (a, b) in HALVES.items():
        e = ent[(ent["time"] >= (a or ent["time"].min())) & (ent["time"] <= (b or ent["time"].max()))]
        vs = []
        for _, r in e.iterrows():
            s = closes[r["asset"]].loc[:r["time"]]
            if len(s) > 73:
                vs.append(float(s.iloc[-1]) / float(s.iloc[-73:-1].max()) - 1)
        missed = gains = 0
        if ctrl_entries is not None:
            ce = ctrl_entries[(ctrl_entries["time"] >= (a or ctrl_entries["time"].min()))
                              & (ctrl_entries["time"] <= (b or ctrl_entries["time"].max()))]
            heldset = pos[pos["w"] > 1e-6][["time", "asset"]]
            for _, r in ce.iterrows():
                s = closes[r["asset"]].loc[r["time"]:r["time"] + pd.Timedelta(days=14)]
                if len(s) < 2 or s.max() / s.iloc[0] - 1 < 0.20:
                    continue
                hv = heldset[(heldset["asset"] == r["asset"]) & (heldset["time"] >= r["time"])
                             & (heldset["time"] <= r["time"] + pd.Timedelta(hours=24))]
                if hv.empty:
                    missed += 1
                    gains += float(s.max() / s.iloc[0] - 1)
        out[k] = {"n_entries": int(len(e)), "vs_3d_high": float(np.mean(vs)) if vs else None,
                  "missed": missed, "missed_gain": gains / missed if missed else None}
    return out


_C: dict = {}


def _closes(assets: list[str]) -> dict:
    need = [a for a in dict.fromkeys(assets) if a not in _C]
    if need:
        c = load_close(need)
        for a in need:
            _C[a] = c[a].dropna()
    return _C


def new_entries(pos: pd.DataFrame) -> pd.DataFrame:
    """(time, asset) where a long position appears (weight > 0 now, not held the hour before)."""
    x = pos[pos["w"] > 1e-6][["time", "asset"]].sort_values(["asset", "time"])
    prev = x.groupby("asset")["time"].shift(1)
    return x[(prev.isna()) | (x["time"] - prev > pd.Timedelta(hours=1))].reset_index(drop=True)


def report(block: str) -> int:
    f, out_md, title, _ = BLOCKS[block]
    runs = doc(f)["runs"]
    have = [r["name"] for r in runs if load_hourly(r["name"]) is not None]
    st = {n: stats(n) for n in [CONTROL] + have}
    c = st[CONTROL]
    adopt = sorted([n for n in have if not n.startswith("b4s_") and beats(st[n], c)],
                   key=lambda n: (st[n]["OOS"]["p10"], st[n]["OOS"]["median"]), reverse=True)
    pct = lambda x: "" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:+.1%}"
    pr = lambda x: "" if x is None else f"{x:.0%}"
    n_tr = declared_total()
    L = [f"# Block {block}: {title} (live strategy xsmom on R1 = control)\n",
         f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC. Rules: `{f}` (declared before any run). Data to 2026-06-30, "
         "both halves; Jul-Oct 2026 informational only._\n",
         f"**Trials:** {n_tr} declared across all blocks; luck threshold about {N01.inv_cdf(1 - 1 / n_tr):.1f} standard errors.\n",
         f"**Adopted: {'`' + adopt[0] + '`' if adopt else 'none'}**{' (also passing: ' + ', '.join(adopt[1:]) + ')' if len(adopt) > 1 else ''}\n",
         f"Not yet run: {', '.join(r['name'] for r in runs if r['name'] not in have) or 'none'}\n",
         "| run | group | IS P>=10% / P>=8% / P<=-10% / worst / median | OOS P>=10% / P>=8% / P<=-10% / worst / median | meets | "
         "beats control | fees/yr OOS | trades/day OOS | INFO P>=10% / median |", "|---|---|---|---|---|---|---|---|---|"]
    cell = lambda s: f"{pr(s['p10'])} / {pr(s['p8'])} / {pr(s['pm10'])} / {pct(s['worst'])} / {pct(s['median'])}"
    grp = {r["name"]: r.get("group", "") for r in runs}
    for n in [CONTROL] + have:
        s = st[n]
        L.append(f"| {n}{' (control)' if n == CONTROL else ''} | {grp.get(n, '')} | {cell(s['IS'])} | {cell(s['OOS'])} | "
                 f"{'yes' if meets(s) else '**no**'} | {'' if n == CONTROL else ('**yes**' if beats(s, c) else 'no')} | "
                 f"{s['OOS']['fees_yr']:.1%} | {s['OOS']['trades_day']:.1f} | {pr(s['INFO'].get('p10'))} / "
                 f"{pct(s['INFO'].get('median'))} |")
    if block == "4b":
        L += ["\n## Concentration\n", "| run | period | avg coins held | max coin weight | worst single-coin contribution in the "
              "5 worst 14d windows |", "|---|---|---|---|---|"]
        for n in have:
            for k, v in pos_detail(n).items():
                wc = v["worst_coin"]
                L.append(f"| {n} | {k} | {v['coins']:.1f} | {v['max_w']:.0%} | "
                         f"{'' if wc is None else f'{wc[0]} {wc[1]:+.1%} (window from {wc[2]})'} |")
    if block == "4d":
        ctrl_pos = HCACHE / "b4d__control_pos.pkl"
        ctrl = new_entries(pd.read_pickle(ctrl_pos)) if ctrl_pos.exists() else None
        L += ["\n## Entries\n", "Entry vs 3-day high = entry close / highest close of the previous 72h - 1 (mean over new entries). "
              "Missed = control entries that rose >= +20% within 14 days which the variant did not hold in the next 24h.\n",
              "| run | period | new entries | entry vs 3d high | big winners missed (mean gain) | limit fill rate |",
              "|---|---|---|---|---|---|"]
        for n in (["b4d__control"] if ctrl is not None else []) + have:
            m = json.loads((ROOT / "runs" / n / "result.json").read_text()) if (ROOT / "runs" / n / "result.json").exists() else {}
            el = (m.get("extra") or {}).get("entry_limits")
            fr = None
            if el:
                fr = sum(1 for x in el if x["filled"]) / len(el)
            for k, v in entry_detail(n, None if n == "b4d__control" else ctrl).items():
                L.append(f"| {n} | {k} | {v['n_entries']} | {pct(v['vs_3d_high'])} | {v['missed']} ({pct(v['missed_gain'])}) | "
                         f"{'' if fr is None or k != 'IS' else f'{fr:.0%} of {len(el)} (whole run)'} |")
    (ROOT / out_md).write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"adopted: {adopt[:3]}")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("block", choices=sorted(BLOCKS))
    ap.add_argument("--resolve-sweep", action="store_true")
    ap.add_argument("--resolve-best-sizing", action="store_true")
    a = ap.parse_args()
    if a.resolve_sweep:
        sys.exit(resolve_sweep(a.block))
    if a.resolve_best_sizing:
        sys.exit(resolve_best_sizing())
    sys.exit(report(a.block))
