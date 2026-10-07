"""Block 5 judging (risk-adjusted + down markets): leaderboard_b5.md. Rules in variants_b5_shorts.yaml.

    python -m lab.b5 --resolve-f       # combos 402-404 (best C, best E)
    python -m lab.b5 --resolve-sweep   # 405-408 (best 2 of B-E at 4h / 12h)
    python -m lab.b5 [runs ...]        # report (default: references + every block-5 run that exists)
"""

from __future__ import annotations

import argparse
import sys

import numpy as np
import pandas as pd
import yaml

from lab import ROOT
from lab.b3 import INFO0, IS_END, OOS0, OOS_END, fwd, windows
from lab.b4c import ls_detail
from lab.data import load_close
from lab.leaderboard import N01, declared_total
from lab.runner import load_hourly
from lab.scorecard import btc_daily_features, by_regime, classify_regimes, metrics

FILE = "variants_b5_shorts.yaml"
REF = "b5ref__b3_s3v2e_core10"            # best existing reference (adopt rule)
LIVE = "b4d__control"                     # live xsmom R1 with recorded positions (== b3_xsmom_r1)
REFS = [("live xsmom R1", LIVE), ("s3v2e_core10", REF), ("s3v2e_tv06_core10", "b5ref__b3_s3v2e_tv06_core10"),
        ("50/50 s3v2e + xsmom R1", "b5ref__c50_s3v2e_xsmom_r1"), ("regime_switch core10", "b5ref__b3_regime_core10")]
HALVES = {"IS": (None, IS_END), "OOS": (OOS0, OOS_END), "INFO": (INFO0, None)}
_BTC = None


def btc() -> pd.Series:
    global _BTC
    if _BTC is None:
        _BTC = load_close(["BTCUSDT"])["BTCUSDT"]
    return _BTC


def judge(name: str) -> dict:
    h = load_hourly(name)
    if h is None:
        raise SystemExit(f"run {name} first")
    b = btc()
    out: dict = {}
    for k, (a, e) in HALVES.items():
        w = windows(h, a, e)
        if w.empty:
            out[k] = {"n": 0}
            continue
        w["btc"] = [b.asof(s + pd.Timedelta(days=14)) / b.asof(s) - 1 for s in w["start"]]
        r = w["ret"]
        dn, up = w[w["btc"] < -0.05], w[w["btc"] > 0.05]
        fl = w[(w["btc"] >= -0.05) & (w["btc"] <= 0.05)]
        x = h.loc[a:e]
        m = metrics(x["equity"].values)
        yrs = (x.index[-1] - x.index[0]) / pd.Timedelta(days=365)
        out[k] = {"n": int(len(r)), "comp": float(w["comp"].median()), "mean": float(r.mean()),
                  "median": float(r.median()), "pm10": float((r <= -0.10).mean()), "worst": float(r.min()),
                  "p10": float((r >= 0.10).mean()), "sharpe": m.get("sharpe"), "mdd": m.get("mdd"),
                  "down": float(dn["ret"].mean()) if len(dn) else None, "n_down": int(len(dn)),
                  "up": float(up["ret"].mean()) if len(up) else None, "n_up": int(len(up)),
                  "flat": float(fl["ret"].mean()) if len(fl) else None, "n_flat": int(len(fl)),
                  "down_pos": float((dn["ret"] > 0).mean()) if len(dn) else None,
                  "fees_yr": float(x["fees"].sum() / x["equity"].mean() / yrs),
                  "trades_day": float(x["trades"].groupby(x.index.floor("D")).sum().mean())}
    req = {k: (out[k]["down"] is not None and out[k]["down"] > 0 and out[k]["pm10"] <= 0.05 and out[k]["worst"] >= -0.15)
           for k in ("IS", "OOS")}
    out["meets"] = req["IS"] and req["OOS"] and (out["OOS"]["sharpe"] or 0) >= 1.0
    out["req"] = req
    return out


def beats_ref(j: dict, r: dict) -> bool:
    return all(j[k]["comp"] > r[k]["comp"] and j[k]["mean"] > r[k]["mean"] for k in ("IS", "OOS"))


def rank(names: list[str], J: dict) -> list[str]:
    key = lambda n: (J[n]["OOS"]["comp"], J[n]["OOS"]["mean"])
    q = sorted([n for n in names if J[n]["meets"]], key=key, reverse=True)
    return q + sorted([n for n in names if n not in q], key=key, reverse=True)


def runs() -> list[dict]:
    return yaml.safe_load((ROOT / FILE).read_text(encoding="utf-8"))["runs"]


def append(lines: list[str]) -> None:
    p = ROOT / FILE
    p.write_text(p.read_text(encoding="utf-8").rstrip("\n") + "\n" + "\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


def resolve_f() -> int:
    if "trial: 402," in (ROOT / FILE).read_text(encoding="utf-8"):
        print("already resolved")
        return 0
    g = {r["name"]: r.get("group") for r in runs()}
    J = {n: judge(n) for n in g if g[n] in ("C", "E")}
    bc = rank([n for n in J if g[n] == "C"], J)[0]
    be = rank([n for n in J if g[n] == "E"], J)[0]
    append([f"  # resolved {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by lab/b5.py --resolve-f: best C = {bc}, best E = {be}",
            f"  - {{name: b5_combo_s3v2e70_C30, trial: 402, group: F, combo: {{books: [[b3_s3v2e_core10, 0.7], [{bc}, 0.3]]}}}}",
            f"  - {{name: b5_combo_s3v2e70_E30, trial: 403, group: F, combo: {{books: [[b3_s3v2e_core10, 0.7], [{be}, 0.3]]}}}}",
            f"  - {{name: b5_combo_s3v2e50_x30_C20, trial: 404, group: F, combo: {{books: [[b3_s3v2e_core10, 0.5], "
            f"[b3_xsmom_r1, 0.3], [{bc}, 0.2]]}}}}"])
    return 0


def resolve_sweep() -> int:
    if "trial: 405," in (ROOT / FILE).read_text(encoding="utf-8"):
        print("already resolved")
        return 0
    g = {r["name"]: r.get("group") for r in runs()}
    J = {n: judge(n) for n in g if g[n] in ("B", "C", "D", "E")}
    best2 = rank(list(J), J)[:2]
    L = [f"  # resolved {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by lab/b5.py --resolve-sweep: best 2 of B-E = {best2}"]
    t = 405
    for n in best2:
        for e in (4, 12):
            ov = f"params: {{select_every_h: {e}}}" if g[n] in ("C", "E") else f"rebalance_every_h: {e}"
            L.append(f"  - {{name: b5s_{n}_r{e}h, trial: {t}, group: sweep, base: {n}, {ov}}}")
            t += 1
    append(L)
    return 0


def corr(name: str, other: pd.Series) -> float | None:
    h = load_hourly(name)
    d = h["equity"].loc[:OOS_END].resample("1D").last().pct_change()
    j = pd.concat([d, other], axis=1).dropna()
    return float(j.iloc[:, 0].corr(j.iloc[:, 1])) if len(j) > 30 else None


def report(names: list[str], out: str = "leaderboard_b5.md") -> int:
    from lab.analogs import features, find_analogs
    labels = {n: lab for lab, n in REFS}
    have = [n for n in names if load_hourly(n) is not None]
    J = {n: judge(n) for n in have}
    ref = J[REF]
    b = btc()
    btc_d = b.loc[:OOS_END].resample("1D").last().pct_change()
    live_d = load_hourly(LIVE)["equity"].loc[:OOS_END].resample("1D").last().pct_change()
    regimes = classify_regimes(btc_daily_features(b))
    f = features()
    today = f[["btc_ret_30d"]].dropna().index[-1]
    f2 = f[(f.index <= OOS_END - pd.Timedelta(days=14)) | (f.index == today)]
    analog_days = [d + pd.Timedelta(hours=23) for d in find_analogs(f2, today, k=30)[0].index]
    pct = lambda x: "" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:+.1%}"
    pr = lambda x: "" if x is None else f"{x:.0%}"
    n_tr = declared_total()
    trials = [n for n in have if not n.startswith(("b5ref__", "b4d__"))]
    adopt = [n for n in rank([n for n in trials if not n.startswith("b5s_")], J) if J[n]["meets"] and beats_ref(J[n], ref)]
    L = ["# Block 5: risk-adjusted profit and down markets (new team objective)\n",
         f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC. Rules: `{FILE}` (declared before any run). Data to 2026-06-30, "
         "both halves (IS 2020-02-15 to 2024-12-31, OOS 2025-01-01 to 2026-06-30); Jul-Oct 2026 informational._\n",
         f"**Trials:** {n_tr} declared across all blocks; luck threshold about {N01.inv_cdf(1 - 1 / n_tr):.1f} standard errors.\n",
         "**Requirements (both halves):** mean 14d return > 0 in DOWN windows (BTC 14d < -5%), P(14d <= -10%) <= 5%, worst "
         "14d >= -15%; OOS Sharpe >= 1.0. **Adopt:** all requirements AND higher median 14d composite AND higher mean 14d return "
         "than s3v2e_core10 in both halves.\n",
         f"**Adopted: {'`' + adopt[0] + '`' if adopt else 'none'}**{' (also passing: ' + ', '.join(adopt[1:]) + ')' if len(adopt) > 1 else ''}\n",
         "\n## Down-market results first (mean 14d return by BTC 14d move; n windows)\n",
         "| run | half | DOWN (BTC < -5%) | % of down windows > 0 | FLAT | UP (BTC > +5%) | down-market req. |",
         "|---|---|---|---|---|---|---|"]
    for n in have:
        for k in ("IS", "OOS", "INFO"):
            s = J[n][k]
            if not s.get("n"):
                continue
            L.append(f"| {labels.get(n, n)} | {k} | {pct(s['down'])} ({s['n_down']}) | {pr(s['down_pos'])} | {pct(s['flat'])} "
                     f"({s['n_flat']}) | {pct(s['up'])} ({s['n_up']}) | "
                     f"{'' if k == 'INFO' else ('yes' if s['down'] is not None and s['down'] > 0 else '**no**')} |")
    L += ["\n## Primary metric, risk limits, verdict\n",
          "| run | half | median 14d composite | mean 14d | median 14d | P(<= -10%) | worst 14d | Sharpe | max DD | P(>= +10%) | "
          "fees/yr | trades/day | meets all | beats s3v2e_core10 |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for n in have:
        for k in ("IS", "OOS", "INFO"):
            s = J[n][k]
            if not s.get("n"):
                continue
            last = k == "OOS"
            L.append(f"| {labels.get(n, n)} | {k} | {s['comp']:.2f} | {pct(s['mean'])} | {pct(s['median'])} | {pr(s['pm10'])} | "
                     f"{pct(s['worst'])} | {s['sharpe']:.2f} | {pct(s['mdd'])} | {pr(s['p10'])} | {s['fees_yr']:.1%} | "
                     f"{s['trades_day']:.1f} | {('**yes**' if J[n]['meets'] else 'no') if last else ''} | "
                     f"{('' if n == REF else ('**yes**' if beats_ref(J[n], ref) else 'no')) if last else ''} |")
    L += ["\n## Regimes, analogs, long / short, correlation (OOS unless noted)\n",
          "Regime slices: mean daily return (days) by BTC regime (config/lab.yaml), OOS. Analogs: mean 14d return after the 30 "
          "historical states nearest to today (outcomes to 2026-06-30). Long / short P&L: sum over the half / mean equity "
          "(runs with recorded positions); short hit = share of short episodes with P&L > 0.\n",
          "| run | bull | bear | chop | shock | analogs 14d mean / P>=10% | long P&L OOS | short P&L OOS | short hit OOS | net short OOS | "
          "corr live | corr BTC |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for n in have:
        h = load_hourly(n)
        rg = by_regime(h.loc[OOS0:OOS_END], regimes)
        cell = lambda r: f"{r['mean_daily']:+.2%} ({r['days']})" if r else ""
        an = fwd(h, analog_days)
        d = ls_detail(n).get("OOS") if (ROOT / ".cache" / "runs" / f"{n}_pos.pkl").exists() else None
        L.append(f"| {labels.get(n, n)} | {cell(rg.get('bull'))} | {cell(rg.get('bear'))} | {cell(rg.get('chop'))} | "
                 f"{cell(rg.get('shock'))} | {pct(an.get('mean'))} / {pr(an.get('p10'))} | "
                 f"{pct(d['long_pnl']) if d else 'n/a'} | {pct(d['short_pnl']) if d else 'n/a'} | "
                 f"{pr(d['hit']) if d else 'n/a'} | {pr(d['net_short']) if d else 'n/a'} | "
                 f"{'' if n == LIVE else format(corr(n, live_d) or 0, '.2f')} | {format(corr(n, btc_d) or 0, '.2f')} |")
    (ROOT / "leaderboard_b5.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"adopted: {adopt}; ranking: {rank(trials, J)[:5]}")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("runs", nargs="*")
    ap.add_argument("--resolve-f", action="store_true")
    ap.add_argument("--resolve-sweep", action="store_true")
    ap.add_argument("--out", default="leaderboard_b5.md")
    a = ap.parse_args()
    if a.resolve_f:
        sys.exit(resolve_f())
    if a.resolve_sweep:
        sys.exit(resolve_sweep())
    sys.exit(report(a.runs or [n for _, n in REFS] + [r["name"] for r in runs()], a.out))
