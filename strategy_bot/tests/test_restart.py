"""(d) Restart safety + late-fill logging. Offline (MockRoostoo + cached history).

    python -m tests.test_restart

1. Mid-day restart: two identical mock accounts. Bot A runs without interruption; bot B
   is stopped and re-created at 06:22 UTC on day 3. Checks: B's targets after the restart
   == before ("targets restored from 00:00"), the startup step places 0 orders, and every
   order after the restart is identical to A's (no extra trades).
2. First restart after this feature ships (no state/targets.json yet): today's 00:00
   targets are restored from logs/decisions.jsonl.
3. Strategy config changed between runs: saved targets are ignored and recomputed.
4. Resting limit orders that fill later are logged as LIMIT_LATE_FILL (during the wait,
   and when the fill races the cancel).
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import pandas as pd

from bot import StrategyBot, load_config
from infra import JsonlLogs
from market_data import BarStore
from portfolio import Portfolio
from tests.hist_data import load_closes
from tests.mock_exchange import MockRoostoo

HERE = Path(__file__).resolve().parent.parent
OUT = HERE / ".cache" / "restart"


def make_cfg(**over) -> dict:
    cfg = load_config(HERE / "config.yaml")
    cfg.pop("sleeves", None)          # single-strategy restart logic (sleeves: tests/test_sleeves.py)
    cfg.update(dry_run=False, poll_s=0, limit_wait_s=0, limit_poll_s=0, **over)
    return cfg


class Sim:
    """One bot on one mock account, driven hour by hour like test_replay."""

    def __init__(self, tag: str, c: pd.DataFrame, start: pd.Timestamp, cfg: dict) -> None:
        self.base, self.c, self.cfg = OUT / tag, c, cfg
        shutil.rmtree(self.base, ignore_errors=True)
        self.ex = MockRoostoo(cfg["universe"], usd=50_000.0)
        self.ex.set_prices(c.loc[start].to_dict())
        self.now = {"t": start - pd.Timedelta(minutes=1)}
        self.bars = BarStore(cfg["universe"], self.base / "state" / "bars.csv")
        self.bars.close = c.loc[:start - pd.Timedelta(hours=1)].iloc[-800:].copy()
        self.bot = self.new_bot(cfg)
        self.bot.step(self.ex.ticker()["Data"], "startup")

    def new_bot(self, cfg: dict) -> StrategyBot:
        bot = StrategyBot(cfg, self.ex, base_dir=self.base, clock=lambda: self.now["t"],
                          sleep=lambda s: None, bars=self.bars)
        bot.setup()
        return bot

    def run_hour(self, h: pd.Timestamp) -> None:
        self.ex.set_prices(self.c.loc[h].to_dict())
        self.now["t"] = h + pd.Timedelta(minutes=59)
        self.bot.poll()
        self.now["t"] = h + pd.Timedelta(hours=1, seconds=30)
        self.bot.poll()

    def restart(self, at: pd.Timestamp, cfg: dict | None = None) -> int:
        """Stop the bot and start a new process-equivalent: fresh StrategyBot, same disk."""
        self.now["t"] = at
        self.bot = self.new_bot(cfg or self.cfg)
        return self.bot.step(self.ex.ticker()["Data"], "startup")

    def read(self, name: str) -> list[dict]:
        p = self.base / "logs" / f"{name}.jsonl"
        return [json.loads(x) for x in p.read_text().splitlines()] if p.exists() else []

    def orders_after(self, t: pd.Timestamp) -> list[tuple]:
        return [(o["action"], json.dumps(o.get("request"), sort_keys=True)) for o in self.read("orders")
                if pd.Timestamp(o["time"]) > t and "response" in o]


def round_t(t: dict) -> dict:
    return {p: round(w, 10) for p, w in t.items()}


def test_midday_restart(c: pd.DataFrame) -> bool:
    cfg = make_cfg()
    hours = c.index[-24 * 5:]
    day0 = hours[0].floor("D") + pd.Timedelta(days=1)
    start = day0 - pd.Timedelta(hours=3)                     # starts 21:00, so day0 00:00 is a daily slot
    restart_at = day0 + pd.Timedelta(days=2, hours=6, minutes=22)
    hrs = hours[(hours >= start) & (hours < day0 + pd.Timedelta(days=4))]
    a, b = Sim("uninterrupted", c, start, cfg), Sim("restarted", c, start, cfg)
    n_start, before = None, None
    for h in hrs:
        if b.now["t"] < restart_at <= h + pd.Timedelta(minutes=59):
            before = dict(b.bot.target)
            fresh = b.bot.strategy.target_weights(b.bars.close[b.bot.pairs], cfg["strategy"])
            n_start = b.restart(restart_at)
            after = dict(b.bot.target)
        a.run_hour(h)
        b.run_hour(h)
    restored = [d for d in b.read("decisions") if d.get("event") == "targets" and d.get("reason") == "restored"]
    moved = {p: (round(before[p], 3), round(fresh.get(p, 0), 3)) for p in before
             if abs(before[p] - fresh.get(p, 0)) > 0.005}
    oa, ob = a.orders_after(restart_at), b.orders_after(restart_at)
    checks = {
        "targets after restart == before (restored from 00:00)": round_t(after) == round_t(before),
        "restore logged as 'restored' from state/targets.json": len(restored) == 1
        and restored[0]["source"] == "state/targets.json",
        "startup step after restart placed 0 orders": n_start == 0,
        f"orders after restart identical to uninterrupted bot ({len(oa)} orders)": oa == ob and len(oa) > 0,
        "end equity identical": abs(a.ex.equity() - b.ex.equity()) < 1e-6,
    }
    print(f"\n== mid-day restart at {restart_at:%Y-%m-%d %H:%M} UTC")
    print(f"   old behaviour (recompute at restart) would have moved: {moved or 'nothing'}")
    return report(checks)


def test_restore_from_log_and_config_change(c: pd.DataFrame) -> bool:
    cfg = make_cfg()
    hours = c.index[-24 * 3:]
    day0 = hours[0].floor("D") + pd.Timedelta(days=1)
    start = day0 - pd.Timedelta(hours=2)
    s = Sim("fallback", c, start, cfg)
    for h in hours[(hours >= start) & (hours < day0 + pd.Timedelta(hours=8))]:
        s.run_hour(h)
    daily = [d for d in s.read("decisions") if d.get("event") == "targets" and d.get("reason") == "daily"][-1]
    before = dict(s.bot.target)
    (s.base / "state" / "targets.json").unlink()            # as on EC2 before this fix shipped
    t1 = day0 + pd.Timedelta(hours=8, minutes=40)
    n1 = s.restart(t1)
    rec1 = [d for d in s.read("decisions") if d.get("event") == "targets"][-1]
    ok_log = (rec1["reason"] == "restored" and rec1["source"] == "logs/decisions.jsonl"
              and max(abs(s.bot.target[p] - before[p]) for p in before) < 1e-6  # log keeps 6 dp
              and n1 == 0
              and (s.base / "state" / "targets.json").exists())
    cfg2 = make_cfg()
    cfg2["strategy"] = {**cfg2["strategy"], "target_vol": 0.6}
    s.restart(t1 + pd.Timedelta(minutes=5), cfg2)
    rec2 = [d for d in s.read("decisions") if d.get("event") == "targets"][-1]
    # vol_method switch (std -> ewma, the 2026-10-05 adoption): fresh targets once, then restored
    cfg_std = make_cfg()
    cfg_std["strategy"] = {**cfg_std["strategy"], "vol_method": "std"}
    cfg_ewma = make_cfg()
    s.restart(t1 + pd.Timedelta(minutes=10), cfg_std)
    s.restart(t1 + pd.Timedelta(minutes=15), cfg_ewma)
    r_switch = [d for d in s.read("decisions") if d.get("event") == "targets"][-1]
    t_switch = dict(s.bot.target)
    s.restart(t1 + pd.Timedelta(minutes=20), cfg_ewma)
    r_again = [d for d in s.read("decisions") if d.get("event") == "targets"][-1]
    t_again = dict(s.bot.target)
    (s.base / "state" / "targets.json").unlink()            # log fallback must not restore std targets
    s.restart(t1 + pd.Timedelta(minutes=25), cfg_ewma)
    r_log = [d for d in s.read("decisions") if d.get("event") == "targets"][-1]
    print(f"\n== restore fallback (daily targets logged at {daily['time'][:16]}) and config change")
    return report({
        "no targets.json: restored from logs/decisions.jsonl, 0 orders, targets.json rewritten": ok_log,
        "strategy config changed: saved targets ignored, computed fresh ('first start')":
            rec2["reason"] == "first start",
        "vol_method std -> ewma: fresh targets once, restored on the next restart":
            r_switch["reason"] == "first start" and r_again["reason"] == "restored"
            and round_t(t_again) == round_t(t_switch),
        "log fallback restores only same-config targets (00:00 ewma daily, not the std ones)":
            r_log["reason"] == "restored" and r_log["source"] == "logs/decisions.jsonl"
            and max(abs(s.bot.target[p] - daily["target"][p]) for p in s.bot.target) < 1e-6,
    })


class LateFill(MockRoostoo):
    """Every limit order rests; it fills on the first status query (mode 'wait') or right
    before the cancel arrives (mode 'race')."""

    def __init__(self, *a, mode: str = "wait", **kw):
        super().__init__(*a, pending_every=1, **kw)
        self.mode = mode

    def query_order(self, order_id=None, **kw):
        if self.mode == "wait" and order_id is not None:
            self.fill_pending(order_id)
        return super().query_order(order_id=order_id, **kw)

    def cancel_order(self, order_id=None, pair=None):
        if self.mode == "race" and order_id is not None:
            self.fill_pending(order_id)
        return super().cancel_order(order_id=order_id, pair=pair)


def test_late_fill_logging() -> bool:
    pairs = ["BTC/USD", "ETH/USD"]
    checks = {}
    for mode, wait_s in (("wait", 30), ("race", 0)):
        out = OUT / f"latefill_{mode}"
        shutil.rmtree(out, ignore_errors=True)
        ex = LateFill(pairs, mode=mode)
        ex.set_prices({"BTC/USD": 85000.0, "ETH/USD": 2700.0})
        logs = JsonlLogs(out)
        port = Portfolio(ex, pairs, ex.exchange_info()["TradePairs"], logs, entry="limit",
                         limit_wait_s=wait_s, poll_s=0, capital_cap_usd=3000, sleep=lambda s: None)
        port.rebalance({"BTC/USD": 0.2, "ETH/USD": -0.0}, ex.ticker()["Data"], band=0.06)
        recs = [json.loads(x) for x in (out / "orders.jsonl").read_text().splitlines()]
        late = [r for r in recs if r["action"] == "LIMIT_LATE_FILL"]
        fallback = [r for r in recs if r["action"] == "MARKET_FALLBACK"]
        good = (len(late) == 1 and late[0]["status"] == "FILLED" and late[0]["avg_price"] > 0
                and late[0]["commission"] > 0 and not fallback)
        checks[f"late fill ({mode}): LIMIT_LATE_FILL logged with price + fee, no market fallback"] = good
    print("\n== late fills of resting limit orders")
    return report(checks)


def report(checks: dict) -> bool:
    for k, v in checks.items():
        print(f"   [{'PASS' if v else 'FAIL'}] {k}")
    return all(checks.values())


def main() -> int:
    c = load_closes()
    ok = test_midday_restart(c) & test_restore_from_log_and_config_change(c) & test_late_fill_logging()
    print(f"\n(d) restart + late-fill tests: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
