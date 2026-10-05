"""(e) Sleeve allocator: s3v2 (band, 00:00) + xsmom (scheduled, 14:00 UTC bar) at 0.5 / 0.5.

    python -m tests.test_sleeves [--days 30]

1. 30-day replay, capital cap $3,000, minimal guard, LISTA forced illiquid on Roostoo:
   0 errors, USD cash never negative, gross within the cap, every day active, no ping-pong
   (never a buy and a sell of the same pair in one step; SOL, held by both sleeves, gets one
   net order per step), xsmom book changes only at its 15:00 UTC decision step (the 14:00
   bar), liquidity guard skips LISTA and logs it, every order is tagged with its sleeve(s).
2. Parity (brake off, guard off, no cap), each sleeve vs its own backtest:
   * xsmom sleeve book == the teammate's own ledger (final_momentum_strategy.execute_target
     with target_at_signal_time) executed at the same prices (max relative equity diff)
   * s3v2 sleeve book weights ~= a standalone single-strategy bot on its own account with
     the same capital (real fills, MiniOrder, maker/taker), tolerance in pp of weight
3. Mid-day restart in sleeve mode: books and both sleeves' targets restored, 0 orders at the
   restart, every later order identical to an uninterrupted run.
Output in .cache/sleeves/ (git-ignored).
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from bot import StrategyBot, load_config
from market_data import BarStore
from tests.hist_data import load_closes, load_symbol
from tests.mock_exchange import MockRoostoo

HERE = Path(__file__).resolve().parent.parent
OUT = HERE / ".cache" / "sleeves"
TM = ["ZEC/USD", "PAXG/USD", "POL/USD", "ICP/USD", "TRX/USD", "LISTA/USD", "STO/USD", "CAKE/USD",
      "TUT/USD", "SOL/USD"]


def all_closes() -> pd.DataFrame:
    core = load_closes()
    extra = {p: load_symbol(p.split("/")[0] + "USDT") for p in TM if p not in core.columns}
    df = core.join(pd.DataFrame(extra), how="outer").sort_index()
    df.index = pd.DatetimeIndex(df.index).tz_convert("UTC")
    return df.reindex(pd.date_range(df.index[0], df.index[-1], freq="1h")).ffill()


def sleeve_cfg(cap: float | None, guard: str, brake: bool = True) -> dict:
    cfg = load_config(HERE / "config.yaml")
    core = list(cfg["universe"])
    cfg.update(dry_run=False, poll_s=0, limit_wait_s=0, limit_poll_s=0, capital_cap_usd=cap,
               activity_guard=guard,
               sleeves=[{"name": "s3v2", "weight": 0.5, "execution": "band", "universe": core,
                         "decision_hour_utc": 0},
                        {"name": "xsmom", "weight": 0.5, "strategy": {"name": "xsmom"}, "universe": TM,
                         "execution": "scheduled", "decision_hour_utc": 15}])
    if not brake:
        cfg.update(dd_soft=-0.99, dd_hard=-0.995)
    return cfg


class Sim:
    def __init__(self, tag: str, c: pd.DataFrame, start: pd.Timestamp, cfg: dict, usd: float = 50_000.0,
                 pairs: list[str] | None = None, vol24: dict[str, float] | None = None) -> None:
        self.base, self.c, self.cfg = OUT / tag, c, cfg
        shutil.rmtree(self.base, ignore_errors=True)
        pairs = pairs or list(dict.fromkeys(p for s in cfg.get("sleeves") or [] for p in s["universe"])) \
            or list(cfg["universe"])
        self.ex = MockRoostoo(pairs, usd=usd)
        self.ex.vol24.update(vol24 or {})
        self.ex.set_prices(c.loc[start, pairs].to_dict())
        self.now = {"t": start - pd.Timedelta(minutes=1)}
        self.bars = BarStore(pairs, self.base / "state" / "bars.csv")
        self.bars.close = c.loc[:start - pd.Timedelta(hours=1), pairs].iloc[-2000:].copy()
        self.pairs = pairs
        self.min_usd = float("inf")
        self.books: list[tuple] = []
        self.bot = self.new_bot()
        self.bot.step(self.ex.ticker()["Data"], "startup")
        self._snap()

    def new_bot(self) -> StrategyBot:
        bot = StrategyBot(self.cfg, self.ex, base_dir=self.base, clock=lambda: self.now["t"],
                          sleep=lambda s: None, bars=self.bars)
        bot.setup()
        return bot

    def _snap(self) -> None:
        self.min_usd = min(self.min_usd, self.ex.usd)
        px = dict(self.ex.px)
        if self.bot.books:
            self.books.append((self.now["t"], {n: (b.equity(px), b.weights(px)) for n, b in self.bot.books.items()}))

    def run_hour(self, h: pd.Timestamp) -> None:
        self.ex.set_prices(self.c.loc[h, self.pairs].to_dict())
        self.now["t"] = h + pd.Timedelta(minutes=59)
        self.bot.poll()
        self._snap()
        self.now["t"] = h + pd.Timedelta(hours=1, seconds=30)
        self.bot.poll()
        self._snap()

    def restart(self, at: pd.Timestamp) -> int:
        self.now["t"] = at
        self.bot = self.new_bot()
        n = self.bot.step(self.ex.ticker()["Data"], "startup")
        self._snap()
        return n

    def read(self, name: str) -> list[dict]:
        p = self.base / "logs" / f"{name}.jsonl"
        return [json.loads(x) for x in p.read_text().splitlines()] if p.exists() else []


def report(title: str, checks: dict) -> bool:
    print(f"\n== {title}")
    for k, v in checks.items():
        print(f"   [{'PASS' if v else 'FAIL'}] {k}")
    return all(checks.values())


SIDE = {"BUY_LIMIT": "buy", "BUY_MARKET": "buy", "MARKET_FALLBACK": None, "SELL_LIMIT": "sell",
        "SELL_MARKET": "sell", "OPEN_SHORT": "sell", "CLOSE_SHORT": "buy"}


def side_of(o: dict) -> str | None:
    s = SIDE.get(o["action"])
    if s is None and o["action"] == "MARKET_FALLBACK":
        s = "buy" if (o.get("request") or {}).get("side") == "BUY" else "sell"
    return s


def test_joint(c: pd.DataFrame, days: int) -> bool:
    cfg = sleeve_cfg(3000.0, "minimal")
    hours = c.index[-24 * days:]
    sim = Sim("joint", c, hours[0], cfg, vol24={"LISTA/USD": 200_000.0})   # below the $1M floor
    for h in hours:
        sim.run_hour(h)
        sim._snap()
    orders = [o for o in sim.read("orders") if "response" in o]
    errors = sim.read("errors") + [o for o in sim.read("orders") if o.get("error")]
    # ping-pong: per step (order time to the minute) and pair, both a buy and a sell?
    steps: dict[tuple, set] = {}
    for o in orders:
        key = (o["time"][:16], (o.get("request") or {}).get("pair"))
        steps.setdefault(key, set()).add(side_of(o))
    pingpong = [k for k, v in steps.items() if {"buy", "sell"} <= v]
    sol_steps = {k for k in steps if k[1] == "SOL/USD"}
    sol_both = [o for o in orders if (o.get("request") or {}).get("pair") == "SOL/USD"
                and len(o.get("sleeves") or {}) >= 2]
    so = [d for d in sim.read("decisions") if d.get("event") == "sleeve_orders"]
    x_times = sorted({pd.Timestamp(d["time"]) for d in so
                      if any("xsmom" in (v or {}) for v in d["by_sleeve_usd"].values())})
    eq = sim.read("equity")
    mult_change = {pd.Timestamp(eq[i]["time"]) for i in range(1, len(eq)) if eq[i]["mult"] != eq[i - 1]["mult"]}
    off_sched = [t for t in x_times if t.hour != 15 and t != pd.Timestamp(eq[0]["time"]) and t not in mult_change]
    tgt = [d for d in sim.read("decisions") if d.get("event") == "targets" and d.get("sleeve") == "xsmom"
           and d.get("reason") != "restored"]
    skipped_ok = bool(tgt) and all("LISTA/USD" in d["liquidity_skipped"] and d["target"]["LISTA/USD"] == 0
                                   for d in tgt)
    days_with = {o["time"][:10] for o in orders}
    all_days = {str(d.date()) for d in hours}
    gross_max = max(sum(abs(v) for v in e["exposure"].values()) for e in eq)
    untagged = [o for o in orders if not o.get("sleeves") and o["action"] not in ("MARKET_FALLBACK",)]
    print(f"\n   {len(orders)} orders over {days} days; xsmom decision trades on {len(x_times)} steps; "
          f"SOL orders with both sleeves netted: {len(sol_both)}; final books "
          f"{ {n: round(v[0], 2) for n, v in sim.books[-1][1].items()} }")
    return report(f"joint replay {days}d, sleeves s3v2 0.5 + xsmom 0.5, cap $3,000", {
        f"0 errors ({len(errors)})": not errors,
        f"USD cash never negative (min ${sim.min_usd:,.2f})": sim.min_usd >= -1e-6,
        f"gross within cap incl. drift (max ${gross_max:,.0f} vs $3,300)": gross_max <= 3300,
        f"every day active ({len(days_with & all_days)}/{len(all_days)})": all_days <= days_with,
        f"no ping-pong: no step buys and sells the same pair ({len(pingpong)} found)": not pingpong,
        f"SOL (both sleeves): at most one direction per step ({len(sol_steps)} SOL steps)": not
        [k for k in pingpong if k[1] == "SOL/USD"],
        f"xsmom book trades only at its 15:00 decision step ({len(off_sched)} off-schedule)": not off_sched,
        "liquidity guard: LISTA skipped at every xsmom decision and logged": skipped_ok,
        f"every order tagged with its sleeve(s) ({len(untagged)} untagged)": not untagged,
    })


def test_parity(c: pd.DataFrame, days: int) -> bool:
    sys.path.insert(0, str(HERE.parent / "teammate_xsmom"))
    import final_momentum_strategy as tm  # noqa: E402

    hours = c.index[-24 * days:]
    cfg = sleeve_cfg(None, "off", brake=False)
    sim = Sim("parity_sleeves", c, hours[0], cfg)
    for h in hours:
        sim.run_hour(h)
    # (a) xsmom book vs the teammate's ledger at the same execution prices
    coins = [p.split("/")[0] for p in TM]
    prices = c[TM].copy()
    prices.columns = coins
    cash, qty = None, np.zeros(len(TM))
    worst, last_slot = 0.0, None
    for t, books in sim.books:
        # prices the bot saw at this snapshot: the hour whose prices were set
        hset = t.floor("h") if t.minute == 59 else t.floor("h") - pd.Timedelta(hours=1)
        if t == sim.books[0][0]:
            hset = hours[0]
        px = sim.c.loc[hset, TM].to_numpy(dtype=float)
        slot = (t.floor("D") + pd.Timedelta(hours=15))
        slot = slot if slot <= t else slot - pd.Timedelta(days=1)
        if cash is None:
            cash = 0.5 * 50_000.0          # sleeve capital (weight x account, no cap) before any fee
        if slot != last_slot and (t.hour == 15 or last_slot is None):
            target = tm.target_at_signal_time(prices, slot - pd.Timedelta(hours=1)).to_numpy(dtype=float)
            cash, qty, *_ = tm.execute_target(cash, qty, px, target, 0.001)
            last_slot = slot
        ref = float(cash + (qty * px).sum())
        worst = max(worst, abs(books["xsmom"][0] / ref - 1))
    # (b) s3v2 sleeve vs a standalone single-strategy bot with the same capital
    cfg1 = sleeve_cfg(None, "off", brake=False)
    cfg1.pop("sleeves")
    solo = Sim("parity_solo", c, hours[0], cfg1, usd=sim.books[0][1]["s3v2"][0], pairs=list(cfg1["universe"]))
    for h in hours:
        solo.run_hour(h)
    diffs = []
    eq_solo = solo.read("equity")
    # compare at each completed-hour step: solo exposure / equity vs sleeve book weights
    se = {pd.Timestamp(e["time"]): e for e in eq_solo}
    sl = {t: b for t, b in sim.books}
    for t, e in se.items():
        if t not in sl:
            continue
        wb = sl[t]["s3v2"][1]
        ws = {p: v / e["equity"] for p, v in e["exposure"].items()}
        diffs.append(max(abs(wb.get(p, 0.0) - ws.get(p, 0.0)) for p in set(wb) | set(ws) | {"BTC/USD"}))
    d = np.array(diffs)
    eq_gap = sim.books[-1][1]["s3v2"][0] / eq_solo[-1]["equity"] - 1
    print(f"\n   xsmom: {len(sim.books)} snapshots, max |book / teammate ledger - 1| = {worst:.2e}")
    print(f"   s3v2: {len(d)} hourly steps, weight diff vs standalone bot: median {np.median(d):.4f}, "
          f"95th pct {np.percentile(d, 95):.4f}, max {d.max():.4f}; final equity gap {eq_gap:+.3%} "
          f"(book charges 0.10% on every trade, real fills are partly maker 0.05%)")
    return report(f"parity {days}d (no cap, brake off, guard off)", {
        "xsmom sleeve == teammate ledger (execute_target), max rel. diff < 1e-9": worst < 1e-9,
        "s3v2 sleeve ~= standalone s3v2 bot: median weight diff < 0.5pp, 95th pct < 2pp":
            np.median(d) < 0.005 and np.percentile(d, 95) < 0.02,
        "s3v2 sleeve final equity within 0.5% of the standalone bot": abs(eq_gap) < 0.005,
    })


def test_restart(c: pd.DataFrame) -> bool:
    cfg = sleeve_cfg(3000.0, "minimal")
    hours = c.index[-24 * 6:]
    day0 = hours[0].floor("D") + pd.Timedelta(days=1)
    start = day0 - pd.Timedelta(hours=2)
    at = day0 + pd.Timedelta(days=2, hours=10, minutes=22)
    hrs = hours[hours >= start]
    a, b = Sim("restart_a", c, start, cfg), Sim("restart_b", c, start, cfg)
    n0 = None
    for h in hrs:
        if b.now["t"] < at <= h + pd.Timedelta(minutes=59):
            before = {n: dict(bk.target) for n, bk in b.bot.books.items()}
            units_before = {n: dict(bk.units) for n, bk in b.bot.books.items()}
            n0 = b.restart(at)
            after = {n: dict(bk.target) for n, bk in b.bot.books.items()}
            units_after = {n: dict(bk.units) for n, bk in b.bot.books.items()}
        a.run_hour(h)
        b.run_hour(h)
    restored = [d for d in b.read("decisions") if d.get("event") == "targets" and d.get("reason") == "restored"]
    key = lambda o: (o["action"], json.dumps(o.get("request"), sort_keys=True))
    oa = [key(o) for o in a.read("orders") if "response" in o and pd.Timestamp(o["time"]) > at]
    ob = [key(o) for o in b.read("orders") if "response" in o and pd.Timestamp(o["time"]) > at]
    return report(f"mid-day restart in sleeve mode at {at:%Y-%m-%d %H:%M} UTC", {
        "both sleeves' targets restored (logged 'restored')": {d["sleeve"] for d in restored} == {"s3v2", "xsmom"}
        and before == after,
        "sleeve books restored from state/sleeves.json": units_before == units_after,
        "restart step placed 0 orders": n0 == 0,
        f"orders after the restart identical to the uninterrupted run ({len(oa)})": oa == ob and len(oa) > 0,
        "end equity identical": abs(a.ex.equity() - b.ex.equity()) < 1e-6,
    })


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30)
    a = ap.parse_args()
    c = all_closes()
    ok = test_joint(c, a.days) & test_parity(c, a.days) & test_restart(c)
    print(f"\n(e) sleeve tests: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
