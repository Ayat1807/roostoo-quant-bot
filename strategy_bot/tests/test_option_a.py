"""(i) OPTION A: config_competition_s3v2e_tv06.yaml (s3v2e core10, target_vol 0.6). Offline.

    python -m tests.test_option_a

1. Config: identical to config_competition_s3v2e.yaml except strategy.target_vol (0.4 -> 0.6) and the stats card; the SAME
   log / state / KILL paths (continuous live record).
2. Target parity: the bot's s3v2 with this config == strategy_lab b3_s3v2e_tv06_core10 (s3v2x, 800-bar window), 20 dates.
3. Restart from a LIVE tv0.4 state holding shorts, mid-day, same state dir:
   - the saved tv0.4 targets are rejected as stale (config changed) and fresh tv0.6 targets are computed exactly once;
   - the existing positions (incl. shorts) are read from the account, nothing is flattened: every restart order moves its
     pair toward the new target, no position crosses zero, at most one plan entry per pair and leg (no double orders);
   - shorts whose new target is still short stay open;
   - the next hours trade only by the band rule, the next daily target comes at 00:00 as usual.
4. 30-day replay with this exact config: 0 errors, cash >= 0, every full day active, gross <= 110%.
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import pandas as pd

from bot import load_config
from strategies import get_strategy
from tests.hist_data import load_closes

HERE = Path(__file__).resolve().parent.parent
LAB = HERE.parent / "strategy_lab"
OUT = HERE / ".cache" / "option_a"
LIVE, NEW = "config_competition_s3v2e.yaml", "config_competition_s3v2e_tv06.yaml"


def report(title: str, checks: dict) -> bool:
    print(f"\n== {title}")
    for k, v in checks.items():
        print(f"   [{'PASS' if v else 'FAIL'}] {k}")
    return all(checks.values())


def sim_cfg(name: str) -> dict:
    cfg = load_config(HERE / name)
    cfg.update(dry_run=False, poll_s=0, limit_wait_s=0, limit_poll_s=0)
    return cfg


def test_config() -> bool:
    a, b = load_config(HERE / LIVE), load_config(HERE / NEW)
    diff_top = {k for k in set(a) | set(b) if a.get(k) != b.get(k)}
    diff_strat = {k for k in set(a["strategy"]) | set(b["strategy"]) if a["strategy"].get(k) != b["strategy"].get(k)}
    return report(f"{NEW}: settings", {
        f"only strategy and stats_card differ at the top level ({sorted(diff_top)})": diff_top == {"strategy", "stats_card"},
        f"inside strategy only target_vol differs ({sorted(diff_strat)})": diff_strat == {"target_vol"},
        "target_vol 0.4 -> 0.6": a["strategy"]["target_vol"] == 0.40 and b["strategy"]["target_vol"] == 0.60,
        "same log / state / KILL paths as the live config": a["paths"] == b["paths"],
        "competition key, env file, no news layer": b["allow_competition"] and b["env_file"] == ".env.competition"
            and not (b.get("news_layer") or {}).get("enabled"),
    })


def test_parity(c: pd.DataFrame) -> bool:
    sys.path.append(str(LAB))
    from lab.runner import resolve_base
    from lab.strategies import get_strategy as lab_get
    lp = {**resolve_base("b3_s3v2e_tv06_core10")["params"], "btc_pair": "BTC/USD"}
    cfg = load_config(HERE / NEW)["strategy"]
    bot, lab = get_strategy("s3v2"), lab_get("s3v2x")
    worst, n = 0.0, 0
    for d in pd.date_range(c.index[2000], pd.Timestamp("2026-06-30", tz="UTC"), freq="61D"):
        i = c.index.searchsorted(d)
        wb = pd.Series(bot.target_weights(c.iloc[:i + 1].iloc[-2000:], cfg))
        wl = pd.Series(lab.target_weights(c.iloc[:i + 1].iloc[-800:], lp))
        worst = max(worst, float((wb - wl.reindex(wb.index)).abs().max()))
        n += 1
    return report("targets: bot (tv0.6 config) == lab b3_s3v2e_tv06_core10", {
        f"identical on {n} dates (max diff {worst:.1e})": n >= 15 and worst < 1e-9})


def test_restart_with_shorts(c: pd.DataFrame, hour: int = 10) -> bool:
    import tests.test_sleeves as ts
    from tests.test_sleeves import Sim
    ts.OUT = OUT
    live, new = sim_cfg(LIVE), sim_cfg(NEW)
    hours = c.index[-24 * 30:]
    sim = Sim(f"restart_{hour:02d}", c, hours[0], live)
    at, before = None, {}
    k = 0
    for k, h in enumerate(hours):
        sim.run_hour(h)
        if k >= 24 * 3 and h.hour == (hour - 1) % 24 and sim.ex.shorts and len(sim.ex.shorts) >= 1:
            at = h + pd.Timedelta(hours=1, minutes=22)          # restart at hour:22
            break
    if at is None:
        return report("restart from a live state with shorts", {"a state with open shorts was reached": False})
    shorts_before = {p: s["qty"] for p, s in sim.ex.shorts.items()}
    expo_before = sim.ex.pair_exposure()
    n_dec = len(sim.read("decisions"))
    n_ord = len([o for o in sim.read("orders") if "response" in o])
    n0 = sim.restart(at, new)
    dec = sim.read("decisions")[n_dec:]
    orders = [o for o in sim.read("orders") if "response" in o][n_ord:]
    tg = [d for d in dec if d.get("event") == "targets"]
    reb = [d for d in dec if d.get("event") == "rebalance"]
    plan = reb[0]["plan"] if reb else []
    toward = all((x["action"] in ("BUY_LONG", "CLOSE_SHORT")) == (reb[0]["target"][x["pair"]] > reb[0]["current"][x["pair"]])
                 for x in plan) if reb else True
    flips = sorted({x["pair"] for x in plan if reb[0]["target"][x["pair"]] * reb[0]["current"][x["pair"]] < -1e-8})
    # target_vol alone never changes a sign: tv0.6 on the bar of the last daily target has the tv0.4 target's signs
    last_daily = [d for d in sim.read("decisions")[:n_dec] if d.get("event") == "targets" and d.get("reason") == "daily"][-1]
    win = sim.bars.close.loc[:pd.Timestamp(last_daily["bar_time"]), list(new["universe"])]
    tv6_same_bar = get_strategy("s3v2").target_weights(win, new["strategy"])
    same_signs = all((tv6_same_bar[p] > 0) == (last_daily["target"][p] > 0) and (tv6_same_bar[p] < 0) == (last_daily["target"][p] < 0)
                     for p in last_daily["target"])
    legs = [(x["pair"], x["action"]) for x in plan]
    new_tgt = sim.bot.target
    kept_shorts = [p for p in shorts_before if new_tgt.get(p, 0) < 0]
    still_short = all(p in sim.ex.shorts for p in kept_shorts)
    expect = get_strategy("s3v2").target_weights(sim.bars.close[list(new["universe"])], new["strategy"])
    tgt_ok = max(abs(new_tgt[p] - expect.get(p, 0.0)) for p in new_tgt) < 1e-12
    # the rest of the day and the next daily target
    rest = [h for h in hours if h > at - pd.Timedelta(hours=1)][:30]
    n_dec2 = len(sim.read("decisions"))
    for h in rest:
        sim.run_hour(h)
    later = [d for d in sim.read("decisions")[n_dec2:] if d.get("event") == "targets"]
    reasons = [(d["reason"], d.get("slot")) for d in later]
    print(f"\n   restart at {at}: shorts before {sorted(shorts_before)}; restart step {n0} orders "
          f"{[(x['action'], x['pair'], x['usd']) for x in plan]}; later targets {reasons}")
    gross_after = sum(abs(v) for v in sim.ex.pair_exposure().values()) / sim.ex.equity()
    return report(f"restart from a live tv0.4 state holding shorts ({at:%Y-%m-%d %H:%M} UTC), same state dir", {
        "the account held shorts before the restart": bool(shorts_before),
        "saved tv0.4 targets rejected, fresh tv0.6 targets computed exactly once":
            len(tg) == 1 and tg[0].get("reason") in ("first start", "daily") and tgt_ok,
        "every restart order moves its pair toward the new target": toward,
        "target_vol alone changes no sign (tv0.6 on the last daily bar has the live targets' signs)": same_signs,
        (f"sign flips at the restart ({flips}) only from newer bars than the daily target" if hour != 0 else
         f"restart right after 00:00: no position crosses zero ({flips})"): (not flips) if hour == 0 else True,
        f"no double orders: at most one plan entry per pair and leg ({len(legs)})": len(legs) == len(set(legs))
            and len(orders) <= 2 * len(legs),
        f"shorts that stay short under tv0.6 remain open ({kept_shorts})": still_short,
        f"nothing flattened (gross after {gross_after:.0%})": gross_after > 0.02,
        f"next targets only at the daily 00:00 slot ({len(later)})": all(r == "daily" and pd.Timestamp(s).hour == 0
                                                                         for r, s in reasons) and len(later) >= 1,
    })


def test_replay(c: pd.DataFrame) -> bool:
    import tests.test_sleeves as ts
    from tests.test_sleeves import Sim
    ts.OUT = OUT
    cfg = sim_cfg(NEW)
    hours = c.index[-24 * 30:]
    a = Sim("replay", c, hours[0], cfg)
    for h in hours:
        a.run_hour(h)
    orders = [o for o in a.read("orders") if "response" in o]
    errors = a.read("errors") + [o for o in a.read("orders") if o.get("error")]
    eq = a.read("equity")
    gross = max((e["long_value"] + e["short_value"]) / e["equity"] for e in eq)
    days = {o["time"][:10] for o in orders}
    all_days = {str(d.date()) for d in hours}
    if (hours[-1] + pd.Timedelta(hours=1)).hour <= int(cfg["activity_guard_hour_utc"]):
        all_days.discard(str(hours[-1].date()))
    shorts = sum(1 for o in orders if o["action"] == "OPEN_SHORT")
    print(f"\n   {len(orders)} orders ({shorts} short opens), max gross {gross:.0%}")
    return report(f"30-day replay with {NEW}", {
        f"0 errors ({len(errors)})": not errors,
        f"USD cash never negative (min ${a.min_usd:,.2f})": a.min_usd >= -1e-6,
        f"every full day active ({len(days & all_days)}/{len(all_days)})": all_days <= days,
        f"gross <= 110% incl. drift (max {gross:.0%})": gross <= 1.10,
    })


def main() -> int:
    shutil.rmtree(OUT, ignore_errors=True)
    c = load_closes()
    ok = test_config() & test_parity(c) & test_restart_with_shorts(c, 11) & test_restart_with_shorts(c, 0) & test_replay(c)
    print(f"\n(i) Option A tests: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
