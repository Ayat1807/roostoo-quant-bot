"""(c) Mock replay: the real StrategyBot runs 30 days of history against MockRoostoo.

    python -m tests.test_replay [--days 30]

Checks: 0 errors, gross exposure within capital_cap_usd, an order on every day,
KILL switch flattens within one poll and trading resumes after it is removed, and an
allow_short=false run never opens a short. Output goes to .cache/replay/ (git-ignored).
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

import pandas as pd

from bot import StrategyBot, load_config
from market_data import BarStore
from tests.hist_data import load_closes
from tests.mock_exchange import MockRoostoo

HERE = Path(__file__).resolve().parent.parent
OUT = HERE / ".cache" / "replay"


def replay(c: pd.DataFrame, days: int, allow_short: bool, kill_day: int | None,
           tag: str, guard: str | None = None) -> dict:
    base = OUT / tag
    shutil.rmtree(base, ignore_errors=True)
    cfg = load_config(HERE / "config.yaml")
    guard = guard or cfg["activity_guard"]          # default: the live config
    cfg.update(dry_run=False, poll_s=0, limit_wait_s=0, limit_poll_s=0, allow_short=allow_short,
               activity_guard=guard)
    cap = float(cfg["capital_cap_usd"])
    pairs = cfg["universe"]
    hours = c.index[-24 * days:]
    start = hours[0]
    ex = MockRoostoo(pairs, usd=50_000.0)
    ex.set_prices(c.loc[start].to_dict())
    now = {"t": start - pd.Timedelta(minutes=1)}
    bars = BarStore(pairs, base / "state" / "bars.csv")
    bars.close = c.loc[:start - pd.Timedelta(hours=1)].iloc[-800:].copy()
    # Simulate an order left resting by a previous run that was killed mid-wait.
    ex.pending_every, ex.n_limit = 1, 0
    px = round(c.loc[start, "ETH/USD"] * 0.99, 2)
    stale_id = ex.place_order("ETH/USD", "BUY", "0.1", "LIMIT", str(px))["OrderDetail"]["OrderID"]
    ex.pending_every, ex.n_limit = 3, 0
    bot = StrategyBot(cfg, ex, base_dir=base, clock=lambda: now["t"], sleep=lambda s: None, bars=bars)
    bot.setup()
    stale_canceled = ex.orders[stale_id]["Status"] == "CANCELED"
    bot.step(ex.ticker()["Data"], "startup")

    eq0 = ex.equity()
    max_gross = 0.0
    kill_on = kill_off = None
    kill_check: dict = {}
    if kill_day is not None:
        kill_on = start + pd.Timedelta(days=kill_day, hours=12)
        kill_off = kill_on + pd.Timedelta(hours=6)
    for h in hours:
        ex.set_prices(c.loc[h].to_dict())
        if kill_on is not None and h == kill_on:
            bot.kill_file.write_text("test")
            kill_check["gross_before"] = ex.gross_exposure()
        now["t"] = h + pd.Timedelta(minutes=59)           # last tick inside hour h
        bot.poll()
        if kill_on is not None and h == kill_on:
            kill_check["gross_after_1_poll"] = ex.gross_exposure()
            kill_check["flat_after_1_poll"] = ex.is_flat()
            kill_check["dust"] = {p: round(v, 2) for p, v in ex.pair_exposure().items() if v > 0.005}
        if kill_off is not None and h == kill_off:
            kill_check["gross_at_removal"] = ex.gross_exposure()
            kill_check["flat_at_removal"] = ex.is_flat()
            bot.kill_file.unlink()
        now["t"] = h + pd.Timedelta(hours=1, seconds=30)  # first tick of next hour: closes bar h
        bot.poll()
        max_gross = max(max_gross, ex.gross_exposure())
    if kill_off is not None:
        kill_check["gross_end"] = ex.gross_exposure()

    logs = base / "logs"
    read = lambda n: [json.loads(x) for x in (logs / f"{n}.jsonl").read_text().splitlines()] \
        if (logs / f"{n}.jsonl").exists() else []
    orders = [o for o in read("orders") if "response" in o]
    errors = read("errors") + [o for o in read("orders") if o.get("error")]
    days_with_orders = {o["time"][:10] for o in orders}
    all_days = {str(d.date()) for d in hours}
    shorts_opened = sum(1 for o in orders if o["action"] == "OPEN_SHORT")
    fallbacks = sum(1 for o in orders if o["action"] == "MARKET_FALLBACK")
    targets = [d for d in read("decisions") if d.get("event") == "targets"]
    guard_recs = [d for d in read("decisions") if d.get("event") == "rebalance"
                  and "minimal_guard" in d.get("reason", "")]
    guard_days = {d["time"][:10] for d in guard_recs}
    max_guard_pairs = max((len({x["pair"] for x in d["plan"]}) for d in guard_recs), default=0)
    pnl = ex.equity() - eq0
    return {"tag": tag, "start": start, "end": hours[-1], "orders": len(orders),
            "errors": errors, "active": f"{len(days_with_orders & all_days)}/{len(all_days)}",
            "inactive_days": sorted(all_days - days_with_orders), "max_gross": max_gross,
            "cap": cap, "pnl": pnl, "pnl_pct_of_cap": pnl / cap, "fees": ex.fees_paid,
            "shorts_opened": shorts_opened, "market_fallbacks": fallbacks,
            "target_updates": len(targets), "kill": kill_check, "calls": ex.calls,
            "stale_canceled": stale_canceled, "guard": guard, "guard_days": len(guard_days),
            "guard_recs": len(guard_recs), "max_guard_pairs": max_guard_pairs}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30)
    a = ap.parse_args()
    c = load_closes()
    ok = True
    for r in (replay(c, a.days, True, kill_day=20, tag="s3v2_shorts_on"),
              replay(c, 7, False, kill_day=None, tag="s3v2_shorts_off"),
              replay(c, a.days, True, kill_day=None, tag="s3v2_guard_full", guard="full"),
              replay(c, a.days, True, kill_day=None, tag="s3v2_guard_off", guard="off")):
        print(f"\n== {r['tag']} (activity_guard={r['guard']}): {r['start']:%Y-%m-%d %H:%M} -> "
              f"{r['end']:%Y-%m-%d %H:%M} UTC")
        if r["guard"] == "minimal":
            print(f"   minimal guard fired on {r['guard_days']} days ({r['guard_recs']} times), "
                  f"max pairs per guard trade {r['max_guard_pairs']}")
        print(f"   orders {r['orders']} (market fallbacks {r['market_fallbacks']}, shorts opened "
              f"{r['shorts_opened']}), target updates {r['target_updates']}, errors {len(r['errors'])}")
        print(f"   active days {r['active']}  inactive: {r['inactive_days'] or 'none'}")
        print(f"   max gross exposure ${r['max_gross']:,.2f} vs cap ${r['cap']:,.0f} "
              f"({r['max_gross'] / r['cap']:.1%})")
        print(f"   PnL ${r['pnl']:+,.2f} ({r['pnl_pct_of_cap']:+.2%} of cap), fees ${r['fees']:,.2f}")
        print(f"   API calls: {r['calls']}")
        if r["kill"]:
            k = r["kill"]
            print(f"   KILL: gross ${k['gross_before']:,.0f} -> ${k['gross_after_1_poll']:,.2f} after 1 poll; "
                  f"${k['gross_at_removal']:,.2f} at removal; ${k['gross_end']:,.0f} at end (resumed)")
            print(f"   KILL dust left (each below MiniOrder / one qty step, untradeable): {k['dust']}")
        checks = {
            "0 errors": not r["errors"],
            "within cap (<=110% incl. drift)": r["max_gross"] <= r["cap"] * 1.10,
            "trade every day": (not r["inactive_days"]) if r["guard"] != "off" else True,
            "stale pending order canceled at startup": r["stale_canceled"],
        }
        if r["kill"]:
            checks["KILL flattens in 1 poll (dust only)"] = r["kill"]["flat_after_1_poll"]
            checks["KILL stays flat (idle)"] = r["kill"]["flat_at_removal"]
            checks["resumes after KILL"] = r["kill"]["gross_end"] > 100
        if r["tag"] == "s3v2_shorts_off":
            checks["no shorts when allow_short=false"] = r["shorts_opened"] == 0
        if r["guard"] == "minimal":
            checks["minimal guard: <= 1 per day, one pair"] = (r["guard_recs"] == r["guard_days"]
                                                               and r["max_guard_pairs"] <= 1)
        if r["guard"] == "off":
            print(f"   [info] guard off: {len(r['inactive_days'])} inactive days "
                  f"(why the competition needs a guard)")
        for name, passed in checks.items():
            print(f"   [{'PASS' if passed else 'FAIL'}] {name}")
            ok &= passed
        if r["errors"]:
            print("   first errors:", r["errors"][:3])
    print(f"\n(c) mock replay: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
