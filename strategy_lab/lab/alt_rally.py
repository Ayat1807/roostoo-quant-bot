"""alt_rally: a point-in-time "broad alt rally" flag. Definition FROZEN 2026-10-05, before any
satellite test (team spec, research block 2). Do not edit the rule; add a new indicator instead.

    python -m lab.alt_rally          # writes reports/alt_rally.csv and reports/alt_rally.md

Daily, from UTC daily closes / quote volumes (data.binance.vision, delisted included), using
only data up to and including day d (known at d's close, 00:00 UTC of d+1):
  pool_d   = top 50 alts by mean daily quote volume over days d-29..d, among Binance USDT
             assets that are not BTC, not stablecoins/fiat/leveraged (excluded at download),
             not tokenised stocks, with >= 60 daily closes of history
  share_d  = fraction of pool_d whose 30d return (close_d / close_{d-30} - 1) beats BTC's
  flag_d   = share_d > 0.60  AND  BTC close_d > mean(BTC close d-29..d)  AND  share_d > share_{d-7}
Trading use: flag_d gates positions on day d+1 (no look-ahead).
Episodes: a start date is a day with flag on and flag off the day before; a start less than
14 days after the previous episode's start is merged into it. Independent episodes = merged
starts. Episodes from 2026-07-01 are the final-exam holdout and are listed separately.
"""

from __future__ import annotations

import sys

import numpy as np
import pandas as pd

from lab import ROOT
from lab.data import load_daily
from lab.universe import stock_tokens

TOP_N, MIN_HIST, SHARE_MIN, RISE_LAG, MERGE_DAYS = 50, 60, 0.60, 7, 14
HOLDOUT = pd.Timestamp("2026-07-01", tz="UTC")
CSV = ROOT / "reports" / "alt_rally.csv"


def compute() -> pd.DataFrame:
    d = load_daily()
    close, qv = d["close"], d["quote_volume"]
    btc = close["BTCUSDT"]
    cols = [c for c in close.columns if c != "BTCUSDT" and c not in set(stock_tokens())]
    hist = close[cols].notna().cumsum()
    mqv = qv[cols].rolling(30, min_periods=30).mean()
    ret30 = close[cols] / close[cols].shift(30) - 1
    btc30 = btc / btc.shift(30) - 1
    btc_ma30 = btc.rolling(30).mean()
    rows = []
    for day in close.index:
        ok = (hist.loc[day] >= MIN_HIST) & mqv.loc[day].notna() & ret30.loc[day].notna()
        pool = mqv.loc[day][ok].sort_values(ascending=False).index[:TOP_N]
        if len(pool) < TOP_N or pd.isna(btc30.get(day)):
            rows.append({"date": day, "share": np.nan, "pool": len(pool)})
            continue
        share = float((ret30.loc[day, pool] > btc30.loc[day]).mean())
        rows.append({"date": day, "share": share, "pool": len(pool),
                     "btc_above_ma30": bool(btc.loc[day] > btc_ma30.loc[day])})
    f = pd.DataFrame(rows).set_index("date")
    f["rising"] = f["share"] > f["share"].shift(RISE_LAG)
    f["flag"] = (f["share"] > SHARE_MIN) & f["btc_above_ma30"].fillna(False).astype(bool) & f["rising"]
    return f


def episodes(flag: pd.Series) -> pd.DataFrame:
    starts = flag.index[flag & ~flag.shift(1, fill_value=False)]
    eps: list[dict] = []
    for s in starts:
        if eps and (s - eps[-1]["start"]).days < MERGE_DAYS:
            eps[-1]["merged_starts"] += 1
            continue
        eps.append({"start": s, "merged_starts": 1})
    e = pd.DataFrame(eps)
    if not e.empty:
        e["flag_days_next_14"] = [int(flag.loc[s:s + pd.Timedelta(days=13)].sum()) for s in e.start]
        e["holdout"] = e.start >= HOLDOUT
    return e


def flag_series() -> pd.Series:
    """Daily flag (index = UTC day d, value known at d's close; use it on day d+1)."""
    f = pd.read_csv(CSV, index_col=0, parse_dates=True)
    return f["flag"].astype(bool)


def main() -> int:
    f = compute()
    CSV.parent.mkdir(exist_ok=True)
    f.to_csv(CSV)
    flag = f["flag"].fillna(False).astype(bool)
    e = episodes(flag)
    raw_starts = int((flag & ~flag.shift(1, fill_value=False)).sum())
    pre = e[~e.holdout] if not e.empty else e
    L = ["# alt_rally episodes\n", (__doc__ or "").split("\n\n")[1].strip() + "\n",
         f"- days with a valid flag: {int(f.share.notna().sum())} ({f.share.first_valid_index():%Y-%m-%d} -> "
         f"{f.index[-1]:%Y-%m-%d}); flag on {flag.mean():.1%} of days",
         f"- raw start dates: {raw_starts}; after merging starts < {MERGE_DAYS}d apart: **{len(e)} independent "
         f"episodes** ({len(pre)} before the 2026-07-01 holdout)\n",
         "| # | start | merged starts | flag days in next 14 | holdout |", "|---|---|---|---|---|"]
    for i, r in e.iterrows():
        L.append(f"| {i + 1} | {r.start:%Y-%m-%d} | {r.merged_starts} | {r.flag_days_next_14} | "
                 f"{'yes' if r.holdout else ''} |")
    (ROOT / "reports" / "alt_rally.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L[2:4]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
