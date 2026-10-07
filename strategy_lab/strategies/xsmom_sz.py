"""xsmom_sz: the live xsmom (strategy_bot/strategies/xsmom.py) with research options for position
sizing, total exposure and number of coins (block 4b). Same eligibility and ranking as live:
EMA24 > EMA168, 72h momentum > 2%, 168 ready bars, ranked by score = mom72 / vol72 (ties by column
order). Defaults reproduce live xsmom exactly (top 5 x 15%, max gross 75%).

Options (cfg):
  select   topk (top_n coins) | all_eligible (every eligible coin) | breadth_k (K = 3 if <= 3 coins
           qualify, 5 if 4-6, 8 if >= 7)
  top_n    K for topk
  gross    full-slot gross G (default 0.75 = max_risky_exposure)
  sizing   equal | score (~ mom/vol) | inv_vol (~ 1/vol72) | score_x_invvol (~ mom/vol^2)
  coin_cap per-coin cap (None = none; equal sizing in topk is G/K anyway); the excess goes pro rata
           to uncapped coins (water filling), whatever is left stays in cash
  exposure none | breadth | vol_target | regime | conviction (sets G, see below)
Slot rule (as live): the selected coins get G x (n selected / K) in total, so empty slots stay in
cash; equal sizing = G/K per coin; weighted sizing splits that total by the sizing score.
  all_eligible: K = n eligible, per coin min(coin_cap, G / n).
Exposure (G before the slot rule):
  breadth    G = 0.75 x min(1, (eligible share of ready coins) / 0.5)
  vol_target final weights scaled so the ex-ante portfolio vol (covariance of the last 168 hourly
             returns, annualised x sqrt(8760)) = 40%, gross capped at 90%
  regime     G = 0.90 if BTC > its 30-day mean (720 hourly closes) and BTC 14-day return > 0, else 0.50
  conviction G = 0.75 x clip(avg score of the selected coins / median of that average at the same
             hour of day over the previous 365 days, 0.5, 1.2), capped at 0.90 (needs a 1-year
             lookback; < 90 past values -> ratio 1)
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from lab.strategies import Strategy

def _xs_defaults() -> dict[str, Any]:
    import sys
    return dict(sys.modules["live_strategies.xsmom"].DEFAULTS)


DEFAULTS: dict[str, Any] = {"select": "topk", "gross": None, "sizing": "equal", "coin_cap": None,
                            "exposure": "none", "vt_target": 0.40, "vt_window": 168, "vt_cap": 0.90,
                            "regime_hi": 0.90, "regime_lo": 0.50, "conv_lo": 0.5, "conv_hi": 1.2,
                            "conv_cap": 0.90, "conv_days": 365, "conv_min": 90, "breadth_ref": 0.5}


def _cap_fill(x: pd.Series, total: float, cap: float | None) -> pd.Series:
    """Split `total` pro rata to x (x > 0); per-coin cap with water filling."""
    w = x / x.sum() * total
    if cap is None:
        return w
    fixed = pd.Series(False, index=w.index)
    for _ in range(len(w)):
        over = (w > cap + 1e-15) & ~fixed
        if not over.any():
            break
        fixed |= over
        w[fixed] = cap
        rest = total - cap * fixed.sum()
        free = ~fixed
        if rest <= 0 or not free.any():
            break
        w[free] = x[free] / x[free].sum() * rest
    return w.clip(upper=cap)


class XSMomSz(Strategy):
    name = "xsmom_sz"
    needs_btc = True

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        p = {**_xs_defaults(), **DEFAULTS, **{k: v for k, v in (cfg or {}).items() if not k.startswith("_")}}
        btc = (cfg or {}).get("_btc")
        need = max(int(p["slow_ema"]), int(p["momentum_hours"]) + 1, int(p["volatility_hours"]) + 1)
        if len(closes) < need:
            raise ValueError(f"xsmom_sz needs {need} hourly bars, have {len(closes)}")
        prices = closes
        returns = prices.pct_change(fill_method=None)
        fast = prices.ewm(span=int(p["fast_ema"]), adjust=False, min_periods=int(p["fast_ema"])).mean()
        slow = prices.ewm(span=int(p["slow_ema"]), adjust=False, min_periods=int(p["slow_ema"])).mean()
        mh = int(p["momentum_hours"])
        momentum = prices / prices.shift(mh) - 1.0
        vol = returns.rolling(int(p["volatility_hours"])).std()
        ready = prices.rolling(int(p["slow_ema"])).count().eq(int(p["slow_ema"]))
        score = momentum / vol.replace(0.0, np.nan)
        elig_m = (fast > slow) & (momentum > float(p["momentum_threshold"])) & ready
        last = prices.index[-1]
        elig = elig_m.loc[last]
        ranked = score.loc[last].where(elig).rank(ascending=False, method="first")
        n_el = int(elig.sum())
        G = float(p["gross"] if p["gross"] is not None else p["max_risky_exposure"])
        if p["select"] == "topk":
            K = int(p["top_n"])
        elif p["select"] == "breadth_k":
            K = 3 if n_el <= 3 else (5 if n_el <= 6 else 8)
        elif p["select"] == "all_eligible":
            K = max(n_el, 1)
        else:
            raise ValueError(f"select {p['select']!r}")
        sel = ranked[ranked <= K].sort_values().index.tolist()
        w = pd.Series(0.0, index=prices.columns)
        if not sel:
            return self.check({k: 0.0 for k in prices.columns})
        # exposure rule -> G
        ex = p["exposure"]
        if ex == "breadth":
            n_ready = int(ready.loc[last].sum())
            share = n_el / n_ready if n_ready else 0.0
            G = G * min(1.0, share / float(p["breadth_ref"]))
        elif ex == "regime":
            if btc is None or len(btc.dropna()) < 721:
                raise ValueError("regime exposure needs >= 721 BTC closes")
            b = btc.dropna()
            up = b.iloc[-1] > b.iloc[-720:].mean() and b.iloc[-1] / b.iloc[-337] - 1 > 0
            G = float(p["regime_hi"] if up else p["regime_lo"])
        elif ex == "conviction":
            G = min(float(p["conv_cap"]), G * self._conviction(score, elig_m, K, last, p))
        elif ex not in ("none", "vol_target"):
            raise ValueError(f"exposure {ex!r}")
        # sizing within the selected coins (slot rule)
        s = score.loc[last, sel]
        v = vol.loc[last, sel]
        if p["select"] == "all_eligible":
            per = G / len(sel)
            cap = p["coin_cap"]
            w[sel] = min(per, float(cap)) if cap is not None else per
        else:
            total = G * len(sel) / K
            x = {"equal": pd.Series(1.0, index=sel), "score": s, "inv_vol": 1.0 / v,
                 "score_x_invvol": s / v}[p["sizing"]]
            cap = None if p["coin_cap"] is None else float(p["coin_cap"])
            w[sel] = _cap_fill(x.astype(float), total, cap) if p["sizing"] != "equal" else \
                (min(G / K, cap) if cap is not None else G / K)
        if ex == "vol_target":
            r = returns[sel].iloc[-int(p["vt_window"]):].fillna(0.0)
            cov = r.cov().values * 8760
            ws = w[sel].values
            sig = float(np.sqrt(max(ws @ cov @ ws, 0.0)))
            if sig > 0:
                k = min(float(p["vt_target"]) / sig, float(p["vt_cap"]) / ws.sum())
                w[sel] = ws * k
        if w.sum() > 1 + 1e-12:
            w = w / w.sum()
        return self.check({k: float(x) for k, x in w.items()})

    @staticmethod
    def _conviction(score, elig_m, K, last, p) -> float:
        """avg score of the selected coins now / its median at the same hour over the past year."""
        rows = score.index[(score.index.hour == last.hour) & (score.index < last)
                           & (score.index >= last - pd.Timedelta(days=int(p["conv_days"])))]
        sc = score.where(elig_m)

        def avg_top(t) -> float:
            r = sc.loc[t].dropna().sort_values(ascending=False, kind="stable")
            return float(r.iloc[:K].mean()) if len(r) else np.nan

        now = avg_top(last)
        hist = pd.Series([avg_top(t) for t in rows], dtype=float).dropna()
        if len(hist) < int(p["conv_min"]) or not np.isfinite(now) or hist.median() <= 0:
            return 1.0
        return float(np.clip(now / hist.median(), float(p["conv_lo"]), float(p["conv_hi"])))
