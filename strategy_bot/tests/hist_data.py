"""Historical hourly closes for tests: Binance 1h klines, Jan 2023 -> now, 10 pairs.

Replaces the prototype's /home/claude/f.pkl. Cached per symbol in strategy_bot/.cache/
(git-ignored) so repeated test runs don't re-download. Built like the reference
research/engine.py::load_klines: hourly index from first to last bar, forward-filled,
columns renamed BTCUSDT -> BTC/USD.
"""

from __future__ import annotations

import time
from pathlib import Path

import pandas as pd
import requests

HERE = Path(__file__).resolve().parent.parent
CACHE = HERE / ".cache"
HOSTS = ("https://data-api.binance.vision", "https://api.binance.com")
SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT",
           "ADAUSDT", "DOGEUSDT", "AVAXUSDT", "LINKUSDT", "DOTUSDT"]
START = "2023-01-01"
HOUR_MS = 3_600_000


def _fetch(symbol: str, start_ms: int, end_ms: int) -> list[list]:
    rows: list[list] = []
    s = start_ms
    while s < end_ms:
        for host in HOSTS:
            try:
                r = requests.get(f"{host}/api/v3/klines", timeout=20, params={
                    "symbol": symbol, "interval": "1h", "startTime": s, "limit": 1000})
                r.raise_for_status()
                k = r.json()
                break
            except (requests.RequestException, ValueError):
                time.sleep(1)
        else:
            raise RuntimeError(f"all Binance hosts failed for {symbol}")
        if not k:
            break
        rows += k
        s = k[-1][0] + HOUR_MS
    return rows


def load_symbol(symbol: str, refresh: bool = False) -> pd.Series:
    """Closes indexed by bar open time (UTC); only completed bars."""
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"{symbol}_1h.csv"
    now_hour_ms = int(time.time() * 1000) // HOUR_MS * HOUR_MS  # current, still-forming bar
    if path.exists() and not refresh:
        ser = pd.read_csv(path, index_col=0, parse_dates=True)["close"]
        ser.index = pd.to_datetime(ser.index, utc=True)
        last_ms = int(ser.index[-1].timestamp() * 1000)
        if last_ms + HOUR_MS < now_hour_ms:  # top up missing recent bars
            new = _fetch(symbol, last_ms + HOUR_MS, now_hour_ms)
            if new:
                add = pd.Series([float(x[4]) for x in new],
                                index=pd.to_datetime([x[0] for x in new], unit="ms", utc=True))
                ser = pd.concat([ser, add])
    else:
        start_ms = int(pd.Timestamp(START, tz="UTC").timestamp() * 1000)
        rows = _fetch(symbol, start_ms, now_hour_ms)
        ser = pd.Series([float(x[4]) for x in rows],
                        index=pd.to_datetime([x[0] for x in rows], unit="ms", utc=True))
    ser = ser[~ser.index.duplicated(keep="last")].sort_index()
    ser = ser[ser.index < pd.Timestamp(now_hour_ms, unit="ms", tz="UTC")]
    ser.rename("close").to_csv(path)
    return ser


def load_closes(refresh: bool = False) -> pd.DataFrame:
    """DataFrame of hourly closes, columns BTC/USD ... DOT/USD (reference engine layout)."""
    frames = {s: load_symbol(s, refresh) for s in SYMBOLS}
    close = pd.DataFrame(frames).sort_index()
    idx = pd.date_range(close.index[0], close.index[-1], freq="1h", tz="UTC")
    close = close.reindex(idx).ffill()
    close.columns = [s.replace("USDT", "/USD") for s in close.columns]
    return close


if __name__ == "__main__":
    c = load_closes()
    print(c.shape, c.index[0], "->", c.index[-1])
    print(c.tail(2))
