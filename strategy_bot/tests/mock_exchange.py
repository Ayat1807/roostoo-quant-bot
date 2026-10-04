"""In-process mock of the Roostoo API as the bot uses it (port of the reference
tests/mock_exchange.py), upgraded to the LIVE response shapes and rules we verified:

* balance -> {"SpotWallet": {...}}; ticker -> {"Data": {...}}; place_order ->
  {"OrderDetail": {...}}; query_order -> {"OrderMatched": [...]}; short_positions ->
  {"Positions": [...]}; business failures raise RoostooAPIError (Success=false).
* quantity must respect AmountPrecision, price*qty > MiniOrder, LIMIT price within 30%
  of market, fees charged in USD (taker 0.1%, maker 0.05%, shorts 0.1%).
* PENDING / CANCELED orders report FilledQuantity == Quantity and FilledAverPrice 0
  (live quirk), so the bot must not trust FilledQuantity.
* Every `pending_every`-th limit order rests (never fills) to exercise cancel + market
  fallback; the others fill immediately at the limit price as maker (as the reference).
"""

from __future__ import annotations

from decimal import Decimal
from typing import Any

from roostoo_client import RoostooAPIError

# Live exchangeInfo values for the universe (from initial_testing/logs/exchange_info.json).
PREC = {"BTC/USD": (2, 5), "ETH/USD": (2, 4), "SOL/USD": (2, 3), "BNB/USD": (2, 3),
        "XRP/USD": (4, 1), "ADA/USD": (4, 1), "DOGE/USD": (5, 0), "AVAX/USD": (3, 2),
        "LINK/USD": (3, 2), "DOT/USD": (3, 2)}


def _decimals(x: Any) -> int:
    e = Decimal(str(x)).normalize().as_tuple().exponent
    return max(0, -int(e))


class MockRoostoo:
    key_label = "testing"
    api_key = "MOCK"

    def __init__(self, pairs: list[str], usd: float = 50_000.0, spread_bps: float = 1.0,
                 taker: float = 0.001, maker: float = 0.0005, short_fee: float = 0.001,
                 pending_every: int = 3) -> None:
        self.pairs, self.usd = pairs, usd
        self.coins = {p.split("/")[0]: 0.0 for p in pairs}
        self.locked = {p.split("/")[0]: 0.0 for p in pairs}
        self.usd_lock = 0.0
        self.shorts: dict[str, dict[str, float]] = {}
        self.px: dict[str, float] = {}
        self.spread, self.taker, self.maker, self.sfee = spread_bps / 1e4, taker, maker, short_fee
        self.oid, self.orders = 0, {}
        self.fees_paid, self.n_orders, self.n_limit = 0.0, 0, 0
        self.pending_every = pending_every
        self.calls: dict[str, int] = {}

    # ----- helpers ----------------------------------------------------------- #
    def set_prices(self, prices: dict[str, float]) -> None:
        self.px = dict(prices)

    def _bid(self, p: str) -> float: return self.px[p] * (1 - self.spread / 2)
    def _ask(self, p: str) -> float: return self.px[p] * (1 + self.spread / 2)

    def _count(self, name: str) -> None:
        self.calls[name] = self.calls.get(name, 0) + 1

    def _fail(self, ep: str, msg: str) -> None:
        raise RoostooAPIError(ep, msg, {"Success": False, "ErrMsg": msg})

    # ----- public ------------------------------------------------------------ #
    def sync_clock(self) -> int: return 0

    def exchange_info(self) -> dict[str, Any]:
        return {"IsRunning": True, "TradePairs": {
            p: {"Coin": p.split("/")[0], "CanTrade": True, "AssetType": "crypto",
                "PricePrecision": PREC[p][0], "AmountPrecision": PREC[p][1], "MiniOrder": 1}
            for p in self.pairs}}

    def ticker(self, pair: str | None = None) -> dict[str, Any]:
        self._count("ticker")
        return {"Success": True, "Data": {p: {"LastPrice": self.px[p], "MaxBid": self._bid(p),
                                              "MinAsk": self._ask(p)} for p in self.pairs}}

    # ----- account ----------------------------------------------------------- #
    def balance(self) -> dict[str, Any]:
        self._count("balance")
        w = {"USD": {"Free": self.usd, "Lock": self.usd_lock}}
        w.update({c: {"Free": q, "Lock": self.locked[c]} for c, q in self.coins.items()})
        return {"Success": True, "ErrMsg": "", "SpotWallet": w, "MarginWallet": {}}

    def short_positions(self) -> dict[str, Any]:
        out = []
        for p, s in self.shorts.items():
            upnl = s["qty"] * (s["entry"] - self._ask(p))
            out.append({"ID": 1, "Pair": p, "ShortQty": s["qty"], "EntryPrice": s["entry"],
                        "Collateral": s["coll"], "CurrentPrice": self._ask(p),
                        "UnrealizedPNL": upnl, "PositionValue": s["coll"] + upnl})
        return {"Success": True, "Positions": out}

    # ----- spot orders ------------------------------------------------------- #
    def place_order(self, pair: str, side: str, quantity: Any, order_type: str = "MARKET",
                    price: Any = None) -> dict[str, Any]:
        self._count("place_order")
        ep = "/v3/place_order"
        q = float(quantity)
        coin = pair.split("/")[0]
        if _decimals(quantity) > PREC[pair][1]:
            self._fail(ep, f"quantity precision: {quantity}")
        if order_type == "LIMIT":
            px = float(price)
            if _decimals(price) > PREC[pair][0]:
                self._fail(ep, f"price precision: {price}")
            if px < self.px[pair] * 0.7 or px > self.px[pair] * 1.3:
                self._fail(ep, "price should not less than market price 30%")
        ref = self._ask(pair) if side == "BUY" else self._bid(pair)
        if q * (float(price) if order_type == "LIMIT" else ref) <= 1:
            self._fail(ep, "order value too small (MiniOrder)")
        self.oid += 1
        od: dict[str, Any] = {"Pair": pair, "OrderID": self.oid, "Side": side, "Type": order_type,
                              "Quantity": q, "Price": float(price or 0), "CommissionCoin": "USD"}
        if order_type == "LIMIT":
            self.n_limit += 1
            if self.pending_every and self.n_limit % self.pending_every == 0:
                # rests on the book: lock funds, live quirk FilledQuantity == Quantity
                if side == "BUY":
                    need = q * od["Price"] * (1 + self.maker)
                    if need > self.usd + 1e-9:
                        self._fail(ep, "insufficient balance")
                    self.usd -= need; self.usd_lock += need; od["_locked"] = need
                else:
                    if q > self.coins[coin] + 1e-12:
                        self._fail(ep, "insufficient balance")
                    self.coins[coin] -= q; self.locked[coin] += q
                od.update(Status="PENDING", Role="MAKER", FilledQuantity=q, FilledAverPrice=0)
                self.orders[self.oid] = od
                return {"Success": True, "ErrMsg": "", "OrderDetail": {k: v for k, v in od.items()
                                                                        if not k.startswith("_")}}
            fill, rate, role = od["Price"], self.maker, "MAKER"
        else:
            fill, rate, role = ref, self.taker, "TAKER"
        notional = q * fill
        fee = notional * rate
        if side == "BUY":
            if notional + fee > self.usd + 1e-6:
                self._fail(ep, "insufficient balance")
            self.usd -= notional + fee; self.coins[coin] += q
        else:
            if q > self.coins[coin] + 1e-12:
                self._fail(ep, "insufficient balance")
            self.coins[coin] -= q; self.usd += notional - fee
        self.fees_paid += fee; self.n_orders += 1
        od.update(Status="FILLED", Role=role, FilledQuantity=q, FilledAverPrice=fill,
                  CommissionChargeValue=fee, CommissionPercent=rate)
        self.orders[self.oid] = od
        return {"Success": True, "ErrMsg": "", "OrderDetail": dict(od)}

    def query_order(self, order_id: Any = None, pair: str | None = None,
                    pending_only: bool | None = None, **_: Any) -> dict[str, Any]:
        self._count("query_order")
        if order_id is not None:
            o = self.orders.get(int(order_id))
            found = [o] if o else []
        else:
            found = [o for o in self.orders.values() if (pair is None or o["Pair"] == pair)
                     and (not pending_only or o["Status"] == "PENDING")]
        if not found:
            return {"Success": False, "ErrMsg": "no order matched"}
        return {"Success": True, "OrderMatched": [{k: v for k, v in o.items() if not k.startswith("_")}
                                                  for o in found]}

    def cancel_order(self, order_id: Any = None, pair: str | None = None) -> dict[str, Any]:
        self._count("cancel_order")
        if (order_id is None) == (pair is None):
            raise ValueError("exactly one of order_id / pair")
        o = self.orders.get(int(order_id))
        if not o or o["Status"] != "PENDING":
            return {"Success": True, "CanceledList": []}
        coin = o["Pair"].split("/")[0]
        if o["Side"] == "BUY":
            self.usd_lock -= o["_locked"]; self.usd += o["_locked"]
        else:
            self.locked[coin] -= o["Quantity"]; self.coins[coin] += o["Quantity"]
        o["Status"] = "CANCELED"  # FilledQuantity stays == Quantity (live quirk)
        return {"Success": True, "CanceledList": [o["OrderID"]]}

    # ----- shorts ------------------------------------------------------------ #
    def short_open(self, pair: str, collateral: Any, order_type: str | None = None,
                   price: Any = None) -> dict[str, Any]:
        self._count("short_open")
        ep = "/v6/short_open"
        coll_req = float(collateral)
        if coll_req < 1:
            self._fail(ep, "minimum collateral is $1")
        entry = self._bid(pair)
        ap = PREC[pair][1]
        qty = float(Decimal(str(coll_req / entry)).quantize(Decimal(1).scaleb(-ap), rounding="ROUND_DOWN"))
        if qty <= 0:
            self._fail(ep, "collateral too small for one quantity step")
        coll = qty * entry  # live: Collateral = ShortQty x EntryPrice
        fee = coll * self.sfee
        if coll + fee > self.usd + 1e-6:
            self._fail(ep, "insufficient balance")
        self.usd -= coll + fee; self.fees_paid += fee; self.n_orders += 1
        s = self.shorts.get(pair)
        if s:
            tq = s["qty"] + qty
            s["entry"] = (s["entry"] * s["qty"] + entry * qty) / tq; s["qty"] = tq; s["coll"] += coll
        else:
            self.shorts[pair] = {"qty": qty, "entry": entry, "coll": coll}
        return {"Success": True, "ID": 1, "Pair": pair, "OrderType": "MARKET", "EntryPrice": entry,
                "ShortQty": qty, "Collateral": coll, "OpenFee": fee, "Status": "OPEN"}

    def short_close(self, pair: str, close_qty: Any = None, close_pct: Any = None) -> dict[str, Any]:
        self._count("short_close")
        s = self.shorts.get(pair)
        if not s:
            self._fail("/v6/short_close", "no open short position for this pair")
        q = s["qty"] if close_qty is None else min(float(close_qty), s["qty"])
        cp = self._ask(pair); frac = q / s["qty"]
        pnl = q * (s["entry"] - cp); fee = q * cp * self.sfee; coll = s["coll"] * frac
        self.usd += coll + pnl - fee; self.fees_paid += fee; self.n_orders += 1
        s["qty"] -= q; s["coll"] -= coll
        full = s["qty"] <= 1e-12
        if full:
            del self.shorts[pair]
        return {"Success": True, "ClosePrice": cp, "RealizedPNL": pnl, "CloseFee": fee,
                "ReturnAmount": coll + pnl - fee, "ClosedQty": q, "FullyClosed": full}

    # ----- test helpers ------------------------------------------------------ #
    def equity(self) -> float:
        e = self.usd + self.usd_lock + sum((self.coins[p.split("/")[0]] + self.locked[p.split("/")[0]])
                                           * self._bid(p) for p in self.pairs)
        return e + sum(x["PositionValue"] for x in self.short_positions()["Positions"])

    def unsellable(self, pair: str) -> float:
        """USD value below which a position can't be traded: max(MiniOrder, one qty step)."""
        return max(1.0, 10 ** -PREC[pair][1] * self.px[pair])

    def pair_exposure(self) -> dict[str, float]:
        out = {p: (self.coins[p.split("/")[0]] + self.locked[p.split("/")[0]]) * self._bid(p)
               for p in self.pairs}
        for p, s in self.shorts.items():
            out[p] += s["qty"] * self._ask(p)
        return out

    def is_flat(self) -> bool:
        """Flat = every pair is down to dust that can't legally be traded."""
        return all(v <= self.unsellable(p) * 1.01 for p, v in self.pair_exposure().items())

    def gross_exposure(self) -> float:
        g = sum((self.coins[p.split("/")[0]] + self.locked[p.split("/")[0]]) * self._bid(p)
                for p in self.pairs)
        return g + sum(s["qty"] * self._ask(p) for p, s in self.shorts.items())
