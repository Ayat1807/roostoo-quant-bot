"""Block 4a addendum report (intraday exits + frequency sweep): leaderboard_b4_exits.md.

    python -m lab.b4x --resolve   # pick the best 2 of block 4a by the declared rule, append sweep runs
    python -m lab.b4x             # report

Rules: variants_b4_exits.yaml (declared before any run). Data to 2026-06-30 (IS / OOS); Jul-Oct 2026 info only.
"""

from __future__ import annotations

import argparse
import json
import sys

import numpy as np
import pandas as pd
import yaml

from lab import ROOT
from lab.b3 import IS_END, OOS0, OOS_END, windows
from lab.b4e import CONTROL, HALVES, tag_windows
from lab.events import load_events
from lab.leaderboard import N01, declared_total
from lab.runner import load_hourly

FILE = "variants_b4_exits.yaml"
SWEEP = [1, 2, 4, 6, 12]


def block_runs() -> list[str]:
    ev = yaml.safe_load((ROOT / "variants_b4_events.yaml").read_text(encoding="utf-8"))["runs"]
    ex = yaml.safe_load((ROOT / FILE).read_text(encoding="utf-8"))["runs"]
    return [r["name"] for r in ev] + [r["name"] for r in ex if r.get("group") == "exits"]


def half_stats(h: pd.DataFrame, ev: pd.DatetimeIndex) -> dict:
    out = {}
    for k, (a, b) in HALVES.items():
        w = windows(h, a, b)
        if w.empty:
            out[k] = {"n": 0}
            continue
        w = tag_windows(w, ev)
        r, re_ = w["ret"], w.loc[w["has_event"], "ret"]
        hj = h.loc[a:b]
        yrs = (hj.index[-1] - hj.index[0]) / pd.Timedelta(days=365)
        out[k] = {"n": int(len(r)), "p10": float((r >= .10).mean()), "p8": float((r >= .08).mean()),
                  "pm10": float((r <= -.10).mean()), "worst": float(r.min()), "median": float(r.median()),
                  "ev_p10": float((re_ >= .10).mean()), "fees_yr": float(hj["fees"].sum() / hj["equity"].mean() / yrs),
                  "trades_day": float(hj["trades"].groupby(hj.index.floor("D")).sum().mean())}
        out[k]["meets"] = out[k]["pm10"] <= 0.10 and out[k]["worst"] >= -0.20
    return out


def exit_summary(name: str) -> dict | None:
    p = ROOT / "runs" / name / "result.json"
    if not p.exists():
        return None
    x = (json.loads(p.read_text()).get("extra") or {}).get("exits")
    if x is None:
        return None
    df = pd.DataFrame(x)
    out = {}
    for k, (a, b) in HALVES.items():
        if df.empty:
            out[k] = {"n": 0}
            continue
        t = pd.to_datetime(df["time"], utc=True)
        d = df[(t >= (a or t.min())) & (t <= (b or t.max()))]
        days = ((b or t.max()) - (a or pd.Timestamp("2020-02-15", tz="UTC"))) / pd.Timedelta(days=1)
        out[k] = {"n": int(len(d)), "per_month": float(len(d) / days * 30.4),
                  "avoided": float(-d.loc[d["pnl_frac"] < 0, "pnl_frac"].sum()),
                  "given_up": float(d.loc[d["pnl_frac"] > 0, "pnl_frac"].sum()),
                  "n_avoided": int((d["pnl_frac"] < 0).sum()), "n_given": int((d["pnl_frac"] > 0).sum())}
    return out


def collect() -> dict:
    ev = pd.DatetimeIndex(load_events(("CPI", "FOMC_DECISION"))["time"]).sort_values()
    rows = {}
    for n in [CONTROL] + block_runs():
        h = load_hourly(n)
        if h is not None:
            rows[n] = half_stats(h, ev)
    return rows


def resolve() -> int:
    doc_txt = (ROOT / FILE).read_text(encoding="utf-8")
    if "{name: b4s_" in doc_txt:
        print("sweep already resolved")
        return 0
    rows = collect()
    cand = [n for n in rows if n != CONTROL and not n.startswith("b4e_fast_")]
    missing = [n for n in block_runs() if n not in rows]
    if missing:
        raise SystemExit(f"run these first: {missing}")
    key = lambda n: (rows[n]["OOS"]["p10"], rows[n]["IS"]["p10"])
    q = sorted([n for n in cand if rows[n]["IS"]["meets"] and rows[n]["OOS"]["meets"]], key=key, reverse=True)
    rest = sorted([n for n in cand if n not in q], key=key, reverse=True)
    best = (q + rest)[:2]
    lines = [f"  # resolved {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by lab/b4x.py --resolve: best 2 = {best} "
             f"(OOS / IS P>=10%: " + ", ".join(f"{n} {rows[n]['OOS']['p10']:.1%} / {rows[n]['IS']['p10']:.1%}"
                                                 for n in best) + ")"]
    t = 281
    for n in best:
        for every in SWEEP:
            lines.append(f"  - {{name: b4s_{n}_r{every}h, trial: {t}, group: sweep, base: {n}, rebalance_every_h: {every}}}")
            t += 1
    (ROOT / FILE).write_text(doc_txt.rstrip("\n") + "\n" + "\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


def report() -> int:
    rows = collect()
    doc = yaml.safe_load((ROOT / FILE).read_text(encoding="utf-8"))
    sweep = [r for r in doc["runs"] if r.get("group") == "sweep"]
    for r in sweep:
        h = load_hourly(r["name"])
        if h is not None:
            ev = pd.DatetimeIndex(load_events(("CPI", "FOMC_DECISION"))["time"]).sort_values()
            rows[r["name"]] = half_stats(h, ev)
    c = rows[CONTROL]
    adopt = []
    for n in rows:
        if not n.startswith("b4x_"):
            continue
        ok = all(rows[n][k]["p10"] > c[k]["p10"] and rows[n][k]["p8"] >= c[k]["p8"] and rows[n][k]["meets"]
                 for k in ("IS", "OOS"))
        rows[n]["adopt"] = ok
        if ok:
            adopt.append(n)
    adopt.sort(key=lambda n: (rows[n]["OOS"]["p10"], rows[n]["IS"]["p10"]), reverse=True)
    pct = lambda x: "" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:+.1%}"
    pr = lambda x: "" if x is None else f"{x:.0%}"
    n_tr = declared_total()
    L = ["# Block 4a addendum: intraday exits + frequency sweep (live strategy xsmom on R1)\n",
         f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC. Rules in `{FILE}` (declared before any run). "
         "Judged on data to 2026-06-30, both halves; Jul-Oct 2026 informational only._\n",
         f"**Trials:** {n_tr} declared across all blocks; luck threshold about {N01.inv_cdf(1 - 1 / n_tr):.1f} "
         "standard errors.\n",
         "**Exit adopt rule:** P(14d >= +10%) strictly above the control and P(>= +8%) not below, both halves, both "
         "constraints met in both halves.\n",
         f"**Exit adopted: {'`' + adopt[0] + '`' if adopt else 'none'}**\n",
         "| run | IS P>=10% / P>=8% / P<=-10% / worst / median | OOS P>=10% / P>=8% / P<=-10% / worst / median | "
         "event windows P>=10% IS / OOS | meets | fees/yr OOS | trades/day OOS | INFO P>=10% / median |",
         "|---|---|---|---|---|---|---|---|"]
    cell = lambda s: f"{pr(s['p10'])} / {pr(s['p8'])} / {pr(s['pm10'])} / {pct(s['worst'])} / {pct(s['median'])}"
    for n, r in rows.items():
        i, o, f = r["IS"], r["OOS"], r["INFO"]
        L.append(f"| {n}{' (control)' if n == CONTROL else ''} | {cell(i)} | {cell(o)} | {pr(i['ev_p10'])} / "
                 f"{pr(o['ev_p10'])} | {'yes' if i['meets'] and o['meets'] else '**no**'} | {o['fees_yr']:.1%} | "
                 f"{o['trades_day']:.1f} | {pr(f.get('p10'))} / {pct(f.get('median'))} |")
    L += ["\n## How often the exits fired; loss avoided vs profit given up\n",
          "Each exit: exited weight x the coin's return from the exit to the next daily decision. Loss avoided = "
          "the coin fell further (sum, % of equity); profit given up = it rose. Net = avoided - given up.\n",
          "| run | period | exits | per month | loss avoided (n) | profit given up (n) | net |", "|---|---|---|---|---|---|---|"]
    for n in rows:
        es = exit_summary(n) if n.startswith("b4x_") else None
        if not es:
            continue
        for k, v in es.items():
            if not v.get("n"):
                continue
            L.append(f"| {n} | {k} | {v['n']} | {v['per_month']:.1f} | {v['avoided']:+.1%} ({v['n_avoided']}) | "
                     f"{v['given_up']:+.1%} ({v['n_given']}) | {v['avoided'] - v['given_up']:+.1%} |")
    (ROOT / "leaderboard_b4_exits.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"exit adopted: {adopt[0] if adopt else None}")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--resolve", action="store_true")
    sys.exit(resolve() if ap.parse_args().resolve else report())
