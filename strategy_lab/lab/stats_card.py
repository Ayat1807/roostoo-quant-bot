"""Stats card for any run (required for every config marked "competition").

    python -m lab.stats_card b3_xsmom_r1 b3_s3v2e_core10 b3_xsmom_tm10 --out reports/stats_card_xsmom_r1.md

One column per run, for IS (start -> 2024-12-31), OOS (2025-01-01 -> 2026-06-30) and Jul-Oct 2026
(INFORMATIONAL ONLY, never a gate): Sharpe, Sortino, Calmar, competition composite
(0.4 Sortino + 0.3 Sharpe + 0.3 Calmar) on the whole period AND as the median over rolling 14-day
windows, max drawdown, P(14d >= +10%), P(>= +8%), P(<= -10%), median / worst / % positive 14d,
fees/yr, trades/day, active days per 14, the same 14d numbers under stress (100% taker fills,
7 bps slippage per fill: lab/robustness.py) and the luck threshold for the global trial count.
Metric definitions: lab/scorecard.metrics (hourly returns, annualised 24 x 365); 14-day windows:
lab/b3.windows (daily step from 00:00 UTC, fully inside the period). The first run is the
subject; the others are shown side by side for comparison. The stressed curve is cached in
.cache/runs/<name>__stress.pkl (a re-run, not a trial).
"""

from __future__ import annotations

import argparse
import subprocess
import sys

import numpy as np
import pandas as pd

from lab import ROOT
from lab.b3 import INFO0, IS_END, OOS0, OOS_END, windows
from lab.leaderboard import N01, declared_total
from lab.runner import HCACHE, load_hourly
from lab.scorecard import metrics

PERIODS = {"IS": (None, IS_END), "OOS": (OOS0, OOS_END), "Jul-Oct 2026 (info only)": (INFO0, None)}


def stressed(name: str) -> pd.DataFrame:
    p = HCACHE / f"{name}__stress.pkl"
    if p.exists():
        return pd.read_pickle(p)
    from lab.robustness import stressed as run_stress
    h = run_stress(name, {})
    h.to_pickle(p)
    return h


def card(name: str) -> dict:
    h = load_hourly(name)
    if h is None:
        raise SystemExit(f"{name}: no hourly curve in .cache/runs (run it first)")
    hs = stressed(name)
    out = {}
    for k, (a, b) in PERIODS.items():
        x = h.loc[a:b]
        m = metrics(x["equity"].values)
        w = windows(h, a, b)
        ws = windows(hs, a, b)
        yrs = (x.index[-1] - x.index[0]) / pd.Timedelta(days=365)
        r = w["ret"] if not w.empty else pd.Series(dtype=float)
        rs = ws["ret"] if not ws.empty else pd.Series(dtype=float)
        out[k] = {
            "from": str(x.index[0].date()), "to": str(x.index[-1].date()), "return": m.get("return"),
            "sharpe": m.get("sharpe"), "sortino": m.get("sortino"), "calmar": m.get("calmar"),
            "comp_full": m.get("composite"), "comp_14d": float(w["comp"].median()) if len(w) else None,
            "mdd": m.get("mdd"), "n": int(len(r)),
            "p10": float((r >= 0.10).mean()) if len(r) else None, "p8": float((r >= 0.08).mean()) if len(r) else None,
            "pm10": float((r <= -0.10).mean()) if len(r) else None,
            "median": float(r.median()) if len(r) else None, "worst": float(r.min()) if len(r) else None,
            "pos": float((r > 0).mean()) if len(r) else None,
            "fees_yr": float(x["fees"].sum() / x["equity"].mean() / yrs),
            "trades_day": float(x["trades"].groupby(x.index.floor("D")).sum().mean()),
            "active14": float(w["active"].mean()) if len(w) else None,
            "s_p10": float((rs >= 0.10).mean()) if len(rs) else None,
            "s_pm10": float((rs <= -0.10).mean()) if len(rs) else None,
            "s_median": float(rs.median()) if len(rs) else None, "s_worst": float(rs.min()) if len(rs) else None,
            "s_return": float(hs["equity"].loc[a:b].iloc[-1] / hs["equity"].loc[a:b].iloc[0] - 1),
        }
        ok = lambda: out[k]["pm10"] is not None and out[k]["pm10"] <= 0.10 and out[k]["worst"] >= -0.20
        out[k]["meets"] = ok()
    return out


ROWS = [("period", "range", None), ("return", "Total return", "pct"), ("sharpe", "Sharpe", "f2"),
        ("sortino", "Sortino", "f2"), ("calmar", "Calmar", "f2"),
        ("comp_full", "Composite, whole period", "f2"), ("comp_14d", "Composite, median of 14d windows", "f2"),
        ("mdd", "Max drawdown", "pct"), ("n", "14d windows", "int"), ("p10", "P(14d >= +10%)", "p"),
        ("p8", "P(14d >= +8%)", "p"), ("pm10", "P(14d <= -10%)", "p"), ("median", "Median 14d", "pct"),
        ("worst", "Worst 14d", "pct"), ("pos", "% positive 14d", "p"), ("meets", "Constraints met", "yn"),
        ("fees_yr", "Fees / yr (of equity)", "pct1"), ("trades_day", "Trades / day", "f1"),
        ("active14", "Active days per 14", "f1"), ("s_return", "Stress: total return", "pct"),
        ("s_p10", "Stress: P(14d >= +10%)", "p"), ("s_pm10", "Stress: P(14d <= -10%)", "p"),
        ("s_median", "Stress: median 14d", "pct"), ("s_worst", "Stress: worst 14d", "pct")]


def fmt(v, kind) -> str:
    if v is None or (isinstance(v, float) and np.isnan(v)):
        return "n/a"
    return {"pct": lambda: f"{v:+.1%}", "pct1": lambda: f"{v:.1%}", "p": lambda: f"{v:.0%}",
            "f2": lambda: f"{v:.2f}", "f1": lambda: f"{v:.1f}", "int": lambda: f"{int(v)}",
            "yn": lambda: "yes" if v else "**no**"}[kind]()


def git_hash() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True,
                              text=True).stdout.strip()
    except OSError:
        return "?"


def render(names: list[str], cards: dict[str, dict]) -> str:
    n_tr = declared_total()
    sr0 = N01.inv_cdf(1 - 1 / n_tr)
    L = [f"# Stats card: `{names[0]}`\n",
         f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by `python -m lab.stats_card "
         f"{' '.join(names)}` at lab commit {git_hash()}. Judged on data to 2026-06-30 (IS / OOS). "
         f"**Jul-Oct 2026 is informational only.**_\n",
         f"**Luck threshold:** {n_tr} trials declared across all blocks; the best of that many tries is expected "
         f"to look about {sr0:.1f} standard errors better than its true value, so small differences between "
         "runs are noise.\n",
         "**Constraints (each half):** P(14d <= -10%) <= 10% and worst 14d >= -20%. **Stress:** 100% taker "
         "fills and 7 bps slippage per fill (lab default 2 bps).\n"]
    for k in PERIODS:
        L += [f"\n## {k}\n", "| metric | " + " | ".join(f"`{n}`" for n in names) + " |",
              "|---|" + "---|" * len(names)]
        for key, label, kind in ROWS:
            if key == "period":
                vals = [f"{cards[n][k]['from']} to {cards[n][k]['to']}" for n in names]
            else:
                vals = [fmt(cards[n][k][key], kind) for n in names]
            L.append(f"| {label} | " + " | ".join(vals) + " |")
    L.append("\n_Sharpe / Sortino / Calmar on hourly returns annualised x 24 x 365; Calmar = annualised return / "
             "|max drawdown|; composite = 0.4 Sortino + 0.3 Sharpe + 0.3 Calmar. 14-day windows step daily from "
             "00:00 UTC and lie fully inside the period._")
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("runs", nargs="+")
    ap.add_argument("--out", help="default reports/stats_card_<first run>.md")
    a = ap.parse_args()
    cards = {n: card(n) for n in a.runs}
    out = ROOT / (a.out or f"reports/stats_card_{a.runs[0]}.md")
    out.write_text(render(a.runs, cards), encoding="utf-8")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
