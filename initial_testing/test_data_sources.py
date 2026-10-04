"""Check that Binance public kline data is reachable and matches Roostoo prices.

If Binance closes track Roostoo LastPrice closely, Binance history can seed the
strategy (Roostoo has no historical-candle endpoint). No keys needed.
Saves logs/results_data_sources.json
"""

from __future__ import annotations

import json
import sys
import time
from typing import Any

import requests

from roostoo_client import LOG_DIR, RoostooClient, append_log, num

BINANCE_HOSTS = ["https://api.binance.com", "https://data-api.binance.vision"]
SYMBOLS = {"BTCUSDT": "BTC/USD", "ETHUSDT": "ETH/USD", "SOLUSDT": "SOL/USD"}
HOURS = 48


def fetch_klines(host: str, symbol: str, interval: str = "1h",
                 limit: int = HOURS) -> tuple[list[list[Any]] | None, str]:
    """GET /api/v3/klines; returns (klines or None, status text). Logged to JSONL."""
    url = f"{host}/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    start = time.perf_counter()
    record: dict[str, Any] = {"ts": int(time.time() * 1000), "method": "GET",
                              "endpoint": f"{host.split('//')[1]}/api/v3/klines",
                              "params": params, "signed": False}
    try:
        r = requests.get(url, params=params, timeout=10)
        record.update(http_status=r.status_code,
                      latency_ms=round((time.perf_counter() - start) * 1000, 1))
        body = r.json() if r.headers.get("content-type", "").startswith("application/json") \
            else {"_raw_text": r.text[:300]}
        # Store a summary only; full kline arrays would bloat the log.
        record["response"] = ({"rows": len(body), "first": body[0], "last": body[-1]}
                              if isinstance(body, list) and body else body)
        append_log(record)
        if r.status_code != 200 or not isinstance(body, list):
            return None, f"HTTP {r.status_code}: {str(body)[:150]}"
        return body, "OK"
    except requests.RequestException as exc:
        record.update(http_status=None, error=str(exc),
                      latency_ms=round((time.perf_counter() - start) * 1000, 1))
        append_log(record)
        return None, f"{type(exc).__name__}: {exc}"


def main() -> int:
    results: dict[str, Any] = {"hosts": {}, "comparison": []}

    # 1) Reachability of each host, with 48 x 1h BTCUSDT klines
    for host in BINANCE_HOSTS:
        kl, status = fetch_klines(host, "BTCUSDT")
        info: dict[str, Any] = {"status": status}
        if kl:
            first_open = time.strftime("%Y-%m-%d %H:%M", time.gmtime(kl[0][0] / 1000))
            last_open = time.strftime("%Y-%m-%d %H:%M", time.gmtime(kl[-1][0] / 1000))
            info.update(rows=len(kl), first_open_utc=first_open, last_open_utc=last_open,
                        row_format="[openTime, open, high, low, close, volume, closeTime, "
                                   "quoteVolume, trades, takerBuyBase, takerBuyQuote, ignore]")
        results["hosts"][host] = info
        print(f"[{host}] {status}" + (f"  rows={info.get('rows')} "
              f"{info.get('first_open_utc')} -> {info.get('last_open_utc')} UTC" if kl else ""))

    working = [h for h, v in results["hosts"].items() if v["status"] == "OK"]
    if not working:
        print("ERROR: no Binance host reachable")
        return 1
    host = working[0]

    # 2) Compare latest Binance close (current, still-open 1h candle) to Roostoo LastPrice
    tickers = RoostooClient().ticker().get("Data", {})
    print(f"\nBinance ({host}) vs Roostoo, last {HOURS}h:")
    print(f"{'pair':<9}{'roostoo last':>14}{'binance close':>15}{'diff %':>9}"
          f"{'48h range':>22}")
    for symbol, pair in SYMBOLS.items():
        kl, status = fetch_klines(host, symbol)
        rp = num(tickers.get(pair, {}), "LastPrice")
        if not kl or not rp:
            print(f"{pair:<9} unavailable ({status}, roostoo={rp})")
            continue
        closes = [float(k[4]) for k in kl]
        bc = closes[-1]
        diff = (rp - bc) / bc * 100
        row = {"pair": pair, "symbol": symbol, "roostoo_last": rp, "binance_close": bc,
               "diff_pct": round(diff, 4), "binance_48h_low": min(closes),
               "binance_48h_high": max(closes), "rows": len(kl)}
        results["comparison"].append(row)
        print(f"{pair:<9}{rp:>14g}{bc:>15g}{diff:>+8.3f}%"
              f"{min(closes):>11g}-{max(closes):<10g}")

    LOG_DIR.mkdir(exist_ok=True)
    (LOG_DIR / "results_data_sources.json").write_text(json.dumps(results, indent=2),
                                                       encoding="utf-8")
    print("\nSaved logs/results_data_sources.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
