"""strategy_bot: runs a plug-in strategy (default S3v2) on Roostoo, unattended.

Loop (port of the reference bot/main.py, on pipeline_bot's infrastructure):
  every poll_s (60 s): one ticker call for all pairs -> hourly bar store
  each completed hour: account snapshot -> drawdown brake -> band rebalance toward target
  daily at rebalance_hour_utc: recompute target weights, persisted to state/targets.json
  restart: reuse the targets of the most recent rebalance slot (00:00 UTC) if they exist
    for the same strategy config; compute fresh ones only if none exist for that slot
  activity guard: if nothing traded today by activity_guard_hour_utc, use guard_band
  KILL file: flatten within one poll, then idle while it exists

Usage (see DEPLOY.md):
  python bot.py --dry-run --max-cycles 2     # decide + log intended orders, then exit
  python bot.py                              # config.yaml (dry_run: true by default)
  python bot.py --live                       # real orders (testing key only for now)
"""

from __future__ import annotations

import argparse
import json
import logging
import signal
import sys
import time
from pathlib import Path
from typing import Any, Callable

import pandas as pd
import requests
import yaml

from infra import JsonlLogs, build_client, setup_logging, utc_iso, write_json_atomic
from market_data import BarStore
from portfolio import Portfolio
from risk import RiskManager
from sleeves import SleeveBook, SleeveSpec, apply_fills, decision_slot, desired_units
from roostoo_client import KeySafetyError, mask_key, num
from strategies import get_strategy

HERE = Path(__file__).resolve().parent
log = logging.getLogger("strategy_bot")


def load_config(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validate_universe(universe: list[str], info: dict[str, Any], tick: dict[str, Any],
                      ) -> tuple[list[str], dict[str, str]]:
    """Keep pairs that are crypto, CanTrade and have live ticker data. Returns (kept, dropped)."""
    kept, dropped = [], {}
    for p in universe:
        spec = info.get(p)
        t = tick.get(p, {})
        if spec is None:
            dropped[p] = "not in exchangeInfo"
        elif spec.get("AssetType", "crypto") != "crypto":
            dropped[p] = f"AssetType={spec.get('AssetType')}"
        elif not spec.get("CanTrade"):
            dropped[p] = "CanTrade=false"
        elif not (num(t, "LastPrice") > 0 and num(t, "MaxBid") > 0 and num(t, "MinAsk") > 0):
            dropped[p] = "no live ticker data"
        else:
            kept.append(p)
    return kept, dropped


class StrategyBot:
    def __init__(self, cfg: dict[str, Any], client: Any, *, base_dir: Path = HERE,
                 clock: Callable[[], pd.Timestamp] | None = None,
                 sleep: Callable[[float], None] = time.sleep, bars: BarStore | None = None,
                 max_cycles: int | None = None) -> None:
        self.cfg, self.c = cfg, client
        self.replay = clock is not None
        self.clock = clock or (lambda: pd.Timestamp.now(tz="UTC"))
        self.sleep_fn = sleep
        paths = cfg.get("paths", {})
        self.log_dir = base_dir / paths.get("log_dir", "logs")
        self.state_dir = base_dir / paths.get("state_dir", "state")
        self.kill_file = base_dir / paths.get("kill_file", "KILL")
        self.logs = JsonlLogs(self.log_dir, self.clock if self.replay else None)
        self.bars = bars
        self.max_cycles = max_cycles
        self.dry = bool(cfg.get("dry_run", True))
        g = cfg.get("activity_guard", "full")
        self.guard_mode = {True: "full", False: "off"}.get(g, str(g)) if isinstance(g, bool) else str(g)
        if self.guard_mode not in ("off", "full", "minimal"):
            raise ValueError(f"activity_guard must be off|full|minimal, got {g!r}")
        self.strategy = get_strategy(cfg["strategy"]["name"])
        # sleeves (optional): several strategies on separate virtual books, netted per coin
        self.sleeve_specs: list[SleeveSpec] | None = None
        if cfg.get("sleeves"):
            self.sleeve_specs = [SleeveSpec.from_cfg(d, cfg["strategy"], cfg["universe"], float(cfg["band"]),
                                                     int(cfg["rebalance_hour_utc"])) for d in cfg["sleeves"]]
            if sum(s.weight for s in self.sleeve_specs) > 1 + 1e-9:
                raise ValueError("sleeve weights must sum to <= 1 (gross <= 1)")
            if len({s.name for s in self.sleeve_specs}) != len(self.sleeve_specs):
                raise ValueError("sleeve names must be unique")
        self.sleeve_strats = {s.name: get_strategy(s.strategy["name"]) for s in self.sleeve_specs or []}
        self.books: dict[str, SleeveBook] = {}
        self.sleeves_file = self.state_dir / "sleeves.json"
        self._sleeve_started: set[str] = set()
        self.pairs: list[str] = []
        self.target: dict[str, float] | None = None
        self.target_time: str | None = None
        self.target_slot: str | None = None      # rebalance slot the targets belong to
        self.mult, self.brake = 1.0, ""
        self.cycle = 0
        self.stop_requested = False
        self.kill_handled = False
        self.last_action: dict[str, Any] | None = None
        self.state_file = self.state_dir / "bot_state.json"
        self.targets_file = self.state_dir / "targets.json"
        st = json.loads(self.state_file.read_text()) if self.state_file.exists() else {}
        self.last_trade_day: str | None = st.get("last_trade_day")

    # ----- setup ----------------------------------------------------------- #

    def setup(self) -> None:
        cfg, c = self.cfg, self.c
        if hasattr(c, "sync_clock"):
            log.info("clock offset %s ms", c.sync_clock())
        info_resp = c.exchange_info()
        if not info_resp.get("IsRunning", True):
            raise RuntimeError("exchange reports IsRunning=false")
        info = info_resp["TradePairs"]
        tick = c.ticker()["Data"]
        wanted = list(cfg["universe"])
        if self.sleeve_specs:
            wanted = list(dict.fromkeys(p for s in self.sleeve_specs for p in s.universe))
        self.pairs, dropped = validate_universe(wanted, info, tick)
        for p, why in dropped.items():
            log.warning("universe: dropping %s (%s)", p, why)
        need_btc = [s.strategy.get("btc_pair", "BTC/USD") for s in self.sleeve_specs or []
                    if s.strategy["name"] == "s3v2"] if self.sleeve_specs else [cfg["strategy"].get("btc_pair", "BTC/USD")]
        if any(b not in self.pairs for b in need_btc):
            raise RuntimeError("BTC/USD (regime filter) failed the universe check")
        for s in self.sleeve_specs or []:
            s.universe = [p for p in s.universe if p in self.pairs]
        if self.sleeve_specs and self.sleeves_file.exists():
            d = json.loads(self.sleeves_file.read_text(encoding="utf-8"))
            self.books = {n: SleeveBook.from_json(b) for n, b in d.get("books", {}).items()
                          if n in {s.name for s in self.sleeve_specs}}
        if self.bars is None:
            self.bars = BarStore(self.pairs, self.state_dir / "bars.csv", self.log_dir / "api_log.jsonl")
            self.bars.load_or_bootstrap(int(cfg["bootstrap_hours"]), self.clock())
        self.port = Portfolio(c, self.pairs, info, self.logs, cfg["entry_order"],
                              float(cfg["limit_wait_s"]), self.dry, cfg.get("capital_cap_usd"),
                              float(cfg.get("limit_poll_s", 15)), sleep=self._sleep_with_heartbeat,
                              should_stop=lambda: self.stop_requested)
        if not self.dry:
            self.cancel_stale_orders()
        self.risk = RiskManager(cfg["dd_soft"], cfg["dd_hard"], cfg["cooloff_h"],
                                cfg.get("peak_days", 14), self.state_dir / "risk.json", self.kill_file)
        self.logs.write("decisions", {
            "event": "start", "pairs": self.pairs, "dropped": dropped, "dry_run": self.dry,
            "strategy": cfg["strategy"], "allow_short": cfg["allow_short"],
            "sleeves": [{"name": s.name, "weight": s.weight, "strategy": s.strategy, "execution": s.execution,
                         "decision_hour_utc": s.decision_hour_utc, "universe": s.universe}
                        for s in self.sleeve_specs or []] or None,
            "liquidity_guard": cfg.get("liquidity_guard"),
            "activity_guard": self.guard_mode,
            "capital_cap_usd": cfg.get("capital_cap_usd"), "bars": len(self.bars.close),
            "last_bar": str(self.bars.close.index[-1]) if len(self.bars.close) else None,
            "key": mask_key(getattr(c, "api_key", "")), "key_label": getattr(c, "key_label", None)})
        log.info("universe (%d): %s | dry_run=%s cap=%s allow_short=%s", len(self.pairs),
                 ", ".join(self.pairs), self.dry, cfg.get("capital_cap_usd"), cfg["allow_short"])

    def cancel_stale_orders(self) -> None:
        """A previous run may have been killed while a limit order rested on the book.
        This bot is the only order placer on its account, so any pending order on a
        universe pair is stale: cancel it by order_id (never cancel-all)."""
        resp = self.c.query_order(pending_only=True)
        stale = [o for o in (resp.get("OrderMatched") or [])
                 if o.get("Status") == "PENDING" and o.get("Pair") in self.pairs]
        for o in stale:
            self.c.cancel_order(order_id=o["OrderID"])
            self.logs.write("orders", {"action": "CANCEL_STALE", "order_id": o["OrderID"],
                                       "pair": o.get("Pair"), "side": o.get("Side"),
                                       "dry_run": False})
            log.warning("canceled stale pending order %s %s %s", o["OrderID"], o.get("Pair"),
                        o.get("Side"))

    # ----- strategy -------------------------------------------------------- #

    def rebalance_slot(self, now: pd.Timestamp) -> pd.Timestamp:
        """Most recent scheduled target time <= now (today's 00:00 UTC by default)."""
        slot = now.floor("D") + pd.Timedelta(hours=int(self.cfg["rebalance_hour_utc"]))
        return slot if slot <= now else slot - pd.Timedelta(days=1)

    def _fingerprint(self) -> dict[str, Any]:
        """Settings that change the targets: a mismatch means saved targets are stale."""
        return {"strategy": self.cfg["strategy"], "allow_short": bool(self.cfg["allow_short"]),
                "pairs": sorted(self.pairs)}

    def liquidity_skip(self, pairs: list[str], tick: dict[str, Any] | None) -> dict[str, str]:
        """Liquidity guard (config liquidity_guard, default on): at decision time skip pairs whose
        Roostoo spread > max_spread_bps or 24h volume (UnitTradeValue) < min_volume_usd."""
        g = {"enabled": True, "max_spread_bps": 15.0, "min_volume_usd": 1_000_000.0,
             **(self.cfg.get("liquidity_guard") or {})}
        if not g["enabled"] or not tick:
            return {}
        out = {}
        for p in pairs:
            t = tick.get(p, {})
            bid, ask = num(t, "MaxBid"), num(t, "MinAsk")
            spread = (ask - bid) / ((ask + bid) / 2) * 1e4 if bid > 0 and ask > 0 else float("inf")
            vol = num(t, "UnitTradeValue") if "UnitTradeValue" in t else float("inf")
            if spread > float(g["max_spread_bps"]):
                out[p] = f"spread {spread:.1f} bps > {g['max_spread_bps']}"
            elif vol < float(g["min_volume_usd"]):
                out[p] = f"24h volume ${vol:,.0f} < ${float(g['min_volume_usd']):,.0f}"
        return out

    def strategy_targets(self, strat: Any, params: dict[str, Any], pairs: list[str],
                         tick: dict[str, Any] | None, upto: pd.Timestamp | None = None
                         ) -> tuple[dict[str, float], dict[str, float], dict[str, str]]:
        """(raw, target, skipped): skipped pairs are removed before the strategy runs (a regime
        input such as btc_pair stays in the data but gets weight 0)."""
        skipped = self.liquidity_skip(pairs, tick)
        keep_input = {params.get("btc_pair")} if params.get("btc_pair") else set()
        cols = [p for p in pairs if p not in skipped or p in keep_input]
        closes = self.bars.close[cols] if upto is None else self.bars.close.loc[:upto, cols]
        raw = strat.target_weights(closes, params)
        raw = {p: (0.0 if p in skipped else raw.get(p, 0.0)) for p in pairs}
        tgt = raw if self.cfg["allow_short"] else {p: max(w, 0.0) for p, w in raw.items()}
        if skipped:
            log.warning("liquidity guard skipped %s", skipped)
        return raw, tgt, skipped

    def compute_targets(self, reason: str, slot: pd.Timestamp, tick: dict[str, Any] | None = None) -> None:
        closes = self.bars.close[self.pairs]
        raw, tgt, skipped = self.strategy_targets(self.strategy, self.cfg["strategy"], self.pairs, tick)
        self.target, self.target_time, self.target_slot = tgt, str(self.clock()), str(slot)
        rec = {"event": "targets", "reason": reason, "strategy": self.strategy.name,
               "slot": str(slot), "bar_time": str(closes.index[-1]),
               "allow_short": self.cfg["allow_short"],
               "raw": {p: round(w, 6) for p, w in raw.items()},
               "target": {p: round(w, 6) for p, w in tgt.items()},
               "gross": round(sum(abs(w) for w in tgt.values()), 6),
               "liquidity_skipped": skipped,
               "fingerprint": self._fingerprint()}
        self.logs.write("decisions", rec)
        write_json_atomic(self.targets_file, {**rec, "target": tgt, "computed_at": self.target_time,
                                              "fingerprint": self._fingerprint()})
        log.info("targets computed: %s (slot %s): %s", reason, slot,
                 {p: round(w, 3) for p, w in tgt.items() if w})

    def restore_targets(self, slot: pd.Timestamp) -> bool:
        """Reuse the targets saved for `slot` (a restart must not move them mid-day).
        Source: state/targets.json; if that file does not exist, the latest 'daily' targets
        event in logs/decisions.jsonl with the same config fingerprint. Any change to the
        strategy config (e.g. vol_method std -> ewma), allow_short or pairs -> fresh targets."""
        saved, source = None, "state/targets.json"
        if self.targets_file.exists():
            try:
                d = json.loads(self.targets_file.read_text(encoding="utf-8"))
            except (OSError, ValueError) as exc:
                self.logs.error("restore_targets", exc)
                d = None
            if d and d.get("fingerprint") == self._fingerprint():
                saved = d
            elif d:
                log.warning("saved targets ignored: strategy config / pairs changed since %s",
                            d.get("computed_at"))
                return False
        else:
            saved, source = self._targets_from_log(slot), "logs/decisions.jsonl"
        if not saved or pd.Timestamp(saved.get("slot", "1970-01-01T00:00:00+00:00")) != slot:
            return False
        tgt = {p: float(saved["target"].get(p, 0.0)) for p in self.pairs}
        self.target, self.target_time, self.target_slot = tgt, saved.get("computed_at") or saved.get("time"), str(slot)
        self.logs.write("decisions", {"event": "targets", "reason": "restored", "slot": str(slot),
                                      "source": source, "computed_at": self.target_time,
                                      "target": {p: round(w, 6) for p, w in tgt.items()}})
        log.info("targets restored from %s (computed %s, from %s): %s", f"{slot:%H:%M}",
                 self.target_time, source, {p: round(w, 3) for p, w in tgt.items() if w})
        if source != "state/targets.json":
            write_json_atomic(self.targets_file, {**saved, "target": tgt, "slot": str(slot),
                                                  "computed_at": self.target_time,
                                                  "fingerprint": self._fingerprint()})
        return True

    def _targets_from_log(self, slot: pd.Timestamp) -> dict[str, Any] | None:
        path = self.log_dir / "decisions.jsonl"
        if not path.exists():
            return None
        found = None
        with path.open(encoding="utf-8") as fh:
            for line in fh:
                if '"targets"' not in line or '"daily"' not in line:
                    continue
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                if (d.get("event") == "targets" and d.get("reason") == "daily"
                        and d.get("fingerprint") == self._fingerprint()   # same config (e.g. vol_method)
                        and bool(d.get("allow_short")) == bool(self.cfg["allow_short"])
                        and set(d.get("target", {})) == set(self.pairs)
                        and slot <= pd.Timestamp(d["time"]) < slot + pd.Timedelta(days=1)):
                    found = {**d, "slot": str(slot), "computed_at": d["time"]}
        return found

    # ----- hourly decision ------------------------------------------------- #

    def step(self, tick: dict[str, Any], reason: str) -> int:
        if self.sleeve_specs:
            return self.step_sleeves(tick, reason)
        now = self.clock()
        equity, sizing, expo, _ = self.port.snapshot(tick)
        self.mult, self.brake = self.risk.scale(now, equity)
        snap = self.port.last_snapshot
        self.logs.write("equity", {
            "equity": round(equity, 4), "sizing_equity": round(sizing, 4),
            "usd": round(snap["usd"], 4), "long_value": round(snap["long_value"], 4),
            "short_value": round(snap["short_value"], 4),
            "gross_exposure_usd": round(sum(abs(v) for v in expo.values()), 4),
            "exposure": {p: round(v, 2) for p, v in expo.items() if v},
            "brake": self.brake, "mult": self.mult})
        hour = now.floor("h")
        daily = hour.hour == int(self.cfg["rebalance_hour_utc"])
        mode = self.guard_mode
        guard = (mode != "off" and hour.hour == int(self.cfg["activity_guard_hour_utc"])
                 and self.last_trade_day != str(now.date()))
        slot = self.rebalance_slot(now)
        if self.target is None or (daily and self.target_slot != str(slot)):
            # first step after a (re)start: reuse this slot's targets if they exist
            if self.target is not None or not self.restore_targets(slot):
                self.compute_targets("daily" if daily else "first start", slot, tick)
        band = float(self.cfg["guard_band"] if (guard and mode == "full") else self.cfg["band"])
        why = f"{reason}{f' +activity_guard({mode})' if guard else ''} brake={self.brake}"
        eff = {p: w * self.mult for p, w in self.target.items()}
        n = self.port.rebalance(eff, tick, band, why)
        if guard and mode == "minimal" and n == 0:
            n = self.minimal_guard_trade(eff, tick, why)
        if n:
            self.last_action = {"time": str(now), "orders": n, "reason": why, "dry_run": self.dry}
            if not self.dry:  # dry-run orders must not satisfy the live activity guard
                self.last_trade_day = str(now.date())
                write_json_atomic(self.state_file, {"last_trade_day": self.last_trade_day})
        log.info("step %s: equity=%.2f sizing=%.2f mult=%s (%s) band=%.2f orders=%d",
                 reason, equity, sizing, self.mult, self.brake, band, n)
        return n

    # ----- sleeves ------------------------------------------------------------ #

    def _sleeve_fp(self, spec: SleeveSpec) -> dict[str, Any]:
        return {"strategy": spec.strategy, "allow_short": bool(self.cfg["allow_short"]),
                "universe": sorted(spec.universe), "execution": spec.execution,
                "decision_hour_utc": spec.decision_hour_utc}

    def _init_books(self, sizing: float, units: dict[str, tuple], px: dict[str, float]) -> None:
        """First start in sleeve mode: each sleeve gets weight x capped capital. Positions
        already in the account are assigned to the first sleeve (its band rule then trades
        them toward its own targets), so nothing is left untracked."""
        held = {p: u[0] - u[1] for p, u in units.items() if abs(u[0] - u[1]) > 1e-12}
        for i, spec in enumerate(self.sleeve_specs):
            if spec.name in self.books:
                continue
            cap = spec.weight * sizing
            if i == 0 and held:
                self.books[spec.name] = SleeveBook(cash=cap - sum(q * px[p] for p, q in held.items()),
                                                   units=dict(held))
            else:
                self.books[spec.name] = SleeveBook(cash=cap)
            log.info("sleeve %s: new book, capital %.2f%s", spec.name, cap,
                     f" (incl. existing holdings {held})" if i == 0 and held else "")

    def _save_books(self) -> None:
        write_json_atomic(self.sleeves_file, {"time": str(self.clock()),
                                              "books": {n: b.to_json() for n, b in self.books.items()}})

    def _sleeve_targets(self, spec: SleeveSpec, book: SleeveBook, now: pd.Timestamp,
                        tick: dict[str, Any]) -> bool:
        """Refresh the sleeve's targets if due. Returns True if computed now (a decision)."""
        slot = decision_slot(now, spec.decision_hour_utc)
        decide = now.floor("h").hour == spec.decision_hour_utc
        fp = self._sleeve_fp(spec)
        first = spec.name not in self._sleeve_started
        self._sleeve_started.add(spec.name)
        valid = book.target is not None and book.fingerprint == fp and book.slot == str(slot)
        if valid and first:
            self.logs.write("decisions", {"event": "targets", "sleeve": spec.name, "reason": "restored",
                                          "slot": str(slot), "source": "state/sleeves.json",
                                          "computed_at": book.computed_at, "target": book.target})
            log.info("sleeve %s: targets restored from %s (computed %s)", spec.name, f"{slot:%H:%M}",
                     book.computed_at)
            return False
        if valid:
            return False
        reason = "daily" if decide else ("first start" if first else "config changed")
        if book.target is not None and book.fingerprint != fp:
            log.warning("sleeve %s: config changed since %s; fresh targets", spec.name, book.computed_at)
        # scheduled sleeves always decide on their decision bar (the bar completed at the slot,
        # e.g. xsmom's 14:00 UTC bar), also on a first start between decisions; band sleeves use
        # the latest bar like single-strategy mode
        upto = slot - pd.Timedelta(hours=1) if spec.execution == "scheduled" else None
        raw, tgt, skipped = self.strategy_targets(self.sleeve_strats[spec.name], spec.strategy,
                                                  spec.universe, tick, upto)
        book.target, book.slot, book.computed_at, book.fingerprint = tgt, str(slot), str(now), fp
        self.logs.write("decisions", {
            "event": "targets", "sleeve": spec.name, "reason": reason, "strategy": spec.strategy["name"],
            "slot": str(slot), "bar_time": str(upto if upto is not None else self.bars.close.index[-1]),
            "target": {p: round(w, 6) for p, w in tgt.items()},
            "gross": round(sum(abs(w) for w in tgt.values()), 6), "liquidity_skipped": skipped,
            "fingerprint": fp})
        log.info("sleeve %s: targets computed: %s (slot %s): %s", spec.name, reason, slot,
                 {p: round(w, 3) for p, w in tgt.items() if w})
        return True

    def step_sleeves(self, tick: dict[str, Any], reason: str) -> int:
        """One decision step in sleeve mode (see sleeves.py)."""
        now = self.clock()
        equity, sizing, expo, units = self.port.snapshot(tick)
        self.mult, self.brake = self.risk.scale(now, equity)
        snap = self.port.last_snapshot
        px = {p: num(tick[p], "LastPrice") for p in self.pairs}
        self._init_books(sizing, units, px)
        total = sum(b.equity(px) for b in self.books.values())
        cap = self.cfg.get("capital_cap_usd")
        scale = min(1.0, float(cap) / total) if cap and total > 0 else 1.0
        wants: dict[str, dict[str, float]] = {}
        for spec in self.sleeve_specs:
            book = self.books[spec.name]
            decided = self._sleeve_targets(spec, book, now, tick)
            wants[spec.name] = desired_units(spec, book, px, self.mult, scale, decided)
        hour = now.floor("h")
        guard = (self.guard_mode != "off" and hour.hour == int(self.cfg["activity_guard_hour_utc"])
                 and self.last_trade_day != str(now.date()))
        n = self._execute_sleeves(wants, units, px, tick, sizing, f"{reason} sleeves brake={self.brake}")
        if guard and n == 0:
            n = self._sleeve_guard(wants, px, scale, sizing, units, tick, reason)
        for spec in self.sleeve_specs:
            apply_fills(spec, self.books[spec.name], wants[spec.name], px)
            self.books[spec.name].last_mult = self.mult
        self._save_books()
        self.logs.write("equity", {
            "equity": round(equity, 4), "sizing_equity": round(sizing, 4), "usd": round(snap["usd"], 4),
            "long_value": round(snap["long_value"], 4), "short_value": round(snap["short_value"], 4),
            "gross_exposure_usd": round(sum(abs(v) for v in expo.values()), 4),
            "exposure": {p: round(v, 2) for p, v in expo.items() if v}, "brake": self.brake,
            "mult": self.mult,
            "sleeves": {nm: {"equity": round(b.equity(px), 2), "cash": round(b.cash, 2),
                             "weights": {p: round(w, 4) for p, w in b.weights(px).items() if abs(w) > 1e-6}}
                        for nm, b in self.books.items()}})
        self.target = {p: sum(b.units.get(p, 0.0) * px[p] for b in self.books.values()) / total
                       if total > 0 else 0.0 for p in self.pairs}
        if n:
            self.last_action = {"time": str(now), "orders": n, "reason": reason, "dry_run": self.dry}
            if not self.dry:
                self.last_trade_day = str(now.date())
                write_json_atomic(self.state_file, {"last_trade_day": self.last_trade_day})
        log.info("step %s (sleeves): equity=%.2f sizing=%.2f mult=%s (%s) orders=%d books=%s", reason,
                 equity, sizing, self.mult, self.brake, n,
                 {nm: round(b.equity(px), 2) for nm, b in self.books.items()})
        return n

    def _execute_sleeves(self, wants: dict[str, dict[str, float]], units: dict[str, tuple],
                         px: dict[str, float], tick: dict[str, Any], sizing: float, why: str) -> int:
        """Net all sleeves' book changes per pair into one account order per pair."""
        tags: dict[str, dict[str, float]] = {}
        total_want: dict[str, float] = {}
        for nm, want in wants.items():
            book = self.books[nm]
            for p in set(want) | set(book.units):
                w_u = want.get(p, book.units.get(p, 0.0))
                total_want[p] = total_want.get(p, 0.0) + w_u
                d = w_u - book.units.get(p, 0.0)
                if abs(d * px[p]) > 1e-9:
                    tags.setdefault(p, {})[nm] = round(d * px[p], 2)
        trade = set(tags)
        # repair: the account drifted from the books (failed / partial order) beyond a threshold
        for p in self.pairs:
            actual = units[p][0] - units[p][1]
            gap_usd = abs(actual - total_want.get(p, 0.0)) * px[p]
            if gap_usd > max(2 * float(self.port.info[p]["MiniOrder"]), 0.005 * sizing):
                trade.add(p)
                tags.setdefault(p, {})["repair"] = round((total_want.get(p, 0.0) - actual) * px[p], 2)
        if not trade:
            return 0
        target_w = {p: (total_want.get(p, 0.0) * px[p] / sizing if sizing > 0 else 0.0) for p in self.pairs}
        self.port.order_tags = tags
        self.logs.write("decisions", {
            "event": "sleeve_orders", "reason": why,
            "net_target_usd": {p: round(total_want.get(p, 0.0) * px[p], 2) for p in sorted(trade)},
            "by_sleeve_usd": {p: tags.get(p, {}) for p in sorted(trade)}})
        try:
            return self.port.rebalance(target_w, tick, 0.0, why, only=trade)
        finally:
            self.port.order_tags = {}

    def _sleeve_guard(self, wants, px, scale, sizing, units, tick, reason) -> int:
        """Minimal activity guard in sleeve mode: one trade on the first band sleeve's pair
        furthest from its target (size min(gap, guard_max_frac) of that sleeve's equity, as the
        single-strategy guard sizes against its own capital)."""
        spec = next((s for s in self.sleeve_specs if s.execution == "band"), None)
        if spec is None:
            return 0
        book = self.books[spec.name]
        eq = book.equity(px) * scale
        if eq <= 0:
            return 0
        tgt = {p: w * self.mult for p, w in (book.target or {}).items()}
        cur = {p: wants[spec.name].get(p, book.units.get(p, 0.0)) * px[p] / eq for p in spec.universe}
        gaps = {p: tgt.get(p, 0.0) - cur[p] for p in spec.universe}
        p = max(gaps, key=lambda k: abs(gaps[k]))
        if abs(gaps[p]) <= 1e-9:
            log.info("minimal guard (sleeves): every pair exactly on target; no trade possible")
            return 0
        mini = float(self.port.info[p]["MiniOrder"])
        size = max(min(abs(gaps[p]), float(self.cfg.get("guard_max_frac", 0.02))), 1.5 * mini / eq)
        wants[spec.name][p] = (cur[p] + (size if gaps[p] > 0 else -size)) * eq / px[p]
        log.info("minimal guard (sleeves): %s/%s gap %+.4f, trade size %.4f of sleeve", spec.name, p,
                 gaps[p], size)
        return self._execute_sleeves(wants, units, px, tick, sizing,
                                     f"{reason} minimal_guard {spec.name}/{p}")

    def minimal_guard_trade(self, eff: dict[str, float], tick: dict[str, Any], why: str) -> int:
        """activity_guard: minimal. One trade on the pair furthest from its target, sized
        min(gap, guard_max_frac of sizing equity) but at least 1.5 x MiniOrder. Tested in
        strategy_lab (guard_minimal): same returns as no guard, every day active."""
        snap = self.port.last_snapshot
        sizing = snap.get("sizing_equity") or 0.0
        cur = snap.get("weights") or {}
        gaps = {p: eff.get(p, 0.0) - cur.get(p, 0.0) for p in self.pairs}
        p = max(gaps, key=lambda k: abs(gaps[k]))
        if abs(gaps[p]) <= 1e-9 or sizing <= 0:
            log.info("minimal guard: every pair exactly on target; no trade possible")
            return 0
        mini = float(self.port.info[p]["MiniOrder"])
        size = max(min(abs(gaps[p]), float(self.cfg.get("guard_max_frac", 0.02))), 1.5 * mini / sizing)
        tw = cur.get(p, 0.0) + (size if gaps[p] > 0 else -size)
        log.info("minimal guard: %s gap %+.4f -> trade toward target, size %.4f of equity", p, gaps[p], size)
        return self.port.rebalance({p: tw}, tick, 0.0, f"{why} minimal_guard {p}", only={p})

    def poll(self) -> None:
        """One ticker call; on a completed hour (or a new KILL file) run a decision step."""
        now = self.clock()
        tick = self.c.ticker()["Data"]
        missing = [p for p in self.pairs if p not in tick]
        prices = {p: num(tick[p], "LastPrice") for p in self.pairs if p in tick}
        closed = self.bars.on_ticker(now, prices)
        kill = self.risk.kill_active()
        if missing:
            self.logs.write("errors", {"where": "ticker", "type": "MissingPairs",
                                       "message": f"no ticker data for {missing}; step skipped"})
        elif closed:
            self.step(tick, "hourly")
            self.kill_handled = kill
        elif kill and not self.kill_handled:
            self.step(tick, "kill_switch")  # react within one poll, not at the next hour
            self.kill_handled = True
        if not kill:
            self.kill_handled = False
        self.heartbeat("running")

    # ----- heartbeat / sleep ------------------------------------------------ #

    def heartbeat(self, status: str) -> None:
        snap = getattr(self, "port", None) and self.port.last_snapshot or {}
        write_json_atomic(self.state_dir / "heartbeat.json", {
            "time": utc_iso(), "ts": int(time.time() * 1000), "sim_time": str(self.clock()),
            "status": status, "cycle": self.cycle, "poll_s": self.cfg["poll_s"],
            "limit_wait_s": self.cfg["limit_wait_s"], "dry_run": self.dry,
            "strategy": self.cfg["strategy"]["name"], "kill_active": self.kill_file.exists(),
            "key_label": getattr(self.c, "key_label", None),
            "capital_cap_usd": self.cfg.get("capital_cap_usd"), "allow_short": self.cfg["allow_short"],
            "equity": snap.get("equity"), "sizing_equity": snap.get("sizing_equity"),
            "usd": snap.get("usd"), "brake": self.brake, "mult": self.mult,
            "target": self.target, "target_time": self.target_time,
            "actual": snap.get("weights"), "last_trade_day": self.last_trade_day,
            "last_action": self.last_action, "pairs": self.pairs})

    def _sleep_with_heartbeat(self, seconds: float) -> None:
        """Used while waiting for limit fills, so the heartbeat stays fresh."""
        self.sleep_fn(seconds)
        if not self.replay:
            self.heartbeat("running (waiting for limit fill)")

    def _sleep(self, seconds: float) -> None:
        end = time.monotonic() + seconds
        while not self.stop_requested and time.monotonic() < end:
            time.sleep(min(1.0, max(0.0, end - time.monotonic())))

    # ----- main loop ------------------------------------------------------- #

    def install_signal_handlers(self) -> None:
        def handler(signum: int, _frame: Any) -> None:
            if self.stop_requested:
                raise KeyboardInterrupt
            self.stop_requested = True
            log.info("signal %s: finishing current cycle, then exiting", signum)
        signal.signal(signal.SIGINT, handler)
        if hasattr(signal, "SIGTERM"):
            signal.signal(signal.SIGTERM, handler)

    def run(self) -> int:
        self.install_signal_handlers()
        delay = 5.0
        while not self.stop_requested:  # startup: retry network trouble instead of dying
            try:
                self.setup()
                tick = self.c.ticker()["Data"]
                self.step(tick, "startup")
                break
            except requests.RequestException as exc:
                self.logs.error("startup", exc)
                log.warning("startup network error (%s); retry in %.0fs", exc, delay)
                self._sleep(delay)
                delay = min(delay * 2, 300)
        self.heartbeat("running")
        poll_s = float(self.cfg["poll_s"])
        net_errors = 0
        while not self.stop_requested:
            if self.max_cycles and self.cycle >= self.max_cycles:
                log.info("max cycles (%d) reached", self.max_cycles)
                break
            t0 = time.monotonic()
            wait = poll_s
            try:
                self.cycle += 1
                self.poll()
                net_errors = 0
            except requests.RequestException as exc:
                net_errors += 1
                wait = min(15 * 2 ** (net_errors - 1), 600)
                self.logs.error("poll:network", exc)
                log.warning("network error (%s); retry in %.0fs", exc, wait)
            except Exception as exc:  # never crash the loop
                self.logs.error("poll", exc)
                log.exception("cycle %d failed; continuing", self.cycle)
            if self.max_cycles and self.cycle >= self.max_cycles:
                continue
            self._sleep(max(0.0, wait - (time.monotonic() - t0)))
        self.heartbeat("stopped")
        log.info("stopped cleanly after %d polls", self.cycle)
        return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", type=Path, default=HERE / "config.yaml")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--live", action="store_true", help="override config: dry_run=false")
    mode.add_argument("--dry-run", action="store_true", help="override config: dry_run=true")
    ap.add_argument("--max-cycles", type=int, help="exit after N polls (after the startup step)")
    args = ap.parse_args()

    cfg = load_config(args.config)
    if args.live:
        cfg["dry_run"] = False
    if args.dry_run:
        cfg["dry_run"] = True
    paths = cfg.get("paths", {})
    log_dir = HERE / paths.get("log_dir", "logs")
    setup_logging(log_dir, int(cfg["bot_log"]["max_bytes"]), int(cfg["bot_log"]["backups"]))
    try:
        client = build_client(bool(cfg.get("allow_competition", False)), log_dir / "api_log.jsonl")
        log.info("key %s label=%s dry_run=%s", mask_key(client.api_key), client.key_label,
                 cfg["dry_run"])
        return StrategyBot(cfg, client, max_cycles=args.max_cycles).run()
    except KeySafetyError as exc:
        log.error("SAFETY: %s", exc)
        return 2
    except KeyboardInterrupt:
        log.info("interrupted")
        return 130
    except Exception:
        log.exception("fatal error during startup")
        return 1


if __name__ == "__main__":
    sys.exit(main())
