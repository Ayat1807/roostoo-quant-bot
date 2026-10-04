"""Binance spot 1h kline cache (all USDT pairs since `data.start`, delisted included).

    python -m lab.data update                 # download / top up everything (resumable)
    python -m lab.data update --symbols BTCUSDT,ETHUSDT
    python -m lab.data info

Sources:
* data.binance.vision monthly zips, listed from the public S3 bucket. The bucket keeps
  delisted symbols, which reduces survivorship bias.
* The REST API (/api/v3/klines) for the months not yet published as zips, only for
  symbols still TRADING.

Data hygiene:
* Since 2025-01 Binance spot kline files use microsecond timestamps; earlier, ms.
* A gap longer than `min_gap_split_days` splits a symbol into separate assets
  (SYMBOL, SYMBOL~2, ...): tickers get reused (LUNAUSDT -> LUNA2 after May 2022).
* Short gaps inside a segment (maintenance) are forward-filled at load time.
* Excluded: leveraged tokens and stablecoin/fiat bases (config/lab.yaml).

Storage (.cache/, git-ignored): klines/<SYM>.pkl (hourly close float64 + quote volume
float32), klines/<SYM>.months.json (manifest of downloaded months), daily.pkl (daily
close and quote-volume panels for ranking and features).
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
import threading
import time
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import numpy as np
import pandas as pd
import requests

from lab import ROOT, load_config

S3 = "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision"
VISION = "https://data.binance.vision"
REST_HOSTS = ("https://data-api.binance.vision", "https://api.binance.com")
HOUR_MS = 3_600_000

CFG = load_config()
CACHE = ROOT / CFG["data"]["cache_dir"]
KL = CACHE / "klines"
_session = threading.local()


def _http() -> requests.Session:
    if not hasattr(_session, "s"):
        _session.s = requests.Session()
    return _session.s


def _get(url: str, params: dict | None = None, timeout: float = 30, tries: int = 4) -> requests.Response:
    for i in range(tries):
        try:
            r = _http().get(url, params=params, timeout=timeout)
            if r.status_code == 404:
                return r
            r.raise_for_status()
            return r
        except requests.RequestException:
            if i == tries - 1:
                raise
            time.sleep(1.5 * (i + 1))
    raise RuntimeError("unreachable")


# --------------------------------------------------------------------------- #
# Symbol universe
# --------------------------------------------------------------------------- #

def _s3_prefixes(prefix: str) -> list[str]:
    out, marker = [], ""
    while True:
        r = _get(S3, {"delimiter": "/", "prefix": prefix, "marker": marker})
        out += re.findall(r"<Prefix>" + re.escape(prefix) + r"([^/]+)/</Prefix>", r.text)
        if "<IsTruncated>true</IsTruncated>" not in r.text:
            return out
        marker = re.findall(r"<NextMarker>(.*?)</NextMarker>", r.text)[-1]


def _s3_months(sym: str) -> list[str]:
    keys, marker = [], ""
    prefix = f"data/spot/monthly/klines/{sym}/1h/"
    while True:
        r = _get(S3, {"prefix": prefix, "marker": marker})
        keys += re.findall(r"<Key>[^<]*?-1h-(\d{4}-\d{2})\.zip</Key>", r.text)
        if "<IsTruncated>true</IsTruncated>" not in r.text:
            return sorted(set(keys))
        marker = re.findall(r"<Key>([^<]*)</Key>", r.text)[-1]


def is_excluded(sym: str) -> bool:
    d = CFG["data"]
    if not sym.endswith("USDT") or re.search(d["exclude_regex"], sym):
        return True
    return sym[:-4] in set(d["exclude_bases"])


def list_symbols() -> list[str]:
    syms = _s3_prefixes("data/spot/monthly/klines/")
    return sorted(s for s in syms if not is_excluded(s))


def trading_symbols() -> dict[str, str]:
    """Current Binance status per USDT symbol (TRADING / BREAK / ...)."""
    for host in REST_HOSTS:
        try:
            info = _get(f"{host}/api/v3/exchangeInfo", timeout=60).json()
            return {s["symbol"]: s["status"] for s in info["symbols"] if s["quoteAsset"] == "USDT"}
        except (requests.RequestException, ValueError, KeyError):
            continue
    raise RuntimeError("Binance exchangeInfo unreachable")


# --------------------------------------------------------------------------- #
# Download
# --------------------------------------------------------------------------- #

def _parse(rows: pd.DataFrame) -> pd.DataFrame:
    """Kline rows (open_time, o, h, l, c, v, close_time, quote_vol, ...) -> close/qv frame."""
    df = rows.iloc[:, [0, 4, 7]].apply(pd.to_numeric, errors="coerce").dropna()
    df.columns = ["t", "close", "quote_volume"]
    t = df["t"].astype("int64")
    t = np.where(t > 10**14, t // 1000, t)  # microseconds (2025+) -> ms
    idx = pd.to_datetime(t, unit="ms", utc=True)
    out = pd.DataFrame({"close": df["close"].astype("float64").values,
                        "quote_volume": df["quote_volume"].astype("float32").values}, index=idx)
    return out[~out.index.duplicated(keep="last")]


def _month(sym: str, ym: str) -> pd.DataFrame | None:
    r = _get(f"{VISION}/data/spot/monthly/klines/{sym}/1h/{sym}-1h-{ym}.zip")
    if r.status_code == 404:
        return None
    with zipfile.ZipFile(io.BytesIO(r.content)) as z:
        with z.open(z.namelist()[0]) as fh:
            raw = pd.read_csv(fh, header=None)
    return _parse(raw)


def _rest_tail(sym: str, start_ms: int) -> pd.DataFrame | None:
    now_hour = int(time.time() * 1000) // HOUR_MS * HOUR_MS
    rows, s = [], start_ms
    while s < now_hour:
        for host in REST_HOSTS:
            try:
                k = _get(f"{host}/api/v3/klines", {"symbol": sym, "interval": "1h",
                                                   "startTime": s, "limit": 1000}).json()
                break
            except (requests.RequestException, ValueError):
                k = None
        if not k or not isinstance(k, list):
            break
        rows += k
        s = int(k[-1][0]) + HOUR_MS
    if not rows:
        return None
    df = _parse(pd.DataFrame(rows))
    return df[df.index < pd.Timestamp(now_hour, unit="ms", tz="UTC")]  # completed bars only


def update_symbol(sym: str, status: str | None) -> tuple[str, int, str]:
    """Download missing months + REST tail for one symbol. Returns (sym, rows, note)."""
    KL.mkdir(parents=True, exist_ok=True)
    path, man_path = KL / f"{sym}.pkl", KL / f"{sym}.months.json"
    done = set(json.loads(man_path.read_text())) if man_path.exists() else set()
    df = pd.read_pickle(path) if path.exists() else None
    months = [m for m in _s3_months(sym) if m >= CFG["data"]["start"]]
    new = [m for m in months if m not in done]
    parts = [df] if df is not None else []
    for ym in new:
        m = _month(sym, ym)
        if m is not None and len(m):
            parts.append(m)
        done.add(ym)
    if parts:
        df = pd.concat(parts)
        df = df[~df.index.duplicated(keep="last")].sort_index()
    note = f"+{len(new)} months"
    if status == "TRADING":
        last_month_end = (pd.Timestamp(max(months) + "-01", tz="UTC") + pd.offsets.MonthBegin(1)
                          if months else pd.Timestamp(CFG["data"]["start"] + "-01", tz="UTC"))
        start = max(last_month_end, df.index[-1] + pd.Timedelta(hours=1)) if df is not None and len(df) \
            else last_month_end
        tail = _rest_tail(sym, int(start.timestamp() * 1000))
        if tail is not None and len(tail):
            df = pd.concat([df, tail]) if df is not None else tail
            df = df[~df.index.duplicated(keep="last")].sort_index()
            note += f", +{len(tail)}h REST"
    if df is None or not len(df):
        return sym, 0, note + " (no data since start)"
    df.to_pickle(path)
    man_path.write_text(json.dumps(sorted(done)))
    return sym, len(df), note


def update(symbols: list[str] | None = None, workers: int = 16) -> None:
    t0 = time.time()
    status = trading_symbols()
    syms = symbols or list_symbols()
    print(f"{len(syms)} symbols to check ({sum(status.get(s) == 'TRADING' for s in syms)} trading)")
    done = 0
    with ThreadPoolExecutor(workers) as ex:
        futs = {ex.submit(update_symbol, s, status.get(s)): s for s in syms}
        for f in as_completed(futs):
            done += 1
            try:
                sym, n, note = f.result()
                if done % 50 == 0 or done == len(syms):
                    print(f"  [{done}/{len(syms)}] {sym}: {n} rows ({note})  {time.time()-t0:.0f}s")
            except Exception as exc:
                print(f"  FAILED {futs[f]}: {exc}")
    build_daily()
    print(f"done in {time.time()-t0:.0f}s")


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #

def _segments(sym: str, s: pd.Series) -> dict[str, pd.Series]:
    """Split on gaps > min_gap_split_days (ticker reuse); name later parts SYM~2, ..."""
    gap = pd.Timedelta(days=CFG["data"]["min_gap_split_days"])
    breaks = np.where(s.index.to_series().diff() > gap)[0]
    if not len(breaks):
        return {sym: s}
    edges = [0, *breaks, len(s)]
    return {(sym if i == 0 else f"{sym}~{i + 1}"): s.iloc[a:b]
            for i, (a, b) in enumerate(zip(edges[:-1], edges[1:]))}


def cached_symbols() -> list[str]:
    return sorted(p.stem for p in KL.glob("*.pkl"))


def load_symbol(sym: str) -> dict[str, pd.DataFrame]:
    """All segments of one cached symbol (base name -> frame)."""
    df = pd.read_pickle(KL / f"{sym}.pkl")
    return {name: df.loc[seg.index] for name, seg in _segments(sym, df["close"]).items()}


def load_close(assets: list[str], start: str | None = None, end: str | None = None) -> pd.DataFrame:
    """Hourly close matrix (UTC), columns = assets ('BTCUSDT' or 'LUNAUSDT~2').

    Each asset is forward-filled only inside its own live range (listing -> last bar), so
    NaN before listing and after delisting. Index = contiguous hours."""
    cols = {}
    for a in assets:
        base = a.split("~")[0]
        seg = load_symbol(base).get(a)
        if seg is None:
            raise KeyError(f"{a} not in cache")
        s = seg["close"]
        full = pd.date_range(s.index[0], s.index[-1], freq="1h", tz="UTC")
        cols[a] = s.reindex(full).ffill()
    close = pd.DataFrame(cols)
    idx = pd.date_range(close.index.min(), close.index.max(), freq="1h", tz="UTC")
    close = close.reindex(idx)
    if start:
        close = close.loc[pd.Timestamp(start, tz="UTC"):]
    if end:
        close = close.loc[:pd.Timestamp(end, tz="UTC")]
    return close


def build_daily() -> None:
    """Daily close (last hourly close of the UTC day) and quote volume for every asset."""
    closes, vols = {}, {}
    for sym in cached_symbols():
        for name, seg in load_symbol(sym).items():
            d = seg.resample("1D")
            closes[name] = d["close"].last()
            vols[name] = d["quote_volume"].sum().astype("float64")
    daily = {"close": pd.DataFrame(closes).sort_index(), "quote_volume": pd.DataFrame(vols).sort_index()}
    pd.to_pickle(daily, CACHE / "daily.pkl")


def load_daily() -> dict[str, pd.DataFrame]:
    return pd.read_pickle(CACHE / "daily.pkl")


def info() -> None:
    syms = cached_symbols()
    d = load_daily()
    c = d["close"]
    alive = c.notna().sum(axis=1)
    print(f"cached symbols: {len(syms)}; assets after gap-splitting: {c.shape[1]}")
    print(f"days: {c.index[0]:%Y-%m-%d} -> {c.index[-1]:%Y-%m-%d}; assets alive on first/last day: "
          f"{alive.iloc[0]} / {alive.iloc[-1]}")
    last = c.apply(lambda s: s.last_valid_index())
    dead = (last < c.index[-1] - pd.Timedelta(days=3)).sum()
    print(f"assets that stopped trading before the end (delisted or renamed): {dead}")
    split = [a for a in c.columns if "~" in a]
    print(f"split by ticker reuse ({len(split)}): {', '.join(split[:15])}{' ...' if len(split) > 15 else ''}")
    size = sum(p.stat().st_size for p in KL.glob("*.pkl")) / 1e6
    print(f"cache size: {size:.0f} MB")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["update", "info", "daily"])
    ap.add_argument("--symbols", help="comma-separated, default: all")
    ap.add_argument("--workers", type=int, default=16)
    a = ap.parse_args()
    if a.cmd == "update":
        update(a.symbols.split(",") if a.symbols else None, a.workers)
    elif a.cmd == "daily":
        build_daily()
    else:
        info()
    return 0


if __name__ == "__main__":
    sys.exit(main())
