"""(g) Competition switch config (config_competition_s3v2e.yaml: s3v2 with EWMA vol on core10). Offline.

    python -m tests.test_competition_s3v2e

1. Config: single strategy (no sleeves), s3v2 + ewma 168h, core10, band 0.06, minimal guard, brake on, shorts on
   (short_scale_bull 0.5), no cap, allow_competition, env_file .env.competition, its OWN log / state / KILL paths
   (different from config_competition.yaml's, so the xsmom books are never read), committed stats card.
2. Target parity: the bot's s3v2 on this config == strategy_lab's b3_s3v2e_core10 strategy (s3v2x, same params, the lab's
   800-bar window) on 30 dates.
3. 30-day replay with this exact config on the mock exchange: fresh state -> first step computes fresh targets
   ("first start") and every startup order moves a pair toward them; 0 errors; cash never negative; gross <= 100% (+drift);
   every full day active; shorts used.
4. Mid-day restart: targets restored from its own state (no recompute), 0 orders at the restart, later orders identical.
5. The old bot's state (state_competition/) present with xsmom books and targets: not read (fresh first start anyway).
6. Switch step (a): KILL_competition on the old xsmom-on-R1 bot flattens all its positions (incl. non-core10 coins).
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import pandas as pd
import yaml

from bot import load_config
from strategies import get_strategy
from tests.hist_data import load_closes

HERE = Path(__file__).resolve().parent.parent
LAB = HERE.parent / "strategy_lab"
OUT = HERE / ".cache" / "competition_s3v2e"
CFG = "config_competition_s3v2e.yaml"


def report(title: str, checks: dict) -> bool:
    print(f"\n== {title}")
    for k, v in checks.items():
        print(f"   [{'PASS' if v else 'FAIL'}] {k}")
    return all(checks.values())


def sim_cfg() -> dict:
    cfg = load_config(HERE / CFG)
    cfg.update(dry_run=False, poll_s=0, limit_wait_s=0, limit_poll_s=0)
    return cfg


def test_config() -> bool:
    cfg = load_config(HERE / CFG)
    old = load_config(HERE / "config_competition.yaml")
    s = cfg["strategy"]
    p, po = cfg["paths"], old["paths"]
    import subprocess
    tracked = subprocess.run(["git", "ls-files", cfg["stats_card"]], cwd=HERE.parent, capture_output=True, text=True).stdout
    return report(f"{CFG}: settings", {
        "single strategy, no sleeves": not cfg.get("sleeves"),
        "s3v2, vol_method ewma, halflife 168h, short_scale_bull 0.5":
            s["name"] == "s3v2" and s["vol_method"] == "ewma" and s["ewma_halflife"] == 168 and s["short_scale_bull"] == 0.5,
        "core10 universe": cfg["universe"] == ["BTC/USD", "ETH/USD", "SOL/USD", "BNB/USD", "XRP/USD", "ADA/USD", "DOGE/USD",
                                               "AVAX/USD", "LINK/USD", "DOT/USD"],
        "band 0.06, minimal guard, brake on (-4% / -7%), shorts on, no cap":
            cfg["band"] == 0.06 and cfg["activity_guard"] == "minimal" and cfg["dd_soft"] == -0.04
            and cfg["dd_hard"] == -0.07 and cfg["allow_short"] is True and cfg["capital_cap_usd"] is None,
        "allow_competition true, env_file .env.competition": cfg["allow_competition"] is True
            and cfg["env_file"] == ".env.competition",
        "own paths logs_competition_s3v2e / state_competition_s3v2e / KILL_competition_s3v2e":
            (p["log_dir"], p["state_dir"], p["kill_file"]) == ("logs_competition_s3v2e", "state_competition_s3v2e",
                                                               "KILL_competition_s3v2e"),
        "no path shared with config_competition.yaml (xsmom books never read)":
            not {p["log_dir"], p["state_dir"], p["kill_file"]} & {po["log_dir"], po["state_dir"], po["kill_file"]},
        f"stats card committed ({cfg['stats_card']})": bool(tracked.strip()),
    })


def test_parity(c: pd.DataFrame) -> bool:
    sys.path.insert(0, str(LAB))
    from lab.runner import resolve_base
    from lab.strategies import get_strategy as lab_get
    lp = {**resolve_base("b3_s3v2e_core10")["params"], "btc_pair": "BTC/USD"}
    cfg = load_config(HERE / CFG)["strategy"]
    bot, lab = get_strategy("s3v2"), lab_get("s3v2x")
    dates = pd.date_range(c.index[2000], pd.Timestamp("2026-06-30", tz="UTC"), freq="41D")   # history from 2023-01
    worst, n = 0.0, 0
    for d in dates:
        i = c.index.searchsorted(d)
        wb = pd.Series(bot.target_weights(c.iloc[:i + 1].iloc[-2000:], cfg))
        wl = pd.Series(lab.target_weights(c.iloc[:i + 1].iloc[-800:], lp))
        worst = max(worst, float((wb - wl.reindex(wb.index)).abs().max()))
        n += 1
    return report(f"targets: bot ({CFG}) == lab b3_s3v2e_core10", {
        f"identical on {n} dates (max diff {worst:.1e})": n >= 25 and worst < 1e-9})


def test_replay_and_restart(c: pd.DataFrame) -> bool:
    import tests.test_sleeves as ts
    from tests.test_sleeves import Sim
    ts.OUT = OUT
    shutil.rmtree(OUT, ignore_errors=True)
    cfg = sim_cfg()
    hours = c.index[-24 * 30:]
    class WithOldState(Sim):
        def new_bot(self):
            # the old xsmom bot's state next to it (books / targets for today's slot): must not be read
            old = self.base / "state_competition"
            old.mkdir(parents=True, exist_ok=True)
            (old / "targets.json").write_text(json.dumps({"target": {"BTC/USD": 0.9}, "slot": str(hours[0].floor("D"))}))
            (old / "sleeves.json").write_text(json.dumps({"books": {"xsmom": {"cash": 1, "units": {"NEAR/USD": 5}}}}))
            return super().new_bot()

    a = WithOldState("replay", c, hours[0], cfg)
    first = [d for d in a.read("decisions") if d.get("event") == "targets"]
    start_reb = [d for d in a.read("decisions") if d.get("event") == "rebalance"]
    toward = all((x["action"] in ("BUY_LONG", "CLOSE_SHORT")) == (r["target"][x["pair"]] > r["current"][x["pair"]])
                 for r in start_reb[:1] for x in r["plan"])
    b = Sim("restart_b", c, hours[0], cfg)
    at = (hours[-1] - pd.Timedelta(days=5)).floor("D") + pd.Timedelta(hours=10, minutes=22)
    out = {}
    for h in hours:
        if "n0" not in out and b.now["t"] < at <= h + pd.Timedelta(minutes=59):
            t0 = dict(b.bot.target)
            out["n0"] = b.restart(at)
            out["same"] = dict(b.bot.target) == t0
            out["restored"] = any(d.get("reason") == "restored" for d in b.read("decisions") if d.get("event") == "targets")
        a.run_hour(h)
        b.run_hour(h)
    orders = [o for o in a.read("orders") if "response" in o]
    errors = a.read("errors") + [o for o in a.read("orders") if o.get("error")]
    eq = a.read("equity")
    gross = max((e["long_value"] + e["short_value"]) / e["equity"] for e in eq)
    days = {o["time"][:10] for o in orders}
    all_days = {str(d.date()) for d in hours}
    if (hours[-1] + pd.Timedelta(hours=1)).hour <= int(cfg["activity_guard_hour_utc"]):
        all_days.discard(str(hours[-1].date()))
    shorts = sum(1 for o in orders if o["action"] == "OPEN_SHORT")
    key = lambda o: (o["action"], json.dumps(o.get("request"), sort_keys=True))
    oa = [key(o) for o in a.read("orders") if "response" in o and pd.Timestamp(o["time"]) > at]
    ob = [key(o) for o in b.read("orders") if "response" in o and pd.Timestamp(o["time"]) > at]
    print(f"\n   {len(orders)} orders over 30 days ({shorts} short opens), max gross {gross:.0%}, first targets "
          f"{ {p: round(w, 3) for p, w in first[0]['target'].items() if w} }")
    ok1 = report(f"30-day replay with {CFG} (fresh state)", {
        f"first step computes fresh targets ({first[0].get('reason')})": first[0].get("reason") == "first start",
        "old bot's state_competition/ not read (no 'restored' at the first start)":
            not any(d.get("reason") == "restored" for d in first[:1]),
        "every startup order moves its pair toward the fresh targets": toward and bool(start_reb),
        f"0 errors ({len(errors)})": not errors,
        f"USD cash never negative (min ${a.min_usd:,.2f})": a.min_usd >= -1e-6,
        f"gross <= 100% incl. drift (max {gross:.0%})": gross <= 1.10,
        f"every full day active ({len(days & all_days)}/{len(all_days)})": all_days <= days,
        f"shorts used ({shorts} opens)": shorts > 0,
    })
    ok2 = report(f"mid-day restart with {CFG} at {at:%Y-%m-%d %H:%M} UTC", {
        "targets restored from its own state (no recompute)": out.get("restored", False) and out.get("same", False),
        "restart step placed 0 orders": out.get("n0") == 0,
        f"orders after the restart identical ({len(oa)})": oa == ob and len(oa) > 0,
        "end equity identical": abs(a.ex.equity() - b.ex.equity()) < 1e-6,
    })
    return ok1 and ok2


def test_old_bot_kill() -> bool:
    """Switch step (a): KILL_competition on the running xsmom-on-R1 sleeve bot sells every position itself, incl. coins
    outside core10 (e.g. NEAR), within one poll, and stays flat."""
    import tests.test_sleeves as ts
    from tests.test_competition import CompSim, comp_cfg, pool_closes
    ts.OUT = OUT
    cfg = comp_cfg()
    cp, prec = pool_closes()
    hours = cp.index[-24 * 6:]
    cp = cp[[q for q in cp.columns if pd.notna(cp.loc[hours[0], q])]]
    sim = CompSim("old_kill", cp, hours[0], cfg, prec).sim
    held_before, k = {}, 0
    for k, h in enumerate(hours):
        sim.run_hour(h)
        held_before = {q for q, v in sim.ex.pair_exposure().items() if v > sim.ex.unsellable(q) * 1.01}
        if k > 30 and len(held_before) >= 3:
            break
    kill = sim.base / cfg["paths"]["kill_file"]
    kill.write_text("switch to s3v2e")
    sim.now["t"] += pd.Timedelta(minutes=1)
    sim.bot.poll()                              # one poll: reacts to KILL without waiting for the hour
    flat1 = sim.ex.is_flat()
    for h in hours[k + 1:k + 4]:
        sim.run_hour(h)
    left = {q: round(v, 2) for q, v in sim.ex.pair_exposure().items() if v > 0.01}
    outside = sorted(held_before - set(load_config(HERE / CFG)["universe"]))
    print(f"\n   held before KILL: {sorted(held_before)} (outside core10: {outside}); dust left: {left}")
    return report("old xsmom bot: KILL_competition flattens itself (switch step a)", {
        f"held >= 3 coins before KILL ({len(held_before)})": len(held_before) >= 3,
        "flat (dust only) after one poll": flat1,
        "still flat 3 hours later": sim.ex.is_flat(),
    })


def main() -> int:
    c = load_closes()
    ok = test_config() & test_parity(c) & test_replay_and_restart(c) & test_old_bot_kill()
    print(f"\n(g) competition s3v2e config tests: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
