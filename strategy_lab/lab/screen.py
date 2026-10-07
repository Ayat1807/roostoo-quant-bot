"""Block 6 track E: per-coin point-in-time statistics and screening persistence (reports/screen_track_e.md).

    python -m lab.screen

Pool: Roostoo crypto pairs with Binance daily history, >= 180 days of history and 30d mean volume >= $10M on the selection
day (as the TREND rule). For each month start (selection day = previous day), from the previous 180 days of daily log returns:
VR(3), VR(7), VR(14) (overlapping q-day vs 1-day variance), Hurst ~ 0.5 + 0.5 log(VR(14)) / log(14), lag-1 autocorrelation,
BTC beta, vol stability (std / mean of the rolling 30d vol), 30d mean volume. Screened = VR(7) > 1 and AC1 > 0.
Persistence: VR(7) over the NEXT 90 days (after the selection day, no overlap) > 1, screened vs not screened, per half.
"""

from __future__ import annotations

import sys

import numpy as np
import pandas as pd

from lab import ROOT
from lab.b3 import IS_END, OOS0, OOS_END
from lab.universe import Universe, _daily, stock_tokens


def vr(x: pd.Series, q: int) -> float:
    x = x.dropna()
    if len(x) < 60 or x.var() == 0:
        return np.nan
    return float(x.rolling(q).sum().var() / (q * x.var()))


def main() -> int:
    d = _daily()
    close, qv = d["close"], d["quote_volume"]
    u = Universe({"type": "satellite", "rule": "TREND", "n_liquid": 10})
    stocks = set(stock_tokens())
    pool = [a for a in close.columns if "~" not in a and a in u._roostoo and a not in stocks]
    lr = np.log(close[pool + ["BTCUSDT"] if "BTCUSDT" not in pool else pool]).diff()
    mqv = qv[pool].rolling(30, min_periods=30).mean()
    hist = close[pool].notna().cumsum()
    rows = []
    for ms in pd.date_range("2020-08-01", "2026-04-01", freq="MS", tz="UTC"):
        prev = ms - pd.Timedelta(days=1)
        if prev not in close.index:
            continue
        past = lr.loc[prev - pd.Timedelta(days=179):prev]
        fut = lr.loc[ms:ms + pd.Timedelta(days=89)]
        btc = past["BTCUSDT"]
        for a in pool:
            if hist.at[prev, a] < 180 or not (mqv.at[prev, a] >= 1e7):
                continue
            x = past[a]
            v7 = vr(x, 7)
            ac = float(x.autocorr(1)) if x.dropna().size > 60 else np.nan
            vol30 = x.rolling(30).std()
            v14 = vr(x, 14)
            rows.append({"month": ms, "asset": a, "vr3": vr(x, 3), "vr7": v7, "vr14": v14,
                         "hurst": 0.5 + 0.5 * np.log(v14) / np.log(14) if v14 and v14 > 0 else np.nan, "ac1": ac,
                         "beta": float(x.cov(btc) / btc.var()) if btc.var() > 0 else np.nan,
                         "vol_stab": float(vol30.std() / vol30.mean()) if vol30.mean() > 0 else np.nan,
                         "vol30_usd": float(mqv.at[prev, a]),
                         "screened": bool(v7 > 1 and ac > 0), "vr7_next90": vr(fut[a], 7)})
    df = pd.DataFrame(rows)
    df["persist"] = df["vr7_next90"] > 1
    L = ["# Track E: per-coin point-in-time statistics and screening persistence\n",
         f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by `python -m lab.screen`. Screened = VR(7d) > 1 and lag-1 "
         "autocorrelation > 0 over the previous 180 days (rule TREND). Persistence = VR(7d) > 1 over the next 90 days._\n",
         "## Does the screen persist out of sample?\n",
         "| period | coin-months screened / not | P(VR7 next 90d > 1): screened | not screened | difference |", "|---|---|---|---|---|"]
    for k, (a, b) in {"IS (to 2024-12)": (None, IS_END), "OOS (2025-01 to 2026-04 selections)": (OOS0, OOS_END)}.items():
        x = df[(df["month"] >= (a or df["month"].min())) & (df["month"] <= b)].dropna(subset=["vr7_next90"])
        s, n = x[x["screened"]], x[~x["screened"]]
        L.append(f"| {k} | {len(s)} / {len(n)} | {s['persist'].mean():.0%} | {n['persist'].mean():.0%} | "
                 f"{s['persist'].mean() - n['persist'].mean():+.0%} |")
    L += ["\n## Average point-in-time stats: screened vs not screened (all months)\n",
          "| group | VR3 | VR7 | VR14 | Hurst | AC1 | BTC beta | vol stability | 30d volume |", "|---|---|---|---|---|---|---|---|---|"]
    for g, x in df.groupby("screened"):
        L.append(f"| {'screened' if g else 'not screened'} | {x.vr3.mean():.2f} | {x.vr7.mean():.2f} | {x.vr14.mean():.2f} | "
                 f"{x.hurst.mean():.2f} | {x.ac1.mean():+.3f} | {x.beta.mean():.2f} | {x.vol_stab.mean():.2f} | "
                 f"${x.vol30_usd.median() / 1e6:,.0f}M |")
    last = df[df["month"] == df["month"].max()].sort_values("vol30_usd", ascending=False)
    L += [f"\n## Latest selection ({last['month'].max():%Y-%m}), top 20 by volume\n",
          "| coin | screened | VR7 | AC1 | Hurst | BTC beta | 30d volume |", "|---|---|---|---|---|---|---|"]
    for _, r in last.head(20).iterrows():
        L.append(f"| {r.asset} | {'yes' if r.screened else ''} | {r.vr7:.2f} | {r.ac1:+.3f} | {r.hurst:.2f} | {r.beta:.2f} | "
                 f"${r.vol30_usd / 1e6:,.0f}M |")
    (ROOT / "reports" / "screen_track_e.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L[3:7]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
