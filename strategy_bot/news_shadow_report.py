"""Forward shadow-log review of the news layer (read-only). Run after a few days on the testing bot:

    python news_shadow_report.py --config config_testing_hmm_cusum.yaml [--days 3]

Reports: headlines fetched / relevant / classified, LLM cost, every veto with its headline and what the coin did during the
veto window vs the other coins (a veto followed by an outperforming coin is flagged as a likely false alarm), how often the
calendar / Fear & Greed rules were active, and the would-be P&L difference: for every hourly step, (would-be weight - actual
weight) x the coin's next-hour return x sizing equity, summed (an approximation: it ignores the 6pp band and fees).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd
import yaml

HERE = Path(__file__).resolve().parent


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config_testing_hmm_cusum.yaml")
    ap.add_argument("--days", type=float, default=3)
    a = ap.parse_args()
    cfg = yaml.safe_load((HERE / a.config).read_text(encoding="utf-8"))
    paths = cfg.get("paths", {})
    log_dir, state_dir = HERE / paths.get("log_dir", "logs"), HERE / paths.get("state_dir", "state")
    p = log_dir / "news_shadow.jsonl"
    if not p.exists():
        print(f"no shadow log at {p}")
        return 2
    recs = [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
    since = pd.Timestamp.now(tz="UTC") - pd.Timedelta(days=a.days)
    recs = [r for r in recs if pd.Timestamp(r["time"]) >= since]
    items = [r for r in recs if r["event"] == "item"]
    steps = [r for r in recs if r["event"] == "step"]
    vetoes = [r for r in items if r.get("rule")]
    closes = pd.read_csv(state_dir / "bars.csv", index_col=0)
    closes.index = pd.to_datetime(closes.index, utc=True)
    eq = [json.loads(x) for x in (log_dir / "equity.jsonl").read_text(encoding="utf-8").splitlines()][-1]
    sizing = float(eq.get("sizing_equity") or eq.get("equity") or 0)
    summ = [r for r in recs if r["event"] == "daily_summary"]
    print(f"News shadow review, last {a.days:g} days (since {since:%Y-%m-%d %H:%M} UTC)\n")
    print(f"headline items classified: {len(items)}; invalid LLM answers: {sum(r['event'] == 'llm_invalid' for r in recs)}; "
          f"cost-cap hits: {sum(r['event'] == 'cost_cap' for r in recs)}")
    for s in summ:
        print(f"  {s['day']}: fetched {s.get('fetched')}, relevant {s.get('relevant')}, classified {s.get('classified')}, "
              f"vetoes {s.get('vetoes')}, LLM ${s.get('llm_cost_usd')}, gross actual {s.get('avg_gross_actual')} vs would "
              f"{s.get('avg_gross_would')}")
    cal = sum(any(f.startswith("calendar") for f in r["fired"]) for r in steps)
    fng = sum(any(f.startswith("fear") for f in r["fired"]) for r in steps)
    print(f"\nsteps: {len(steps)}; calendar rule active in {cal}, Fear & Greed rule in {fng}")
    print("\nVetoes (likely false alarm = the coin beat the other coins' average during the veto window):")
    if not vetoes:
        print("  none")
    for v in vetoes:
        coin = f"{v['llm']['coin']}/USD"
        t0 = pd.Timestamp(v["time"]).floor("h")
        win = closes.loc[t0:t0 + pd.Timedelta(hours=72)]
        if coin in win.columns and len(win) > 1:
            r = win.iloc[-1] / win.iloc[0] - 1
            others = r.drop(coin).mean()
            flag = "LIKELY FALSE ALARM" if r[coin] > others else "coin underperformed (veto would have helped)"
            print(f"  {v['time'][:16]} {coin}: {v['headline'][:80]} | coin {r[coin]:+.1%} vs others {others:+.1%} over "
                  f"{len(win) - 1}h -> {flag}")
        else:
            print(f"  {v['time'][:16]} {coin}: {v['headline'][:80]} | no price window yet")
    pnl = 0.0
    for s in steps:
        t = pd.Timestamp(s["time"]).floor("h") - pd.Timedelta(hours=1)        # the bar that just closed
        nxt = t + pd.Timedelta(hours=1)
        if t not in closes.index or nxt not in closes.index:
            continue
        for p, (eff, would) in (s.get("changed") or {}).items():
            if p in closes.columns:
                pnl += (would - eff) * (closes.at[nxt, p] / closes.at[t, p] - 1) * sizing
    print(f"\nWould-be P&L difference (layer minus actual, approximate): ${pnl:+,.2f} "
          f"({pnl / sizing:+.3%} of sizing equity ${sizing:,.0f})" if sizing else "\nno equity record")
    return 0


if __name__ == "__main__":
    sys.exit(main())
