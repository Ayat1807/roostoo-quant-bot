"""Binance spot 5-minute klines (close, quote volume) for the Roostoo pool, 2023-01 to 2026-09 (block 10).

    python -m lab.klines5m          # -> .cache/klines_5m/<SYM>.pkl (float32), monthly files from data.binance.vision
"""

from __future__ import annotations

import io
import json
import sys
import zipfile
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd
import requests

from lab import ROOT

OUT = ROOT / ".cache" / "klines_5m"
URL = "https://data.binance.vision/data/spot/monthly/klines/{s}/5m/{s}-5m-{y}-{m:02d}.zip"
MONTHS = [(d.year, d.month) for d in pd.date_range("2023-01-01", "2026-09-01", freq="MS")]


def month(sym: str, y: int, m: int) -> pd.DataFrame | None:
    for attempt in range(4):
        try:
            r = requests.get(URL.format(s=sym, y=y, m=m), timeout=60)
            if r.status_code == 404:
                return None
            r.raise_for_status()
            with zipfile.ZipFile(io.BytesIO(r.content)) as z:
                raw = z.read(z.namelist()[0])
            df = pd.read_csv(io.BytesIO(raw), header=None, usecols=[0, 4, 7])
            if not str(df.iat[0, 0]).isdigit():          # header row in some files
                df = df.iloc[1:].astype(float)
            t = df[0].astype("int64")
            unit = "us" if t.iloc[0] > 10**14 else "ms"   # spot files switched to microseconds in 2025
            return pd.DataFrame({"close": df[4].astype("float32").values, "qv": df[7].astype("float32").values},
                                index=pd.to_datetime(t.values, unit=unit, utc=True))
        except (requests.RequestException, zipfile.BadZipFile, ValueError):
            continue
    print(f"  FAILED {sym} {y}-{m:02d}", flush=True)
    return None


def symbol(sym: str) -> str:
    p = OUT / f"{sym}.pkl"
    if p.exists():
        return f"{sym}: cached"
    parts = [x for x in (month(sym, y, m) for y, m in MONTHS) if x is not None]
    if not parts:
        return f"{sym}: no data"
    df = pd.concat(parts).sort_index()
    df = df[~df.index.duplicated(keep="last")]
    df.to_pickle(p)
    return f"{sym}: {len(df)} bars {df.index[0]:%Y-%m} -> {df.index[-1]:%Y-%m}"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    pairs = json.loads((ROOT / "data" / "roostoo_pairs.json").read_text())["pairs"]
    syms = sorted({v["binance"] for v in pairs.values()} | {"BTCUSDT"})
    with ThreadPoolExecutor(6) as ex:
        for msg in ex.map(symbol, syms):
            print(" ", msg, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
