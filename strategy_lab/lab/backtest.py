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

bar="30m" (MFT runs) simulates on 30-minute bars: the strategy sees 30m closes and may
re-target every `rebalance_every_h` (e.g. 0.5); clock-time rules stay in hours (14-day
peak, 24h cool-off, 00:00 targets, 20:00 guard). The output is resampled to hourly
(equity at the hour's last bar, fees/turnover/trades summed) so the scorecard,
leaderboard and analogs treat every run identically.

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
BPH = {"15m": 4, "30m": 2, "1h": 1}   # bars per hour


@dataclass
class RunConfig:
    name: str
    strategy: str = "s3v2"
    params: dict[str, Any] = field(default_factory=dict)
    universe: dict[str, Any] = field(default_factory=lambda: {"type": "list", "assets": []})
    start: str = "2020-01-01"
    end: str | None = None
    rebalance_hour_utc: int = 0
    rebalance_every_h: float = 24
    bar: str = "1h"                  # 15m | 30m | 1h
    check_every_h: int = 1          # band checks / trades / brake only every N hours (2h, 4h cadence)
    band: float = 0.06
    activity_guard: str = "full"     # off | full (1pp band, live bot) | minimal | band_edge
    guard_hour_utc: int = 20
    guard_band: float = 0.01        # 'full' mode band
    guard_max_frac: float = 0.02    # 'minimal' mode: max trade size, fraction of equity
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
    execution: str = "band"         # band (hourly band checks) | scheduled (trade fully only at refresh)
    events: dict[str, Any] | None = None   # macro-event overlays (block 4, see _event_plan); None = off
    exits: dict[str, Any] | None = None    # intraday exits between decisions (block 4, see run()); None = off
    record_positions: bool = False  # sparse per-coin weight / long and short P&L per hour (res["positions"])
    entry_limit: dict[str, Any] | None = None   # patient entry limits (block 4d): {offset, through}; None = off
    changepoint: dict[str, Any] | None = None   # block 6 A3: {method cusum|bocpd, threshold, cut, k}; None = off

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "RunConfig":
        known = {f for f in cls.__dataclass_fields__}
        extra = set(d) - known
        if extra:
            raise ValueError(f"unknown run settings: {sorted(extra)}")
        cfg = cls(**d)
        if isinstance(cfg.activity_guard, bool):  # back-compat: True -> live behaviour
            cfg.activity_guard = "full" if cfg.activity_guard else "off"
        if cfg.activity_guard not in ("off", "full", "minimal", "band_edge"):
            raise ValueError(f"activity_guard must be off|full|minimal|band_edge, got {cfg.activity_guard!r}")
        if cfg.execution not in ("band", "scheduled"):
            raise ValueError(f"execution must be band|scheduled, got {cfg.execution!r}")
        if cfg.bar not in BPH:
            raise ValueError(f"bar must be one of {sorted(BPH)}, got {cfg.bar!r}")
        if cfg.events and cfg.bar != "1h":
            raise ValueError("events overlays need bar=1h")
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
        self.bph = BPH[rc.bar]
        warm = pd.Timedelta(hours=rc.lookback_bars / self.bph + 24)
        start = pd.Timestamp(rc.start, tz="UTC")
        end = pd.Timestamp(rc.end, tz="UTC") if rc.end else None
        self.closes = closes if closes is not None else self.universe.load_closes(start - warm, end, rc.bar)
        self.volume = None
        if getattr(self.strategy, "needs_volume", False):   # e.g. breakout volume confirmation
            self.volume = self.universe.load_closes(start - warm, end, rc.bar, field="quote_volume") \
                .reindex(index=self.closes.index, columns=self.closes.columns).fillna(0.0)
        self.start, self.end = start, end
        self.specs = self.universe.specs()
        self.lows = None
        if rc.entry_limit:                  # hourly lows (lab/lows.py) for limit fills
            from lab.lows import load_lows
            self.lows = load_lows(list(self.closes.columns), self.closes.index).values

    # ------------------------------------------------------------------ #
    def run(self) -> dict[str, Any]:
        rc, c = self.rc, self.closes
        t0 = time.time()
        assets = list(c.columns)
        self.assets_ = assets
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
        sched_mult = None           # scheduled execution: multiplier at the last scheduled trade
        ev = self._event_plan(idx, assets) if rc.events else None
        cash_mode = False           # breakout overlay: BTC fell > threshold after an event
        ev_log: dict[str, Any] = {"breakout_up": [], "breakout_down": [], "derisk_bars": 0, "fast_refreshes": 0}
        # intraday exits (rc.exits, long book only; checked at every hourly close between target refreshes):
        #   trend_break  EMA24 < EMA168 (hourly closes) on a held coin -> sell it
        #   stop         close <= entry x (1 - pct); entry = average buy price of the current holding
        #   trailing     close <= highest close since entry x (1 - pct)
        # an exited coin stays out until the next target refresh (the daily decision); each exit is
        # logged with what the coin did from the exit to that refresh (loss avoided / profit given up)
        xe = rc.exits
        if xe:
            if xe["type"] not in ("trend_break", "stop", "trailing"):
                raise ValueError(f"exits.type must be trend_break|stop|trailing, got {xe['type']!r}")
            if xe["type"] == "trend_break":
                ema_f = c.ewm(span=24, adjust=False, min_periods=24).mean().values
                ema_s = c.ewm(span=168, adjust=False, min_periods=168).mean().values
        x_entry = np.zeros(A)
        x_high = np.zeros(A)
        exited = np.zeros(A, dtype=bool)
        x_pending: list[dict[str, Any]] = []
        x_log: list[dict[str, Any]] = []
        pos_rows: list[tuple] = []          # (k, j, signed weight at bar end, long pnl, short pnl) if any != 0
        hold_start = np.full(A, -1)         # bar index when the current position (either side) opened
        # patient entry limits: a NEW long entry at a scheduled trade rests as a limit at decision price x (1 - offset)
        # until the next target refresh; it fills (at the limit, maker fee, no slippage) at the first later hourly bar
        # whose low <= limit x (1 - through); otherwise it is cancelled at the next refresh. Other trades as usual.
        el = rc.entry_limit
        pend: dict[int, dict[str, Any]] = {}
        el_log: list[dict[str, Any]] = []
        # changepoint cut (block 6 A3, lab/changepoint.py): a held coin whose score against its position exceeds the
        # threshold has its target multiplied by `cut` (0.5 or 0) until the next target refresh; the cut trades at once
        cpc = rc.changepoint
        cp_cut = np.ones(A)
        cp_log: dict[str, Any] = {"cuts": 0, "events": []}
        if cpc:
            from lab.changepoint import scores as cp_scores
            reset = np.array([(t.hour == rc.rebalance_hour_utc and t.minute == 0) for t in idx])
            cp_dn, cp_up = cp_scores(c, cpc["method"], reset, float(cpc.get("k", 0.5)))
        needs_hold = getattr(self.strategy, "needs_holdings", False)
        p_prev = None
        rec = {k: np.zeros(i1 - i0) for k in ("equity", "cash", "long", "short", "gross",
                                               "turnover", "fees", "trades", "mult")}
        targets_log: list[dict[str, Any]] = []
        n_trades_total = 0
        mult = 1.0

        for k, i in enumerate(range(i0, i1)):
            ts = idx[i]
            # price: live close, else last close (delisted), else 0 (not listed yet; no
            # position can exist and the asset is masked from trading)
            p = np.nan_to_num(np.where(alive_all[i], px_all[i], last_px[i]), nan=0.0)
            if rc.record_positions:
                if p_prev is not None:
                    dp = np.where((p > 0) & (p_prev > 0), p - p_prev, 0.0)
                    pl_bar, ps_bar = lu * dp, -su * dp
                else:
                    pl_bar = ps_bar = np.zeros(A)
                p_prev = p
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
            # between checks (check_every_h > 1): targets still refresh on schedule, but the
            # brake, band checks and trades wait for the next check bar
            is_check = rc.check_every_h <= 1 or (ts.minute == 0 and ts.hour % rc.check_every_h == 0)
            if is_check:
                mult = 1.0
            if rc.brake and is_check:
                lo = min(max(peak_floor - i0, k - rc.peak_days * 24 * self.bph), k)
                dd = eq / eq_hist[lo:k + 1].max() - 1
                if k < flat_until:
                    mult = 0.0
                elif dd < rc.dd_hard:
                    mult = 0.0
                    flat_until = k + rc.cooloff_h * self.bph
                    peak_floor = i0 + k + rc.cooloff_h * self.bph
                elif dd < rc.dd_soft:
                    mult = 0.5
            # 4) targets: on schedule, or at the first bar
            # sub-daily refreshes are anchored at rebalance_hour_utc (00:00 for s3v2 -> unchanged;
            # 14:00 for xsmom -> a 12h refresh runs at 02:00 / 14:00)
            anchor = self.start.floor("D") + pd.Timedelta(hours=rc.rebalance_hour_utc)
            hours_since = (ts - anchor) / pd.Timedelta(hours=1)
            sched = (ts.hour == rc.rebalance_hour_utc and ts.minute == 0) if rc.rebalance_every_h == 24 \
                else hours_since % rc.rebalance_every_h == 0
            if ev is not None:
                extra = False
                if sched:
                    cash_mode = False                  # the daily decision ends a post-event cash spell
                if ev["fast"] is not None and ev["fast"][i] and not sched \
                        and hours_since % ev["fast_every_h"] == 0:
                    extra = True
                    ev_log["fast_refreshes"] += 1
                for e_id, pre in ev["breakout"].get(i, []):
                    if e_id in ev["fired"]:
                        continue
                    r = last_px[i, ev["btc"]] / last_px[pre, ev["btc"]] - 1
                    if r > ev["up"]:
                        ev["fired"].add(e_id)
                        extra, cash_mode = True, False
                        ev_log["breakout_up"].append(str(ts))
                    elif r < ev["down"]:
                        ev["fired"].add(e_id)
                        cash_mode = True
                        ev_log["breakout_down"].append(str(ts))
                sched = sched or extra
            if cpc and sched:
                cp_cut[:] = 1.0
            if el and sched:
                for j, x in pend.items():
                    el_log.append({**x, "filled": None})
                pend.clear()
            if xe and sched:
                for x in x_pending:          # what the exited coin did until this refresh
                    r = (p[x["j"]] / x["px"] - 1) if x["px"] > 0 and p[x["j"]] > 0 else 0.0
                    x_log.append({"time": x["time"], "asset": assets[x["j"]], "w": x["w"], "ret_to_refresh": r,
                                  "pnl_frac": x["w"] * r})   # > 0 profit given up, < 0 loss avoided
                x_pending.clear()
                exited[:] = False
            if target is None or sched:
                ti = i if (sched or target is not None) else self._last_sched(i)
                members = self.universe.members(idx[ti], assets, alive_all[ti])
                target = np.zeros(A)
                if members:
                    window = c.iloc[max(0, ti - rc.lookback_bars + 1):ti + 1][members]
                    try:
                        bpw = bp if self.volume is None else {
                            **bp, "_volume": self.volume.iloc[max(0, ti - rc.lookback_bars + 1):ti + 1][members]}
                        if needs_hold:     # e.g. xsmom_ls big_gap_swap: the current book and holding time
                            sz = min(eq, rc.capital_cap_usd) if rc.capital_cap_usd else eq
                            w_now = (lu - su) * p / max(sz, 1e-9)          # same basis as the trade check
                            bpw = {**bpw, "_mult": mult,
                                   "_held": {assets[j]: float(w_now[j]) for j in np.where(np.abs(w_now) > 1e-4)[0]},
                                   "_held_h": {assets[j]: (k - hold_start[j]) / self.bph
                                               for j in np.where(hold_start >= 0)[0]}}
                        if getattr(self.strategy, "needs_btc", False):   # e.g. xsmom_sz regime exposure
                            bpw = {**bpw, "_btc": c[self.universe.btc_asset].iloc[max(0, ti - rc.lookback_bars + 1):ti + 1]}
                        w = self.strategy.target_weights(window, bpw)
                    except ValueError:  # not enough history yet
                        w = {}
                    for a, v in w.items():
                        if a in members:
                            target[assets.index(a)] = v if (rc.allow_short or v > 0) else 0.0
                targets_log.append({"time": str(idx[ti]), "members": len(members),
                                    "target": {a: round(float(target[assets.index(a)]), 5)
                                               for a in members if target[assets.index(a)]}})
            if not is_check:      # hold; record mark-to-market only
                self._record(rec, k, eq, cash, lu, su, p, 0.0, 0.0, 0, mult)
                if rc.record_positions:
                    self._pos(pos_rows, k, lu, su, p, eq, pl_bar, ps_bar)
                continue
            tgt = target * mult
            g = np.abs(tgt).sum()
            if g > 1:
                tgt = tgt / g
            ev_key: tuple = ()
            if ev is not None:
                if cash_mode:
                    tgt = np.zeros(A)
                if ev["derisk"] is not None and ev["derisk"][i]:
                    ev_log["derisk_bars"] += 1
                    g = np.abs(tgt).sum()
                    if g > ev["max_gross"]:
                        tgt = tgt * (ev["max_gross"] / g)
                g0 = np.abs(target * mult).sum()
                ev_key = (cash_mode, round(float(np.abs(tgt).sum() / g0), 9) if g0 > 0 else 1.0)
            cp_new = np.zeros(A, dtype=bool)
            if cpc:
                lw0, sw0 = lu * p / max(eq, 1e-9), su * p / max(eq, 1e-9)
                thr = float(cpc["threshold"])
                hit = (((lw0 > exit_eps) & (cp_dn[i] > thr)) | ((sw0 > exit_eps) & (cp_up[i] > thr))) & (cp_cut == 1.0)                     & (not sched)
                cp_new = hit & alive_all[i]
                cp_cut[cp_new] = float(cpc["cut"])
                cp_log["cuts"] += int(cp_new.sum())
                cp_log["events"] += [(str(ts), assets[j]) for j in np.where(cp_new)[0]]
                tgt = tgt * cp_cut
            # 5) band check + per-leg plan (strategy_bot portfolio.py), then activity guard
            sizing = min(eq, rc.capital_cap_usd) if rc.capital_cap_usd else eq
            guard_hour = (exact and rc.activity_guard != "off" and ts.hour == rc.guard_hour_utc and ts.minute == 0
                          and last_trade_day != ts.date())
            band = rc.guard_band if (guard_hour and rc.activity_guard == "full") else rc.band
            lw = lu * p / sizing
            sw = su * p / sizing
            cw = lw - sw
            holding = (lw > exit_eps) | (sw > exit_eps)
            hedged = (lw > exit_eps) & (sw > exit_eps)
            if rc.execution == "scheduled":
                # strategy_bot sleeve execution "scheduled": move fully to target at each refresh
                # (and when the brake / KILL multiplier changes); no trades in between
                # event overlays (cash spell, de-risk cap) act like a multiplier change
                due = sched or sched_mult is None or (mult, ev_key) != sched_mult
                trade = ((np.abs(tgt - cw) > 1e-9) | hedged) if due else np.zeros(A, dtype=bool)
                if due:
                    sched_mult = (mult, ev_key)
            else:
                trade = (np.abs(tgt - cw) > band) | ((tgt == 0) & holding) | hedged
            trade |= cp_new
            if xe:
                held = lw > exit_eps
                np.maximum(x_high, np.where(held, p, 0.0), out=x_high)
                if not sched:
                    if xe["type"] == "trend_break":     # long: EMA24 < EMA168; short (if any): EMA24 > EMA168
                        fire = (held & (ema_f[i] < ema_s[i])) | ((sw > exit_eps) & (ema_f[i] > ema_s[i]))
                    elif xe["type"] == "stop":
                        fire = held & (x_entry > 0) & (p <= x_entry * (1 - float(xe["pct"])))
                    else:
                        fire = held & (x_high > 0) & (p <= x_high * (1 - float(xe["pct"])))
                    fire &= ~exited & alive_all[i]
                    for j in np.where(fire)[0]:
                        x_pending.append({"time": str(ts), "j": int(j), "px": float(p[j]), "w": float(cw[j])})
                    exited |= fire
                    trade |= fire
                tgt = np.where(exited, 0.0, tgt)
                lu_before = lu.copy()
            if el:
                sizing_el = min(eq, rc.capital_cap_usd) if rc.capital_cap_usd else eq
                for j in list(pend):                     # fills of resting entry limits
                    x = pend[j]
                    if tgt[j] <= 0:                      # target gone (brake / KILL / refresh): cancel
                        el_log.append({**x, "filled": None})
                        pend.pop(j)
                        continue
                    lo = self.lows[i, j]
                    if alive_all[i, j] and np.isfinite(lo) and lo <= x["limit"] * (1 - float(el.get("through", 0.001))):
                        ap = amount_precision(assets[j], x["limit"], self.specs)
                        q = floor_qty(min(tgt[j] * sizing_el, cash / (1 + costs["maker"])) / x["limit"], ap)
                        if q > 0 and q * x["limit"] > mini:
                            cost = q * x["limit"]
                            f = cost * costs["maker"]
                            cash -= cost + f
                            lu[j] += q
                            fees, turnover, ntr = fees + f, turnover + cost, ntr + 1
                            el_log.append({**x, "filled": str(ts)})
                        pend.pop(j)
                if trade.any():
                    lw_now = lu * p / sizing
                    new = trade & (lw_now <= exit_eps) & (tgt > 0) & (su <= 0)
                    for j in np.where(new)[0]:
                        if j not in pend:
                            pend[int(j)] = {"placed": str(ts), "asset": assets[j], "limit": float(p[j]) * (1 - float(el["offset"]))}
                    trade &= ~new
            trade &= alive_all[i]
            if trade.any():
                cash, f, tv, n = self._execute({j: tgt[j] for j in np.where(trade)[0]}, lw, sw, sizing,
                                               p, cash, lu, su, entry, coll, spot_fee, sfee, slip,
                                               mini, exact)
                fees, turnover, ntr = fees + f, turnover + tv, ntr + n
            if guard_hour and ntr == 0 and rc.activity_guard in ("minimal", "band_edge"):
                # one trade on the pair furthest from target (= closest to crossing its band,
                # since the band is the same for every pair)
                gap = np.where(alive_all[i], tgt - cw, 0.0)
                j = int(np.argmax(np.abs(gap)))
                if abs(gap[j]) > 1e-9:
                    if rc.activity_guard == "minimal":
                        size = max(min(abs(gap[j]), rc.guard_max_frac), 1.5 * mini / sizing)
                        tw_j = cw[j] + np.sign(gap[j]) * size
                    else:
                        tw_j = tgt[j]
                    cash, f, tv, n = self._execute({j: tw_j}, lw, sw, sizing, p, cash, lu, su,
                                                   entry, coll, spot_fee, sfee, slip, mini, exact)
                    fees, turnover, ntr = fees + f, turnover + tv, ntr + n
            nz = np.abs(lu - su) > 1e-15
            hold_start[nz & (hold_start < 0)] = k
            hold_start[~nz] = -1
            if xe:                           # entry price / high since entry of the long book
                add = lu > lu_before + 1e-15
                x_entry = np.where(add, (x_entry * lu_before + (lu - lu_before) * p) / np.maximum(lu, 1e-300), x_entry)
                x_high = np.where(add & (lu_before <= 1e-15), p, x_high)
                gone = lu <= 1e-15
                x_entry[gone] = 0.0
                x_high[gone] = 0.0
            if ntr:
                last_trade_day = ts.date()
            n_trades_total += ntr
            short_val = coll + su * (entry - p)
            eq_hist[k] = cash + float(np.dot(lu, p)) + float(short_val.sum())
            self._record(rec, k, eq_hist[k], cash, lu, su, p, turnover, fees, ntr, mult)
            if rc.record_positions:
                self._pos(pos_rows, k, lu, su, p, eq_hist[k], pl_bar, ps_bar)
        hourly = pd.DataFrame(rec, index=idx[i0:i1])
        if self.bph > 1:
            g = hourly.resample("1h")
            hourly = pd.concat([g[["equity", "cash", "long", "short", "gross"]].last(),
                                g[["turnover", "fees", "trades"]].sum(), g[["mult"]].min()],
                               axis=1)[list(rec)]
        return {"config": rc, "hourly": hourly, "targets": targets_log,
                "assets": assets, "runtime_s": round(time.time() - t0, 1),
                "trades_total": n_trades_total, "events": ev_log if ev is not None else None,
                "extra": ({"exits": x_log} if xe else {}) | ({"entry_limits": el_log} if el else {}) |
                         ({"changepoint": cp_log} if cpc else {}) | ({"strategy_stats": dict(self.strategy.stats)}
                                                              if getattr(self.strategy, "stats", None) else {}) or None,
                "positions": (pd.DataFrame(pos_rows, columns=["k", "j", "w", "pl", "ps"]).assign(
                    time=lambda d: idx[i0:i1][d["k"].values], asset=lambda d: np.array(assets)[d["j"].values])
                    .drop(columns=["k", "j"]) if rc.record_positions else None)}

    @staticmethod
    def _pos(rows: list, k: int, lu, su, p, eq, pl_bar, ps_bar) -> None:
        w = (lu - su) * p / max(eq, 1e-9)
        for j in np.where((np.abs(w) > 1e-9) | (pl_bar != 0) | (ps_bar != 0))[0]:
            rows.append((k, int(j), float(w[j]), float(pl_bar[j]), float(ps_bar[j])))

    # ------------------------------------------------------------------ #
    def _event_plan(self, idx: pd.DatetimeIndex, assets: list[str]) -> dict[str, Any]:
        """Precompute the event overlays (data/events.csv, lab/events.py) on the bar grid.

        A decision at bar i happens when bar i CLOSES, at tau_i = idx[i] + 1h (the bot's hourly
        step). Settings (rc.events), each optional:
          fast:     {types, every_h, days_after}: on the UTC dates of an event and the next
                    `days_after` days, extra target refreshes every `every_h` hours (anchored like
                    the sweep, at rebalance_hour_utc), on top of the daily decision
          derisk:   {types, before_h, after_h, max_gross}: steps with e - before_h <= tau < e + after_h
                    cap gross at max_gross (weights scaled down proportionally)
          breakout: {types, within_h, up, down}: at each step with e < tau <= e + within_h, BTC
                    return vs the last close at or before e; first crossing per event: > up -> an
                    extra decision now; < down -> cash until the next daily decision
        Overlay changes (cash spell, cap on/off) trade fully, like a brake multiplier change.
        """
        from lab.events import load_events
        e = self.rc.events
        tau = idx + pd.Timedelta(hours=1)
        out: dict[str, Any] = {"fast": None, "derisk": None, "breakout": {}, "fired": set(),
                               "btc": assets.index(self.universe.btc_asset)}

        def times(spec: dict) -> pd.DatetimeIndex:
            ev = load_events(tuple(spec.get("types", ("CPI", "FOMC_DECISION"))))
            return pd.DatetimeIndex(ev["time"]).sort_values()

        if e.get("fast"):
            f = e["fast"]
            days = {t.floor("D") + pd.Timedelta(days=d) for t in times(f)
                    for d in range(int(f.get("days_after", 2)) + 1)}
            out["fast"] = np.array([t.floor("D") in days for t in tau])
            out["fast_every_h"] = float(f["every_h"])
        if e.get("derisk"):
            d = e["derisk"]
            on = np.zeros(len(idx), dtype=bool)
            for t in times(d):
                a = tau.searchsorted(t - pd.Timedelta(hours=float(d.get("before_h", 24))))
                b = tau.searchsorted(t + pd.Timedelta(hours=float(d.get("after_h", 4))))
                on[a:b] = True
            out["derisk"], out["max_gross"] = on, float(d["max_gross"])
        if e.get("breakout"):
            b = e["breakout"]
            out["up"], out["down"] = float(b.get("up", 0.02)), float(b.get("down", -0.02))
            for k, t in enumerate(times(b)):
                pre = int(tau.searchsorted(t, side="right")) - 1       # last close at or before the event
                if pre < 0:
                    continue
                j = pre + 1
                while j < len(idx) and tau[j] <= t + pd.Timedelta(hours=float(b.get("within_h", 4))):
                    out["breakout"].setdefault(j, []).append((k, pre))
                    j += 1
        return out

    # ------------------------------------------------------------------ #
    def _execute(self, plan: dict[int, float], lw, sw, sizing, p, cash, lu, su, entry, coll,
                 spot_fee, sfee, slip, mini, exact):
        """Move each pair j to weight plan[j]: per-leg, reductions before increases.
        Returns (cash, fees, turnover, n_trades)."""
        assets = self.assets_
        plan_red, plan_inc = [], []
        for j, tw in plan.items():
            if lw[j] > max(tw, 0):
                plan_red.append(("SELL", j, (lw[j] - max(tw, 0)) * sizing))
            if sw[j] > max(-tw, 0):
                plan_red.append(("COVER", j, (sw[j] - max(-tw, 0)) * sizing))
            if tw > 0 and tw > lw[j]:
                plan_inc.append(("BUY", j, (tw - lw[j]) * sizing))
            if tw < 0 and -tw > sw[j]:
                plan_inc.append(("SHORT", j, (-tw - sw[j]) * sizing))
        fees = turnover = 0.0
        n = 0
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
            n += 1
        return cash, fees, turnover, n

    @staticmethod
    def _record(rec, k, eq, cash, lu, su, p, turnover, fees, ntr, mult) -> None:
        rec["equity"][k] = eq
        rec["cash"][k] = cash
        rec["long"][k] = float(np.dot(lu, p))
        rec["short"][k] = float((su * p).sum())
        rec["gross"][k] = (rec["long"][k] + rec["short"][k]) / max(eq, 1e-9)
        rec["turnover"][k] = turnover
        rec["fees"][k] = fees
        rec["trades"][k] = ntr
        rec["mult"][k] = mult

    def _last_sched(self, i: int) -> int:
        """Index of the latest scheduled rebalance bar <= i (for the first target)."""
        rc, idx = self.rc, self.closes.index
        for j in range(i, max(-1, i - 24 * 7 * self.bph), -1):
            if rc.rebalance_every_h != 24 or (idx[j].hour == rc.rebalance_hour_utc and idx[j].minute == 0):
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
