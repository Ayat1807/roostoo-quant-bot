"""Research block 2 report: leaderboard_b2.md (runs end 2026-06-30; Jul-Oct 2026 is the holdout).

    python -m lab.block [--groups D,E]

Per run: full / in-sample (2020-02-15 -> 2024) / OOS (2025-01 -> 2026-06) metrics, OOS rolling
14-day windows (median, % positive, worst, median composite), fees and trades per day, average
gross exposure, Deflated Sharpe vs the global trial count, and the protocol's "beats live"
test (IS Sharpe > b2_core's AND OOS Sharpe > b2_core's AND OOS 14d median composite >= b2_core's).
Conditional views (informative, not used for adoption):
  * alt_rally: 14-day results starting at each independent alt_rally episode start (frozen
    indicator, lab/alt_rally.py; episodes whose 14 days end by 2026-06-30)
  * analog-to-today: mean / % positive / worst of the next 14 days after the 30 nearest
    historical analogs of today's market state (lab/analogs.py), candidates <= 2026-06-16
"""

from __future__ import annotations

import argparse
import json
import math
import sys

import numpy as np
import pandas as pd
import yaml

from lab import ROOT
from lab.alt_rally import episodes, flag_series
from lab.analogs import features, find_analogs
from lab.leaderboard import EULER, N01, deflated_sharpe, declared_total
from lab.runner import load_hourly

FILE = "variants_b2.yaml"
BASE = "b2_core"
OOS0, END = pd.Timestamp("2025-01-01", tz="UTC"), pd.Timestamp("2026-06-30 23:00", tz="UTC")
TITLES = {"base": "Baseline (live config)", "D": "D: frequency sweep", "E": "E: own improvements",
          "B": "B: satellites (standalone books)", "C": "C: core + satellite"}


def fwd14(h: pd.DataFrame, day: pd.Timestamp) -> tuple[float, float]:
    """(14-day return, max drawdown inside the window) from `day`."""
    t0, t1 = day, day + pd.Timedelta(days=14)
    if t1 > h.index[-1] or t0 < h.index[0]:
        return np.nan, np.nan
    e = h["equity"].loc[t0:t1]
    return float(e.iloc[-1] / e.iloc[0] - 1), float((e / e.cummax() - 1).min())


def cond_stats(vals: list[tuple[float, float]]) -> dict[str, float]:
    v = pd.DataFrame(vals, columns=["ret", "dd"]).dropna()
    if v.empty:
        return {}
    return {"n": int(len(v)), "mean": float(v.ret.mean()), "median": float(v.ret.median()),
            "p25": float(v.ret.quantile(0.25)), "pct_pos": float((v.ret > 0).mean()),
            "worst": float(v.ret.min()), "worst_dd": float(v.dd.min())}


def helps(f: dict, b: dict) -> bool:
    """Declared filter test: higher median AND p25, worst drawdown not worse."""
    return bool(f and b and f["median"] > b["median"] and f["p25"] > b["p25"] and f["worst_dd"] >= b["worst_dd"])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--groups", help="comma-separated groups to include (default: all run)")
    a = ap.parse_args()
    doc = yaml.safe_load((ROOT / FILE).read_text(encoding="utf-8"))
    decl = {r["name"]: r for r in doc["runs"]}
    want = set(a.groups.split(",")) | {"base"} if a.groups else None
    n_trials = declared_total()
    # alt_rally episode starts usable before the holdout
    flag = flag_series().fillna(False).astype(bool)
    flag.index = pd.DatetimeIndex(flag.index)
    if flag.index.tz is None:
        flag.index = flag.index.tz_localize("UTC")
    eps = episodes(flag)
    ep_starts = [s + pd.Timedelta(days=1) for s in eps.start if s + pd.Timedelta(days=15) <= END]
    # analogs of today (holdout outcomes excluded: candidates <= 2026-06-16)
    f = features()
    today = f[["btc_ret_30d"]].dropna().index[-1]
    f2 = f[(f.index <= END - pd.Timedelta(days=14)) | (f.index == today)]
    analog_days = list(find_analogs(f2, today, k=30)[0].index)

    rows, hourly = [], {}
    for name, r in decl.items():
        p = ROOT / "runs" / name / "result.json"
        if not p.exists() or (want and r.get("group") not in want):
            continue
        sc = json.loads(p.read_text())["scorecard"]
        h = load_hourly(name)
        if h is None:
            continue
        hourly[name] = h
        per, w, act = sc["periods"], sc["rolling_14d"].get("out_of_sample", {}), sc["activity"]
        rows.append({
            "run": name, "group": r.get("group"), "trial": r.get("trial"), "note": r.get("note", ""),
            "full_ret": per["full"]["return"], "full_sharpe": per["full"]["sharpe"], "full_mdd": per["full"]["mdd"],
            "is_sharpe": per["in_sample"]["sharpe"], "oos_ret": per["out_of_sample"]["return"],
            "oos_sharpe": per["out_of_sample"]["sharpe"], "oos_mdd": per["out_of_sample"]["mdd"],
            "w_med": w.get("median_return"), "w_pos": w.get("pct_positive"), "w_worst": w.get("worst_return"),
            "w_comp": w.get("median_composite"), "w_active": w.get("pct_windows_all_days_active"),
            "fees_yr": act["fees_per_year_pct_equity"], "trades_day": act["trades_per_day"],
            "gross": act["avg_gross_exposure"],
            "alt": cond_stats([fwd14(h, d) for d in ep_starts]),
            "analog": cond_stats([fwd14(h, d + pd.Timedelta(hours=23)) for d in analog_days]),
        })
    df = pd.DataFrame(rows).set_index("run")
    if BASE not in df.index:
        print("run b2_core first")
        return 1
    # DSR across block trials (hourly OOS Sharpe), global trial count
    sr = {}
    for n, h in hourly.items():
        r = h["equity"].loc[OOS0:END].pct_change().dropna()
        sr[n] = (r, float(r.mean() / r.std()))
    trial_runs = [n for n in df.index if decl[n].get("trial") is not None]
    var_sr = float(np.var([sr[n][1] for n in trial_runs], ddof=1)) if len(trial_runs) > 1 else 0.0
    yrs = len(sr[BASE][0]) / (24 * 365)
    sr0_ann = math.sqrt(var_sr) * ((1 - EULER) * N01.inv_cdf(1 - 1 / n_trials)
                                   + EULER * N01.inv_cdf(1 - 1 / (n_trials * math.e))) * math.sqrt(24 * 365)
    df["dsr"] = [deflated_sharpe(sr[n][0], n_trials, var_sr)[0] if var_sr > 0 else np.nan for n in df.index]
    b = df.loc[BASE]
    df["beats_live"] = ((df.is_sharpe > b.is_sharpe) & (df.oos_sharpe > b.oos_sharpe) & (df.w_comp >= b.w_comp)
                        & df.group.isin(["D", "E", "C"]))
    se = math.sqrt((1 + b.oos_sharpe ** 2 / 2) / yrs)

    pct = lambda x: "" if x is None or pd.isna(x) else f"{x:+.1%}"
    L = ["# Research block 2 leaderboard\n",
         f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC. All runs end 2026-06-30 23:00; "
         f"**2026-07-01 onward is the untouched final exam**. In-sample 2020-02-15 to 2024-12-31; "
         f"OOS 2025-01-01 to 2026-06-30 ({yrs:.2f} years)._\n",
         f"**Luck threshold:** {n_trials} declared trials across all blocks. One standard error of an "
         f"annualised OOS Sharpe is about **{se:.2f}**. The best-of-{n_trials} luck level (DSR SR*) is about "
         f"**{sr0_ann:.2f}** annualised. DSR < 0.95 means the result can't be told apart from luck.\n",
         f"**Beats live** = IS Sharpe > {b.is_sharpe:.2f} AND OOS Sharpe > {b.oos_sharpe:.2f} AND OOS 14d "
         f"median composite >= {b.w_comp:.2f} (b2_core). Only D, E and C runs can be adopted, and only "
         f"after passing the final exam.\n",
         f"Conditional columns (heavy tails, so median / 25th percentile / worst drawdown, not Sharpe): "
         f"**alt_rally** = next 14 days from each of the {len(ep_starts)} independent alt_rally episode starts "
         f"before the holdout; **analogs** = next 14 days after the 30 nearest analogs of today "
         f"({today:%Y-%m-%d}). Each cell: median / p25 / worst in-window drawdown.\n"]
    for g in ["base", "D", "E", "B", "C"]:
        x = df[df.group == g]
        if x.empty:
            continue
        x = x.sort_values("w_comp", ascending=False)
        L += [f"\n## {TITLES[g]}\n",
              "| run | full ret | full SR | IS SR | OOS ret | OOS SR | OOS maxDD | 14d med | 14d %pos | "
              "14d worst | 14d comp | 14/14 active | trades/day | fees/yr | avg gross | alt_rally 14d med/p25/DD | "
              "analogs 14d med/p25/DD | DSR | beats live |", "|" + "---|" * 19]
        for n, r in x.iterrows():
            al, an = r.alt or {}, r.analog or {}
            L.append(f"| {n} | {pct(r.full_ret)} | {r.full_sharpe:.2f} | {r.is_sharpe:.2f} | {pct(r.oos_ret)} | "
                     f"{r.oos_sharpe:.2f} | {pct(r.oos_mdd)} | {r.w_med:+.2%} | {r.w_pos:.0%} | {pct(r.w_worst)} | "
                     f"{r.w_comp:.2f} | {r.w_active:.0%} | {r.trades_day:.1f} | {r.fees_yr:.1%} | {r.gross:.2f} | "
                     f"{pct(al.get('median'))} / {pct(al.get('p25'))} / {pct(al.get('worst_dd'))} | "
                     f"{pct(an.get('median'))} / {pct(an.get('p25'))} / {pct(an.get('worst_dd'))} | "
                     f"{'' if pd.isna(r.dsr) else f'{r.dsr:.2f}'} | {'**yes**' if r.beats_live else ''} |")
    # declared literature-filter test: each filtered satellite vs the same satellite without it
    filt = [n for n in df.index if n.startswith("b_r1_") and n.split("_")[-1] in ("jump", "near", "dual", "rvb", "rfng")]
    if filt:
        L += ["", "## Literature filters: does the filter help? (declared test)", "",
              "HELPS = higher median AND higher 25th-percentile 14-day return, with no worse worst drawdown, "
              "in BOTH the alt_rally-episode windows and the analog-to-today windows, vs the same satellite "
              "without the filter.", "",
              "| satellite | filter | alt_rally med / p25 / DD (base -> filtered) | analogs med / p25 / DD (base -> filtered) | helps |",
              "|---|---|---|---|---|"]
        trip = lambda c: f"{pct(c.get('median'))} / {pct(c.get('p25'))} / {pct(c.get('worst_dd'))}" if c else "n/a"
        for n in filt:
            bn = "_".join(n.split("_")[:3])
            if bn not in df.index:
                continue
            fa, ba, fn, bnn = df.loc[n, "alt"], df.loc[bn, "alt"], df.loc[n, "analog"], df.loc[bn, "analog"]
            ok = helps(fa, ba) and helps(fn, bnn)
            L.append(f"| {bn} | {n.split('_')[-1]} | {trip(ba)} -> {trip(fa)} | {trip(bnn)} -> {trip(fn)} | "
                     f"{'**yes**' if ok else 'no'} |")
    cands = list(df.index[df.beats_live])
    L += ["\n## Candidates for the final exam\n",
          ("Runs that beat live on all three criteria: " + ", ".join(cands)) if cands
          else "None: no D/E/C run beats live on all three criteria, so nothing goes to the final exam."]
    out = ROOT / "leaderboard_b2.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    df.drop(columns=["alt", "analog", "note"]).to_csv(ROOT / "reports" / "block2_runs.csv")
    print("\n".join(L[:5]))
    print(df[["group", "is_sharpe", "oos_sharpe", "oos_ret", "w_med", "w_pos", "w_comp", "trades_day",
              "fees_yr", "dsr", "beats_live"]].round(3).to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
