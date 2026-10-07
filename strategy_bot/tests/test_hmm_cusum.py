"""(h) Forward-test candidate HMM2 + CUSUM cut (config_testing_hmm_cusum.yaml; strategy_lab b7_hmm2_cusum). Offline.

    python -m tests.test_hmm_cusum

1. Config: testing key only, cap $10,000, own paths, flags on, no path shared with any other config.
2. HMM parity: the bot's RegimeHMM (monthly walk-forward fit, filtered p_crisis) == strategy_lab data/regime/hmm2.csv on
   every 5th day of the last 24 months (same Binance BTC history, from the lab cache).
3. CUSUM parity: the bot's cusum_scores on its 2000-bar window == lab/changepoint.cusum (full history, reset at the
   decision bar) at 300 random hours within 0.05 (EWMA start-up of the 2000-bar window; the threshold is 4).
4. Target parity: every daily target of a 30-day replay == strategy_lab's s3v2x_regime (regime_hmm 2) on the same bars
   (identical at the decision log's 6 decimals).
5. 30-day replay with the exact config on the mock exchange: 0 errors, cash >= 0, every full day active, cuts traded at once,
   no cut on a daily-target bar, cut events vs the lab backtest of b7_hmm2_cusum on the same window (agreement >= 80%).
6. Restart right after a cut: targets and cuts restored (no recompute), 0 orders at the restart, later orders identical.
7. Shared-account guard: a fresh live heartbeat with the same key label in another state dir is detected.
8. Flags off (live competition config): fingerprint has no regime / changepoint keys.
"""

from __future__ import annotations

import json
import shutil
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

from bot import StrategyBot, load_config, shared_account_conflicts
from regime_live import RegimeHMM, cusum_scores
from tests.hist_data import load_closes

HERE = Path(__file__).resolve().parent.parent
LAB = HERE.parent / "strategy_lab"
OUT = HERE / ".cache" / "hmm_cusum"
CFG = "config_testing_hmm_cusum.yaml"
sys.path.insert(0, str(LAB))
from lab.data import load_close  # noqa: E402

BTC = load_close(["BTCUSDT"])["BTCUSDT"]
BTC = BTC[BTC.index >= pd.Timestamp("2020-01-01", tz="UTC")]


def lab_fetch(now: pd.Timestamp) -> pd.Series:
    return BTC[BTC.index < now.floor("h")]


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
    mine = {cfg["paths"][k] for k in ("log_dir", "state_dir", "kill_file")}
    others = set()
    for f in HERE.glob("config*.yaml"):
        if f.name == CFG:
            continue
        p = (load_config(f).get("paths") or {})
        others |= {p.get("log_dir", "logs"), p.get("state_dir", "state"), p.get("kill_file", "KILL")}
    return report(f"{CFG}: settings", {
        "testing key (.env), competition refused": cfg["env_file"] == ".env" and cfg["allow_competition"] is False,
        "capital_cap_usd 10000": cfg["capital_cap_usd"] == 10000,
        "flags on: regime_hmm 2 states, cut 0.5 x p; CUSUM threshold 4, cut 0.5":
            cfg["regime_hmm"]["enabled"] and cfg["regime_hmm"]["states"] == 2 and cfg["regime_hmm"]["crisis_cut"] == 0.5
            and cfg["changepoint_cut"]["enabled"] and cfg["changepoint_cut"]["threshold"] == 4
            and cfg["changepoint_cut"]["cut"] == 0.5,
        "s3v2e core10 strategy, targets on the 00:00 bar (rebalance_hour_utc 1)": cfg["strategy"]["vol_method"] == "ewma"
            and cfg["rebalance_hour_utc"] == 1 and len(cfg["universe"]) == 10,
        "own log / state / KILL paths, shared with no other config": not mine & others,
        "no sleeves, no stats_card needed (not competition)": not cfg.get("sleeves"),
    })


def test_hmm_parity() -> bool:
    lab = pd.read_csv(LAB / "data" / "regime" / "hmm2.csv", index_col=0)
    lab.index = pd.to_datetime(lab.index, utc=True)
    d = OUT / "hmm"
    shutil.rmtree(d, ignore_errors=True)
    rh = RegimeHMM(d, lab_fetch, 2)
    days = lab.index[(lab.index >= lab.index[-1] - pd.Timedelta(days=730))][::5]
    worst, n = 0.0, 0
    t0 = time.time()
    for day in days:
        p, _ = rh.p_crisis(day, day + pd.Timedelta(days=1, hours=1))
        worst = max(worst, abs(p - float(lab.at[day, "p_crisis"])))
        n += 1
    print(f"   {n} days, {len(set(d.strftime('%Y-%m') for d in days))} monthly fits, max |p_bot - p_lab| {worst:.1e} "
          f"[{time.time() - t0:.0f}s]")
    return report("HMM2: bot == strategy_lab walk-forward probabilities", {f"identical on {n} days": worst < 1e-6})


def test_cusum_parity(c: pd.DataFrame) -> bool:
    from lab.changepoint import cusum, standardized
    reset = np.array([t.hour == 0 for t in c.index])
    dn, up = cusum(standardized(c), reset)
    rng = np.random.default_rng(0)
    idx = rng.choice(np.arange(3000, len(c)), 300, replace=False)
    worst = 0.0
    for i in idx:
        t = c.index[i]
        rb = t.floor("D")                              # the last reset bar (hour 0) at or before t
        win = c.iloc[i - 1999:i + 1]
        d, u = cusum_scores(win, rb)
        worst = max(worst, float(np.max(np.abs(d.values - dn[i]))), float(np.max(np.abs(u.values - up[i]))))
    return report("CUSUM: bot (2000-bar window) == lab (full history)", {
        f"300 random hours, max |diff| {worst:.1e} <= 0.05 (about 1% of the threshold 4; the bot's EWMA vol starts "
        f"2000 bars back, the lab's in 2020; cut decisions are compared in the replay)": worst <= 0.05})


class HSim:
    """test_sleeves.Sim with the bot's HMM fed from the lab cache."""

    def __new__(cls, tag, c, start, cfg):
        import tests.test_sleeves as ts
        from tests.test_sleeves import Sim
        ts.OUT = OUT

        class _S(Sim):
            def new_bot(self):
                bot = StrategyBot(self.cfg, self.ex, base_dir=self.base, clock=lambda: self.now["t"],
                                  sleep=lambda s: None, bars=self.bars)
                bot.hmm = RegimeHMM(bot.state_dir, lab_fetch, 2)
                bot.setup()
                return bot
        return _S(tag, c, start, cfg)


def test_replay(c: pd.DataFrame) -> bool:
    from lab.backtest import Backtest, RunConfig
    from lab.runner import resolve_base
    from lab.strategies import get_strategy as lab_get
    cfg = sim_cfg()
    hours = c.index[-24 * 30:]
    a = HSim("replay", c, hours[0], cfg)
    b = HSim("restart", c, hours[0], cfg)
    out: dict = {}
    for h in hours:
        a.run_hour(h)
        if "n0" not in out:
            cuts_b = len(b.read("decisions"))
        b.run_hour(h)
        if "n0" not in out and any(d.get("event") == "changepoint_cut" for d in b.read("decisions")[cuts_b:]) \
                and h.hour not in (0, 23):
            at = h + pd.Timedelta(hours=1, minutes=10)
            before = (dict(b.bot.target), dict(b.bot.cuts))
            n_ord = len([o for o in b.read("orders") if "response" in o])
            out["n0"] = b.restart(at)
            out["same"] = (dict(b.bot.target), dict(b.bot.cuts)) == before
            out["at"] = at
            out["orders_at_restart"] = len([o for o in b.read("orders") if "response" in o]) - n_ord
    dec = a.read("decisions")
    tg = [d for d in dec if d.get("event") == "targets" and d.get("reason") in ("daily", "first start")]
    cuts = [d for d in dec if d.get("event") == "changepoint_cut"]
    orders = [o for o in a.read("orders") if "response" in o]
    errors = a.read("errors") + [o for o in a.read("orders") if o.get("error")]
    # target parity vs the lab strategy on the same bars
    lp = {**resolve_base("b7_hmm2_cusum")["params"], "btc_pair": "BTC/USD"}
    lab_s = lab_get("s3v2x_regime")
    worst = 0.0
    for d in tg:
        bar = pd.Timestamp(d["bar_time"])
        win = c.loc[:bar].iloc[-800:]
        wl = lab_s.target_weights(win, lp)
        # the decision log keeps 6 decimals: compare at that precision (identical, not approximately)
        worst = max(worst, max(abs(round(float(wl.get(p, 0.0)), 6) - float(d["target"][p])) for p in d["target"]))
    # cuts: traded at once, never on a daily-target bar
    cut_bars = {(pd.Timestamp(d["time"]).floor("h") - pd.Timedelta(hours=1), p) for d in cuts for p in d["pairs"]}
    traded = all(any(o.get("request", {}).get("pair") == p and pd.Timestamp(o["time"]) == pd.Timestamp(d["time"])
                     for o in orders) for d in cuts for p in d["pairs"])
    on_daily = [x for x in cut_bars if x[0].hour == 0]
    # vs the lab backtest on the same window (fresh start)
    spec = {**resolve_base("b7_hmm2_cusum"), "name": "chk", "start": str(hours[0]), "end": str(hours[-1])}
    lab_ev = set()
    r = Backtest(RunConfig.from_dict(spec)).run()
    for t, asset in (r["extra"] or {}).get("changepoint", {}).get("events", []):
        lab_ev.add((pd.Timestamp(t), asset.replace("USDT", "/USD")))
    agree = len(cut_bars & lab_ev) / max(len(cut_bars | lab_ev), 1)
    eq = a.read("equity")
    days = {o["time"][:10] for o in orders}
    all_days = {str(x.date()) for x in hours}
    if (hours[-1] + pd.Timedelta(hours=1)).hour <= int(cfg["activity_guard_hour_utc"]):
        all_days.discard(str(hours[-1].date()))
    regimes = [d["regime"]["p_crisis"] for d in tg if d.get("regime")]
    print(f"\n   {len(orders)} orders, {len(cut_bars)} cuts (lab {len(lab_ev)}, agreement {agree:.0%}), "
          f"{len(tg)} daily targets, p_crisis range {min(regimes):.2f}-{max(regimes):.2f}")
    key = lambda o: (o["action"], json.dumps(o.get("request"), sort_keys=True))
    at = out.get("at")
    oa = [key(o) for o in a.read("orders") if "response" in o and at is not None and pd.Timestamp(o["time"]) > at]
    ob = [key(o) for o in b.read("orders") if "response" in o and at is not None and pd.Timestamp(o["time"]) > at]
    ok1 = report(f"30-day replay with {CFG}", {
        f"daily targets == lab s3v2x_regime at the log's 6 decimals (max diff {worst:.1e})": worst < 1e-12 and len(tg) >= 29,
        f"0 errors ({len(errors)})": not errors,
        f"USD cash never negative (min ${a.min_usd:,.2f})": a.min_usd >= -1e-6,
        f"every full day active ({len(days & all_days)}/{len(all_days)})": all_days <= days,
        f"cuts fired ({len(cut_bars)}) and each traded in the same step": len(cut_bars) > 0 and traded,
        f"no cut on a daily-target bar ({len(on_daily)})": not on_daily,
        f"cut events agree with the lab backtest ({agree:.0%} >= 80%)": agree >= 0.8,
        "HMM probability logged with every daily target": len(regimes) == len(tg),
    })
    ok2 = report(f"restart right after a cut ({out.get('at')})", {
        "targets and cuts restored": out.get("same", False),
        f"0 orders at the restart ({out.get('orders_at_restart')})": out.get("n0") == 0,
        f"orders after the restart identical ({len(oa)})": oa == ob and len(oa) > 0,
        "end equity identical": abs(a.ex.equity() - b.ex.equity()) < 1e-6,
    })
    return ok1 and ok2


def test_guards() -> bool:
    d = HERE / "state_zz_guardtest"
    d.mkdir(exist_ok=True)
    try:
        (d / "heartbeat.json").write_text(json.dumps({"ts": int(time.time() * 1000), "time": "now", "status": "running",
                                                      "dry_run": False, "key_label": "testing"}))
        cfg = load_config(HERE / CFG)
        hit = shared_account_conflicts(cfg, "testing")
        miss = shared_account_conflicts(cfg, "competition")
    finally:
        shutil.rmtree(d, ignore_errors=True)
    from tests.mock_exchange import MockRoostoo
    live = StrategyBot(load_config(HERE / "config_competition_s3v2e.yaml"), MockRoostoo(["BTC/USD"]), base_dir=OUT / "fp")
    live.pairs = ["BTC/USD"]
    fp = live._fingerprint()
    return report("guards", {
        "another live bot on the same key label is detected": any("state_zz_guardtest" in x for x in hit),
        "a bot on a different key label is not": not any("state_zz_guardtest" in x for x in miss),
        "live competition config: flags off, fingerprint unchanged": "regime_hmm" not in fp and "changepoint_cut" not in fp
            and live.hmm_cfg is None and live.cp_cfg is None,
    })


def main() -> int:
    shutil.rmtree(OUT, ignore_errors=True)
    c = load_closes()
    ok = test_config() & test_guards() & test_hmm_parity() & test_cusum_parity(c) & test_replay(c)
    print(f"\n(h) HMM2 + CUSUM forward-test tests: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
