"""Leaderboard across all stored runs, with overfitting flags.

    python -m lab.leaderboard            # writes leaderboard.md

Ranking: out-of-sample (2025-01 -> now) rolling 14-day windows, by median composite
(0.4 Sortino + 0.3 Sharpe + 0.3 Calmar), tie-broken by % positive windows.

Overfitting flags:
* DSR: Deflated Sharpe Ratio (Bailey & Lopez de Prado 2014). Probability that the
  run's true OOS Sharpe exceeds the maximum Sharpe expected from luck alone across N
  trials (N = declared trials in variants.yaml), adjusting for skew and fat tails.
  DSR < 0.95 means the result is not distinguishable from the best of N random tries.
* "noise vs baseline": OOS Sharpe differs from its baseline by less than 1 standard
  error of a Sharpe estimate (SE ~ sqrt((1 + SR^2/2) / years)).
* "OOS >> IS": OOS Sharpe exceeds in-sample Sharpe by > 0.75, typical of a lucky period.
"""

from __future__ import annotations

import json
import math
import sys
from statistics import NormalDist

import numpy as np
import pandas as pd
import yaml

from lab import ROOT
from lab.runner import load_hourly

N01 = NormalDist()
EULER = 0.5772156649
BASELINES = {"guard": "s3v2_base", "params": "guard_minimal", "universe": "guard_minimal",
             "bench": "s3v2_base"}


def deflated_sharpe(r: pd.Series, n_trials: int, sr_var_trials: float) -> tuple[float, float]:
    """Return (DSR probability, SR* threshold) using per-period (hourly) Sharpe."""
    r = r.dropna()
    t = len(r)
    sr = r.mean() / r.std()
    skew = float(((r - r.mean()) ** 3).mean() / r.std() ** 3)
    kurt = float(((r - r.mean()) ** 4).mean() / r.std() ** 4)
    sr0 = math.sqrt(max(sr_var_trials, 1e-12)) * (
        (1 - EULER) * N01.inv_cdf(1 - 1 / n_trials) + EULER * N01.inv_cdf(1 - 1 / (n_trials * math.e)))
    denom = math.sqrt(max(1e-12, 1 - skew * sr + (kurt - 1) / 4 * sr ** 2))
    z = (sr - sr0) * math.sqrt(t - 1) / denom
    return N01.cdf(z), sr0


def collect() -> pd.DataFrame:
    rows = []
    for p in sorted((ROOT / "runs").glob("*/result.json")):
        m = json.loads(p.read_text())
        sc = m["scorecard"]
        oos, full, isp = (sc["periods"].get(k, {}) for k in ("out_of_sample", "full", "in_sample"))
        w = sc["rolling_14d"].get("out_of_sample", {})
        a = sc["activity"]
        rows.append({
            "run": m["name"], "group": m.get("group"), "trial": m.get("trial"),
            "oos_ret": oos.get("return"), "oos_sharpe": oos.get("sharpe"), "oos_mdd": oos.get("mdd"),
            "is_sharpe": isp.get("sharpe"), "full_sharpe": full.get("sharpe"), "full_ret": full.get("return"),
            "w_median_comp": w.get("median_composite"), "w_median_ret": w.get("median_return"),
            "w_pct_pos": w.get("pct_positive"), "w_worst": w.get("worst_return"), "w_worst_dd": w.get("worst_dd"),
            "w_active": w.get("median_active_days"), "w_all_active": w.get("pct_windows_all_days_active"),
            "fees_yr": a.get("fees_per_year_pct_equity"), "corr_s3v2": sc.get("corr_daily_vs_s3v2"),
            "note": m.get("note") or ""})
    return pd.DataFrame(rows)


def main() -> int:
    doc = yaml.safe_load((ROOT / "variants.yaml").read_text(encoding="utf-8"))
    n_trials = int(doc.get("declared_trials", len(doc["runs"])))
    ledger = json.loads((ROOT / "runs" / "trials.json").read_text())
    df = collect()
    strat = df[df.group != "bench"]
    yrs_oos = None
    # cross-trial variance of per-period (hourly) OOS Sharpe, for the DSR threshold
    hourly_sr = {}
    for run in df.run:
        h = load_hourly(run)
        if h is None:
            continue
        r = h["equity"].loc[pd.Timestamp("2025-01-01", tz="UTC"):].pct_change().dropna()
        hourly_sr[run] = (r, float(r.mean() / r.std()))
        yrs_oos = len(r) / (24 * 365)
    var_sr = float(np.var([hourly_sr[r][1] for r in strat.run if r in hourly_sr], ddof=1))
    dsr, flags = {}, {}
    for _, row in df.iterrows():
        f = []
        if row.run in hourly_sr:
            p, sr0 = deflated_sharpe(hourly_sr[row.run][0], n_trials, var_sr)
            dsr[row.run] = p
            if p < 0.95:
                f.append("DSR<0.95")
        base = BASELINES.get(row.group)
        if base and base != row.run and base in set(df.run):
            b = df.set_index("run").loc[base, "oos_sharpe"]
            se = math.sqrt((1 + b ** 2 / 2) / yrs_oos)
            if abs(row.oos_sharpe - b) < se:
                f.append(f"noise vs {base}")
        if row.oos_sharpe is not None and row.is_sharpe is not None and row.oos_sharpe - row.is_sharpe > 0.75:
            f.append("OOS>>IS")
        if row.w_all_active is not None and row.w_all_active < 0.9 and row.group != "bench":
            f.append("fails daily activity")
        flags[row.run] = ", ".join(f)
    df["dsr"] = df.run.map(dsr)
    df["flags"] = df.run.map(flags)
    df = df.sort_values(["w_median_comp", "w_pct_pos"], ascending=False).reset_index(drop=True)
    sr0_ann = math.sqrt(var_sr) * ((1 - EULER) * N01.inv_cdf(1 - 1 / n_trials)
                                   + EULER * N01.inv_cdf(1 - 1 / (n_trials * math.e))) * math.sqrt(24 * 365)
    se_ann = math.sqrt((1 + 1.2 ** 2 / 2) / yrs_oos)

    L = ["# strategy_lab leaderboard\n",
         f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC from runs/*/result.json. "
         f"Declared trials: {n_trials} (executed runs incl. re-runs: {ledger['total_runs']}). "
         f"Out-of-sample = 2025-01-01 -> {pd.Timestamp.now(tz='UTC'):%Y-%m-%d} ({yrs_oos:.2f} years)._\n",
         "Ranked by **OOS rolling 14-day windows** (the competition horizon): median composite "
         "(0.4 Sortino + 0.3 Sharpe + 0.3 Calmar), then % of windows positive.\n",
         f"**How much is noise?** With {yrs_oos:.1f} OOS years, one standard error of an annualised Sharpe "
         f"is about **{se_ann:.2f}**. The luck threshold for the best of {n_trials} trials (DSR SR*) is about "
         f"**{sr0_ann:.2f}** annualised above zero. Differences smaller than these are not evidence.\n",
         "| # | run | group | OOS ret | OOS Sharpe | OOS maxDD | IS Sharpe | full Sharpe | 14d med comp | "
         "14d med ret | 14d % pos | 14d worst | 14/14 active | fees/yr | corr s3v2 | DSR | flags |",
         "|" + "---|" * 17]
    for i, r in df.iterrows():
        L.append(f"| {i + 1} | {r.run} | {r.group} | {r.oos_ret:+.1%} | {r.oos_sharpe:.2f} | {r.oos_mdd:+.1%} | "
                 f"{r.is_sharpe:.2f} | {r.full_sharpe:.2f} | {r.w_median_comp:.2f} | {r.w_median_ret:+.2%} | "
                 f"{r.w_pct_pos:.0%} | {r.w_worst:+.1%} | {r.w_all_active:.0%} | {r.fees_yr:.1%} | "
                 f"{'' if pd.isna(r.corr_s3v2) else f'{r.corr_s3v2:.2f}'} | "
                 f"{'' if pd.isna(r.dsr) else f'{r.dsr:.2f}'} | {r['flags']} |")
    rec = (ROOT / "reports" / "recommendation.md")
    if rec.exists():
        L.append("\n" + rec.read_text(encoding="utf-8"))
    (ROOT / "leaderboard.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L[:6]))
    print(df[["run", "group", "oos_ret", "oos_sharpe", "oos_mdd", "is_sharpe", "w_median_comp", "w_pct_pos",
              "w_all_active", "dsr", "flags"]].round(3).to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
