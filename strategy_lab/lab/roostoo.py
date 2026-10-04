"""Which coins Roostoo lists today (public endpoints, no API key), mapped to Binance.

    python -m lab.roostoo        # writes strategy_lab/data/roostoo_pairs.json

Kept: AssetType == crypto, CanTrade, and live ticker data (OMNI/TON had none when
checked). AmountPrecision / PricePrecision / MiniOrder are used by the backtester.
"""

from __future__ import annotations

import json
import sys
import time

import requests

from lab import ROOT

BASE = "https://mock-api.roostoo.com"
OUT = ROOT / "data" / "roostoo_pairs.json"


def fetch() -> dict:
    info = requests.get(f"{BASE}/v3/exchangeInfo", timeout=20).json()
    tick = requests.get(f"{BASE}/v3/ticker", params={"timestamp": int(time.time() * 1000)},
                        timeout=20).json().get("Data", {})
    pairs, dropped = {}, {}
    for p, s in sorted(info["TradePairs"].items()):
        t = tick.get(p, {})
        if s.get("AssetType") != "crypto":
            dropped[p] = f"AssetType={s.get('AssetType')}"
        elif not s.get("CanTrade"):
            dropped[p] = "CanTrade=false"
        elif not t.get("LastPrice"):
            dropped[p] = "no ticker data"
        else:
            pairs[p] = {"binance": s["Coin"] + "USDT", "AmountPrecision": s["AmountPrecision"],
                        "PricePrecision": s["PricePrecision"], "MiniOrder": s["MiniOrder"],
                        "usd_volume_24h": t.get("UnitTradeValue")}
    return {"fetched_utc": time.strftime("%Y-%m-%d %H:%M", time.gmtime()), "pairs": pairs,
            "dropped": dropped}


def load() -> dict:
    return json.loads(OUT.read_text(encoding="utf-8"))


def binance_to_roostoo() -> dict[str, dict]:
    """'BTCUSDT' -> spec (incl. 'pair': 'BTC/USD')."""
    return {v["binance"]: {**v, "pair": p} for p, v in load()["pairs"].items()}


if __name__ == "__main__":
    d = fetch()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(d, indent=1), encoding="utf-8")
    print(f"{len(d['pairs'])} crypto pairs kept, {len(d['dropped'])} dropped -> {OUT}")
    print("dropped:", {k: v for k, v in d["dropped"].items() if "stock" not in v})
    sys.exit(0)
