"""s3v2x: S3v2 with two research knobs (lab only; identical to live s3v2 by default).

  n_divisor: null -> divide by N = number of pairs (live s3v2); an int (e.g. 10) keeps
             per-coin sizing fixed as the universe widens (20-30 coins).
  parking_asset: e.g. PAXGUSDT. Capital not allocated by the signal (1 - gross) is put
             into this asset (x parking_frac) instead of USD. It is excluded from the
             signal and the vol/N computation. PAXG = tokenised gold, listed on Roostoo.
  signal:    "sign" (live), "ema_ensemble" (block 6 A2: mean of sign(EMA fast - EMA slow) over ema_pairs) or "tstat": per horizon t = r_h / (sigma_bar * sqrt(h)), score_h =
             clip(t, -tstat_cap, tstat_cap) / tstat_cap (s3v2_smooth).
  vol_method: "std" (live: std of the last vol_win bar returns) or "ewma" (EWMA std,
             halflife ewma_halflife bars; s3v2_ewma_vol).
  no_trade:  list of columns used as signal inputs only (e.g. BTCUSDT as the regime filter
             on a universe without BTC): their weight is set to 0 after sizing.
  bars_per_year: vol annualisation; 8760 for hourly bars (live), 17520 for 30m bars
             (s3v2_fast: horizons/vol_win/regime_win are then counted in 30m bars).
  max_gross: gross cap (default 1.0 = live). floor_breadth / floor_gross (block 8 U6): when at least floor_breadth coins
             share the same signal sign and the gross is below floor_gross, all weights are scaled up proportionally to
             floor_gross (per-coin cap max_w still applies; default off).
Verified equal to s3v2 with defaults by tests/test_strategies.py.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from lab.strategies import Strategy, live

DEFAULTS = {**live.s3v2.DEFAULTS, "n_divisor": None, "parking_asset": None, "parking_frac": 1.0,
            "bars_per_year": 24 * 365, "signal": "sign", "tstat_cap": 2.0,
            "vol_method": "std", "ewma_halflife": 168,
            "no_trade": [], "max_gross": 1.0, "floor_breadth": None, "floor_gross": 0.5}


class S3v2x(Strategy):
    name = "s3v2x"

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        p = {**DEFAULTS, **(cfg or {})}
        park = p["parking_asset"]
        sig_cols = [c for c in closes.columns if c != park]
        c = closes[sig_cols].dropna(axis=1, how="any")
        horizons = tuple(p["horizons"])
        need = max(max(horizons), int(p["vol_win"]), int(p["regime_win"])) + 1
        if len(c) < need:
            raise ValueError(f"need {need} bars, have {len(c)}")
        last = c.iloc[-1]
        ret = c.pct_change()
        if p["signal"] == "tstat":
            sd = ret.iloc[-int(p["vol_win"]):].std()
            cap = float(p["tstat_cap"])
            sig = sum((np.log(last / c.iloc[-1 - h]) / (sd * np.sqrt(h))).clip(-cap, cap) / cap
                      for h in horizons) / len(horizons)
        elif p["signal"] == "ema_ensemble":      # block 6 A2: equal-weight vote of EMA crossovers (spans in bars)
            pairs = p.get("ema_pairs") or [[8, 24], [24, 96], [48, 192], [96, 384]]
            sig = sum(np.sign(c.ewm(span=f, adjust=False).mean().iloc[-1] - c.ewm(span=s_, adjust=False).mean().iloc[-1])
                      for f, s_ in pairs) / len(pairs)
        else:
            sig = sum(np.sign(last / c.iloc[-1 - h] - 1) for h in horizons) / len(horizons)
        if p["vol_method"] == "ewma":
            rv = ret.ewm(halflife=float(p["ewma_halflife"])).std().iloc[-1] * np.sqrt(float(p["bars_per_year"]))
        else:
            rv = ret.iloc[-int(p["vol_win"]):].std() * np.sqrt(float(p["bars_per_year"]))
        n = int(p["n_divisor"]) if p["n_divisor"] else len(c.columns)
        raw = sig * (float(p["target_vol"]) / rv) / n
        btc = c[p["btc_pair"]]
        bull = btc.iloc[-1] > btc.iloc[-int(p["regime_win"]):].mean()
        raw = raw.where(raw >= 0, raw * (float(p["short_scale_bull"]) if bull else 1.0))
        raw = raw.clip(-float(p["max_w"]), float(p["max_w"]))
        if p["floor_breadth"] is not None:       # block 8 U6: exposure floor when most coins trend the same way
            sg = np.sign(sig)
            agree = max(int((sg > 0).sum()), int((sg < 0).sum()))
            g0 = float(raw.abs().sum())
            if agree >= int(p["floor_breadth"]) and 0 < g0 < float(p["floor_gross"]):
                raw = (raw * float(p["floor_gross"]) / g0).clip(-float(p["max_w"]), float(p["max_w"]))
                self.__dict__.setdefault("stats", {"floor_fired": 0, "decisions": 0})["floor_fired"] += 1
            self.__dict__.setdefault("stats", {"floor_fired": 0, "decisions": 0})["decisions"] += 1
        g = raw.abs().sum()
        cap = min(1.0, float(p["max_gross"]))
        if g > cap:
            raw = raw / g * cap
        w = raw.reindex(closes.columns).fillna(0.0)
        for a in p["no_trade"] or []:
            if a in w.index:
                w[a] = 0.0
        if park and park in closes.columns and pd.notna(closes[park].iloc[-1]):
            w[park] = float(p["parking_frac"]) * max(0.0, 1.0 - float(raw.abs().sum()))
        return self.check({k: float(v) for k, v in w.items()})
