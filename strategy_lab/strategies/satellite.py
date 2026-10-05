"""Satellite strategies (research block 2; lab only). Long-only, weights are fractions of the
SATELLITE book (its own capital; combined with the core in lab/combine.py).

Common sizing: each held coin w = (1/k) * min(1, target_vol / vol_i), vol_i = std of hourly
returns over the last 720 bars (30d) x sqrt(8760); per-coin cap `cap` (default 0.5 of the
book = 10% of total equity at a 20% satellite share; 1/k <= 0.25 never reaches it); sum <= 1.
Gate: gate="alt_rally" holds nothing unless the frozen alt_rally flag (lab/alt_rally.py) was on
at the previous UTC day's close.

  sat_breakout  4h bars built from the hourly window (complete groups of 4 from the end).
                Entry: close > highest close of the prior `entry_bars` (20) AND bar volume >
                vol_mult (1.5) x mean volume of the prior 20 bars. Exit: close < lowest close
                of the prior `exit_bars` (10). Sticky top-k: a holding stays until its own
                exit; free slots are filled by entry strength (close / prior high - 1).
                (Re-ranking every bar churned ~5 swaps/day in trials 31-33.)
  sat_trend     S3v2 logic long-only: score = mean sign of 24/72/168/336h returns,
                w = max(score, 0) * min(1, target_vol / vol) / k.
  sat_rs        Daily relative-strength rotation: score = 14d return / (hourly std x
                sqrt(336)); hold the top k with score > 0; a holding stays while its rank
                <= 2k and score > 0 (hysteresis).
Stateless: sticky state is rebuilt by simulating the rule over the window.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any

import numpy as np
import pandas as pd

from lab.strategies import Strategy

COMMON = {"k": 4, "target_vol": 0.8, "cap": 0.5, "gate": None, "vol_bars": 720}


@lru_cache(maxsize=1)
def _alt_flag() -> pd.Series:
    from lab.alt_rally import flag_series
    f = flag_series()
    f.index = pd.DatetimeIndex(f.index).tz_convert("UTC") if f.index.tz else pd.DatetimeIndex(f.index).tz_localize("UTC")
    return f


def gate_open(ts: pd.Timestamp, gate: str | None) -> bool:
    if not gate:
        return True
    if gate != "alt_rally":
        raise ValueError(f"unknown gate {gate!r}")
    return bool(_alt_flag().get(ts.floor("D") - pd.Timedelta(days=1), False))


def size(held: list[str], closes: pd.DataFrame, p: dict[str, Any]) -> dict[str, float]:
    w = {a: 0.0 for a in closes.columns}
    if not held:
        return w
    r = closes[held].pct_change().iloc[-int(p["vol_bars"]):]
    vol = r.std() * np.sqrt(24 * 365)
    k = int(p["k"])
    for a in held:
        v = vol.get(a)
        w[a] = min(float(p["cap"]), (1 / k) * (min(1.0, float(p["target_vol"]) / v) if v and v > 0 else 0.0))
    g = sum(w.values())
    if g > 1:
        w = {a: x / g for a, x in w.items()}
    return w


class SatBreakout(Strategy):
    name = "sat_breakout"
    needs_volume = True

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        p = {**COMMON, "entry_bars": 20, "exit_bars": 10, "vol_mult": 1.5, **(cfg or {})}
        flat = {a: 0.0 for a in closes.columns}
        if not gate_open(closes.index[-1], p["gate"]):
            return self.check(flat)
        vol_in = p.get("_volume")
        if vol_in is None:
            raise ValueError("sat_breakout needs the volume window (_volume)")
        n4 = len(closes) // 4
        ent, ext, k = int(p["entry_bars"]), int(p["exit_bars"]), int(p["k"])
        if n4 < ent + 2:
            raise ValueError("not enough history")
        cols = list(closes.columns)
        c = closes.iloc[-n4 * 4:].values.reshape(n4, 4, -1)[:, -1, :]
        v = vol_in.reindex(columns=cols).iloc[-n4 * 4:].fillna(0).values.reshape(n4, 4, -1).sum(axis=1)
        held: list[int] = []
        for t in range(ent, n4):
            px = c[t]
            prior_hi = np.nanmax(c[t - ent:t], axis=0)
            prior_lo = np.nanmin(c[t - ext:t], axis=0)
            vmean = v[t - ent:t].mean(axis=0)
            held = [j for j in held if not (px[j] < prior_lo[j]) and not np.isnan(px[j])]
            if len(held) < k:
                strength = px / prior_hi - 1
                cand = [j for j in np.argsort(-np.nan_to_num(strength, nan=-np.inf))
                        if j not in held and px[j] > prior_hi[j] and v[t, j] > float(p["vol_mult"]) * vmean[j]]
                held += cand[: k - len(held)]
        return self.check(size([cols[j] for j in held], closes, p))


class SatTrend(Strategy):
    name = "sat_trend"

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        p = {**COMMON, "horizons": [24, 72, 168, 336], **(cfg or {})}
        if not gate_open(closes.index[-1], p["gate"]):
            return self.check({a: 0.0 for a in closes.columns})
        c = closes.dropna(axis=1, how="any")
        hz = [int(h) for h in p["horizons"]]
        if len(c) < max(hz) + 1:
            raise ValueError("not enough history")
        last = c.iloc[-1]
        score = sum(np.sign(last / c.iloc[-1 - h] - 1) for h in hz) / len(hz)
        vol = c.pct_change().iloc[-int(p["vol_bars"]):].std() * np.sqrt(24 * 365)
        k = int(p["k"])
        w = {a: 0.0 for a in closes.columns}
        for a in c.columns:
            if score[a] > 0 and vol[a] > 0:
                w[a] = min(float(p["cap"]), float(score[a]) * min(1.0, float(p["target_vol"]) / vol[a]) / k)
        g = sum(w.values())
        if g > 1:
            w = {a: x / g for a, x in w.items()}
        return self.check(w)


class SatRS(Strategy):
    name = "sat_rs"

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        p = {**COMMON, "lookback": 336, **(cfg or {})}
        if not gate_open(closes.index[-1], p["gate"]):
            return self.check({a: 0.0 for a in closes.columns})
        lb, k = int(p["lookback"]), int(p["k"])
        n = len(closes)
        if n < lb + 2:
            raise ValueError("not enough history")
        held: list[str] = []
        # daily decision points from the oldest usable one to the window end
        for end in range(n - ((n - lb - 1) // 24) * 24, n + 1, 24):
            win = closes.iloc[end - lb - 1:end].dropna(axis=1, how="any")
            if win.shape[1] == 0:
                held = []
                continue
            ret = win.iloc[-1] / win.iloc[0] - 1
            sd = win.pct_change().std() * np.sqrt(lb)
            score = (ret / sd).replace([np.inf, -np.inf], np.nan).dropna().sort_values(ascending=False)
            rank = {a: i + 1 for i, a in enumerate(score.index)}
            held = [a for a in held if a in rank and rank[a] <= 2 * k and score[a] > 0]
            for a in score.index:
                if len(held) >= k:
                    break
                if a not in held and score[a] > 0:
                    held.append(a)
        return self.check(size(held, closes, p))
