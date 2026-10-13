"""Reads the live account (source of truth) and turns target weights into Roostoo orders.

Port of the reference bot/portfolio.py. Same plan logic:
  * a pair trades only if |target - current| > band, or target is 0 while we still hold it
  * reductions first (free cash / collateral), then increases
  * spot: LIMIT at our side of the touch (maker 0.05%), cancel after `limit_wait_s`,
    MARKET for the remainder; shorts via /v6 (collateral), closes via short_close
Changes vs the reference, each for a live-API fact or a safety rule:
  * balance is read from SpotWallet (extract_wallet), short_positions from ["Positions"].
  * capital_cap_usd: weights are sized against min(actual equity, cap).
  * Filled quantity of a limit order is measured from the coin balance change, because
    live PENDING/CANCELED orders report FilledQuantity == Quantity (with FilledAverPrice 0).
  * An order-creating request that times out is never resent: we look for the order
    (pending orders on that pair), cancel it if found, log, and let the next hourly
    cycle re-read the account.
  * Quantities are floored with Decimal (no float artefacts like 0.29*100=28.999...).
  * Every order request and full response goes to logs/orders.jsonl. A limit order that
    rests and fills later (during the wait, or racing the cancel) gets its own
    LIMIT_LATE_FILL record with the final query response (fill price, commission).
"""

from __future__ import annotations

import logging
import time
from decimal import Decimal
from typing import Any, Callable

import requests

from roostoo_client import RoostooAPIError, extract_wallet, num, round_to_precision

log = logging.getLogger("strategy_bot.exec")


def floor_to(x: float, decimals: int) -> float:
    """Round |x| DOWN to `decimals` places (reference semantics, Decimal-exact)."""
    return float(round_to_precision(abs(x), int(decimals)))


class Portfolio:
    def __init__(self, client: Any, pairs: list[str], info: dict[str, dict], logs: Any,
                 entry: str = "limit", limit_wait_s: float = 300, dry_run: bool = False,
                 capital_cap_usd: float | None = None, poll_s: float = 15,
                 sleep: Callable[[float], None] = time.sleep,
                 should_stop: Callable[[], bool] = lambda: False) -> None:
        self.c, self.pairs, self.info, self.logs = client, pairs, info, logs
        self.entry, self.limit_wait_s, self.dry = entry, limit_wait_s, dry_run
        self.cap = capital_cap_usd
        self.cash_cap = False       # config cash_cap_orders: BUY_LONG / OPEN_SHORT sized down to the free USD at order time
        self.sizing_frac = 1.0      # config sizing_frac: weights sized against sizing x this (cash reserve for fees / short collateral)
        self.poll_s, self.sleep, self.should_stop = poll_s, sleep, should_stop
        self.last_snapshot: dict[str, Any] = {}
        self.order_tags: dict[str, dict[str, float]] = {}   # sleeve mode: pair -> {sleeve: usd}

    # ---------- state ----------
    def _short_positions(self) -> list[dict[str, Any]]:
        try:
            return self.c.short_positions().get("Positions") or []
        except RoostooAPIError as exc:  # e.g. shorts disabled on this account
            self.logs.error("short_positions", exc)
            return []

    def snapshot(self, tick: dict[str, dict]) -> tuple[float, float, dict, dict]:
        """(actual equity, sizing equity, signed USD exposure per pair, units per pair).

        Long legs are valued at the bid, shorts at the ask (the side we'd exit at), like
        the reference. Sizing equity = min(actual, capital_cap_usd)."""
        wallet = extract_wallet(self.c.balance())
        shorts = {p["Pair"]: p for p in self._short_positions()}
        usd = wallet.get("USD", {})
        equity = num(usd, "Free") + num(usd, "Lock")
        expo: dict[str, float] = {}
        units: dict[str, tuple[float, float, float]] = {}
        long_val = short_val = 0.0
        for pair in self.pairs:
            coin = pair.split("/")[0]
            w = wallet.get(coin, {})
            q_long = num(w, "Free") + num(w, "Lock")
            t = tick.get(pair, {})           # large pools: a pair may be missing from one ticker
            bid, ask = num(t, "MaxBid"), num(t, "MinAsk")
            sp = shorts.get(pair)
            q_short = num(sp, "ShortQty") if sp else 0.0
            pv = num(sp, "PositionValue") if sp else 0.0
            equity += q_long * bid + pv
            long_val += q_long * bid
            short_val += pv
            expo[pair] = q_long * bid - q_short * ask
            units[pair] = (q_long, q_short, num(w, "Free"))
        sizing = (min(equity, self.cap) if self.cap else equity) * self.sizing_frac
        self.last_snapshot = {"equity": equity, "sizing_equity": sizing,
                              "usd": num(usd, "Free") + num(usd, "Lock"),
                              "usd_free": num(usd, "Free"), "long_value": long_val,
                              "short_value": short_val,
                              "weights": {p: (expo[p] / sizing if sizing else 0.0) for p in self.pairs}}
        return equity, sizing, expo, units

    # ---------- planning ----------
    def rebalance(self, target_w: dict[str, float], tick: dict[str, dict], band: float,
                  reason: str = "", only: set[str] | None = None) -> int:
        """Band rebalance toward target_w. `only` restricts planning to those pairs (used
        by the minimal activity guard: one pair, band 0)."""
        equity, sizing, expo, units = self.snapshot(tick)
        cur_w = {p: (expo[p] / sizing if sizing else 0.0) for p in self.pairs}
        # Per-leg weights. Roostoo keeps spot longs and /v6 shorts as separate books, so a
        # pair can hold both legs at once (e.g. unsellable long dust + a new short). The
        # reference planned on the NET weight only and could leave both legs open forever
        # (even under KILL). Planning per leg gives identical orders when one leg exists.
        long_w = {p: (units[p][0] * num(tick.get(p, {}), "MaxBid") / sizing if sizing else 0.0)
                  for p in self.pairs}
        short_w = {p: (units[p][1] * num(tick.get(p, {}), "MinAsk") / sizing if sizing else 0.0)
                   for p in self.pairs}
        plan = []
        for p in self.pairs:
            if only is not None and p not in only:
                continue
            tw, cw = float(target_w.get(p, 0.0)), cur_w[p]
            holding = long_w[p] > 1e-4 or short_w[p] > 1e-4
            hedged = long_w[p] > 1e-4 and short_w[p] > 1e-4
            if abs(tw - cw) <= band and not (tw == 0 and holding) and not hedged:
                continue
            plan.append((p, tw))
        # reductions first (free cash/collateral), then increases
        reduce_steps, increase_steps = [], []
        for p, tw in plan:
            lw, sw = long_w[p], short_w[p]
            if lw > max(tw, 0):
                reduce_steps.append(("SELL_LONG", p, (lw - max(tw, 0)) * sizing))
            if sw > max(-tw, 0):
                reduce_steps.append(("CLOSE_SHORT", p, (sw - max(-tw, 0)) * sizing))
            if tw > 0 and tw > lw:
                increase_steps.append(("BUY_LONG", p, (tw - lw) * sizing))
            if tw < 0 and -tw > sw:
                increase_steps.append(("OPEN_SHORT", p, (-tw - sw) * sizing))
        n = 0
        for action, p, usd in reduce_steps + increase_steps:
            if self.should_stop():  # shutdown requested: place no new orders
                log.info("stop requested: skipping remaining planned orders")
                break
            try:
                if self.cash_cap and action in ("BUY_LONG", "OPEN_SHORT"):
                    # at full gross a buy can exceed the free USD (drift, short collateral): size it to the cash
                    # instead of letting the exchange reject it every hour
                    free = num(extract_wallet(self.c.balance()).get("USD", {}), "Free")
                    room = max(free - 1.0, 0.0) / 1.002
                    if room < usd:
                        if room < max(1.0, float(self.info[p]["MiniOrder"])):
                            self.logs.write("orders", {"action": action, "pair": p, "usd": round(usd, 2),
                                                       "skipped": f"cash: free USD {free:.2f}", "dry_run": self.dry})
                            log.info("%s %s skipped: free USD %.2f", action, p, free)
                            continue
                        self.logs.write("orders", {"action": action, "pair": p, "usd": round(room, 2),
                                                   "capped_from": round(usd, 2), "free_usd": round(free, 2), "dry_run": self.dry})
                        usd = room
                if self._execute(action, p, usd, tick, units):
                    n += 1
            except requests.RequestException as exc:
                # Network failure mid-order: never resend blindly (see _after_timeout).
                self.logs.error(f"order:{action}:{p}", exc)
                log.error("%s %s network failure: %s", action, p, exc)
            except Exception as exc:  # business error or bug: log and continue with the rest
                self.logs.error(f"order:{action}:{p}", exc)
                self.logs.write("orders", {"action": action, "pair": p, "usd": usd,
                                           "error": str(exc), "dry_run": self.dry})
                log.error("%s %s failed: %s", action, p, exc)
        self.logs.write("decisions", {
            "event": "rebalance", "reason": reason, "band": band, "equity": equity,
            "sizing_equity": sizing, "current": {p: round(w, 5) for p, w in cur_w.items()},
            "target": {p: round(float(target_w.get(p, 0.0)), 5) for p in self.pairs},
            "plan": [{"action": a, "pair": p, "usd": round(u, 2)} for a, p, u in
                     reduce_steps + increase_steps],
            "orders": n, "dry_run": self.dry})
        return n

    # ---------- execution ----------
    def _execute(self, action: str, pair: str, usd: float, tick: dict, units: dict) -> bool:
        spec = self.info[pair]
        ap, mini = int(spec["AmountPrecision"]), float(spec["MiniOrder"])
        bid, ask = num(tick[pair], "MaxBid"), num(tick[pair], "MinAsk")
        q_long, q_short, q_free = units[pair]
        if action == "SELL_LONG":
            qty = min(floor_to(usd / bid, ap), floor_to(q_free, ap))
            return self._spot(pair, "SELL", qty, bid, ask, mini)
        if action == "BUY_LONG":
            qty = floor_to(usd / ask, ap)
            return self._spot(pair, "BUY", qty, bid, ask, mini)
        if action == "CLOSE_SHORT":
            qty = min(floor_to(usd / ask, ap), q_short)
            if qty <= 0:
                return False
            close_qty = qty if qty < q_short else None  # None = close the whole position
            req = {"pair": pair, "close_qty": close_qty}
            if self.dry:
                self._log_order(action, req, None)
                return True
            try:
                r = self.c.short_close(pair, close_qty=close_qty)
            except requests.RequestException:
                self._log_order(action, req, None, error="TIMEOUT: not resent; next cycle re-reads positions")
                raise
            self._log_order(action, req, r)
            return True
        if action == "OPEN_SHORT":
            coll = round(usd / 1.001, 2)  # fee is charged on top of collateral
            if coll < max(1.0, mini):
                return False
            req = {"pair": pair, "collateral": coll}
            if self.dry:
                self._log_order(action, req, None)
                return True
            try:
                r = self.c.short_open(pair, coll)
            except requests.RequestException:
                self._log_order(action, req, None, error="TIMEOUT: not resent; next cycle re-reads positions")
                raise
            self._log_order(action, req, r)
            return True
        raise ValueError(f"unknown action {action}")

    def _coin_qty(self, pair: str) -> float:
        w = extract_wallet(self.c.balance()).get(pair.split("/")[0], {})
        return num(w, "Free") + num(w, "Lock")

    def _place(self, action: str, pair: str, side: str, qty: float, order_type: str,
               price: float | None = None) -> dict[str, Any]:
        """Send one spot order. On a network failure: look for the order, cancel it if it
        is pending, log, and re-raise. The request itself is never resent."""
        req = {"pair": pair, "side": side, "type": order_type, "quantity": qty, "price": price}
        try:
            r = self.c.place_order(pair, side, Decimal(str(qty)), order_type,
                                   None if price is None else Decimal(str(price)))
        except requests.RequestException:
            found = self._after_timeout(pair)
            self._log_order(action, req, None,
                            error=f"TIMEOUT: not resent; pending orders found and canceled: {found}")
            raise
        self._log_order(action, req, r)
        return r.get("OrderDetail") or {}

    def _after_timeout(self, pair: str) -> list[int]:
        """After an order request timed out, check whether it reached the exchange."""
        try:
            q = self.c.query_order(pair=pair, pending_only=True)
            ids = [o["OrderID"] for o in (q.get("OrderMatched") or []) if o.get("Status") == "PENDING"]
            for oid in ids:
                self.c.cancel_order(order_id=oid)
            return ids
        except Exception as exc:  # still offline: next cycle re-reads the account
            self.logs.error(f"after_timeout:{pair}", exc)
            return []

    def _spot(self, pair: str, side: str, qty: float, bid: float, ask: float, mini: float) -> bool:
        ref = ask if side == "BUY" else bid
        if qty <= 0 or qty * ref <= mini:  # live rule: price * qty must be > MiniOrder
            return False
        action = f"{side}_{self.entry.upper()}"
        if self.dry:
            px = bid if side == "BUY" else ask
            self._log_order(action, {"pair": pair, "side": side, "quantity": qty,
                                     "type": "LIMIT" if self.entry == "limit" else "MARKET",
                                     "price": px if self.entry == "limit" else None,
                                     "ref_price": ref, "notional": round(qty * ref, 2)}, None)
            return True
        if self.entry != "limit":
            self._place("MARKET", pair, side, qty, "MARKET")
            return True

        pp = int(self.info[pair]["PricePrecision"])
        px = round(bid if side == "BUY" else ask, pp)  # rest at our side of the book (maker)
        before = self._coin_qty(pair)
        o = self._place("LIMIT", pair, side, qty, "LIMIT", px)
        rested = o.get("Status") == "PENDING"
        t_placed = time.time()
        deadline = t_placed + self.limit_wait_s
        while o.get("Status") == "PENDING" and time.time() < deadline:
            self.sleep(self.poll_s)
            m = (self.c.query_order(order_id=o["OrderID"]).get("OrderMatched") or [None])[0]
            o = m or o
        if o.get("Status") == "PENDING":
            try:
                self.c.cancel_order(order_id=o["OrderID"])
            except RoostooAPIError as exc:  # e.g. it filled a moment ago: check below
                self.logs.error(f"cancel:{pair}:{o['OrderID']}", exc)
            # the order may have filled between the last query and the cancel
            final = (self.c.query_order(order_id=o["OrderID"]).get("OrderMatched") or [o])[0]
            filled = min(abs(self._coin_qty(pair) - before), qty)
            ap = int(self.info[pair]["AmountPrecision"])
            rest = floor_to(qty - filled, ap)
            if side == "SELL":  # never sell more than we actually hold now
                rest = min(rest, floor_to(self._free_qty(pair), ap))
            self.logs.write("orders", {"action": "LIMIT_TIMEOUT", "pair": pair, "order_id": o["OrderID"],
                                       "qty": qty, "filled": filled, "rest": rest,
                                       "final_status": final.get("Status"), "dry_run": False})
            log.info("LIMIT_TIMEOUT %s %s order %s: filled %s of %s while resting, final status %s, "
                     "market remainder %s", side, pair, o["OrderID"], filled, qty, final.get("Status"), rest)
            if final.get("Status") == "FILLED":
                self._log_late_fill(pair, side, final, t_placed, "filled before cancel took effect")
            if rest * ref > mini:
                self._place("MARKET_FALLBACK", pair, side, rest, "MARKET")
        elif rested:
            self._log_late_fill(pair, side, o, t_placed, "filled while resting")
        return True

    def _log_late_fill(self, pair: str, side: str, o: dict[str, Any], t_placed: float, how: str) -> None:
        """A limit order that rested (PENDING at placement) and filled later: the placement
        record in orders.jsonl still says PENDING, so record the fill separately."""
        rec = {"action": "LIMIT_LATE_FILL", "pair": pair, "side": side, "order_id": o.get("OrderID"),
               "status": o.get("Status"), "how": how, "filled_qty": o.get("FilledQuantity"),
               "avg_price": o.get("FilledAverPrice"), "commission": o.get("CommissionChargeValue"),
               "role": o.get("Role"), "waited_s": round(time.time() - t_placed, 1),
               "response": o, "dry_run": False}
        self.logs.write("orders", rec)
        log.info("LIMIT_LATE_FILL %s %s order %s (%s): qty %s @ %s, fee %s, after %.0fs", side, pair,
                 o.get("OrderID"), how, o.get("FilledQuantity"), o.get("FilledAverPrice"),
                 o.get("CommissionChargeValue"), rec["waited_s"])

    def _free_qty(self, pair: str) -> float:
        return num(extract_wallet(self.c.balance()).get(pair.split("/")[0], {}), "Free")

    def _log_order(self, action: str, request: dict, response: dict | None,
                   error: str | None = None) -> None:
        rec: dict[str, Any] = {"action": action, "request": request, "dry_run": self.dry}
        tag = self.order_tags.get(request.get("pair"))
        if tag:
            rec["sleeves"] = tag      # which sleeve(s) caused this order (USD change per sleeve)
        if response is not None:
            rec["response"] = response
        if error:
            rec["error"] = error
        self.logs.write("orders", rec)
        od = (response or {}).get("OrderDetail") or response or {}
        log.info("%s%s %s -> %s", "[DRY RUN] " if self.dry else "", action, request,
                 {k: od[k] for k in ("Status", "FilledQuantity", "FilledAverPrice",
                                     "CommissionChargeValue", "ShortQty", "EntryPrice",
                                     "ClosedQty", "ClosePrice") if k in od} or error or "")
