"""Live trading round-trips on the TESTING account (tiny orders, BTC/USD only).

    python test_trading.py --confirm

Steps (each request is logged to logs/api_log.jsonl):
  a) far-away LIMIT BUY -> query -> cancel -> query (expect CANCELED)
  b) MARKET BUY then MARKET SELL of the same BTC -> taker fee, fill vs bid/ask
  c) LIMIT BUY at best bid, wait up to ~2 min -> maker fee (or cancel)
  d) short_open $20 -> short_positions -> close 50% -> close rest -> positions == []
  e) final balance + USD reconciliation against fees and PnL

Safety: refuses to run without --confirm or with a non-"testing" key label,
keeps total notional under MAX_TOTAL_NOTIONAL, and touches only one pair.
Saves logs/results_trading.json
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from decimal import Decimal
from typing import Any

from roostoo_client import (
    LOG_DIR,
    SHORTS_DISABLED_MESSAGE,
    KeySafetyError,
    RoostooAPIError,
    RoostooClient,
    extract_wallet,
    mask_key,
    num,
    round_price,
    round_to_precision,
)

PAIR = "BTC/USD"
COIN = "BTC"
MAX_TOTAL_NOTIONAL = 200.0  # hard cap across every order in this script (USD)
MARKET_NOTIONAL = 15.0      # step b, per side
MAKER_NOTIONAL = 15.0       # step c
SHORT_COLLATERAL = 20.0     # step d
MAKER_WAIT_S = 120
POLL_S = 10


class Budget:
    """Tracks cumulative notional and refuses to exceed the cap."""

    def __init__(self, cap: float) -> None:
        self.cap = cap
        self.used = 0.0

    def spend(self, amount: float, what: str) -> None:
        if self.used + amount > self.cap:
            raise RuntimeError(f"notional cap: {what} (${amount:.2f}) would exceed "
                               f"${self.cap:.0f} (used ${self.used:.2f})")
        self.used += amount
        print(f"    budget: +${amount:.2f} for {what} -> ${self.used:.2f} / ${self.cap:.0f}")


class TradingTest:
    def __init__(self, client: RoostooClient) -> None:
        self.c = client
        self.budget = Budget(MAX_TOTAL_NOTIONAL)
        self.rules: dict[str, Any] = {}
        self.fees: list[dict[str, Any]] = []        # every fee charged, valued in USD
        self.round_trips: list[dict[str, float]] = []  # spot buy/sell pairs
        self.short_pnl = 0.0
        self.errors: list[dict[str, str]] = []
        self.out: dict[str, Any] = {"pair": PAIR}

    # ----- helpers --------------------------------------------------------- #

    def book(self) -> tuple[float, float]:
        t = self.c.ticker(PAIR)["Data"][PAIR]
        return num(t, "MaxBid"), num(t, "MinAsk")

    def qty_for(self, notional: float, price: float) -> Decimal:
        """Quantity rounded DOWN to AmountPrecision, bumped until > MiniOrder."""
        ap = int(self.rules["AmountPrecision"])
        step = Decimal(1).scaleb(-ap)
        q = round_to_precision(notional / price, ap)
        while q * Decimal(str(price)) <= Decimal(str(self.rules["MiniOrder"])):
            q += step
        return q

    def wallet(self) -> dict[str, Any]:
        return extract_wallet(self.c.balance())

    def coin_free(self) -> float:
        return num(self.wallet().get(COIN, {}), "Free")

    def record_fee(self, step: str, od: dict[str, Any]) -> dict[str, Any]:
        """Turn an OrderDetail into a fee record (USD-valued, implied %)."""
        qty, px = num(od, "FilledQuantity"), num(od, "FilledAverPrice")
        fee = num(od, "CommissionChargeValue")
        coin = od.get("CommissionCoin", "USD")
        fee_usd = fee if coin == "USD" else fee * px
        rec = {
            "step": step, "kind": f"spot_{str(od.get('Role', '?')).lower()}",
            "side": od.get("Side"), "type": od.get("Type"), "role": od.get("Role"),
            "status": od.get("Status"), "qty": qty, "price": px,
            "notional": qty * px, "fee": fee, "fee_coin": coin, "fee_usd": fee_usd,
            "CommissionPercent": od.get("CommissionPercent"),
            "implied_pct": (fee_usd / (qty * px) * 100) if qty * px else None,
        }
        if qty > 0:
            self.fees.append(rec)
        print(f"    {rec['side']} {rec['type']} {rec['role']} {rec['status']}: "
              f"qty={qty:g} @ {px}  fee={fee:g} {coin} (${fee_usd:.6f})  "
              f"CommissionPercent={rec['CommissionPercent']}  implied={rec['implied_pct']}")
        return rec

    def query_status(self, order_id: int) -> dict[str, Any]:
        q = self.c.query_order(order_id=order_id)
        matched = q.get("OrderMatched") or []
        return matched[0] if matched else {}

    def flatten(self, step: str, bought: float, buy_px: float, coin_before: float) -> None:
        """MARKET SELL whatever the buy actually added to the free balance."""
        ap = int(self.rules["AmountPrecision"])
        added = self.coin_free() - coin_before
        sell_qty = round_to_precision(min(added, bought), ap)
        print(f"    bought {bought:g}, free {COIN} increased by {added:g} -> selling {sell_qty}")
        if sell_qty <= 0:
            self.round_trips.append({"buy_qty": bought, "buy_px": buy_px,
                                     "sell_qty": 0.0, "sell_px": 0.0})
            return
        bid, ask = self.book()
        self.budget.spend(float(sell_qty) * bid, f"{step} MARKET SELL")
        od = self.c.place_order(PAIR, "SELL", sell_qty, "MARKET")["OrderDetail"]
        rec = self.record_fee(step + "_sell", od)
        rec.update(ticker_bid=bid, ticker_ask=ask,
                   slippage_vs_bid_pct=(rec["price"] - bid) / bid * 100 if bid else None)
        self.round_trips.append({"buy_qty": bought, "buy_px": buy_px,
                                 "sell_qty": rec["qty"], "sell_px": rec["price"]})

    # ----- steps ----------------------------------------------------------- #

    def step_a_limit_cancel(self) -> None:
        print("\n(a) LIMIT BUY at ~50% of bid -> query -> cancel -> query")
        bid, _ = self.book()
        px = round_price(bid * 0.5, int(self.rules["PricePrecision"]))
        qty = self.qty_for(float(self.rules["MiniOrder"]) * 1.1, float(px))
        self.budget.spend(float(qty * px), "a) LIMIT BUY (locked)")
        od = self.c.place_order(PAIR, "BUY", qty, "LIMIT", px)["OrderDetail"]
        oid = od["OrderID"]
        print(f"    placed OrderID={oid} Status={od.get('Status')} Role={od.get('Role')} "
              f"price={px} qty={qty} CommissionPercent={od.get('CommissionPercent')}")
        s1 = self.query_status(oid)
        print(f"    query  -> Status={s1.get('Status')}")
        cancel = self.c.cancel_order(order_id=oid)
        print(f"    cancel -> CanceledList={cancel.get('CanceledList')}")
        s2 = self.query_status(oid)
        print(f"    query  -> Status={s2.get('Status')} "
              f"({'OK' if s2.get('Status') == 'CANCELED' else 'UNEXPECTED'})")
        self.out["a"] = {"order_id": oid, "price": float(px), "qty": float(qty),
                         "placed_status": od.get("Status"), "placed_role": od.get("Role"),
                         "quoted_CommissionPercent": od.get("CommissionPercent"),
                         "status_after_query": s1.get("Status"),
                         "canceled_list": cancel.get("CanceledList"),
                         "status_after_cancel": s2.get("Status")}

    def step_b_market_round_trip(self) -> None:
        print("\n(b) MARKET BUY then MARKET SELL (taker fee)")
        bid, ask = self.book()
        qty = self.qty_for(MARKET_NOTIONAL, ask)
        coin_before = self.coin_free()
        self.budget.spend(float(qty) * ask, "b) MARKET BUY")
        od = self.c.place_order(PAIR, "BUY", qty, "MARKET")["OrderDetail"]
        rec = self.record_fee("b_buy", od)
        rec.update(ticker_bid=bid, ticker_ask=ask,
                   slippage_vs_ask_pct=(rec["price"] - ask) / ask * 100 if ask else None)
        self.flatten("b", rec["qty"], rec["price"], coin_before)
        self.out["b"] = [f for f in self.fees if f["step"].startswith("b_")]

    def step_c_maker(self) -> None:
        print(f"\n(c) LIMIT BUY at best bid, wait up to {MAKER_WAIT_S}s (maker fee)")
        bid, ask = self.book()
        px = round_price(bid, int(self.rules["PricePrecision"]))
        qty = self.qty_for(MAKER_NOTIONAL, float(px))
        coin_before = self.coin_free()
        self.budget.spend(float(qty * px), "c) LIMIT BUY at bid")
        od = self.c.place_order(PAIR, "BUY", qty, "LIMIT", px)["OrderDetail"]
        oid = od["OrderID"]
        print(f"    placed OrderID={oid} @ {px} (bid={bid}, ask={ask}) "
              f"Status={od.get('Status')} Role={od.get('Role')}")
        status, waited = od, 0
        while status.get("Status") not in ("FILLED", "CANCELED") and waited < MAKER_WAIT_S:
            time.sleep(POLL_S)
            waited += POLL_S
            status = self.query_status(oid) or status
            print(f"    t+{waited}s Status={status.get('Status')} "
                  f"filled={num(status, 'FilledQuantity'):g}")
        result: dict[str, Any] = {"order_id": oid, "price": float(px), "qty": float(qty),
                                  "waited_s": waited, "final_status": status.get("Status")}
        if status.get("Status") != "FILLED":
            cancel = self.c.cancel_order(order_id=oid)
            result["canceled"] = cancel.get("CanceledList")
            status = self.query_status(oid) or status
            print(f"    not filled within {MAKER_WAIT_S}s -> canceled "
                  f"(Status={status.get('Status')})")
        filled = num(status, "FilledQuantity")
        if filled > 0:
            rec = self.record_fee("c_maker", status)
            result["fee"] = rec
            self.flatten("c", filled, num(status, "FilledAverPrice"), coin_before)
        else:
            result["note"] = "maker order did not fill; maker fee not observed"
        self.out["c"] = result

    def step_d_short(self) -> None:
        print(f"\n(d) short_open {PAIR} ${SHORT_COLLATERAL:g} -> close 50% -> close rest")
        result: dict[str, Any] = {"allowed": None}
        existing = [p for p in (self.c.short_positions().get("Positions") or [])
                    if p.get("Pair") == PAIR]
        if existing:
            result["skipped"] = "pre-existing short on this pair; not touching it"
            print("    SKIP: account already has a short on", PAIR)
            self.out["d"] = result
            return
        bid, _ = self.book()
        self.budget.spend(SHORT_COLLATERAL, "d) short_open collateral")
        try:
            op = self.c.short_open(PAIR, SHORT_COLLATERAL)
        except RoostooAPIError as exc:
            result["allowed"] = SHORTS_DISABLED_MESSAGE not in exc.err_msg.lower()
            result["ErrMsg"] = exc.err_msg
            self.errors.append({"step": "d", "endpoint": exc.endpoint, "ErrMsg": exc.err_msg})
            print(f"    SHORT REJECTED: {exc.err_msg!r} -> continuing")
            self.out["d"] = result
            return
        result["allowed"] = True
        qty, entry = num(op, "ShortQty"), num(op, "EntryPrice")
        open_fee = num(op, "OpenFee")
        result["open"] = op
        result["open_fee_pct"] = open_fee / (qty * entry) * 100 if qty * entry else None
        result["entry_vs_bid_pct"] = (entry - bid) / bid * 100 if bid else None
        self.fees.append({"step": "d_open", "kind": "short_open", "fee_usd": open_fee,
                          "notional": qty * entry, "implied_pct": result["open_fee_pct"]})
        print(f"    open: ID={op.get('ID')} Status={op.get('Status')} qty={qty:g} "
              f"@ {entry} (bid {bid}) collateral={num(op, 'Collateral'):g} "
              f"OpenFee={open_fee:g} -> {result['open_fee_pct']}%")
        pos = self.c.short_positions().get("Positions")
        result["positions_after_open"] = pos
        print(f"    positions: {pos}")

        closes = []
        for label, kwargs in (("close_50pct", {"close_pct": 50}), ("close_rest", {})):
            if closes and closes[-1].get("FullyClosed"):
                break
            cl = self.c.short_close(PAIR, **kwargs)
            cq, cp, cf = num(cl, "ClosedQty"), num(cl, "ClosePrice"), num(cl, "CloseFee")
            cl["_label"] = label
            cl["_fee_pct"] = cf / (cq * cp) * 100 if cq * cp else None
            closes.append(cl)
            self.budget.spend(cq * cp, f"d) {label}")
            self.short_pnl += num(cl, "RealizedPNL")
            self.fees.append({"step": f"d_{label}", "kind": "short_close", "fee_usd": cf,
                              "notional": cq * cp, "implied_pct": cl["_fee_pct"]})
            print(f"    {label}: qty={cq:g} @ {cp} PnL={num(cl, 'RealizedPNL'):.6f} "
                  f"fee={cf:g} ({cl['_fee_pct']}%) return={num(cl, 'ReturnAmount'):g} "
                  f"FullyClosed={cl.get('FullyClosed')}")
        result["closes"] = closes
        pos = self.c.short_positions().get("Positions")
        result["positions_after_close"] = pos
        print(f"    positions after close: {pos} "
              f"({'OK' if pos == [] else 'UNEXPECTED - not empty'})")
        self.out["d"] = result

    # ----- run ------------------------------------------------------------- #

    def run(self) -> int:
        self.c.sync_clock()
        self.rules = self.c.exchange_info()["TradePairs"][PAIR]
        print(f"Rules {PAIR}: {self.rules}")
        start = self.wallet()
        usd0 = num(start.get("USD", {}), "Free") + num(start.get("USD", {}), "Lock")
        coin0 = num(start.get(COIN, {}), "Free") + num(start.get(COIN, {}), "Lock")
        pend = self.c.pending_count()
        print(f"Start: USD={usd0:,.6f} {COIN}={coin0:g}  pending={pend.get('OrderPairs')}")
        self.out["start"] = {"usd": usd0, "coin": coin0, "pending": pend.get("OrderPairs")}

        for step in (self.step_a_limit_cancel, self.step_b_market_round_trip,
                     self.step_c_maker, self.step_d_short):
            try:
                step()
            except RoostooAPIError as exc:
                print(f"    STEP FAILED: {exc.endpoint}: {exc.err_msg!r}")
                self.errors.append({"step": step.__name__, "endpoint": exc.endpoint,
                                    "ErrMsg": exc.err_msg})

        # (e) Reconciliation
        print("\n(e) Final balance and reconciliation")
        end = self.wallet()
        usd1 = num(end.get("USD", {}), "Free") + num(end.get("USD", {}), "Lock")
        coin1 = num(end.get(COIN, {}), "Free") + num(end.get(COIN, {}), "Lock")
        fees_total = sum(f["fee_usd"] for f in self.fees)
        spot_pnl = sum(t["sell_qty"] * (t["sell_px"] - t["buy_px"]) for t in self.round_trips)
        # BTC bought but not sold back (rounding dust), valued at its buy price.
        retained = sum((t["buy_qty"] - t["sell_qty"]) * t["buy_px"] for t in self.round_trips)
        coin_fees_usd = sum(f["fee_usd"] for f in self.fees if f.get("fee_coin") == COIN)
        retained -= coin_fees_usd  # coin-denominated fees already explain part of it
        spent = usd0 - usd1
        explained = fees_total - spot_pnl - self.short_pnl + retained
        print(f"    start USD {usd0:,.6f} -> end USD {usd1:,.6f}: spent {spent:.6f}")
        print(f"    fees {fees_total:.6f} - spot PnL {spot_pnl:.6f} - short PnL "
              f"{self.short_pnl:.6f} + {COIN} retained at cost {retained:.6f} "
              f"= {explained:.6f}")
        print(f"    difference: {spent - explained:+.6f} USD  "
              f"({COIN} {coin0:g} -> {coin1:g})")
        print(f"    total notional used: ${self.budget.used:.2f}")
        self.out["e"] = {"usd_start": usd0, "usd_end": usd1, "usd_spent": spent,
                         "fees_total_usd": fees_total, "spot_pnl": spot_pnl,
                         "short_pnl": self.short_pnl, "retained_coin_cost": retained,
                         "explained": explained, "unexplained": spent - explained,
                         "coin_start": coin0, "coin_end": coin1,
                         "notional_used": self.budget.used}
        self.out["fees"] = self.fees
        self.out["errors"] = self.errors
        LOG_DIR.mkdir(exist_ok=True)
        (LOG_DIR / "results_trading.json").write_text(
            json.dumps(self.out, indent=2, default=str), encoding="utf-8")
        print("\nSaved logs/results_trading.json")
        return 1 if self.errors else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--confirm", action="store_true",
                    help="required: places real orders on the TESTING account")
    args = ap.parse_args()
    if not args.confirm:
        print("Refusing to trade without --confirm. This places real orders on the "
              "TESTING account (total notional < $%d)." % MAX_TOTAL_NOTIONAL)
        return 2
    client = RoostooClient.from_env()
    try:
        client.assert_testing_key()
    except KeySafetyError as exc:
        print(f"ERROR: {exc}")
        return 2
    print(f"Trading with key {mask_key(client.api_key)} (label={client.key_label}) on {PAIR}")
    return TradingTest(client).run()


if __name__ == "__main__":
    sys.exit(main())
