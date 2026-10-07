"""xsmom_ls: the live xsmom plus long/short and hysteresis research options (block 4c).
Defaults reproduce live xsmom exactly (long only, top 5 x 15%, gross 75%).

  shorts      off | combined. Short-eligible: EMA24 < EMA168 AND 72h momentum < -2% (and 168 ready bars);
              long-eligible as live. All eligible coins ranked together by |score| = |mom72 / vol72|
              (ties by column order); one combined top K (top_n) at +-max_asset_weight each.
  max_shorts  at most N shorts in the book (further shorts are skipped, the next coin fills the slot)
  short_gate  none | btc_below_30d: shorts only while BTC < its 30-day mean (720 hourly closes)
  swap_mult   big_gap_swap hysteresis (None = off, live behaviour). Uses the current book (cfg["_held"]:
              asset -> signed weight, cfg["_held_h"]: asset -> hours held, injected by the backtester):
              a holding still eligible on its side is kept unless it fell out of the top `swap_rank` (8)
              AND a coin not held has |score| >= swap_mult x the holding's |score| AND it was held at least
              min_hold_h (12) hours; then the best such candidate replaces it (worst-ranked holdings first).
              A holding no longer eligible on its side is dropped (as live). Free slots are filled by the
              best-ranked coins not held.
"""

from __future__ import annotations

import sys
from typing import Any

import numpy as np
import pandas as pd

from lab.strategies import Strategy

DEFAULTS: dict[str, Any] = {"shorts": "off", "max_shorts": None, "short_gate": "none", "swap_mult": None,
                            "swap_rank": 8, "min_hold_h": 12}


class XSMomLS(Strategy):
    name = "xsmom_ls"
    needs_btc = True
    needs_holdings = True

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        xs = dict(sys.modules["live_strategies.xsmom"].DEFAULTS)
        p = {**xs, **DEFAULTS, **{k: v for k, v in (cfg or {}).items() if not k.startswith("_")}}
        if not hasattr(self, "stats"):
            self.stats = {"decisions": 0, "swaps": 0, "kept_by_hysteresis": 0, "short_slots": 0}
        self.stats["decisions"] += 1
        held = dict((cfg or {}).get("_held") or {})
        held_h = dict((cfg or {}).get("_held_h") or {})
        btc = (cfg or {}).get("_btc")
        need = max(int(p["slow_ema"]), int(p["momentum_hours"]) + 1, int(p["volatility_hours"]) + 1)
        if len(closes) < need:
            raise ValueError(f"xsmom_ls needs {need} hourly bars, have {len(closes)}")
        prices = closes
        returns = prices.pct_change(fill_method=None)
        last = prices.index[-1]
        fast = prices.ewm(span=int(p["fast_ema"]), adjust=False, min_periods=int(p["fast_ema"])).mean().loc[last]
        slow = prices.ewm(span=int(p["slow_ema"]), adjust=False, min_periods=int(p["slow_ema"])).mean().loc[last]
        mh = int(p["momentum_hours"])
        mom = (prices / prices.shift(mh) - 1.0).loc[last]
        vol = returns.rolling(int(p["volatility_hours"])).std().loc[last]
        ready = prices.rolling(int(p["slow_ema"])).count().eq(int(p["slow_ema"])).loc[last]
        score = mom / vol.replace(0.0, np.nan)
        thr = float(p["momentum_threshold"])
        long_ok = (fast > slow) & (mom > thr) & ready
        short_ok = pd.Series(False, index=prices.columns)
        if p["shorts"] == "combined":
            short_ok = (fast < slow) & (mom < -thr) & ready
            if p["short_gate"] == "btc_below_30d":
                if btc is None or len(btc.dropna()) < 720:
                    raise ValueError("short gate needs >= 720 BTC closes")
                b = btc.dropna()
                if not b.iloc[-1] < b.iloc[-720:].mean():
                    short_ok[:] = False
            elif p["short_gate"] != "none":
                raise ValueError(f"short_gate {p['short_gate']!r}")
        elif p["shorts"] != "off":
            raise ValueError(f"shorts {p['shorts']!r}")
        side = pd.Series(0, index=prices.columns)
        side[long_ok] = 1
        side[short_ok] = -1
        elig = side != 0
        ranked = score.abs().where(elig).rank(ascending=False, method="first")
        order = ranked.dropna().sort_values().index.tolist()          # best first
        K, wa = int(p["top_n"]), float(p["max_asset_weight"])
        max_s = None if p["max_shorts"] is None else int(p["max_shorts"])

        def take(cands: list[str], book: dict[str, int], slots: int) -> None:
            for a in cands:
                if slots <= 0:
                    break
                if a in book:
                    continue
                if side[a] < 0 and max_s is not None and sum(1 for s in book.values() if s < 0) >= max_s:
                    continue
                book[a] = int(side[a])
                slots -= 1

        book: dict[str, int] = {}
        if p["swap_mult"] is None or not held:
            take(order, book, K)
        else:
            m, top_r, min_h = float(p["swap_mult"]), int(p["swap_rank"]), float(p["min_hold_h"])
            keep = {a: int(np.sign(w)) for a, w in held.items()
                    if a in side.index and w != 0 and side[a] == int(np.sign(w))}
            cands = [a for a in order if a not in keep]
            for a in sorted(keep, key=lambda x: -ranked.get(x, np.inf)):      # worst-ranked first
                if ranked[a] <= top_r or held_h.get(a, 0) < min_h:
                    continue
                trial = dict(keep)
                trial.pop(a)
                for c in cands:
                    if abs(score[c]) >= m * abs(score[a]):
                        if side[c] < 0 and max_s is not None and sum(1 for s in trial.values() if s < 0) >= max_s:
                            continue
                        keep = trial
                        keep[c] = int(side[c])
                        self.stats["swaps"] += 1
                        cands.remove(c)
                        break
                    break       # candidates are sorted by |score|: the best one is not good enough
            self.stats["kept_by_hysteresis"] += sum(1 for a in keep if ranked[a] > K)
            book = dict(list(keep.items())[:K])
            take(cands, book, K - len(book))
        self.stats["short_slots"] += sum(1 for v in book.values() if v < 0)
        w = {a: 0.0 for a in prices.columns}
        for a, s in book.items():
            w[a] = s * wa
        if sum(abs(v) for v in w.values()) > float(p["max_risky_exposure"]) + 1e-12:
            raise ValueError("xsmom_ls: gross cap exceeded")
        return self.check(w)
