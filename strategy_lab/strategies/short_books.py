"""Down-market books (block 5, variants_b5_shorts.yaml). All called by the backtester at every hourly bar
(rebalance_every_h 1, scheduled execution): a full selection happens at the decision bar (decision_bar_utc, every
select_every_h hours from it); at the other bars only the intraday exit rule runs and every other holding keeps its
current weight (cfg["_held"] / cfg["_mult"] from the backtester), so nothing else trades.

slow_short (C)  universe coins with EMA(7d) < EMA(30d) (hourly closes, spans 168 / 720) AND 14-day return < -5%, only
                while BTC < its 30-day mean (720 hourly closes) AND alt breadth < 40% (share of non-BTC coins with a close
                above their own 30-day mean); most negative 14d return first; up to n_short at -wa each.
                Intraday: cover a short as soon as EMA(7d) > EMA(30d).
breakdown_short (E) coins whose close is below the lowest hourly close of the previous 20 days (480 bars) with last-24h
                quote volume > 1.5 x the average daily quote volume of the previous 20 days, only while BTC < its 30-day
                mean; deepest breakdown first; up to n_short at -wa. Stop: cover when close > breakdown level + 1 ATR
                (ATR = mean absolute daily close-to-close change over the last 14 days, close-only proxy). A short is also
                covered after max_days (14) or at a decision where BTC >= its 30-day mean.
beta_hedge (D)  live xsmom longs plus a short split equally between BTC and ETH sized to the long book's beta to BTC
                (hourly returns, last 720 bars; beta capped at 1): hedge = beta x long gross, only while the gate holds
                (btc_below_30d: BTC < its 30-day mean; btc_7d: BTC 168h return < -5%). Decision only (no intraday rule).
                Gross above 1 is scaled down by the backtester (shorts need collateral cash).
"""

from __future__ import annotations

import sys
from typing import Any

import numpy as np
import pandas as pd

from lab.strategies import Strategy


def _btc_below_mean(btc: pd.Series | None, n: int = 720) -> bool:
    if btc is None or len(btc.dropna()) < n:
        return False
    b = btc.dropna()
    return bool(b.iloc[-1] < b.iloc[-n:].mean())


def _is_decision(last: pd.Timestamp, p: dict) -> bool:
    h0, every = int(p["decision_bar_utc"]), int(p["select_every_h"])
    return last.minute == 0 and (last.hour - h0) % every == 0


def _keep(held: dict, mult: float, cols: list[str]) -> dict[str, float]:
    m = mult or 1.0
    return {c: (held.get(c, 0.0) / m) for c in cols}


class SlowShort(Strategy):
    name = "slow_short"
    needs_btc = True
    needs_holdings = True
    DEF = {"n_short": 3, "wa": 0.15, "fast": 168, "slow": 720, "ret_h": 336, "ret_thr": -0.05, "breadth_max": 0.40,
           "decision_bar_utc": 14, "select_every_h": 24, "btc_asset": "BTCUSDT"}

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        p = {**self.DEF, **{k: v for k, v in (cfg or {}).items() if not k.startswith("_")}}
        cols, last = list(closes.columns), closes.index[-1]
        held = (cfg or {}).get("_held") or {}
        st = self.__dict__.setdefault("stats", {"decisions": 0, "gate_on": 0, "covers": 0})
        if not _is_decision(last, p):
            out = _keep(held, (cfg or {}).get("_mult", 1.0), cols)
            shorts = [c for c, v in out.items() if v < 0]
            if shorts:
                x = closes[shorts]
                ef = x.ewm(span=p["fast"], adjust=False).mean().iloc[-1]
                es = x.ewm(span=p["slow"], adjust=False).mean().iloc[-1]
                for c in shorts:
                    if ef[c] > es[c]:
                        out[c] = 0.0
                        st["covers"] += 1
            return self.check(out)
        st["decisions"] += 1
        out = {c: 0.0 for c in cols}
        btc = (cfg or {}).get("_btc")
        alts = [c for c in cols if c != p["btc_asset"]]
        sma = closes[alts].iloc[-p["slow"]:].mean()
        ok = closes[alts].iloc[-p["slow"]:].notna().all()
        above = (closes[alts].iloc[-1] > sma)[ok]
        breadth = float(above.mean()) if len(above) else 1.0
        if not (_btc_below_mean(btc, p["slow"]) and breadth < p["breadth_max"]):
            return self.check(out)
        st["gate_on"] += 1
        ready = closes.iloc[-p["slow"]:].notna().all()
        ef = closes.ewm(span=p["fast"], adjust=False).mean().iloc[-1]
        es = closes.ewm(span=p["slow"], adjust=False).mean().iloc[-1]
        r14 = closes.iloc[-1] / closes.iloc[-1 - p["ret_h"]] - 1
        cand = [c for c in cols if ready[c] and ef[c] < es[c] and r14[c] < p["ret_thr"]]
        for c in sorted(cand, key=lambda c: (r14[c], cols.index(c)))[: int(p["n_short"])]:
            out[c] = -float(p["wa"])
        return self.check(out)


class BreakdownShort(Strategy):
    name = "breakdown_short"
    needs_btc = True
    needs_holdings = True
    needs_volume = True
    DEF = {"n_short": 3, "wa": 0.15, "low_h": 480, "vol_mult": 1.5, "atr_days": 14, "max_days": 14,
           "decision_bar_utc": 14, "select_every_h": 24}

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        p = {**self.DEF, **{k: v for k, v in (cfg or {}).items() if not k.startswith("_")}}
        cols, last = list(closes.columns), closes.index[-1]
        cfg = cfg or {}
        held = cfg.get("_held") or {}
        lvl: dict = self.__dict__.setdefault("levels", {})       # asset -> (stop level, entry time)
        st = self.__dict__.setdefault("stats", {"decisions": 0, "gate_on": 0, "entries": 0, "stops": 0, "timeouts": 0})
        out = _keep(held, cfg.get("_mult", 1.0), cols)
        for c in [c for c in lvl if out.get(c, 0.0) >= 0]:      # position gone (brake / delisting): forget it
            lvl.pop(c)
        for c, (stop, t0) in list(lvl.items()):                    # intraday stop and time limit
            px = closes[c].iloc[-1]
            if px > stop:
                out[c] = 0.0
                lvl.pop(c)
                st["stops"] += 1
            elif last - t0 >= pd.Timedelta(days=int(p["max_days"])):
                out[c] = 0.0
                lvl.pop(c)
                st["timeouts"] += 1
        if not _is_decision(last, p):
            return self.check(out)
        st["decisions"] += 1
        if not _btc_below_mean(cfg.get("_btc")):
            for c in list(lvl):
                out[c] = 0.0
                lvl.pop(c)
            return self.check(out)
        st["gate_on"] += 1
        vol = cfg.get("_volume")
        lh = int(p["low_h"])
        prev_low = closes.iloc[-1 - lh:-1].min()
        ready = closes.iloc[-1 - lh:].notna().all()
        c_now = closes.iloc[-1]
        v24 = vol.iloc[-24:].sum() if vol is not None else pd.Series(0.0, index=cols)
        vavg = vol.iloc[-1 - lh - 24:-24].sum() / (lh / 24) if vol is not None else pd.Series(np.inf, index=cols)
        daily = closes.iloc[::-1].iloc[::24].iloc[::-1]          # one close per 24h, ending at the last bar
        atr = daily.diff().abs().iloc[-int(p["atr_days"]):].mean()
        cand = [c for c in cols if ready[c] and c_now[c] < prev_low[c] and v24[c] > p["vol_mult"] * vavg[c]
                and c not in lvl]
        free = int(p["n_short"]) - len(lvl)
        for c in sorted(cand, key=lambda c: (c_now[c] / prev_low[c], cols.index(c)))[:max(free, 0)]:
            out[c] = -float(p["wa"])
            lvl[c] = (float(prev_low[c] + atr[c]), last)
            st["entries"] += 1
        return self.check(out)


class BetaHedge(Strategy):
    name = "beta_hedge"
    needs_btc = True
    DEF = {"gate": "btc_below_30d", "beta_h": 720, "hedge": ["BTCUSDT", "ETHUSDT"], "beta_cap": 1.0}

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        p = {**self.DEF, **{k: v for k, v in (cfg or {}).items() if not k.startswith("_")}}
        live = sys.modules["live_strategies.xsmom"]
        w = live.xsmom_weights(closes, {**live.DEFAULTS, **{k: v for k, v in p.items() if k in live.DEFAULTS}})
        out = {c: float(w.get(c, 0.0)) for c in closes.columns}
        st = self.__dict__.setdefault("stats", {"decisions": 0, "hedged": 0})
        st["decisions"] += 1
        btc = (cfg or {}).get("_btc")
        if btc is None or len(btc.dropna()) < p["beta_h"] + 1:
            return self.check(out)
        b = btc.dropna()
        gate = (b.iloc[-1] < b.iloc[-720:].mean()) if p["gate"] == "btc_below_30d" else (b.iloc[-1] / b.iloc[-169] - 1 < -0.05)
        longs = {c: v for c, v in out.items() if v > 0}
        hedge = [h for h in p["hedge"] if h in closes.columns and closes[h].iloc[-p["beta_h"]:].notna().all()]
        if not gate or not longs or not hedge:
            return self.check(out)
        r = closes[list(longs)].iloc[-p["beta_h"] - 1:].pct_change(fill_method=None).iloc[1:].fillna(0.0)
        port = (r * pd.Series(longs)).sum(axis=1) / sum(longs.values())
        rb = b.pct_change().reindex(port.index).fillna(0.0)
        beta = float(np.clip(port.cov(rb) / rb.var(), 0.0, p["beta_cap"])) if rb.var() > 0 else 0.0
        size = beta * sum(longs.values())
        for h in hedge:
            out[h] = out.get(h, 0.0) - size / len(hedge)
        st["hedged"] += 1
        return self.check(out)
