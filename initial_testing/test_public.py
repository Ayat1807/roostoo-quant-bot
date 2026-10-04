"""Public endpoints: serverTime (clock offset), exchangeInfo, ticker (all pairs).

No keys needed.  Saves:
  logs/exchange_info.json, logs/ticker_snapshot.json, logs/results_public.json
"""

from __future__ import annotations

import json
import sys
import time
from typing import Any

from roostoo_client import LOG_DIR, RoostooClient, num


def save_json(name: str, data: Any) -> None:
    LOG_DIR.mkdir(exist_ok=True)
    (LOG_DIR / name).write_text(json.dumps(data, indent=2), encoding="utf-8")


def top_liquid_table(info: dict[str, Any], tickers: dict[str, Any], n: int = 10) -> list[dict]:
    """Rows for the n pairs with the highest UnitTradeValue (24h USD volume)."""
    ranked = sorted(tickers.items(), key=lambda kv: num(kv[1], "UnitTradeValue"), reverse=True)
    rows = []
    for pair, t in ranked[:n]:
        rules = info.get("TradePairs", {}).get(pair, {})
        rows.append({
            "pair": pair,
            "UnitTradeValue": num(t, "UnitTradeValue"),
            "LastPrice": num(t, "LastPrice"),
            "PricePrecision": rules.get("PricePrecision"),
            "AmountPrecision": rules.get("AmountPrecision"),
            "MiniOrder": rules.get("MiniOrder"),
            "CanTrade": rules.get("CanTrade"),
        })
    return rows


def main() -> int:
    client = RoostooClient()  # no keys: public endpoints only

    # 1) Server time + clock offset (median of 3 samples to reduce jitter)
    offsets = [client.sync_clock() for _ in range(3)]
    offset = sorted(offsets)[1]
    client.clock_offset_ms = offset
    server_ms = client.server_time()["ServerTime"]
    print(f"[serverTime] ServerTime={server_ms}  local={int(time.time()*1000)}  "
          f"offset samples={offsets} ms -> using {offset} ms")

    # 2) exchangeInfo
    info = client.exchange_info()
    save_json("exchange_info.json", info)
    pairs = sorted(info.get("TradePairs", {}))
    print(f"\n[exchangeInfo] IsRunning={info.get('IsRunning')}  "
          f"InitialWallet={info.get('InitialWallet')}  pairs={len(pairs)}")
    print("Pairs:", ", ".join(pairs))

    # 3) Ticker for all pairs
    tick = client.ticker()
    save_json("ticker_snapshot.json", tick)
    data = tick.get("Data", {})
    print(f"\n[ticker] Success={tick.get('Success')}  pairs in ticker={len(data)}")
    missing = sorted(set(pairs) - set(data))
    if missing:
        print("  Pairs in exchangeInfo but not in ticker:", missing)

    # 4) Precision table for the 10 most liquid pairs
    rows = top_liquid_table(info, data)
    print("\nTop 10 by UnitTradeValue:")
    print(f"{'pair':<12}{'24h USD vol':>18}{'last':>14}{'PxPrec':>8}{'AmtPrec':>9}{'MiniOrder':>11}")
    for r in rows:
        print(f"{r['pair']:<12}{r['UnitTradeValue']:>18,.0f}{r['LastPrice']:>14g}"
              f"{r['PricePrecision']!s:>8}{r['AmountPrecision']!s:>9}{r['MiniOrder']!s:>11}")

    # 5) Single-pair ticker (BTC/USD) to confirm the `pair` param works
    btc = client.ticker("BTC/USD").get("Data", {}).get("BTC/USD", {})
    print(f"\n[ticker BTC/USD] {btc}")

    save_json("results_public.json", {
        "clock_offset_ms": offset,
        "clock_offset_samples_ms": offsets,
        "is_running": info.get("IsRunning"),
        "initial_wallet": info.get("InitialWallet"),
        "pairs": pairs,
        "ticker_pair_count": len(data),
        "top10": rows,
        "btc_ticker": btc,
    })
    print("\nOK: public endpoints reachable. Saved logs/exchange_info.json, "
          "logs/ticker_snapshot.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
