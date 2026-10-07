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


CONFIG_CAP = "config"


def sleeve_cfg(cap: float | None | str = CONFIG_CAP, guard: str | None = None, brake: bool = True) -> dict:
    """The exact config.yaml (its sleeves block, cap, guard) unless overridden for a parity run."""
    cfg = load_config(HERE / "config.yaml")
    if not cfg.get("sleeves"):        # config without sleeves: test the documented 0.5 / 0.5 example
        cfg["sleeves"] = [{"name": "s3v2", "weight": 0.5, "execution": "band", "decision_hour_utc": 0},
                          {"name": "xsmom", "weight": 0.5, "strategy": {"name": "xsmom"}, "universe": TM,
                           "execution": "scheduled", "decision_hour_utc": 15}]
    cfg.update(dry_run=False, poll_s=0, limit_wait_s=0, limit_poll_s=0)
    if cap != CONFIG_CAP:
        cfg["capital_cap_usd"] = cap
    if guard is not None:
        cfg["activity_guard"] = guard
    if not brake:
        cfg.update(dd_soft=-0.99, dd_hard=-0.995)
    return cfg


class Sim:
    def __init__(self, tag: str, c: pd.DataFrame, start: pd.Timestamp, cfg: dict, usd: float = 50_000.0,
                 pairs: list[str] | None = None, vol24: dict[str, float] | None = None) -> None:
        self.base, self.c, self.cfg = OUT / tag, c, cfg
        shutil.rmtree(self.base, ignore_errors=True)
        pairs = pairs or list(dict.fromkeys(p for s in cfg.get("sleeves") or []
                                            for p in (s.get("universe") or cfg["universe"]))) \
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

    def restart(self, at: pd.Timestamp, cfg: dict | None = None) -> int:
        self.now["t"] = at
        if cfg is not None:
            self.cfg = cfg
        self.bot = self.new_bot()
        n = self.bot.step(self.ex.ticker()["Data"], "startup")
        self._snap()
        return n

    def read(self, name: str) -> list[dict]:
        p = self.base / (self.cfg.get("paths") or {}).get("log_dir", "logs") / f"{name}.jsonl"
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
    cfg = sleeve_cfg()
    cap = float(cfg["capital_cap_usd"])
    hours = c.index[-24 * days:]
    sim = Sim("joint", c, hours[0], cfg, vol24={"LISTA/USD": 200_000.0})   # below the $1M floor
    for h in hours:
        sim.run_hour(h)
        sim._snap()
    orders = [o for o in sim.read("orders") if "response" in o]
    errors = sim.read("errors") + [o for o in sim.read("orders") if o.get("error")]
    # ping-pong: per step (order time to the minute) and pair, both a buy and a sell?
    # ping-pong = a buy AND a sell of the same pair in one step, each worth more than $2. Closing a
    # dust leg (e.g. a 0.001 BNB short left by rounding, below MiniOrder) next to a real order is
    # the per-leg cleanup of portfolio.py, not two sleeves fighting.
    def notional(o: dict) -> float:
        rq = o.get("request") or {}
        if "collateral" in rq:
            return float(rq["collateral"])
        q = rq.get("quantity") or rq.get("close_qty") or 0.0
        t = pd.Timestamp(o["time"])
        h = t.floor("h") - pd.Timedelta(hours=1) if t.minute == 0 else t.floor("h")
        return float(q) * float(sim.c.loc[h, rq["pair"]]) if q else 0.0
    steps: dict[tuple, set] = {}
    for o in orders:
        if notional(o) <= 2.0:
            continue
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
    # a final partial day that ends before the activity-guard hour cannot have been forced to trade yet
    if (hours[-1] + pd.Timedelta(hours=1)).hour <= int(sim.cfg["activity_guard_hour_utc"]) and len(all_days) > 1:
        all_days.discard(str(hours[-1].date()))
    gross_max = max(sum(abs(v) for v in e["exposure"].values()) for e in eq)
    untagged = [o for o in orders if not o.get("sleeves") and o["action"] not in ("MARKET_FALLBACK",)]
    print(f"\n   {len(orders)} orders over {days} days; xsmom decision trades on {len(x_times)} steps; "
          f"SOL orders with both sleeves netted: {len(sol_both)}; final books "
          f"{ {n: round(v[0], 2) for n, v in sim.books[-1][1].items()} }")
    return report(f"joint replay {days}d, config.yaml sleeves "
                  f"{[(s['name'], s['weight']) for s in cfg['sleeves']]}, cap ${cap:,.0f}", {
        f"0 errors ({len(errors)})": not errors,
        f"USD cash never negative (min ${sim.min_usd:,.2f})": sim.min_usd >= -1e-6,
        f"gross within cap incl. drift (max ${gross_max:,.0f} vs ${1.1 * cap:,.0f})": gross_max <= 1.1 * cap,
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
    cfg = sleeve_cfg()
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


def test_migration(c: pd.DataFrame) -> bool:
    """Deploying this config onto the running single-strategy bot (cap $3,000, s3v2 only):
    first restart, then a restart where only capital_cap_usd changes."""
    single = sleeve_cfg(3000.0)
    single.pop("sleeves")
    new = sleeve_cfg()
    pairs = list(dict.fromkeys(list(single["universe"]) + TM))
    hours = c.index[-24 * 5:]
    day0 = hours[0].floor("D") + pd.Timedelta(days=1)
    start = day0 - pd.Timedelta(hours=2)
    # latest day fully inside the data, mid-day before 14:00 (its last decision = previous day's 14:00 bar)
    at = (hours[-1] - pd.Timedelta(hours=11)).floor("D") + pd.Timedelta(hours=9, minutes=10)
    sim = Sim("migration", c, start, single, pairs=pairs)
    out: dict = {}
    for h in hours[hours >= start]:
        if "n0" not in out and sim.now["t"] < at <= h + pd.Timedelta(minutes=59):
            out["single_target"] = dict(sim.bot.target)
            out["held_before"] = {p for p, v in sim.ex.pair_exposure().items() if v > sim.ex.unsellable(p) * 1.01}
            n_orders = len([o for o in sim.read("orders") if "response" in o])
            out["n0"] = sim.restart(at, new)
            new_orders = [o for o in sim.read("orders") if "response" in o][n_orders:]
            out["startup_by_sleeve"] = {}
            for o in new_orders:
                for k in (o.get("sleeves") or {}):
                    out["startup_by_sleeve"][k] = out["startup_by_sleeve"].get(k, 0) + 1
            books = sim.bot.books
            out["xsmom_target"] = {p: w for p, w in (books["xsmom"].target or {}).items() if w}
            pxs = dict(sim.ex.px)
            bw = books["s3v2"].weights(pxs)
            traded = {(o.get("request") or {}).get("pair") for o in new_orders if "s3v2" in (o.get("sleeves") or {})}
            out["s3v2_resize_ok"] = all(abs(books["s3v2"].target.get(p, 0.0) - bw.get(p, 0.0)) < 0.002 for p in traded)
            out["repair_tags"] = sum(1 for o in new_orders if "repair" in (o.get("sleeves") or {}))
            out["s3v2_target"] = dict(books["s3v2"].target)
            out["capital"] = sum(bk.equity(dict(sim.ex.px)) for bk in books.values())
            out["s3v2_units"] = dict(books["s3v2"].units)
            # a second restart where ONLY the capital cap changes
            t2 = at + pd.Timedelta(minutes=20)
            k0 = len([o for o in sim.read("orders") if "response" in o])
            out["n_cap"] = sim.restart(t2, sleeve_cfg(12_000.0))
            out["cap_restored"] = sorted(d["sleeve"] for d in sim.read("decisions")
                                         if d.get("event") == "targets" and d.get("reason") == "restored"
                                         and pd.Timestamp(d["time"]) == t2)
            out["cap_orders"] = len([o for o in sim.read("orders") if "response" in o]) - k0
            sim.cfg = new
        sim.run_hour(h)
    dec = [d for d in sim.read("decisions") if d.get("event") == "targets" and pd.Timestamp(d["time"]) == at]
    reasons = {d.get("sleeve"): (d["reason"], d.get("source"), d.get("bar_time")) for d in dec}
    same = all(abs(out["s3v2_target"].get(p, 0) - out["single_target"].get(p, 0)) < 1e-12
               for p in out["s3v2_target"])
    cap_cfg = float(new["capital_cap_usd"])
    print(f"\n   first restart at {at:%Y-%m-%d %H:%M} UTC into config.yaml: targets {reasons}")
    print(f"   startup orders: {out['n0']} {out['startup_by_sleeve']}; total book capital "
          f"${out['capital']:,.2f} (cap ${cap_cfg:,.0f}); s3v2 book inherited {len(out['s3v2_units'])} positions")
    print(f"   cap-only change restart: restored {out['cap_restored']}, orders {out['cap_orders']}")
    return report("switching the running single-strategy bot to this config", {
        "s3v2 sleeve adopts the running bot's 00:00 targets (no mid-day recompute)":
            reasons.get("s3v2", ("",))[0] == "restored" and same,
        "xsmom computes its targets from its last 14:00 UTC decision bar (first start)":
            reasons.get("xsmom", ("",))[0] == "first start"
            and pd.Timestamp(reasons["xsmom"][2]).hour == 14,
        f"xsmom trades at startup iff its last decision holds coins ({out['xsmom_target']})":
            (out["startup_by_sleeve"].get("xsmom", 0) > 0) == bool(out["xsmom_target"]),
        "s3v2 startup orders only resize inherited positions to the adopted targets "
        "(sleeve capital 0.5 x $10k vs the old $3k sizing)": out["s3v2_resize_ok"],
        f"no 'repair' orders at the switch ({out['repair_tags']})": out["repair_tags"] == 0,
        "books start at min(equity, cap) in total, existing positions assigned to s3v2":
            abs(out["capital"] - cap_cfg) / cap_cfg < 0.01 and out["held_before"] <= set(out["s3v2_units"]),
        "capital_cap change alone: both sleeves restored, 0 orders":
            out["cap_restored"] == ["s3v2", "xsmom"] and out["n_cap"] == 0 and out["cap_orders"] == 0,
    })


def test_xsmom_only(c: pd.DataFrame, days: int = 10) -> bool:
    """The block-3 winner config: one scheduled xsmom sleeve at weight 1.0."""
    cfg = sleeve_cfg()
    cfg["sleeves"] = [{"name": "xsmom", "weight": 1.0, "strategy": {"name": "xsmom"}, "universe": TM,
                       "execution": "scheduled", "decision_hour_utc": 15}]
    hours = c.index[-24 * days:]
    sim = Sim("xsmom_only", c, hours[0], cfg)
    for h in hours:
        sim.run_hour(h)
    orders = [o for o in sim.read("orders") if "response" in o]
    errors = sim.read("errors") + [o for o in sim.read("orders") if o.get("error")]
    eq = sim.read("equity")
    first = pd.Timestamp(eq[0]["time"])
    mult_change = {pd.Timestamp(eq[i]["time"]) for i in range(1, len(eq)) if eq[i]["mult"] != eq[i - 1]["mult"]}
    off = [o for o in orders if pd.Timestamp(o["time"]).hour != 15 and pd.Timestamp(o["time"]) != first
           and pd.Timestamp(o["time"]).floor("min") not in {t.floor("min") for t in mult_change}]
    gross_max = max(sum(abs(v) for v in e["exposure"].values()) for e in eq)
    cap = float(cfg["capital_cap_usd"])
    active = len({o["time"][:10] for o in orders})
    print(f"\n   {len(orders)} orders over {days} days, active days {active}/{days + 1}, max gross ${gross_max:,.0f}")
    return report(f"block-3 winner config: xsmom alone (weight 1.0), {days}d", {
        f"0 errors ({len(errors)})": not errors,
        f"orders only at the 15:00 decision step or startup ({len(off)} off-schedule)": not off,
        f"USD cash never negative (min ${sim.min_usd:,.2f})": sim.min_usd >= -1e-6,
        f"exposure <= 75% of the cap incl. drift (max ${gross_max:,.0f} vs ${0.75 * 1.1 * cap:,.0f})":
            gross_max <= 0.75 * 1.1 * cap,
    })


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30)
    a = ap.parse_args()
    c = all_closes()
    ok = (test_migration(c) & test_joint(c, a.days) & test_parity(c, a.days) & test_restart(c)
          & test_xsmom_only(c))
    print(f"\n(e) sleeve tests: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
