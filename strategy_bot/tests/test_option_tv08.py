"""config_competition_s3v2e_tv08.yaml (s3v2e core10, target_vol 0.8 / max_w 0.4, brake -6% / -10% flat 12h). Offline.

    python -m tests.test_option_tv08

1. Config: identical to config_competition_s3v2e.yaml except strategy.target_vol (0.4 -> 0.8), strategy.max_w (0.3 -> 0.4),
   the brake (dd_soft -0.06, dd_hard -0.10, cooloff_h 12), brake_reset_before and the stats card; the SAME log / state /
   KILL paths (continuous live record).
2. Target parity: the bot's s3v2 with this config == strategy_lab b3_s3v2e_tv08_w04_core10 (s3v2x, 800-bar window), 20 dates.
3. Restart from the LIVE state after a hard stop (account flat, cooloff running for 20 more hours), same state dir:
   - the running cooloff is cleared once (brake_reset_before), the peak restarts at the current equity, the saved tv0.4
     targets are rejected as stale and fresh tv0.8 targets are computed exactly once, positions are opened at the restart
     (no waiting out the old 24h), every order moves its pair toward the new target, no double orders;
   - the reset is ONE-SHOT: a later cooloff with the same config is respected (state/risk.json: brake_reset);
   - a brake_reset_before in the past does nothing.
4. 30-day replay with this exact config: 0 errors, cash >= 0, every full day active, gross <= 110%.
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import pandas as pd

from bot import load_config
from risk import RiskManager
from strategies import get_strategy
from tests.hist_data import load_closes

HERE = Path(__file__).resolve().parent.parent
LAB = HERE.parent / "strategy_lab"
OUT = HERE / ".cache" / "option_tv08"
LIVE, NEW = "config_competition_s3v2e.yaml", "config_competition_s3v2e_tv08.yaml"
LAB_RUN = "b3_s3v2e_tv08_w04_core10"


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
        f"top level: only strategy, brake, brake_reset_before, sizing_frac, cash_cap_orders, stats_card differ ({sorted(diff_top)})":
            diff_top == {"strategy", "stats_card", "dd_soft", "dd_hard", "cooloff_h", "brake_reset_before", "sizing_frac", "cash_cap_orders"},
        f"inside strategy only target_vol and max_w differ ({sorted(diff_strat)})": diff_strat == {"target_vol", "max_w"},
        "target_vol 0.8, max_w 0.4 (= lab b3_s3v2e_tv08_w04_core10)": b["strategy"]["target_vol"] == 0.80 and b["strategy"]["max_w"] == 0.40,
        "brake -6% / -10%, flat 12h": b["dd_soft"] == -0.06 and b["dd_hard"] == -0.10 and b["cooloff_h"] == 12,
        "brake_reset_before is 2026-10-16 00:00 UTC (deploy window after the CPI freeze)":
            pd.Timestamp(b["brake_reset_before"]) == pd.Timestamp("2026-10-16T00:00:00Z"),
        "same log / state / KILL paths as the live config": a["paths"] == b["paths"],
        "competition key, env file, no news layer": b["allow_competition"] and b["env_file"] == ".env.competition"
            and not (b.get("news_layer") or {}).get("enabled"),
    })


def test_parity(c: pd.DataFrame) -> bool:
    sys.path.append(str(LAB))
    from lab.runner import resolve_base
    from lab.strategies import get_strategy as lab_get
    lp = {**resolve_base(LAB_RUN)["params"], "btc_pair": "BTC/USD"}
    cfg = load_config(HERE / NEW)["strategy"]
    bot, lab = get_strategy("s3v2"), lab_get("s3v2x")
    worst, n = 0.0, 0
    for d in pd.date_range(c.index[2000], pd.Timestamp("2026-06-30", tz="UTC"), freq="61D"):
        i = c.index.searchsorted(d)
        wb = pd.Series(bot.target_weights(c.iloc[:i + 1].iloc[-2000:], cfg))
        wl = pd.Series(lab.target_weights(c.iloc[:i + 1].iloc[-800:], lp))
        worst = max(worst, float((wb - wl.reindex(wb.index)).abs().max()))
        n += 1
    return report(f"targets: bot (tv0.8 config) == lab {LAB_RUN}", {
        f"identical on {n} dates (max diff {worst:.1e})": n >= 15 and worst < 1e-9})


def test_restart_after_hard_stop(c: pd.DataFrame) -> bool:
    import tests.test_sleeves as ts
    from tests.test_sleeves import Sim
    ts.OUT = OUT
    live, new = sim_cfg(LIVE), sim_cfg(NEW)
    hours = c.index[-24 * 30:]
    sim = Sim("restart_hard_stop", c, hours[0], live)
    for h in hours[:24 * 4]:
        sim.run_hour(h)
    # a hard stop at hour 96 (as the live bot's after the spike): flat for 24h, peak reset
    h0 = hours[24 * 4]
    sim.bot.risk.flat_until = sim.bot.risk.reset_at = h0 + pd.Timedelta(hours=1) + pd.Timedelta(hours=24)
    sim.bot.risk._save()
    for h in hours[24 * 4: 24 * 4 + 4]:
        sim.run_hour(h)
    gross_flat = sum(abs(v) for v in sim.ex.pair_exposure().values()) / sim.ex.equity()
    eq_log = sim.read("equity")
    cooloff_seen = any("cooloff" in (e.get("brake") or "") for e in eq_log[-3:])
    at = hours[24 * 4 + 4] + pd.Timedelta(minutes=22)                  # restart with ~20h of cooloff left
    n_dec, n_ord = len(sim.read("decisions")), len([o for o in sim.read("orders") if "response" in o])
    n0 = sim.restart(at, new)
    dec = sim.read("decisions")[n_dec:]
    orders = [o for o in sim.read("orders") if "response" in o][n_ord:]
    tg = [d for d in dec if d.get("event") == "targets"]
    reb = [d for d in dec if d.get("event") == "rebalance"]
    plan = reb[0]["plan"] if reb else []
    toward = all((x["action"] in ("BUY_LONG", "CLOSE_SHORT")) == (reb[0]["target"][x["pair"]] > reb[0]["current"][x["pair"]])
                 for x in plan) if reb else False
    legs = [(x["pair"], x["action"]) for x in plan]
    risk_state = json.loads(sim.bot.risk.state_path.read_text(encoding="utf-8"))
    brake_now = (sim.read("equity")[-1].get("brake") or "")
    expect = get_strategy("s3v2").target_weights(sim.bars.close[list(new["universe"])], new["strategy"])
    tgt_ok = max(abs(sim.bot.target[p] - expect.get(p, 0.0)) for p in sim.bot.target) < 1e-12
    gross_after = sum(abs(v) for v in sim.ex.pair_exposure().values()) / sim.ex.equity()
    # one-shot: a later cooloff under the same config is respected
    rm = RiskManager(new["dd_soft"], new["dd_hard"], new["cooloff_h"], 14, sim.bot.risk.state_path, sim.bot.kill_file,
                     pd.Timestamp(new["brake_reset_before"]))
    rm.flat_until = at + pd.Timedelta(hours=5)
    later_mult, later_why = rm.scale(at + pd.Timedelta(hours=1), sim.ex.equity())
    # a reset time in the past does nothing
    rm2 = RiskManager(new["dd_soft"], new["dd_hard"], new["cooloff_h"], 14, OUT / "rm2.json", sim.bot.kill_file,
                      pd.Timestamp("2020-01-01T00:00:00Z"))
    rm2.flat_until = at + pd.Timedelta(hours=5)
    past_mult, _ = rm2.scale(at, 100.0)
    print(f"\n   hard stop at {h0 + pd.Timedelta(hours=1)}, gross while flat {gross_flat:.1%}; restart at {at}: step orders {n0} "
          f"{[(x['action'], x['pair'], x['usd']) for x in plan]}; brake now '{brake_now}'; risk.json {risk_state.get('flat_until')} "
          f"/ brake_reset {risk_state.get('brake_reset')}")
    return report(f"restart after a hard stop (cooloff running), same state dir, at {at:%Y-%m-%d %H:%M} UTC", {
        f"the live bot was flat in cooloff before the restart (gross {gross_flat:.1%})": cooloff_seen and gross_flat < 0.07,
        "the cooloff is cleared at the first decision and the peak restarts at the current equity":
            "brake_reset" in brake_now and "cooloff" not in brake_now and risk_state.get("flat_until") is None
            and pd.Timestamp(risk_state["reset_at"]) == at.floor("min") or pd.Timestamp(risk_state["reset_at"]) <= at,
        "saved tv0.4 targets rejected, fresh tv0.8 targets computed exactly once":
            len(tg) == 1 and tg[0].get("reason") in ("first start", "daily") and tgt_ok,
        f"positions opened at the restart, no waiting (gross after {gross_after:.0%}, {len(orders)} orders)":
            gross_after > 0.10 and len(orders) >= 1,
        "every restart order moves its pair toward the new target": toward,
        f"no double orders: at most one plan entry per pair and leg ({len(legs)})": len(legs) == len(set(legs))
            and len(orders) <= 2 * len(legs),
        f"one-shot: a later cooloff with the same config is respected ({later_why})": later_mult == 0.0 and "cooloff" in later_why,
        "a brake_reset_before in the past does nothing": past_mult == 0.0,
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
    brakes = sorted({(e.get("brake") or "").split(" ")[0].split("=")[0] for e in eq})
    capped = [o for o in a.read("orders") if "capped_from" in o or "skipped" in o]
    print(f"\n   {len(orders)} orders ({shorts} short opens), max gross {gross:.0%}, brake states {brakes}, cash-capped orders {len(capped)}")
    return report(f"30-day replay with {NEW}", {
        f"0 errors ({len(errors)})": not errors,
        f"USD cash never negative (min ${a.min_usd:,.2f})": a.min_usd >= -1e-6,
        f"every full day active ({len(days & all_days)}/{len(all_days)})": all_days <= days,
        f"gross <= 110% incl. drift (max {gross:.0%})": gross <= 1.10,
    })


def main() -> int:
    shutil.rmtree(OUT, ignore_errors=True)
    c = load_closes()
    ok = test_config() & test_parity(c) & test_restart_after_hard_stop(c) & test_replay(c)
    print(f"\n(i) tv0.8 config tests: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
