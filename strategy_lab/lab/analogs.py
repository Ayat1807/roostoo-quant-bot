"""Analog testing: which past market states look like today, and what happened next?

    python -m lab.analogs [--date 2026-10-04] [--k 30] [--runs s3v2_base,guard_off,...]

Daily features (BTC unless noted), computed point-in-time from daily closes:
  btc_ret_30d, btc_ret_90d      BTC return over 30 / 90 days
  dist_365d_high                close / 365-day max close - 1
  vol30_pct                     percentile of BTC 30-day realised vol vs all history so far
  px_vs_ma14, px_vs_ma30        close / 14-day or 30-day mean - 1
  rally_90d_low                 close / 90-day min close - 1
  alt_breadth                   share of the top-20 coins by trailing 30-day volume
                                (point in time, ex BTC, ex stablecoins/stock tokens) whose
                                30-day return beats BTC's
Distance: Euclidean on z-scored features (z over all dates with complete features).
Analogs: the k nearest dates, at least `min_sep` days apart (greedy by distance),
excluding the last `exclude_last` days, and only dates with 14 days of forward data.
For each analog: BTC's next-14-day return and each strategy run's next-14-day return
(from the run's stored hourly equity, i.e. its real path into that window).
Writes reports/analogs_<date>.md.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from lab import ROOT
from lab.data import load_daily
from lab.runner import load_hourly
from lab.universe import stock_tokens

FEATURES = ["btc_ret_30d", "btc_ret_90d", "dist_365d_high", "vol30_pct", "px_vs_ma14",
            "px_vs_ma30", "rally_90d_low", "alt_breadth"]
DEFAULT_RUNS = ["s3v2_base", "guard_off", "guard_minimal", "guard_band_edge", "p_shorts_off",
                "hold_btc", "hold_ew10"]
REPORTS = ROOT / "reports"


def features() -> pd.DataFrame:
    d = load_daily()
    close, qv = d["close"], d["quote_volume"]
    btc = close["BTCUSDT"].dropna()
    r1 = btc.pct_change()
    vol30 = r1.rolling(30).std()
    f = pd.DataFrame(index=btc.index)
    f["btc_ret_30d"] = btc / btc.shift(30) - 1
    f["btc_ret_90d"] = btc / btc.shift(90) - 1
    f["dist_365d_high"] = btc / btc.rolling(365).max() - 1
    f["vol30_pct"] = vol30.expanding(min_periods=365).rank(pct=True)
    f["px_vs_ma14"] = btc / btc.rolling(14).mean() - 1
    f["px_vs_ma30"] = btc / btc.rolling(30).mean() - 1
    f["rally_90d_low"] = btc / btc.rolling(90).min() - 1
    # alt breadth: top-20 by trailing 30d volume (known at the day's close), ex BTC
    excl = set(stock_tokens()) | {"BTCUSDT"}
    cols = [c for c in close.columns if c not in excl]
    mqv = qv[cols].rolling(30, min_periods=20).mean()
    ret30 = close[cols] / close[cols].shift(30) - 1
    breadth = []
    for day in f.index:
        row = mqv.loc[day].dropna()
        top = row.sort_values(ascending=False).index[:20]
        r = ret30.loc[day, top].dropna()
        breadth.append(float((r > f.loc[day, "btc_ret_30d"]).mean()) if len(r) >= 10 else np.nan)
    f["alt_breadth"] = breadth
    f["btc_close"] = btc
    return f


def find_analogs(f: pd.DataFrame, date: pd.Timestamp, k: int = 30, min_sep: int = 14,
                 exclude_last: int = 30, horizon: int = 14) -> tuple[pd.DataFrame, pd.Series]:
    x = f[FEATURES].dropna()
    z = (x - x.mean()) / x.std()
    if date not in z.index:
        raise ValueError(f"no complete features for {date.date()}")
    target = z.loc[date]
    cand = z[(z.index <= date - pd.Timedelta(days=exclude_last)) &
             (z.index <= f.index[-1] - pd.Timedelta(days=horizon))]
    dist = np.sqrt(((cand - target) ** 2).sum(axis=1)).sort_values()
    picked: list[pd.Timestamp] = []
    for day in dist.index:
        if all(abs((day - p).days) >= min_sep for p in picked):
            picked.append(day)
        if len(picked) == k:
            break
    out = f.loc[picked, FEATURES].copy()
    out.insert(0, "distance", dist.loc[picked].values)
    return out, z.loc[date]


def forward_returns(dates: list[pd.Timestamp], runs: list[str], f: pd.DataFrame,
                    horizon: int = 14) -> pd.DataFrame:
    rows = []
    for day in dates:
        t0, t1 = day + pd.Timedelta(hours=23), day + pd.Timedelta(days=horizon, hours=23)
        row = {"btc_fwd": f["btc_close"].get(day + pd.Timedelta(days=horizon), np.nan) / f["btc_close"].loc[day] - 1}
        for r in runs:
            h = load_hourly(r)
            if h is None or t1 > h.index[-1] or t0 < h.index[0]:
                row[r] = np.nan
                continue
            e = h["equity"]
            row[r] = e.asof(t1) / e.asof(t0) - 1
        rows.append(row)
    return pd.DataFrame(rows, index=dates)


def report(date: str | None, k: int, runs: list[str]) -> Path:
    f = features()
    day = pd.Timestamp(date, tz="UTC") if date else f[FEATURES].dropna().index[-1]
    analogs, zt = find_analogs(f, day, k)
    fwd = forward_returns(list(analogs.index), runs, f)
    tbl = analogs.join(fwd)
    REPORTS.mkdir(exist_ok=True)
    L = [f"# Analog report: market state on {day:%Y-%m-%d}\n",
         f"_{k} nearest historical dates (z-scored Euclidean distance on {len(FEATURES)} daily features, "
         f">= 14 days apart, last 30 days excluded). Next-14-day results per strategy run._\n",
         "## Today's features\n", "| feature | value | z-score |", "|---|---|---|"]
    for c in FEATURES:
        L.append(f"| {c} | {f.loc[day, c]:+.3f} | {zt[c]:+.2f} |")
    L.append("\n## Next-14-day results across the analogs\n")
    L.append("| series | mean | median | % positive | worst | best |")
    L.append("|---|---|---|---|---|---|")
    for c in ["btc_fwd"] + runs:
        s = tbl[c].dropna()
        if len(s):
            L.append(f"| {'BTC price' if c == 'btc_fwd' else c} | {s.mean():+.2%} | {s.median():+.2%} | "
                     f"{(s > 0).mean():.0%} | {s.min():+.2%} | {s.max():+.2%} |")
    L.append("\n## Analog dates (sanity check)\n")
    head = "| date | dist | " + " | ".join(FEATURES) + " | BTC fwd 14d | " + " | ".join(runs) + " |"
    L.append(head)
    L.append("|" + "---|" * (2 + len(FEATURES) + 1 + len(runs)))
    for d0, r in tbl.iterrows():
        L.append(f"| {d0:%Y-%m-%d} | {r['distance']:.2f} | " + " | ".join(f"{r[c]:+.3f}" for c in FEATURES)
                 + f" | {r['btc_fwd']:+.2%} | " + " | ".join(f"{r[c]:+.2%}" if pd.notna(r[c]) else "n/a" for c in runs) + " |")
    path = REPORTS / f"analogs_{day:%Y-%m-%d}.md"
    path.write_text("\n".join(L) + "\n", encoding="utf-8")
    tbl.to_csv(REPORTS / f"analogs_{day:%Y-%m-%d}.csv")
    return path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date")
    ap.add_argument("--k", type=int, default=30)
    ap.add_argument("--runs", default=",".join(DEFAULT_RUNS))
    a = ap.parse_args()
    p = report(a.date, a.k, a.runs.split(","))
    print(p.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
