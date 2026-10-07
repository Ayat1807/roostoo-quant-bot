"""xsmom_lsx: long/short xsmom with intraday re-evaluation (block 4c, variants_b4c_lsx.yaml).

Eligibility (on hourly closes, as live): long = EMA24 > EMA168 AND 72h momentum > +2%; short = EMA24 < EMA168
AND 72h momentum < -2%; both need 168 ready bars. score(w) = w x (mom24 / vol24) + (1 - w) x (mom72 / vol72),
vol = std of the last 24 / 72 hourly returns. Longs ranked by score desc, shorts by score asc (ties: column order).

Daily decision (the 14:00 UTC bar, wall clock 15:00): full re-selection: up to `n_long` (5) longs and up to
`n_short` (S) shorts at `wa` (15%) each, only eligible coins (shorts only if the gate allows); total gross capped
at G (all scaled down equally). min_positions = 1: if nothing is eligible, hold the single strongest |score| coin
(ready, direction allowed by the gate) at wa / 2 in its direction.

Checks (every `check_h` hours between daily decisions; the backtest calls target_weights at each refresh with
the current book in cfg["_held"] / cfg["_held_h"] and the brake multiplier in cfg["_mult"]):
  exit   a holding that fails its own side's eligibility is closed
  flip   a coin closed by `exit` that now ranks in the top S shorts (top 5 longs) opens the reverse position if
         that side has a free slot, or replaces that side's weakest holding if |score| >= m x the weakest's |score|
         and the weakest was held >= min_hold_h
  swap   per side, the weakest holding is replaced by the best non-held candidate of that side if the candidate's
         |score| >= m x the holding's |score| AND the holding ranks outside the top (K + 2) of its side (K = 5 / S)
         AND it was held >= min_hold_h (repeated while the rule holds)
  free slots stay empty until the next daily decision; a coin closed at a check cannot be re-entered (any side)
  for one full interval (check_h hours); unchanged holdings keep their current weight (no resizing between
  daily decisions); new positions get wa, reduced so that the gross stays <= G.
Defaults (shorts off via n_short 0, no checks) reproduce live xsmom.
"""

from __future__ import annotations

import sys
from typing import Any

import numpy as np
import pandas as pd

from lab.strategies import Strategy

DEFAULTS: dict[str, Any] = {"n_long": 5, "n_short": 0, "wa": 0.15, "gross_cap": 0.75, "short_gate": "none",
                            "w": 0.0, "min_positions": 0, "check_h": None, "swap_m": 1.5, "min_hold_h": 6,
                            "decision_bar_utc": 14}


class XSMomLSX(Strategy):
    name = "xsmom_lsx"
    needs_btc = True
    needs_holdings = True

    def _stat(self, k: str, n: int = 1) -> None:
        if not hasattr(self, "stats"):
            self.stats = {"daily": 0, "checks": 0, "exits": 0, "flips": 0, "swaps": 0, "fallback_min_pos": 0,
                          "short_slots_daily": 0}
        self.stats[k] = self.stats.get(k, 0) + n

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        xs = dict(sys.modules["live_strategies.xsmom"].DEFAULTS)
        p = {**xs, **DEFAULTS, **{k: v for k, v in (cfg or {}).items() if not k.startswith("_")}}
        cfg = cfg or {}
        need = max(int(p["slow_ema"]), int(p["momentum_hours"]) + 1, int(p["volatility_hours"]) + 1)
        if len(closes) < need:
            raise ValueError(f"xsmom_lsx needs {need} hourly bars, have {len(closes)}")
        prices, last = closes, closes.index[-1]
        if not hasattr(self, "cool"):
            self.cool: dict[str, pd.Timestamp] = {}
        rets = prices.pct_change(fill_method=None)
        fast = prices.ewm(span=int(p["fast_ema"]), adjust=False, min_periods=int(p["fast_ema"])).mean().loc[last]
        slow = prices.ewm(span=int(p["slow_ema"]), adjust=False, min_periods=int(p["slow_ema"])).mean().loc[last]
        m72 = (prices / prices.shift(72) - 1.0).loc[last]
        v72 = rets.iloc[-72:].std()
        ready = prices.iloc[-int(p["slow_ema"]):].notna().all()
        thr = float(p["momentum_threshold"])
        w = float(p["w"])
        s72 = m72 / v72.replace(0.0, np.nan)
        if w:
            m24 = (prices / prices.shift(24) - 1.0).loc[last]
            v24 = rets.iloc[-24:].std()
            score = w * (m24 / v24.replace(0.0, np.nan)) + (1 - w) * s72
        else:
            score = s72
        cols = list(prices.columns)
        long_ok = (fast > slow) & (m72 > thr) & ready & score.notna()
        short_ok = (fast < slow) & (m72 < -thr) & ready & score.notna()
        gate_ok = True
        if p["short_gate"] == "btc_below_30d":
            b = cfg.get("_btc")
            if b is None or len(b.dropna()) < 720:
                raise ValueError("short gate needs >= 720 BTC closes")
            b = b.dropna()
            gate_ok = bool(b.iloc[-1] < b.iloc[-720:].mean())
        elif p["short_gate"] != "none":
            raise ValueError(f"short_gate {p['short_gate']!r}")
        if not gate_ok or int(p["n_short"]) == 0:
            short_ok[:] = False
        pos = {c: i for i, c in enumerate(cols)}
        L = sorted([c for c in cols if long_ok[c]], key=lambda c: (-score[c], pos[c]))
        S = sorted([c for c in cols if short_ok[c]], key=lambda c: (score[c], pos[c]))
        nL, nS, wa, G = int(p["n_long"]), int(p["n_short"]), float(p["wa"]), float(p["gross_cap"])
        cooling = {a for a, t in self.cool.items() if t > last}
        daily = last.hour == int(p["decision_bar_utc"]) and last.minute == 0
        held = {a: v for a, v in (cfg.get("_held") or {}).items() if a in pos}
        mult = float(cfg.get("_mult", 1.0)) or 1.0

        if daily or p["check_h"] is None:
            self._stat("daily")
            book = {a: 1 for a in [c for c in L if c not in cooling][:nL]}
            book.update({a: -1 for a in [c for c in S if c not in cooling][:nS]})
            self._stat("short_slots_daily", sum(1 for v in book.values() if v < 0))
            out = {c: 0.0 for c in cols}
            if not book and int(p["min_positions"]) >= 1:
                cand = [c for c in cols if ready[c] and pd.notna(score[c]) and (score[c] > 0 or (gate_ok and nS > 0))
                        and c not in cooling]
                if cand:
                    best = max(cand, key=lambda c: (abs(score[c]), -pos[c]))
                    out[best] = float(np.sign(score[best])) * wa / 2
                    self._stat("fallback_min_pos")
                return self.check(out)
            for a, s in book.items():
                out[a] = s * wa
            g = sum(abs(v) for v in out.values())
            if g > G:
                out = {a: v * G / g for a, v in out.items()}
            return self.check(out)

        # ---- intraday check -------------------------------------------------------------------- #
        self._stat("checks")
        check_h = float(p["check_h"])
        m, min_h = float(p["swap_m"]), float(p["min_hold_h"])
        hh = cfg.get("_held_h") or {}
        cur = {a: v / mult for a, v in held.items()}          # weights before the brake multiplier
        side = {a: (1 if v > 0 else -1) for a, v in cur.items()}
        closed: set[str] = set()
        old_side = dict(side)
        for a, s in list(side.items()):                     # exit: fails its own eligibility
            if (s > 0 and not long_ok[a]) or (s < 0 and not short_ok[a]):
                closed.add(a)
                side.pop(a)
                self._stat("exits")
        new: set[str] = set()
        lists = {1: L, -1: S}
        caps = {1: nL, -1: nS}

        def weakest(sd: int) -> str | None:
            hs = [a for a, s in side.items() if s == sd]
            return min(hs, key=lambda a: (abs(score[a]) if pd.notna(score[a]) else 0.0, -pos[a])) if hs else None

        for a in sorted(closed, key=lambda c: pos[c]):     # flip
            sd = -old_side[a]                               # reverse direction only
            if caps[sd] == 0 or a not in lists[sd][:caps[sd]]:
                continue
            if sum(1 for s in side.values() if s == sd) < caps[sd]:
                side[a] = sd
            else:
                wk = weakest(sd)
                if wk is None or hh.get(wk, 0) < min_h or abs(score[a]) < m * abs(score[wk]):
                    continue
                side.pop(wk)
                closed.add(wk)
                side[a] = sd
            new.add(a)
            closed.discard(a)
            self._stat("flips")
        for sd in (1, -1):                                  # swap
            K = caps[sd]
            top = lists[sd][:K + 2]
            while True:
                wk = weakest(sd)
                if wk is None or wk in top or hh.get(wk, 0) < min_h:
                    break
                cand = [c for c in lists[sd] if c not in side and c not in cooling and c not in closed]
                if not cand or abs(score[cand[0]]) < m * abs(score[wk]):
                    break
                side.pop(wk)
                closed.add(wk)
                side[cand[0]] = sd
                new.add(cand[0])
                self._stat("swaps")
        for a in closed:
            self.cool[a] = last + pd.Timedelta(hours=check_h)
        out = {c: 0.0 for c in cols}
        for a, s in side.items():
            out[a] = cur[a] if a in cur and a not in new else 0.0
        kept = sum(abs(v) for v in out.values())
        if new:
            each = min(wa, max(G - kept, 0.0) / len(new))
            for a in new:
                out[a] = side[a] * each
        return self.check(out)
