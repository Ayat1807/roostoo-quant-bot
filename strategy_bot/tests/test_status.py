"""status.py (display only): sleeve-aware view, checked against a replay on the mock exchange.

    python -m tests.test_status

1. Competition config (one xsmom sleeve on R1): right after a 15:00 decision that traded,
   status shows the sleeve, its targets (== state/sleeves.json), its last decision (== the
   step just run) and next decision, ONLY the active universe (the R1 list + holdings), and
   actual weights == the mock account's post-trade weights (the heartbeat's own 'actual' is
   the pre-trade snapshot). Again one hour later (no new fills).
2. Single-strategy config (config.yaml without sleeves): same actual check after a trade.
3. status.py makes no API calls and writes nothing (files under the bot dir unchanged).
Output in .cache/status/.
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pandas as pd

import status
from tests.test_competition import CompSim, comp_cfg, pool_closes

HERE = Path(__file__).resolve().parent.parent
OUT = HERE / ".cache" / "status"


def report(title: str, checks: dict) -> bool:
    print(f"\n== {title}")
    for k, v in checks.items():
        print(f"   [{'PASS' if v else 'FAIL'}] {k}")
    return all(checks.values())


def account_weights(ex) -> dict[str, float]:
    eq = ex.equity()
    return {p: v / eq for p, v in ex.pair_exposure().items() if abs(v) > 1e-9}


def max_gap(a: dict[str, float], b: dict[str, float]) -> float:
    return max([abs(a.get(p, 0.0) - b.get(p, 0.0)) for p in set(a) | set(b)] or [0.0])


def snapshot_files(base: Path) -> dict[str, float]:
    return {str(p): p.stat().st_mtime_ns for p in base.rglob("*") if p.is_file()}


def test_competition() -> bool:
    import tests.test_sleeves as ts
    ts.OUT = OUT
    cfg = comp_cfg()
    c, prec = pool_closes()
    hours = c.index[-24 * 8:]
    c = c[[p for p in c.columns if pd.notna(c.loc[hours[0], p])]]
    cs = CompSim("competition", c, hours[0], cfg, prec)
    sim = cs.sim
    found = None
    for i, h in enumerate(hours):
        n_before = len([o for o in sim.read("orders") if "response" in o])
        sim.run_hour(h)
        n_new = len([o for o in sim.read("orders") if "response" in o]) - n_before
        if h.hour == 14 and n_new > 0 and i > 24:
            found = (i, h, n_new)
            break
    if found is None:
        return report("status: competition config", {"a 15:00 decision with trades in the window": False})
    i, h, n_new = found
    now = sim.now["t"]
    files0 = snapshot_files(sim.base)
    d = status.build(cfg, sim.base, now=now)
    lines, _ = status.render(cfg, d)
    files1 = snapshot_files(sim.base)
    text = "\n".join(lines)
    print("\n" + text)
    bot = sim.bot
    book = bot.books["xsmom"]
    sv = d["sleeves"][0]
    r1 = bot.r1s["xsmom"]
    members = list(r1.state["selected"]) if hasattr(r1, "state") and r1.state else bot.sleeve_specs[0].universe
    acct = account_weights(sim.ex)
    hb_gap = max_gap({p: w for p, w in (d["hb"].get("actual") or {}).items()}, acct)
    gap = max_gap(d["actual"], acct)
    held = {p for p, w in acct.items() if abs(w) > 1e-4}
    ok1 = report(f"status right after the {h + pd.Timedelta(hours=1):%Y-%m-%d %H:%M} decision ({n_new} orders)", {
        "one sleeve block: xsmom, weight 1, scheduled 15:00": sv["name"] == "xsmom" and sv["weight"] == 1.0
        and sv["execution"] == "scheduled" and sv["decision_hour_utc"] == 15,
        "sleeve targets == state/sleeves.json book target": sv["target"] == {p: float(w) for p, w in book.target.items()},
        f"last decision == this step ({sv['last_decision'] and sv['last_decision']['time']})":
            bool(sv["last_decision"]) and pd.Timestamp(sv["last_decision"]["time"]) == now
            and sv["slot"] == str(h + pd.Timedelta(hours=1)),
        f"next decision is tomorrow 15:00 ({sv['next_decision']})":
            pd.Timestamp(sv["next_decision"]) == h + pd.Timedelta(hours=25),
        f"table = active universe only ({len(d['pairs'])} rows, pool {len(bot.pairs)})":
            set(d["pairs"]) == set(sv["universe"]) | held and len(d["pairs"]) < len(bot.pairs),
        "universe == the bot's current R1 members": set(bot.sleeve_specs[0].universe) <= set(sv["universe"])
            and set(sv["universe"]) == set(members),
        f"actual == account after fills (max gap {gap:.2e}; heartbeat's pre-trade actual off by {hb_gap:.1%})":
            gap < 2e-3 and hb_gap > 0.05,
        "no 'strategy=s3v2' / 'Targets computed' lines in sleeve mode":
            "strategy=s3v2" not in text and "Targets computed" not in text,
        "status wrote nothing": files0 == files1,
    })
    sim.run_hour(hours[i + 1])                        # one hour later: snapshot includes the fills
    d2 = status.build(cfg, sim.base, now=sim.now["t"])
    gap2 = max_gap(d2["actual"], account_weights(sim.ex))
    ok2 = report("one hour later (no new orders)", {
        f"actual == account (max gap {gap2:.2e})": gap2 < 2e-3,
        "last decision unchanged": d2["sleeves"][0]["last_decision"]["time"] == sv["last_decision"]["time"],
    })
    return ok1 and ok2


def test_single() -> bool:
    import tests.test_sleeves as ts
    from tests.test_sleeves import Sim, all_closes
    ts.OUT = OUT
    cfg = copy.deepcopy(ts.sleeve_cfg())
    cfg.pop("sleeves", None)
    cfg["capital_cap_usd"] = None
    c = all_closes()
    hours = c.index[-24 * 3:]
    sim = Sim("single", c, hours[0], cfg)
    # the startup step traded (s3v2 from cash): status right after it
    sim.bot.heartbeat("running")
    d = status.build(cfg, sim.base, now=sim.now["t"])
    lines, _ = status.render(cfg, d)
    acct = account_weights(sim.ex)
    gap = max_gap(d["actual"], acct)
    n = len([o for o in sim.read("orders") if "response" in o])
    print("\n" + "\n".join(lines[:4]))
    return report("single-strategy config: status right after the startup trades", {
        f"startup traded ({n} orders)": n > 0,
        f"actual == account after fills (max gap {gap:.2e})": gap < 2e-3,
        "table lists the configured pairs": set(d["pairs"]) == set(sim.bot.pairs),
    })


def main() -> int:
    ok = test_competition() & test_single()
    print(f"\nstatus tests: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
