"""Sleeve option event_refresh (strategy_lab block 4a, b4e_fast_12h; OFF in every shipped config).

    python -m tests.test_event_refresh

1. sleeve_slot: extra decision at 03:00 UTC (15:00 + 12h) only on event days (the event's UTC date
   and the 2 days after), the daily 15:00 decision unchanged.
2. Replay (config_competition.yaml + event_refresh, 30 days on the mock exchange): extra decisions logged
   as "event refresh" exactly at 03:00 on event days; orders only at 15:00, 03:00 on event days, startup
   or a brake change; the targets at each extra decision == xsmom on the R1 members' closes up to the
   02:00 bar (the lab's refresh bar); 0 errors.
3. Without the option the sleeve fingerprint has no event key (running books keep their targets).
4. A missing calendar file stops the bot at start.
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pandas as pd

from sleeves import SleeveSpec, event_days, sleeve_slot
from tests.test_competition import CompSim, comp_cfg, pool_closes

HERE = Path(__file__).resolve().parent.parent
OUT = HERE / ".cache" / "event_refresh"
EVR = {"calendar": "data/events.csv", "every_h": 12, "days_after": 2,
       "types": ["CPI", "FOMC_DECISION", "FOMC_MINUTES"]}


def report(title: str, checks: dict) -> bool:
    print(f"\n== {title}")
    for k, v in checks.items():
        print(f"   [{'PASS' if v else 'FAIL'}] {k}")
    return all(checks.values())


def ts(s: str) -> pd.Timestamp:
    return pd.Timestamp(s, tz="UTC")


def test_slot() -> bool:
    spec = SleeveSpec.from_cfg({"name": "x", "weight": 1, "strategy": {"name": "xsmom"}, "universe": ["BTC/USD"],
                                "execution": "scheduled", "decision_hour_utc": 15, "event_refresh": EVR},
                               {}, [], 0.06, 0)
    days = event_days(HERE / "data/events.csv", EVR["types"], 2)
    cases = {  # CPI 2026-09-11 12:30 UTC, FOMC 2026-09-16 18:00 UTC
        "2026-09-11 03:30": "2026-09-11 03:00", "2026-09-11 02:59": "2026-09-10 15:00",
        "2026-09-13 03:10": "2026-09-13 03:00", "2026-09-14 03:30": "2026-09-13 15:00",
        "2026-09-11 15:00": "2026-09-11 15:00", "2026-09-16 04:00": "2026-09-16 03:00",
        "2026-09-09 03:30": "2026-09-08 15:00"}
    got = {k: str(sleeve_slot(ts(k), spec, days)) for k in cases}
    ok = all(pd.Timestamp(got[k]) == ts(v) for k, v in cases.items())
    for k, v in cases.items():
        print(f"   now {k} -> slot {got[k]} (want {v})")
    return report("sleeve_slot with event_refresh every 12h", {"all cases": ok})


def test_replay(days: int = 30) -> bool:
    import tests.test_sleeves as tsl
    tsl.OUT = OUT
    cfg = comp_cfg()
    cfg["sleeves"] = copy.deepcopy(cfg["sleeves"])
    cfg["sleeves"][0]["event_refresh"] = EVR
    c, prec = pool_closes()
    hours = c.index[-24 * days:]
    c = c[[p for p in c.columns if pd.notna(c.loc[hours[0], p])]]
    cs = CompSim("replay", c, hours[0], cfg, prec)
    sim = cs.sim
    for h in hours:
        sim.run_hour(h)
    ev = event_days(HERE / "data/events.csv", EVR["types"], 2)
    dec = [d for d in sim.read("decisions") if d.get("event") == "targets" and d.get("sleeve") == "xsmom"]
    extra = [d for d in dec if d.get("reason") == "event refresh"]
    want = sorted(t for t in pd.date_range(hours[0].floor("D") + pd.Timedelta(days=1, hours=3),
                                            hours[-1], freq="1D") if t.date() in ev)
    got = sorted(pd.Timestamp(d["slot"]) for d in extra)
    eq = sim.read("equity")
    first = pd.Timestamp(eq[0]["time"])
    mult_change = {pd.Timestamp(eq[i]["time"]).floor("min") for i in range(1, len(eq)) if eq[i]["mult"] != eq[i - 1]["mult"]}
    orders = [o for o in sim.read("orders") if "response" in o]
    off = [o for o in orders if not (pd.Timestamp(o["time"]).hour == 15
                                     or (pd.Timestamp(o["time"]).hour == 3 and pd.Timestamp(o["time"]).date() in ev)
                                     or pd.Timestamp(o["time"]) == first
                                     or pd.Timestamp(o["time"]).floor("min") in mult_change)]
    # target parity at each extra decision: xsmom on the R1 members' closes up to the 02:00 bar
    from strategies import get_strategy
    xs = get_strategy("xsmom")
    worst = 0.0
    for d in extra:
        bar = pd.Timestamp(d["bar_time"])
        members = [p for p, w in d["target"].items()]
        win = c.loc[:bar, members].iloc[-2000:]
        skipped = set(d.get("liquidity_skipped") or {})
        ref = xs.target_weights(win[[p for p in members if p not in skipped]], {})
        diff = max([abs(ref.get(p, 0.0) - d["target"][p]) for p in members] or [0.0])
        worst = max(worst, diff)
    errors = sim.read("errors")
    return report(f"{days}-day replay with event_refresh (every 12h, 2 days after)", {
        f"extra decisions exactly at 03:00 on event days ({len(got)}: {[str(t.date()) for t in got]})":
            got == want and len(got) > 0,
        "extra decisions use the 02:00 bar": all(pd.Timestamp(d["bar_time"]).hour == 2 for d in extra),
        f"targets == xsmom on that bar (max diff {worst:.1e})": worst < 1e-12,
        f"orders only at 15:00 / 03:00 on event days / startup / brake change ({len(off)} off)": not off,
        f"0 errors ({len(errors)})": not errors,
    })


def test_flag_off_and_missing_calendar() -> bool:
    import tests.test_sleeves as tsl
    from bot import StrategyBot
    from tests.mock_exchange import MockRoostoo
    tsl.OUT = OUT
    cfg = comp_cfg()
    bot = StrategyBot(cfg, MockRoostoo(["BTC/USD"]), base_dir=OUT / "off")
    bot.r1s = {}
    bot.sleeve_specs[0].universe = ["BTC/USD"]
    fp_off = bot._sleeve_fp(bot.sleeve_specs[0])
    bad = copy.deepcopy(cfg)
    bad["sleeves"][0]["event_refresh"] = {**EVR, "calendar": "data/missing.csv"}
    try:
        StrategyBot(bad, MockRoostoo(["BTC/USD"]), base_dir=OUT / "bad")
        refused = False
    except (FileNotFoundError, OSError):
        refused = True
    return report("flag off / missing calendar", {
        "no event key in the fingerprint when the option is off": "event_refresh" not in fp_off,
        "missing calendar file -> the bot refuses to start": refused,
        "shipped configs keep event_refresh off": all("event_refresh:" not in ln.split("#")[0]
                                                      for f in HERE.glob("config*.yaml")
                                                      for ln in f.read_text(encoding="utf-8").splitlines()),
    })


def main() -> int:
    ok = test_slot() & test_flag_off_and_missing_calendar() & test_replay()
    print(f"\nevent_refresh tests: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
