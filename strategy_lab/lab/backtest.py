"""Hourly portfolio backtester with strategy_bot's execution rules and Roostoo costs.

Same rules as strategy_bot (portfolio.py / bot.py / risk.py):
  * targets from Strategy.target_weights(closes[-lookback_bars:], params), recomputed
    every `rebalance_every_h` hours at `rebalance_hour_utc` (s3v2: daily at 00:00)
  * each hour, per pair: trade only if |target - current| > band, or target == 0 while
    still holding; plan per leg (long book and short book are separate on Roostoo);
    reductions before increases
  * drawdown brake vs rolling `peak_days` peak (soft -> x0.5, hard -> flat for cooloff_h,
    then the peak resets), activity guard (guard_band at guard hour if no trade that day)
  * capital_cap_usd: weights sized against min(equity, cap)
Costs (config/lab.yaml): taker 0.10% / maker 0.05% (spot_maker_share mix), shorts 0.10%,
2 bps slippage, $1 MiniOrder, quantities floored to AmountPrecision (Roostoo's value for
listed coins, else derived from price: ceil(log10(price)) decimals, which reproduces
Roostoo's precision for all 10 S3v2 coins).

Timing: the decision at bar t uses closes <= t and fills at close[t] (+/- slippage), like
research/engine.py; the bot does the same a few seconds after the bar closes.

engine_mode=True switches to the reference research engine's simplifications (no
rounding, no MiniOrder, no guard, exit threshold 1e-9) to verify reproduction exactly.
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass, field
from typing import Any

import numpy as np
import pandas as pd

from lab import load_config
from lab.strategies import get_strategy
from lab.universe import Universe

LAB = load_config()


@dataclass
class RunConfig:
    name: str
    strategy: str = "s3v2"
    params: dict[str, Any] = field(default_factory=dict)
    universe: dict[str, Any] = field(default_factory=lambda: {"type": "list", "assets": []})
    start: str = "2020-01-01"
    end: str | None = None
    rebalance_hour_utc: int = 0
    rebalance_every_h: int = 24
    band: float = 0.06
    activity_guard: bool = True
    guard_hour_utc: int = 20
    guard_band: float = 0.01
    allow_short: bool = True
    brake: bool = True
    dd_soft: float = -0.04
    dd_hard: float = -0.07
    cooloff_h: int = 24
    peak_days: int = 14
    initial_equity: float = LAB["backtest"]["initial_equity"]
    capital_cap_usd: float | None = LAB["backtest"]["capital_cap_usd"]
    lookback_bars: int = LAB["backtest"]["lookback_bars"]
    costs: dict[str, float] = field(default_factory=lambda: dict(LAB["costs"]))
    engine_mode: bool = False

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "RunConfig":
        known = {f for f in cls.__dataclass_fields__}
        extra = set(d) - known
        if extra:
            raise ValueError(f"unknown run settings: {sorted(extra)}")
        cfg = cls(**d)
        cfg.costs = {**LAB["costs"], **(d.get("costs") or {})}
        return cfg


def amount_precision(asset: str, price: float, specs: dict[str, dict]) -> int:
    if asset in specs:
        return int(specs[asset]["AmountPrecision"])
    return max(0, math.ceil(math.log10(price))) if price > 0 else 0


def floor_qty(q: float, ap: int) -> float:
    f = 10.0 ** ap
    return math.floor(q * f + 1e-9) / f


class Backtest:
    def __init__(self, rc: RunConfig, closes: pd.DataFrame | None = None) -> None:
        self.rc = rc
        self.strategy = get_strategy(rc.strategy)
        self.universe = Universe(rc.universe)
        warm = pd.Timedelta(hours=rc.lookback_bars + 24)
        start = pd.Timestamp(rc.start, tz="UTC")
        end = pd.Timestamp(rc.end, tz="UTC") if rc.end else None
        self.closes = closes if closes is not None else self.universe.load_closes(start - warm, end)
        self.start, self.end = start, end
        self.specs = self.universe.specs()

    # ------------------------------------------------------------------ #
    def run(self) -> dict[str, Any]:
        rc, c = self.rc, self.closes
        t0 = time.time()
        assets = list(c.columns)
        A = len(assets)
        px_all = c.values
        alive_all = ~np.isnan(px_all)
        last_px = pd.DataFrame(px_all, columns=assets).ffill().values  # for delisting exits
        idx = c.index
        i0 = int(idx.searchsorted(self.start))
        i1 = len(idx) if self.end is None else int(idx.searchsorted(self.end, side="right"))
        costs = rc.costs
        spot_fee = costs["maker"] * costs["spot_maker_share"] + costs["taker"] * (1 - costs["spot_maker_share"])
        slip, sfee, mini = costs["slippage"], costs["short"], costs["min_order_usd"]
        if rc.engine_mode:  # reference engine: one flat rate on traded USD
            spot_fee = sfee = costs["taker"]
        exact = not rc.engine_mode
        exit_eps = 1e-4 if exact else 1e-9
        bp = {"btc_pair": self.universe.btc_asset, **rc.params}

        cash = rc.initial_equity
        lu = np.zeros(A)            # long units
        su = np.zeros(A)            # short units
        entry = np.zeros(A)         # short entry price (weighted)
        coll = np.zeros(A)          # short collateral
        target = None               # np.array of weights (aligned to assets)
        members: list[str] = []
        flat_until, peak_floor = -1, i0
        eq_hist = np.empty(i1 - i0)
        last_trade_day = None
        rec = {k: np.zeros(i1 - i0) for k in ("equity", "cash", "long", "short", "gross",
                                               "turnover", "fees", "trades", "mult")}
        targets_log: list[dict[str, Any]] = []
        n_trades_total = 0

        for k, i in enumerate(range(i0, i1)):
            ts = idx[i]
            p = np.where(alive_all[i], px_all[i], last_px[i])
            fees = turnover = 0.0
            ntr = 0
            # 1) forced exit of delisted assets (no more prices) at the last price
            dead = (~alive_all[i]) & ((lu > 0) | (su > 0))
            for j in np.where(dead)[0]:
                cash, f, tv = self._close_long(j, lu[j], p[j], cash, spot_fee, slip, lu)
                fees, turnover = fees + f, turnover + tv
                cash, f, tv = self._close_short(j, su[j], p[j], cash, sfee, slip, su, coll, entry)
                fees, turnover, ntr = fees + f, turnover + tv, ntr + 1
            # 2) mark to market
            short_val = coll + su * (entry - p)
            eq = cash + float(np.dot(lu, p)) + float(short_val.sum())
            eq_hist[k] = eq
            # 3) drawdown brake (engine/risk.py semantics)
            mult = 1.0
            if rc.brake:
                lo = min(max(peak_floor - i0, k - rc.peak_days * 24), k)
                dd = eq / eq_hist[lo:k + 1].max() - 1
                if k < flat_until:
                    mult = 0.0
                elif dd < rc.dd_hard:
                    mult = 0.0
                    flat_until = k + rc.cooloff_h
                    peak_floor = i0 + k + rc.cooloff_h
                elif dd < rc.dd_soft:
                    mult = 0.5
            # 4) targets: on schedule, or at the first bar
            hours_since = (ts - self.start) / pd.Timedelta(hours=1)
            sched = ts.hour == rc.rebalance_hour_utc if rc.rebalance_every_h == 24 \
                else hours_since % rc.rebalance_every_h == 0
            if target is None or sched:
                ti = i if (sched or target is not None) else self._last_sched(i)
                members = self.universe.members(idx[ti], assets, alive_all[ti])
                target = np.zeros(A)
                if members:
                    window = c.iloc[max(0, ti - rc.lookback_bars + 1):ti + 1][members]
                    try:
                        w = self.strategy.target_weights(window, bp)
                    except ValueError:  # not enough history yet
                        w = {}
                    for a, v in w.items():
                        if a in members:
                            target[assets.index(a)] = v if (rc.allow_short or v > 0) else 0.0
                targets_log.append({"time": str(idx[ti]), "members": len(members),
                                    "target": {a: round(float(target[assets.index(a)]), 5)
                                               for a in members if target[assets.index(a)]}})
            tgt = target * mult
            g = np.abs(tgt).sum()
            if g > 1:
                tgt = tgt / g
            # 5) band check + per-leg plan (strategy_bot portfolio.py)
            sizing = min(eq, rc.capital_cap_usd) if rc.capital_cap_usd else eq
            guard = (exact and rc.activity_guard and ts.hour == rc.guard_hour_utc
                     and last_trade_day != ts.date())
            band = rc.guard_band if guard else rc.band
            lw = lu * p / sizing
            sw = su * p / sizing
            cw = lw - sw
            holding = (lw > exit_eps) | (sw > exit_eps)
            hedged = (lw > exit_eps) & (sw > exit_eps)
            trade = (np.abs(tgt - cw) > band) | ((tgt == 0) & holding) | hedged
            trade &= alive_all[i]
            if trade.any():
                plan_red, plan_inc = [], []
                for j in np.where(trade)[0]:
                    tw = tgt[j]
                    if lw[j] > max(tw, 0):
                        plan_red.append(("SELL", j, (lw[j] - max(tw, 0)) * sizing))
                    if sw[j] > max(-tw, 0):
                        plan_red.append(("COVER", j, (sw[j] - max(-tw, 0)) * sizing))
                    if tw > 0 and tw > lw[j]:
                        plan_inc.append(("BUY", j, (tw - lw[j]) * sizing))
                    if tw < 0 and -tw > sw[j]:
                        plan_inc.append(("SHORT", j, (-tw - sw[j]) * sizing))
                for act, j, usd in plan_red + plan_inc:
                    pj = p[j]
                    ap = amount_precision(assets[j], pj, self.specs) if exact else None
                    q = usd / pj
                    if exact:
                        q = floor_qty(q, ap)
                    if act == "SELL":
                        q = min(q, lu[j])
                        if q <= 0 or (exact and q * pj <= mini):
                            continue
                        cash, f, tv = self._close_long(j, q, pj, cash, spot_fee, slip, lu)
                    elif act == "COVER":
                        q = min(q, su[j])
                        if q <= 0 or (exact and q * pj <= mini and q < su[j]):
                            continue
                        cash, f, tv = self._close_short(j, q, pj, cash, sfee, slip, su, coll, entry)
                    elif act == "BUY":
                        buy_px = pj * (1 + slip)
                        q = min(q, cash / (buy_px * (1 + spot_fee)))
                        if exact:
                            q = floor_qty(q, ap)
                        if q <= 0 or (exact and q * pj <= mini):
                            continue
                        cost = q * buy_px
                        f = cost * spot_fee
                        cash -= cost + f
                        lu[j] += q
                        tv = cost
                    else:  # SHORT: collateral sized so collateral + fee fits
                        sell_px = pj * (1 - slip)
                        if exact:
                            q = floor_qty(min(usd / 1.001, cash / (1 + sfee)) / sell_px, ap)
                        else:
                            q = min(q, cash / (sell_px * (1 + sfee)))
                        if q <= 0 or (exact and q * sell_px < max(1.0, mini)):
                            continue
                        new_coll = q * sell_px
                        f = new_coll * sfee
                        if new_coll + f > cash + 1e-9:
                            continue
                        cash -= new_coll + f
                        tot = su[j] + q
                        entry[j] = (entry[j] * su[j] + sell_px * q) / tot
                        su[j] = tot
                        coll[j] += new_coll
                        tv = new_coll
                    fees += f
                    turnover += tv
                    ntr += 1
                if ntr:
                    last_trade_day = ts.date()
            n_trades_total += ntr
            short_val = coll + su * (entry - p)
            eq_after = cash + float(np.dot(lu, p)) + float(short_val.sum())
            rec["equity"][k] = eq_after
            eq_hist[k] = eq_after
            rec["cash"][k] = cash
            rec["long"][k] = float(np.dot(lu, p))
            rec["short"][k] = float((su * p).sum())
            rec["gross"][k] = (rec["long"][k] + rec["short"][k]) / max(eq_after, 1e-9)
            rec["turnover"][k] = turnover
            rec["fees"][k] = fees
            rec["trades"][k] = ntr
            rec["mult"][k] = mult
        hourly = pd.DataFrame(rec, index=idx[i0:i1])
        return {"config": rc, "hourly": hourly, "targets": targets_log,
                "assets": assets, "runtime_s": round(time.time() - t0, 1),
                "trades_total": n_trades_total}

    # ------------------------------------------------------------------ #
    def _last_sched(self, i: int) -> int:
        """Index of the latest scheduled rebalance bar <= i (for the first target)."""
        rc, idx = self.rc, self.closes.index
        for j in range(i, max(-1, i - 24 * 7), -1):
            if rc.rebalance_every_h != 24 or idx[j].hour == rc.rebalance_hour_utc:
                return j
        return i

    @staticmethod
    def _close_long(j, q, pj, cash, fee_rate, slip, lu):
        if q <= 0:
            return cash, 0.0, 0.0
        proceeds = q * pj * (1 - slip)
        f = proceeds * fee_rate
        lu[j] -= q
        if lu[j] < 1e-12:
            lu[j] = 0.0
        return cash + proceeds - f, f, proceeds

    @staticmethod
    def _close_short(j, q, pj, cash, fee_rate, slip, su, coll, entry):
        if q <= 0 or su[j] <= 0:
            return cash, 0.0, 0.0
        q = min(q, su[j])
        cover_px = pj * (1 + slip)
        frac = q / su[j]
        c_back = coll[j] * frac
        pnl = q * (entry[j] - cover_px)
        f = q * cover_px * fee_rate
        su[j] -= q
        coll[j] -= c_back
        if su[j] < 1e-12:
            su[j] = coll[j] = entry[j] = 0.0
        return cash + c_back + pnl - f, f, q * cover_px


def run(spec: dict[str, Any], closes: pd.DataFrame | None = None) -> dict[str, Any]:
    return Backtest(RunConfig.from_dict(spec), closes).run()
