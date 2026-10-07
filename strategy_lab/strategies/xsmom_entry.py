"""xsmom_entry: live xsmom with entry-timing filters (block 4d, variants_b4d_entry.yaml).

Ranking and eligibility exactly as live (EMA24 > EMA168, mom72 > 2%, 168 ready bars, score mom72 / vol72, top 5 x 15%).
Walking down the ranking, a coin already held (cfg["_held"], injected by the backtester) is kept as live; a coin NOT
held (a new entry) must also pass the filter, else it is skipped and the next ranked eligible coin is considered:
  pullback       last-24h return <= 0
  not_extended   close <= (1 + ext) x the lowest close of the last 72h  (ext 6% or 10%)
  resistance     NOT (H x (1 - 1.5%) <= close < H and touches >= 2), H = highest close of the last 720h; a touch = a
                 run of hourly closes >= H x (1 - 0.5%); runs closer than 24h count as one touch
  none           live behaviour (patient_limit is an execution option in the backtester, entry_limit)
"""

from __future__ import annotations

import sys
from typing import Any

import numpy as np
import pandas as pd

from lab.strategies import Strategy

DEFAULTS = {"entry_filter": "none", "ext": 0.06, "res_band": 0.015, "touch_band": 0.005, "res_hours": 720,
            "touch_gap_h": 24, "min_touches": 2}


class XSMomEntry(Strategy):
    name = "xsmom_entry"
    needs_holdings = True

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        xs = sys.modules["live_strategies.xsmom"]
        p = {**xs.DEFAULTS, **DEFAULTS, **{k: v for k, v in (cfg or {}).items() if not k.startswith("_")}}
        held = {a for a, v in ((cfg or {}).get("_held") or {}).items() if v > 0}
        prices = closes
        need = max(int(p["slow_ema"]), int(p["momentum_hours"]) + 1, int(p["volatility_hours"]) + 1)
        if len(prices) < need:
            raise ValueError(f"xsmom_entry needs {need} hourly bars, have {len(prices)}")
        rets = prices.pct_change(fill_method=None)
        last = prices.index[-1]
        fast = prices.ewm(span=int(p["fast_ema"]), adjust=False, min_periods=int(p["fast_ema"])).mean().loc[last]
        slow = prices.ewm(span=int(p["slow_ema"]), adjust=False, min_periods=int(p["slow_ema"])).mean().loc[last]
        mh = int(p["momentum_hours"])
        mom = prices.iloc[-1] / prices.iloc[-1 - mh] - 1.0
        vol = rets.iloc[-int(p["volatility_hours"]):].std()
        ready = prices.iloc[-int(p["slow_ema"]):].notna().all()
        score = mom / vol.replace(0.0, np.nan)
        elig = (fast > slow) & (mom > float(p["momentum_threshold"])) & ready
        ranked = score.where(elig).rank(ascending=False, method="first").dropna().sort_values().index.tolist()
        f = p["entry_filter"]
        if not hasattr(self, "stats"):
            self.stats = {"decisions": 0, "skipped_new": 0, "new_entries": 0}
        self.stats["decisions"] += 1
        pick: list[str] = []
        for a in ranked:
            if len(pick) >= int(p["top_n"]):
                break
            if a not in held and f != "none" and not self._ok(prices[a], f, p):
                self.stats["skipped_new"] += 1
                continue
            if a not in held:
                self.stats["new_entries"] += 1
            pick.append(a)
        w = {a: 0.0 for a in prices.columns}
        for a in pick:
            w[a] = float(p["max_asset_weight"])
        return self.check(w)

    @staticmethod
    def _ok(s: pd.Series, f: str, p: dict) -> bool:
        c = float(s.iloc[-1])
        if f == "pullback":
            return c / float(s.iloc[-25]) - 1 <= 0
        if f == "not_extended":
            return c <= (1 + float(p["ext"])) * float(s.iloc[-72:].min())
        if f == "resistance":
            win = s.iloc[-int(p["res_hours"]):]
            H = float(win.max())
            if not (H * (1 - float(p["res_band"])) <= c < H):
                return True
            near = np.where(win.values >= H * (1 - float(p["touch_band"])))[0]
            touches = 1 + int((np.diff(near) > int(p["touch_gap_h"])).sum()) if len(near) else 0
            return touches < int(p["min_touches"])
        raise ValueError(f"entry_filter {f!r}")
