"""Research block 3 (competition objective) report: leaderboard_b3.md.

    python -m lab.b3

Judged ONLY on data to 2026-06-30, in both halves:
  IS  = run start -> 2024-12-31,  OOS = 2025-01-01 -> 2026-06-30
Informational only (never a gate): 2026-07-01 -> latest (the block-2 holdout, already spent).
Primary metric: P(14d return >= +10%) and P(>= +8%) over all rolling 14-day windows (daily step).
Constraints (each half): P(14d <= -10%) <= 10% AND worst 14d >= -20%.
Selection (fixed in variants_b3.yaml before running): highest OOS P(>= +10%) among runs meeting
both constraints in both halves (ties: higher IS P(>= +10%)); if none: s3v2e_tv06 on core10 if it
qualifies, else s3v2e on core10.
Also: P(<= -10%), worst / mean / median 14d, median composite, fees, trades/day, active days per
14d, alt_rally-episode and analog-to-today 14-day results, daily-return correlation with
s3v2e on core10, time in each mode for regime runs, the xsmom tm10 universe-choice check
(2023-01 -> 2025-09, before the teammate's sample), trial count and luck threshold.
"""

from __future__ import annotations

import json
import math
import sys

import numpy as np
import pandas as pd
import yaml

from lab import ROOT
from lab.alt_rally import episodes, flag_series
from lab.analogs import features, find_analogs
from lab.leaderboard import EULER, N01, declared_total
from lab.runner import load_hourly
from lab.scorecard import metrics

FILE = "variants_b3.yaml"
REF = "b3_s3v2e_core10"
IS_END = pd.Timestamp("2024-12-31 23:00", tz="UTC")
OOS0, OOS_END = pd.Timestamp("2025-01-01", tz="UTC"), pd.Timestamp("2026-06-30 23:00", tz="UTC")
INFO0 = pd.Timestamp("2026-07-01", tz="UTC")
TM_CHECK = (pd.Timestamp("2023-01-01", tz="UTC"), pd.Timestamp("2025-09-09 23:00", tz="UTC"))
TM_SAMPLE = (pd.Timestamp("2025-09-10 14:00", tz="UTC"), pd.Timestamp("2026-09-30 13:00", tz="UTC"))


def windows(h: pd.DataFrame, a: pd.Timestamp | None, b: pd.Timestamp | None) -> pd.DataFrame:
    """All 14-day windows (daily step, starting 00:00 UTC) fully inside [a, b]."""
    x = h.loc[a:b]
    if len(x) < 24 * 15:
        return pd.DataFrame()
    eq, tr = x["equity"], x["trades"]
    act = tr.groupby(tr.index.floor("D")).sum() > 0
    out = []
    for s in pd.date_range(x.index[0].ceil("D"), x.index[-1] - pd.Timedelta(days=14), freq="1D"):
        e = eq.loc[s:s + pd.Timedelta(days=14)]
        if len(e) < 24 * 14:
            continue
        m = metrics(e.values)
        out.append({"start": s, "ret": e.iloc[-1] / e.iloc[0] - 1, "dd": float((e / e.cummax() - 1).min()),
                    "comp": m.get("composite", np.nan),
                    "active": int(act.loc[s:s + pd.Timedelta(days=13)].sum())})
    return pd.DataFrame(out)


def wstats(w: pd.DataFrame) -> dict:
    if w.empty:
        return {"n": 0}
    r = w["ret"]
    return {"n": int(len(r)), "p10": float((r >= 0.10).mean()), "p8": float((r >= 0.08).mean()),
            "pm10": float((r <= -0.10).mean()), "worst": float(r.min()), "mean": float(r.mean()),
            "median": float(r.median()), "comp": float(w["comp"].median()), "active": float(w["active"].mean())}


def fwd(h: pd.DataFrame, days: list[pd.Timestamp]) -> dict:
    vals = []
    for d in days:
        e = h["equity"].loc[d:d + pd.Timedelta(days=14)]
        if len(e) >= 24 * 14 and e.index[-1] <= OOS_END:
            vals.append(e.iloc[-1] / e.iloc[0] - 1)
    v = pd.Series(vals, dtype=float)
    return {} if v.empty else {"n": int(len(v)), "mean": float(v.mean()), "median": float(v.median()),
                               "p10": float((v >= 0.10).mean())}


def main() -> int:
    doc = yaml.safe_load((ROOT / FILE).read_text(encoding="utf-8"))
    decl = {r["name"]: r for r in doc["runs"]}
    n_trials = declared_total()
    flag = flag_series().fillna(False).astype(bool)
    flag.index = pd.DatetimeIndex(flag.index)
    if flag.index.tz is None:
        flag.index = flag.index.tz_localize("UTC")
    eps = [s + pd.Timedelta(days=1) for s in episodes(flag).start if s + pd.Timedelta(days=15) <= OOS_END]
    f = features()
    today = f[["btc_ret_30d"]].dropna().index[-1]
    f2 = f[(f.index <= OOS_END - pd.Timedelta(days=14)) | (f.index == today)]
    analog_days = [d + pd.Timedelta(hours=23) for d in find_analogs(f2, today, k=30)[0].index]
    ref = load_hourly(REF)
    ref_d = ref["equity"].loc[:OOS_END].resample("1D").last().pct_change() if ref is not None else None
    rows = []
    for name, r in decl.items():
        h = load_hourly(name)
        if h is None:
            continue
        p = ROOT / "runs" / name / "result.json"
        act = json.loads(p.read_text())["scorecard"]["activity"] if p.exists() else {}
        hj = h.loc[:OOS_END]
        days = hj["trades"].groupby(hj.index.floor("D")).sum()
        yrs = (hj.index[-1] - hj.index[0]) / pd.Timedelta(days=365)
        row = {"run": name, "group": r.get("group"), "trial": r.get("trial"),
               "IS": wstats(windows(h, None, IS_END)), "OOS": wstats(windows(h, OOS0, OOS_END)),
               "INFO": wstats(windows(h, INFO0, None)),
               "fees_yr": float(hj["fees"].sum() / hj["equity"].mean() / yrs),
               "trades_day": float(days.mean()), "alt": fwd(h, eps), "analog": fwd(h, analog_days),
               "corr": None, "modes": None}
        if ref_d is not None and name != REF:
            d = hj["equity"].resample("1D").last().pct_change()
            j = pd.concat([d, ref_d], axis=1).dropna()
            row["corr"] = float(j.iloc[:, 0].corr(j.iloc[:, 1])) if len(j) > 30 else None
        if name.startswith("b3_xsmom_tm10"):
            row["tm_check"] = wstats(windows(h, *TM_CHECK))
            row["tm_sample"] = wstats(windows(h, *TM_SAMPLE))
        ok = lambda s: s.get("n", 0) > 0 and s["pm10"] <= 0.10 and s["worst"] >= -0.20
        row["meets"] = ok(row["IS"]) and ok(row["OOS"])
        rows.append(row)
    # regime modes (time in each mode), computed with the strategy's own mode function
    mode_info = regime_mode_shares()
    for row in rows:
        if decl[row["run"]].get("strategy") == "regime_switch":
            row["modes"] = mode_info
    # selection rule
    q = [r for r in rows if r["meets"] and r["trial"] is not None]
    q.sort(key=lambda r: (r["OOS"]["p10"], r["IS"]["p10"]), reverse=True)
    if q:
        winner, why = q[0]["run"], "highest OOS P(>= +10%) among runs meeting both constraints in both halves"
    else:
        by = {r["run"]: r for r in rows}
        tv6 = by.get("b3_s3v2e_tv06_core10")
        if tv6 and tv6["meets"]:
            winner, why = "b3_s3v2e_tv06_core10", "fallback 1: no run qualified; s3v2e_tv06 on core10 qualifies"
        else:
            winner, why = REF, "fallback 2: no run qualified (nor s3v2e_tv06 core10): s3v2e on core10"
    write(rows, n_trials, winner, why, len(eps), today)
    write_sweep(decl)
    print(f"winner: {winner} ({why})")
    return 0


def regime_mode_shares() -> dict:
    """Share of days in each mode, IS / OOS / INFO, from the frozen mode function."""
    sys.path.insert(0, str(ROOT))
    from lab.data import load_close
    from lab.strategies import get_strategy  # noqa: F401  (loads lab strategies)
    mod = sys.modules.get("lab_strategies.regime")
    btc = load_close(["BTCUSDT"])["BTCUSDT"]
    days = pd.date_range("2020-02-15", btc.index[-1].floor("D"), freq="1D", tz="UTC")
    m = pd.Series({d: mod.mode_at(btc, d) for d in days})
    out = {}
    for k, (a, b) in {"IS": (None, IS_END), "OOS": (OOS0, OOS_END), "INFO": (INFO0, None)}.items():
        x = m.loc[a:b]
        out[k] = {mm: float((x == mm).mean()) for mm in ("ATTACK", "BASE", "DEFEND")}
    return out


def write_sweep(decl: dict) -> None:
    """Addendum frequency sweep: base runs and their refresh variants side by side (data to
    2026-06-30; not eligible as the winner by themselves)."""
    from lab.runner import resolve_base
    add = yaml.safe_load((ROOT / "variants_b3_addendum.yaml").read_text(encoding="utf-8"))
    groups: dict[str, list[tuple[float, str]]] = {}
    for r in add["runs"]:
        groups.setdefault(r["base"], []).append((float(r["rebalance_every_h"]), r["name"]))
    pct = lambda x: "" if x is None else f"{x:+.1%}"
    pr = lambda x: "" if x is None else f"{x:.0%}"
    L = ["\n## Frequency sweep (standing rule; target refresh 1h to daily, horizons fixed in calendar time)\n",
         "Side by side per base strategy; data to 2026-06-30. Sweep runs are not eligible as the block-3 "
         "winner by themselves.\n",
         "| base | refresh | fees/yr | trades/day | IS P>=10% / P<=-10% | OOS P>=10% / P<=-10% | OOS median 14d |",
         "|---|---|---|---|---|---|---|"]
    for base, items in groups.items():
        own = float(resolve_base(base).get("rebalance_every_h", 24))
        for every, name in sorted(items + [(own, base)]):
            h = load_hourly(name)
            if h is None:
                L.append(f"| {base} | {every:g}h | not run | | | | |")
                continue
            hj = h.loc[:OOS_END]
            yrs = (hj.index[-1] - hj.index[0]) / pd.Timedelta(days=365)
            fees = float(hj["fees"].sum() / hj["equity"].mean() / yrs)
            tpd = float(hj["trades"].groupby(hj.index.floor("D")).sum().mean())
            i, o = wstats(windows(h, None, IS_END)), wstats(windows(h, OOS0, OOS_END))
            L.append(f"| {base} | {every:g}h{' (base)' if name == base else ''} | {fees:.1%} | {tpd:.1f} | "
                     f"{pr(i.get('p10'))} / {pr(i.get('pm10'))} | {pr(o.get('p10'))} / {pr(o.get('pm10'))} | "
                     f"{pct(o.get('median'))} |")
    out = ROOT / "leaderboard_b3.md"
    out.write_text(out.read_text(encoding="utf-8") + "\n".join(L) + "\n", encoding="utf-8")


def write(rows: list[dict], n_trials: int, winner: str, why: str, n_eps: int, today: pd.Timestamp) -> None:
    pct = lambda x: "" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:+.1%}"
    pr = lambda x: "" if x is None else f"{x:.0%}"
    sr0 = N01.inv_cdf(1 - 1 / n_trials)
    L = ["# Research block 3: competition objective (14-day return)\n",
         f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC. Judged on data to 2026-06-30 only: "
         f"IS = start to 2024-12-31, OOS = 2025-01-01 to 2026-06-30. **Jul 1 to Oct 4 2026 is INFORMATIONAL "
         f"ONLY** (the block-2 holdout, already spent), never a gate._\n",
         f"**Trials:** {n_trials} declared across all blocks (block 3: 41 + 20 addendum sweep). With that many tries, the best "
         f"P(>= +10%) is expected to look about {sr0:.1f} standard errors better than its true value; treat "
         f"small differences as noise.\n",
         "**Constraints (each half):** P(14d <= -10%) <= 10% and worst 14d >= -20%. **Selection:** highest "
         "OOS P(>= +10%) among runs meeting both, in both halves.\n",
         f"**Selected: `{winner}`**: {why}.\n",
         "| run | group | IS P>=10% / P>=8% / P<=-10% / worst | OOS P>=10% / P>=8% / P<=-10% / worst | "
         "OOS mean / median 14d | OOS comp | meets both halves | fees/yr | trades/day | active d/14 | "
         "alt_rally 14d mean / P>=10% | analogs 14d mean / P>=10% | corr s3v2e | INFO Jul-Oct P>=10% / median |",
         "|" + "---|" * 15]
    for r in sorted(rows, key=lambda r: (r["meets"], r["OOS"].get("p10", 0)), reverse=True):
        i, o, inf = r["IS"], r["OOS"], r["INFO"]
        cell = lambda s: (f"{pr(s.get('p10'))} / {pr(s.get('p8'))} / {pr(s.get('pm10'))} / {pct(s.get('worst'))}"
                          if s.get("n") else "n/a")
        L.append(f"| {r['run']} | {r['group']} | {cell(i)} | {cell(o)} | {pct(o.get('mean'))} / "
                 f"{pct(o.get('median'))} | {o.get('comp', float('nan')):.2f} | {'**yes**' if r['meets'] else 'no'} | "
                 f"{r['fees_yr']:.1%} | {r['trades_day']:.1f} | {o.get('active', float('nan')):.1f} | "
                 f"{pct(r['alt'].get('mean'))} / {pr(r['alt'].get('p10'))} | "
                 f"{pct(r['analog'].get('mean'))} / {pr(r['analog'].get('p10'))} | "
                 f"{'' if r['corr'] is None else format(r['corr'], '.2f')} | "
                 f"{pr(inf.get('p10'))} / {pct(inf.get('median'))} |")
    mi = next((r["modes"] for r in rows if r.get("modes")), None)
    if mi:
        L += ["\n## Regime switch: share of days in each mode\n", "| period | ATTACK | BASE | DEFEND |",
              "|---|---|---|---|"]
        for k, v in mi.items():
            L.append(f"| {k} | {v['ATTACK']:.0%} | {v['BASE']:.0%} | {v['DEFEND']:.0%} |")
    tm = [r for r in rows if "tm_check" in r]
    if tm:
        L += ["\n## xsmom on tm10: universe-choice check (selection bias)\n",
              "The teammate picked the 10 coins with data up to Sep 2026. **2023-01 to 2025-09 is before the "
              "teammate's sample**, so it is the out-of-sample test of the universe choice; the teammate's own "
              "sample (2025-09-10 to 2026-09-30) is shown for comparison.\n",
              "| run | 2023-01 to 2025-09: windows / P>=10% / P<=-10% / median / worst | teammate sample: windows / "
              "P>=10% / P<=-10% / median / worst |", "|---|---|---|"]
        for r in tm:
            c, s = r["tm_check"], r["tm_sample"]
            f = lambda x: (f"{x['n']} / {pr(x['p10'])} / {pr(x['pm10'])} / {pct(x['median'])} / {pct(x['worst'])}"
                           if x.get("n") else "n/a")
            L.append(f"| {r['run']} | {f(c)} | {f(s)} |")
    L.append(f"\nalt_rally columns: {n_eps} independent episodes ending by 2026-06-30. Analogs: 30 nearest "
             f"historical states to {today:%Y-%m-%d} (outcomes to 2026-06-30).")
    (ROOT / "leaderboard_b3.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    pd.DataFrame([{k: v for k, v in r.items() if k not in ("alt", "analog", "modes")} for r in rows]) \
        .to_json(ROOT / "reports" / "block3_runs.json", orient="records", indent=1, default_handler=str)


if __name__ == "__main__":
    sys.exit(main())
