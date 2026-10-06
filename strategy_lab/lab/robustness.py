"""Real-market robustness (block 3 addendum, item 2; not selection trials).

    python -m lab.robustness b3_xsmom_tm10 b3_c50_s3v2e_xsmom_tm10

Re-runs each declared run (a combo re-runs both books) with 100% taker fills (spot_maker_share 0,
the lab default) and +5 bps extra slippage per fill (slippage 0.0002 -> 0.0007), and prints the
block-3 metrics next to the base result. Writes reports/robustness.md.
"""

from __future__ import annotations

import sys

import pandas as pd
import yaml

from lab import ROOT, load_config
from lab.b3 import INFO0, IS_END, OOS0, OOS_END, windows, wstats
from lab.backtest import run
from lab.combine import combine_hourly
from lab.runner import load_hourly, resolve_base

COSTS = {**load_config()["costs"], "spot_maker_share": 0.0, "slippage": 0.0007}


def combo_of(name: str) -> dict | None:
    for f in sorted(ROOT.glob("variants*.yaml")):
        for r in yaml.safe_load(f.read_text(encoding="utf-8")).get("runs", []):
            if r["name"] == name and "combo" in r:
                return r["combo"]
    return None


def stressed(name: str, memo: dict) -> pd.DataFrame:
    if name in memo:
        return memo[name]
    cb = combo_of(name)
    if cb:
        sat = cb.get("satellite") or cb["satellite_from"][0]
        h = combine_hourly(stressed(cb["core"], memo), stressed(sat, memo), float(cb["sat_share"]))
    else:
        spec = {**resolve_base(name), "name": name + "__stress", "costs": COSTS}
        h = run(spec)["hourly"]
    memo[name] = h
    return h


def stats(h: pd.DataFrame) -> dict:
    hj = h.loc[:OOS_END]
    yrs = (hj.index[-1] - hj.index[0]) / pd.Timedelta(days=365)
    return {"IS": wstats(windows(h, None, IS_END)), "OOS": wstats(windows(h, OOS0, OOS_END)),
            "INFO": wstats(windows(h, INFO0, None)),
            "fees": float(hj["fees"].sum() / hj["equity"].mean() / yrs)}


def main() -> int:
    names = sys.argv[1:]
    memo: dict = {}
    pr = lambda x: f"{x:.0%}"
    pct = lambda x: f"{x:+.1%}"
    L = ["# Real-market robustness\n",
         "Same runs with **100% taker fills** (0.10%) and **+5 bps extra slippage per fill** (7 bps total). "
         "Judged on data to 2026-06-30; Jul-Oct 2026 informational only.\n",
         "| run | costs | fees/yr | IS P>=10% / P<=-10% / worst | OOS P>=10% / P<=-10% / worst | OOS median 14d | "
         "meets both halves | INFO Jul-Oct P>=10% / median |", "|---|---|---|---|---|---|---|---|"]
    ok = lambda s: s.get("n", 0) > 0 and s["pm10"] <= 0.10 and s["worst"] >= -0.20
    for n in names:
        for label, h in (("base (lab: taker + 2 bps)", load_hourly(n)), ("taker + 7 bps", stressed(n, memo))):
            s = stats(h)
            i, o, inf = s["IS"], s["OOS"], s["INFO"]
            L.append(f"| {n} | {label} | {s['fees']:.1%} | {pr(i['p10'])} / {pr(i['pm10'])} / {pct(i['worst'])} | "
                     f"{pr(o['p10'])} / {pr(o['pm10'])} / {pct(o['worst'])} | {pct(o['median'])} | "
                     f"{'yes' if ok(i) and ok(o) else 'no'} | {pr(inf['p10'])} / {pct(inf['median'])} |")
    out = ROOT / "reports" / "robustness.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
