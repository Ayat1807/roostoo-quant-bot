"""Hourly high / low for the Roostoo pool (block 4d patient_limit fills), from Binance spot klines.

    python -m lab.lows            # fetch / extend .cache/klines_hl/<SYM>.pkl (high, low, close)

Same source and hour labels (open time, UTC) as the close cache in lab/data.py; a test compares the closes.
"""

from __future__ import annotations

import json
import sys
import time

import pandas as pd
import requests

from lab import ROOT
from lab.data import load_close

OUT = ROOT / ".cache" / "klines_hl"
URL = "https://api.binance.com/api/v3/klines"
START = pd.Timestamp("2020-01-01", tz="UTC")


def pool() -> list[str]:
    d = json.loads((ROOT / "data" / "roostoo_pairs.json").read_text())["pairs"]
    return sorted({v["binance"] for v in d.values()})


def fetch(sym: str, start: pd.Timestamp, end: pd.Timestamp) -> pd.DataFrame:
    rows, t = [], int(start.timestamp() * 1000)
    stop = int(end.timestamp() * 1000)
    while t < stop:
        for attempt in range(5):
            try:
                r = requests.get(URL, params={"symbol": sym, "interval": "1h", "startTime": t, "limit": 1000}, timeout=30)
                if r.status_code == 400:
                    return pd.DataFrame()
                r.raise_for_status()
                k = r.json()
                break
            except requests.RequestException:
                time.sleep(2 * (attempt + 1))
        else:
            raise RuntimeError(f"{sym}: Binance klines failed")
        if not k:
            break
        rows += k
        t = k[-1][0] + 3600_000
        time.sleep(0.12)
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(rows).iloc[:, [0, 2, 3, 4]]
    df.columns = ["t", "high", "low", "close"]
    df.index = pd.to_datetime(df["t"], unit="ms", utc=True)
    return df[["high", "low", "close"]].astype(float)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    end = load_close(["BTCUSDT"]).index[-1] + pd.Timedelta(hours=1)
    syms = pool()
    for i, s in enumerate(syms):
        p = OUT / f"{s}.pkl"
        old = pd.read_pickle(p) if p.exists() else None
        start = (old.index[-1] + pd.Timedelta(hours=1)) if old is not None and len(old) else START
        if start >= end:
            continue
        df = fetch(s, start, end)
        if old is not None:
            df = pd.concat([old, df])
            df = df[~df.index.duplicated(keep="last")]
        if len(df):
            df.to_pickle(p)
        print(f"  [{i + 1}/{len(syms)}] {s}: {len(df)} bars", flush=True)
    return 0


def load_lows(assets: list[str], index: pd.DatetimeIndex) -> pd.DataFrame:
    """Hourly lows on `index` (NaN where missing; segment suffixes like 'LUNAUSDT~2' map to the base file)."""
    cols = {}
    for a in assets:
        p = OUT / f"{a.split('~')[0]}.pkl"
        cols[a] = pd.read_pickle(p)["low"].reindex(index) if p.exists() else pd.Series(float("nan"), index=index)
    return pd.DataFrame(cols, index=index)


if __name__ == "__main__":
    sys.exit(main())
