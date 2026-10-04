"""Signed, read-only endpoints: balance, pending_count, short_positions.

Requires initial_testing/.env with the TESTING key (ROOSTOO_KEY_LABEL=testing).
Saves logs/results_account.json
"""

from __future__ import annotations

import json
import sys
from typing import Any

from roostoo_client import (
    LOG_DIR,
    KeySafetyError,
    RoostooAPIError,
    RoostooClient,
    extract_wallet,
    mask_key,
    num,
)


def wallet_value_usd(wallet: dict[str, Any], tickers: dict[str, Any]) -> float:
    """Mark the wallet to market using LastPrice (Free + Lock)."""
    total = 0.0
    for coin, bal in wallet.items():
        qty = num(bal, "Free") + num(bal, "Lock")
        if coin == "USD":
            total += qty
        else:
            total += qty * num(tickers.get(f"{coin}/USD", {}), "LastPrice")
    return total


def main() -> int:
    client = RoostooClient.from_env()
    try:
        client.assert_testing_key()
    except KeySafetyError as exc:
        print(f"ERROR: {exc}")
        return 2
    print(f"Using key {mask_key(client.api_key)} (label={client.key_label})")
    print(f"Clock offset: {client.sync_clock()} ms")

    results: dict[str, Any] = {"errors": []}

    # Balance
    try:
        bal = client.balance()
        wallet: dict[str, Any] = extract_wallet(bal)
        tickers = client.ticker().get("Data", {})
        usd = wallet.get("USD", {})
        print(f"\n[balance] USD Free={num(usd, 'Free'):,.2f}  Lock={num(usd, 'Lock'):,.2f}")
        holdings = {c: b for c, b in wallet.items()
                    if c != "USD" and (num(b, "Free") + num(b, "Lock")) > 0}
        print(f"Holdings ({len(holdings)}):" if holdings else "Holdings: none besides USD")
        for c, b in sorted(holdings.items()):
            print(f"  {c:<10} Free={num(b, 'Free'):<16g} Lock={num(b, 'Lock'):g}")
        total = wallet_value_usd(wallet, tickers)
        print(f"Wallet value (marked at LastPrice): ${total:,.2f}")
        print("Response top-level keys:", list(bal))
        results.update(start_usd_free=num(usd, "Free"), start_usd_lock=num(usd, "Lock"),
                       holdings=holdings, wallet_value_usd=total, balance_keys=list(bal))
    except RoostooAPIError as exc:
        print(f"[balance] FAILED: {exc.err_msg}")
        results["errors"].append({"endpoint": exc.endpoint, "ErrMsg": exc.err_msg})

    # Pending orders
    try:
        pc = client.pending_count()
        print(f"\n[pending_count] Success={pc.get('Success')} ErrMsg={pc.get('ErrMsg')!r} "
              f"TotalPending={num(pc, 'TotalPending'):g} OrderPairs={pc.get('OrderPairs')}")
        results["pending"] = {"TotalPending": num(pc, "TotalPending"),
                              "OrderPairs": pc.get("OrderPairs"), "ErrMsg": pc.get("ErrMsg")}
    except RoostooAPIError as exc:
        print(f"[pending_count] FAILED: {exc.err_msg}")
        results["errors"].append({"endpoint": exc.endpoint, "ErrMsg": exc.err_msg})

    # Short positions
    try:
        sp = client.short_positions()
        positions = sp.get("Positions")
        print(f"\n[short_positions] Success={sp.get('Success')} Positions={positions}")
        results["short_positions"] = positions
    except RoostooAPIError as exc:
        print(f"[short_positions] FAILED: {exc.err_msg}")
        results["errors"].append({"endpoint": exc.endpoint, "ErrMsg": exc.err_msg})

    LOG_DIR.mkdir(exist_ok=True)
    (LOG_DIR / "results_account.json").write_text(json.dumps(results, indent=2),
                                                  encoding="utf-8")
    print("\nSaved logs/results_account.json")
    return 1 if results["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
