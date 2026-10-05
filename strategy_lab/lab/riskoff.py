"""Risk-off switches for the satellite (research block 2 literature filters; frozen 2026-10-05
before any test). Daily, point-in-time: the value for UTC day d uses data up to d's close and
applies to day d+1.

    python -m lab.riskoff        # writes reports/riskoff.csv (fetches Fear & Greed history)

  riskoff_vb  (Kyriazis 2019; Maghyereh & Ziadat 2024): BTC 7-day realised vol (std of hourly
              returns over the last 168 h, annualised) above its 90th percentile over the
              trailing 365 days (min 180), OR alt breadth < 40% (alt_rally share: fraction of
              the top-50 liquid alts beating BTC over 30 days, lab/alt_rally.py)
  riskoff_fng Crypto Fear & Greed index (alternative.me, daily since 2018-02) > 80 or < 20
"""

from __future__ import annotations

import sys
from functools import lru_cache

import numpy as np
import pandas as pd
import requests

from lab import ROOT
from lab.data import load_close

CSV = ROOT / "reports" / "riskoff.csv"
FNG_URL = "https://api.alternative.me/fng/"


def fetch_fng() -> pd.Series:
    d = requests.get(FNG_URL, params={"limit": 0, "format": "json"}, timeout=60).json()["data"]
    s = pd.Series({pd.Timestamp(int(x["timestamp"]), unit="s", tz="UTC").floor("D"): float(x["value"]) for x in d})
    return s.sort_index()


def compute() -> pd.DataFrame:
    btc = load_close(["BTCUSDT"])["BTCUSDT"]
    r = btc.pct_change()
    vol7 = (r.rolling(168, min_periods=150).std() * np.sqrt(24 * 365)).resample("1D").last()
    pct = vol7.rolling(365, min_periods=180).apply(lambda x: (x[:-1] < x[-1]).mean() if len(x) > 1 else np.nan,
                                                  raw=True)
    alt = pd.read_csv(ROOT / "reports" / "alt_rally.csv", index_col=0, parse_dates=True)["share"]
    alt.index = pd.DatetimeIndex(alt.index).tz_convert("UTC") if alt.index.tz else pd.DatetimeIndex(alt.index).tz_localize("UTC")
    f = pd.DataFrame({"btc_vol7": vol7, "btc_vol7_pct": pct}).join(alt.rename("breadth"), how="left")
    f["riskoff_vb"] = (f.btc_vol7_pct > 0.90) | (f.breadth < 0.40)
    fng = fetch_fng().reindex(f.index)
    f["fng"] = fng
    f["riskoff_fng"] = (fng > 80) | (fng < 20)
    return f


@lru_cache(maxsize=1)
def series() -> pd.DataFrame:
    f = pd.read_csv(CSV, index_col=0, parse_dates=True)
    f.index = pd.DatetimeIndex(f.index).tz_convert("UTC") if f.index.tz else pd.DatetimeIndex(f.index).tz_localize("UTC")
    return f


def riskoff_on(ts: pd.Timestamp, kind: str) -> bool:
    """True if the switch was on at the previous UTC day's close (flat the satellite today)."""
    col = {"vol_breadth": "riskoff_vb", "fng": "riskoff_fng"}[kind]
    v = series()[col].get(ts.floor("D") - pd.Timedelta(days=1))
    return bool(v) if v is not None and not pd.isna(v) else False


def main() -> int:
    f = compute()
    CSV.parent.mkdir(exist_ok=True)
    f.to_csv(CSV)
    pre = f.loc[:"2026-06-30"]
    print(f"days {len(f)}; riskoff_vb on {pre.riskoff_vb.mean():.1%} of days to 2026-06-30 "
          f"(vol {(pre.btc_vol7_pct > 0.9).mean():.1%}, breadth<40% {(pre.breadth < 0.4).mean():.1%}); "
          f"riskoff_fng on {pre.riskoff_fng.mean():.1%} (FNG available from {f.fng.first_valid_index():%Y-%m-%d})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
