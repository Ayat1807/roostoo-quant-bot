"""(f) Competition config (config_competition.yaml: one xsmom sleeve on the R1 universe).

    python -m tests.test_competition [--days 30]

1. Universe parity: the bot's R1 selection (universe_r1.py, REAL Binance 1d klines fetched over
   the network, 120-day window as in production) == strategy_lab's Universe(rule R1) for b3_xsmom_r1
   on several past month-starts (spread check off: no Roostoo spread history exists).
2. Target parity: on 20+ decision dates (the 14:00 UTC bar) the bot path (its R1 selection + the
   xsmom plug-in on the last 2000 hourly bars) == the lab path of b3_xsmom_r1 (lab universe +
   lab windowing). Plus: the bot's Binance hourly fetch == the lab's cached closes (sample).
3. 30-day replay with the exact config_competition.yaml on a mock exchange holding the Roostoo
   pool: 0 errors, cash never negative, orders only at the 15:00 decision (or startup), the R1
   list re-selected at the month start (logged, saved with its dates) and equal to the lab's.
4. Mid-day restart: R1 list, books and targets restored (no re-selection, 0 orders), later
   orders identical to an uninterrupted run.
Uses strategy_lab's local caches for prices (same Binance data) and output in .cache/competition/.
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
from market_data import BarStore, fetch_binance_hourly
from tests.mock_exchange import MockRoostoo
from universe_r1 import DEFAULTS, fetch_binance_daily, select_r1

HERE = Path(__file__).resolve().parent.parent
LAB = HERE.parent / "strategy_lab"
OUT = HERE / ".cache" / "competition"
sys.path.insert(0, str(LAB))
from lab.data import load_close, load_daily  # noqa: E402
from lab.strategies import get_strategy as lab_strategy  # noqa: E402
from lab.universe import Universe  # noqa: E402

LAB_R1 = {"type": "satellite", "rule": "R1", "n_liquid": 15, "k": 5, "min_history_days": 90,
          "min_quote_volume_usd": 1.0e7, "crash_guard": False, "exclude_core": False}
ROOSTOO = json.loads((LAB / "data" / "roostoo_pairs.json").read_text())["pairs"]


def comp_cfg() -> dict:
    cfg = load_config(HERE / "config_competition.yaml")
    cfg.update(dry_run=False, poll_s=0, limit_wait_s=0, limit_poll_s=0)
    return cfg


def to_pair(sym: str) -> str:
    return sym[:-4] + "/USD"


def report(title: str, checks: dict) -> bool:
    print(f"\n== {title}")
    for k, v in checks.items():
        print(f"   [{'PASS' if v else 'FAIL'}] {k}")
    return all(checks.values())


def lab_table(start: str, end: str) -> pd.Series:
    u = Universe(LAB_R1)
    return u._sat_table(pd.Timestamp(start, tz="UTC"), pd.Timestamp(end, tz="UTC"))


def test_universe_parity(params: dict) -> tuple[bool, dict]:
    pool = sorted(to_pair(v["binance"]) for v in ROOSTOO.values())
    end = pd.Timestamp("2026-10-01", tz="UTC")
    daily = {p: fetch_binance_daily(p, end, 1000) for p in pool}
    months = pd.date_range(pd.Timestamp("2025-03-01", tz="UTC"), end, freq="MS")
    tab = lab_table("2025-02-27", "2026-10-02")
    rows, ok = [], True
    for ms in months:
        as_of = ms - pd.Timedelta(days=1)
        win = {p: (None if d is None else d.loc[as_of - pd.Timedelta(days=119):as_of]) for p, d in daily.items()}
        bot, _ = select_r1(win, as_of, {**params, "max_spread_bps": None})
        lab = [to_pair(a) for a in tab.get(ms, [])]
        same = bot == lab
        ok &= same
        rows.append((ms, same, bot, lab))
    for ms, same, bot, lab in rows:
        print(f"   {ms:%Y-%m}: {'same' if same else 'DIFF'} ({len(bot)}) {'' if same else f'bot-lab {sorted(set(bot) - set(lab))} lab-bot {sorted(set(lab) - set(bot))}'}")
    return report(f"R1 universe: bot (live Binance 1d klines) == lab on {len(rows)} month-starts",
                  {"identical selection and order on every month-start": ok}), daily


def test_target_parity(params: dict, daily: dict) -> bool:
    tab = lab_table("2025-02-27", "2026-10-02")
    syms = sorted({a for m in tab for a in m})
    close = load_close(syms)
    close.columns = [to_pair(a) for a in close.columns]
    xs = lab_strategy("xsmom")
    dates = [d for d in pd.date_range(pd.Timestamp("2025-03-03 14:00", tz="UTC"),
                                      pd.Timestamp("2026-09-28 14:00", tz="UTC"), freq="17D")]
    worst, n, same = 0.0, 0, True
    for ts in dates:
        ms = ts.floor("D").replace(day=1)
        as_of = ms - pd.Timedelta(days=1)
        win = {p: (None if d is None else d.loc[as_of - pd.Timedelta(days=119):as_of]) for p, d in daily.items()}
        bot_mem, _ = select_r1(win, as_of, {**params, "max_spread_bps": None})
        lab_mem = [to_pair(a) for a in tab.get(ts.floor("D"), [])]
        i = close.index.get_loc(ts)
        lab_alive = [p for p in lab_mem if p in close.columns and pd.notna(close[p].iloc[i])]
        bot_alive = [p for p in bot_mem if p in close.columns and pd.notna(close[p].iloc[i])]
        wl = pd.Series(xs.target_weights(close.iloc[i - 1999:i + 1][lab_alive], {}))
        wb = pd.Series(xs.target_weights(close.iloc[:i + 1].iloc[-2000:][bot_alive], {}))
        idx = wl.index.union(wb.index)
        worst = max(worst, float((wl.reindex(idx).fillna(0) - wb.reindex(idx).fillna(0)).abs().max()))
        same &= set(wl[wl > 0].index) == set(wb[wb > 0].index)
        n += 1
    # the bot's live Binance hourly fetch equals the lab cache (sample coin and window)
    s_bot = fetch_binance_hourly("ZEC/USD", 300, now=pd.Timestamp("2026-09-30 12:00", tz="UTC"))
    s_lab = load_close(["ZECUSDT"])["ZECUSDT"].reindex(s_bot.index)
    data_same = float((s_bot - s_lab).abs().max()) < 1e-9
    print(f"\n   {n} decision dates, max |w_bot - w_lab| = {worst:.1e}; same coins every date: {same}")
    return report("xsmom targets: bot path == lab b3_xsmom_r1 path", {
        f"identical targets on {n} decision dates (>= 20)": n >= 20 and worst < 1e-12 and same,
        "bot's Binance hourly fetch == lab cache (ZEC, 300 bars)": data_same,
    })


class CompSim:
    """test_sleeves.Sim, plus the R1 fetch served from the lab's daily panel (offline)."""

    def __init__(self, tag: str, c: pd.DataFrame, start: pd.Timestamp, cfg: dict, prec: dict) -> None:
        from tests.test_sleeves import Sim
        self.calls = 0
        d = load_daily()
        self.dclose, self.dqv = d["close"], d["quote_volume"]
        outer = self

        class _S(Sim):
            def new_bot(self):
                bot = StrategyBot(self.cfg, self.ex, base_dir=self.base, clock=lambda: self.now["t"],
                                  sleep=lambda s: None, bars=self.bars)
                bot.setup()
                for r in bot.r1s.values():
                    r.fetch = outer.fetch
                return bot

        self.prec = prec
        orig = MockRoostoo.__init__

        def init(ex, pairs, usd=50_000.0, **kw):
            orig(ex, pairs, usd=usd, prec=prec, **kw)
        MockRoostoo.__init__ = init
        try:
            self.sim = _S(tag, c, start, cfg, pairs=list(c.columns))
        finally:
            MockRoostoo.__init__ = orig

    def fetch(self, pair: str, end: pd.Timestamp, days: int) -> pd.DataFrame | None:
        self.calls += 1
        sym = ROOSTOO.get(pair, {}).get("binance") or pair.split("/")[0] + "USDT"
        if sym not in self.dclose.columns:
            return None
        lo, hi = end - pd.Timedelta(days=days), end - pd.Timedelta(days=1)
        df = pd.DataFrame({"close": self.dclose[sym].loc[lo:hi], "quote_volume": self.dqv[sym].loc[lo:hi]})
        return df[df["close"].notna()]


def pool_closes() -> tuple[pd.DataFrame, dict]:
    frames, prec = {}, {}
    for pair, v in ROOSTOO.items():
        try:
            s = load_close([v["binance"]])[v["binance"]]
        except KeyError:
            continue
        frames[pair] = s
        prec[pair] = (int(v["PricePrecision"]), int(v["AmountPrecision"]))
    c = pd.DataFrame(frames).sort_index()
    c.index = pd.DatetimeIndex(c.index).tz_convert("UTC")
    return c.reindex(pd.date_range(c.index[0], c.index[-1], freq="1h")).ffill(), prec


def test_replay(days: int) -> bool:
    cfg = comp_cfg()
    c, prec = pool_closes()
    hours = c.index[-24 * days:]
    alive = [p for p in c.columns if pd.notna(c.loc[hours[0], p])]
    c = c[alive]
    cs = CompSim("replay", c, hours[0], cfg, prec)
    sim = cs.sim
    for h in hours:
        sim.run_hour(h)
    orders = [o for o in sim.read("orders") if "response" in o]
    errors = sim.read("errors") + [o for o in sim.read("orders") if o.get("error")]
    eq = sim.read("equity")
    first = pd.Timestamp(eq[0]["time"])
    mult_change = {pd.Timestamp(eq[i]["time"]).floor("min") for i in range(1, len(eq)) if eq[i]["mult"] != eq[i - 1]["mult"]}
    off = [o for o in orders if pd.Timestamp(o["time"]).hour != 15 and pd.Timestamp(o["time"]) != first
           and pd.Timestamp(o["time"]).floor("min") not in mult_change]
    res = [d for d in sim.read("decisions") if d.get("event") == "universe_reselect"]
    st = json.loads((sim.base / "state_competition" / "universe_r1.json").read_text())
    first_month = min(pd.Timestamp(d["as_of"], tz="UTC") for d in res) + pd.Timedelta(days=1)
    lab = lab_table(str((first_month - pd.Timedelta(days=2)).date()), str(hours[-1].date()))
    match = all([to_pair(a) for a in lab.get(pd.Timestamp(d["as_of"], tz="UTC") + pd.Timedelta(days=1), [])]
                == d["selected"] for d in res)
    gross = max(sum(abs(v) for v in e["exposure"].values()) / e["equity"] for e in eq)
    months = sorted({d["as_of"] for d in res})
    print(f"\n   {len(orders)} orders, {len(c.columns)} pool pairs, re-selections as of {months}, "
          f"max gross {gross:.0%} of equity; current list {st['selected']}")
    return report(f"{days}-day replay with config_competition.yaml (xsmom on R1, no cap)", {
        f"0 errors ({len(errors)})": not errors,
        f"USD cash never negative (min ${sim.min_usd:,.2f})": sim.min_usd >= -1e-6,
        f"orders only at the 15:00 decision or startup ({len(off)} off-schedule)": not off,
        f"R1 re-selected at start and at the month start ({len(res)} logged)": len(res) >= 2 if hours[0].month != hours[-1].month else len(res) >= 1,
        "every selection == the lab's for that month": match,
        "state_competition/universe_r1.json saved with month, as_of, selected_at": {"month", "as_of", "selected_at", "selected"} <= set(st),
        f"gross <= 75% of equity incl. drift (max {gross:.0%})": gross <= 0.75 * 1.1,
    })


def test_restart() -> bool:
    cfg = comp_cfg()
    c, prec = pool_closes()
    hours = c.index[-24 * 6:]
    alive = [p for p in c.columns if pd.notna(c.loc[hours[0], p])]
    c = c[alive]
    start = hours[0]
    at = (hours[-1] - pd.Timedelta(hours=11)).floor("D") + pd.Timedelta(hours=10, minutes=22)
    a, b = CompSim("restart_a", c, start, cfg, prec), CompSim("restart_b", c, start, cfg, prec)
    out = {}
    for h in hours:
        if "n0" not in out and b.sim.now["t"] < at <= h + pd.Timedelta(minutes=59):
            before = {n: (dict(bk.target), dict(bk.units)) for n, bk in b.sim.bot.books.items()}
            calls0 = b.calls
            out["n0"] = b.sim.restart(at)
            out["refetch"] = b.calls - calls0
            out["same"] = before == {n: (dict(bk.target), dict(bk.units)) for n, bk in b.sim.bot.books.items()}
        a.sim.run_hour(h)
        b.sim.run_hour(h)
    key = lambda o: (o["action"], json.dumps(o.get("request"), sort_keys=True))
    oa = [key(o) for o in a.sim.read("orders") if "response" in o and pd.Timestamp(o["time"]) > at]
    ob = [key(o) for o in b.sim.read("orders") if "response" in o and pd.Timestamp(o["time"]) > at]
    return report(f"mid-day restart with config_competition.yaml at {at:%Y-%m-%d %H:%M} UTC", {
        "books and targets restored": out.get("same", False),
        f"R1 list restored from state (no re-selection: {out.get('refetch')} fetches)": out.get("refetch") == 0,
        "restart step placed 0 orders": out.get("n0") == 0,
        f"orders after the restart identical ({len(oa)})": oa == ob,
        "end equity identical": abs(a.sim.ex.equity() - b.sim.ex.equity()) < 1e-6,
    })


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30)
    a = ap.parse_args()
    shutil.rmtree(OUT, ignore_errors=True)
    import tests.test_sleeves as ts
    ts.OUT = OUT
    params = {**DEFAULTS, **comp_cfg()["sleeves"][0]["universe_rule"]}
    ok_u, daily = test_universe_parity(params)
    ok = ok_u & test_target_parity(params, daily) & test_replay(a.days) & test_restart()
    print(f"\n(f) competition config tests: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
