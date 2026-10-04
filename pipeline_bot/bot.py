"""Pipeline bot: a deliberately trivial strategy to test the full system end to end.

    data (Roostoo ticker + Binance seed) -> decision (price vs 24h SMA)
      -> MARKET orders -> JSONL logs + heartbeat -> runs unattended

Strategy: LONG `notional_usd` of BTC when last price > SMA of the last `sma_hours`
hourly closes, else FLAT (or SHORT if allow_short). The current position is always
read from the exchange, never assumed.

Usage (see RUNNING.md):
    python bot.py                         # uses config.yaml (dry_run: true by default)
    python bot.py --interval-min 1 --max-cycles 3
    python bot.py --live --interval-min 1 --force-flip-every 5
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import signal
import sys
import time
import traceback
from dataclasses import dataclass
from datetime import datetime, timezone
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any, Callable

import requests
import yaml

from roostoo_client import (
    KeySafetyError,
    RoostooAPIError,
    RoostooClient,
    append_log,
    extract_wallet,
    fmt_decimal,
    mask_key,
    num,
    round_to_precision,
)

HERE = Path(__file__).resolve().parent
HOUR_MS = 3_600_000
BINANCE_HOSTS = ("https://api.binance.com", "https://data-api.binance.vision")
SEED_HOURS = 48

log = logging.getLogger("pipeline_bot")


# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #

@dataclass
class Config:
    pair: str
    binance_symbol: str
    notional_usd: float
    interval_min: float
    sma_hours: int
    allow_short: bool
    dry_run: bool
    allow_competition: bool
    long_threshold_frac: float
    log_dir: Path
    state_dir: Path
    kill_file: Path
    bot_log_max_bytes: int
    bot_log_backups: int

    @property
    def coin(self) -> str:
        return self.pair.split("/")[0]


def load_config(path: Path) -> Config:
    raw: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8"))
    paths = raw.get("paths", {})
    blog = raw.get("bot_log", {})
    return Config(
        pair=raw["pair"],
        binance_symbol=raw.get("binance_symbol", "BTCUSDT"),
        notional_usd=float(raw["notional_usd"]),
        interval_min=float(raw["interval_min"]),
        sma_hours=int(raw["sma_hours"]),
        allow_short=bool(raw.get("allow_short", False)),
        dry_run=bool(raw.get("dry_run", True)),
        allow_competition=bool(raw.get("allow_competition", False)),
        long_threshold_frac=float(raw.get("long_threshold_frac", 0.5)),
        log_dir=HERE / paths.get("log_dir", "logs"),
        state_dir=HERE / paths.get("state_dir", "state"),
        kill_file=HERE / paths.get("kill_file", "KILL"),
        bot_log_max_bytes=int(blog.get("max_bytes", 5_000_000)),
        bot_log_backups=int(blog.get("backups", 5)),
    )


# --------------------------------------------------------------------------- #
# Small utilities
# --------------------------------------------------------------------------- #

def utc_iso(ts: float | None = None) -> str:
    return datetime.fromtimestamp(ts or time.time(), tz=timezone.utc).isoformat(timespec="seconds")


def write_json_atomic(path: Path, data: Any) -> None:
    """Write via temp file + rename so readers never see a half-written file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
    os.replace(tmp, path)


class JsonlLogs:
    """decisions / orders / equity / errors .jsonl files, one record per line."""

    def __init__(self, log_dir: Path) -> None:
        self.dir = log_dir
        self.dir.mkdir(parents=True, exist_ok=True)

    def write(self, name: str, record: dict[str, Any]) -> None:
        append_log({"time": utc_iso(), "ts": int(time.time() * 1000), **record},
                   self.dir / f"{name}.jsonl")

    def error(self, where: str, exc: BaseException) -> None:
        self.write("errors", {"where": where, "type": type(exc).__name__,
                              "message": str(exc)[:1000],
                              "traceback": traceback.format_exc()[-4000:]})


def setup_logging(cfg: Config) -> None:
    cfg.log_dir.mkdir(parents=True, exist_ok=True)
    fmt = logging.Formatter("%(asctime)s %(levelname)-7s %(message)s", "%Y-%m-%d %H:%M:%S")
    fh = RotatingFileHandler(cfg.log_dir / "bot.log", maxBytes=cfg.bot_log_max_bytes,
                             backupCount=cfg.bot_log_backups, encoding="utf-8")
    fh.setFormatter(fmt)
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    log.handlers[:] = [fh, sh]
    log.setLevel(logging.INFO)


# --------------------------------------------------------------------------- #
# Price history (hourly buckets, persisted to state/prices.json)
# --------------------------------------------------------------------------- #

class PriceHistory:
    """Last observed price per UTC hour. Binance 1h closes and Roostoo ticker
    samples both land in the same hourly buckets, so the SMA is always an SMA of
    hourly closes no matter how often we sample."""

    def __init__(self, path: Path, keep_hours: int) -> None:
        self.path = path
        self.keep_hours = keep_hours
        self.buckets: dict[int, float] = {}
        if path.exists():
            try:
                raw = json.loads(path.read_text(encoding="utf-8"))
                self.buckets = {int(k): float(v) for k, v in raw.get("hourly", {}).items()}
            except (ValueError, OSError) as exc:
                log.warning("could not read %s (%s); starting empty", path, exc)

    def add(self, ts_ms: int, price: float) -> None:
        self.buckets[ts_ms // HOUR_MS] = price
        cutoff = ts_ms // HOUR_MS - self.keep_hours
        self.buckets = {h: p for h, p in self.buckets.items() if h > cutoff}

    def save(self) -> None:
        write_json_atomic(self.path, {"updated": utc_iso(),
                                      "hourly": {str(h): p for h, p in sorted(self.buckets.items())}})

    def sma(self, hours: int) -> float | None:
        """Mean of the latest `hours` hourly closes, or None if we have fewer."""
        latest = [p for _, p in sorted(self.buckets.items())][-hours:]
        return sum(latest) / len(latest) if len(latest) >= hours else None

    def seed_from_binance(self, symbol: str, hours: int, api_log: Path) -> str:
        """Fill buckets with 1h closes; returns the host used. Raises if all fail."""
        last_err = ""
        for host in BINANCE_HOSTS:
            start = time.perf_counter()
            rec: dict[str, Any] = {"ts": int(time.time() * 1000), "method": "GET",
                                   "endpoint": f"{host.split('//')[1]}/api/v3/klines",
                                   "params": {"symbol": symbol, "interval": "1h", "limit": hours}}
            try:
                r = requests.get(f"{host}/api/v3/klines", params=rec["params"], timeout=10)
                rec.update(http_status=r.status_code,
                           latency_ms=round((time.perf_counter() - start) * 1000, 1))
                rows = r.json() if r.status_code == 200 else None
                rec["response"] = {"rows": len(rows)} if isinstance(rows, list) else r.text[:300]
                append_log(rec, api_log)
                if isinstance(rows, list) and rows:
                    for k in rows:  # k[0]=open time ms, k[4]=close
                        self.buckets[int(k[0]) // HOUR_MS] = float(k[4])
                    return host
                last_err = f"{host}: HTTP {r.status_code}"
            except (requests.RequestException, ValueError) as exc:
                rec.update(error=str(exc))
                append_log(rec, api_log)
                last_err = f"{host}: {exc}"
            log.warning("Binance seed failed on %s", last_err)
        raise RuntimeError(f"all Binance hosts failed ({last_err})")


# --------------------------------------------------------------------------- #
# Position (always read from the exchange)
# --------------------------------------------------------------------------- #

@dataclass
class Position:
    usd_free: float
    usd_lock: float
    usd_short_collateral: float  # SpotWallet.USD.ShortCollateral (live-only field)
    coin_free: float
    coin_lock: float
    short_qty: float
    short_value: float           # Collateral + UnrealizedPNL from /v6/short_positions
    bid: float
    ask: float
    last: float
    side: str                    # LONG | SHORT | FLAT

    @property
    def coin_value(self) -> float:
        return (self.coin_free + self.coin_lock) * self.bid

    @property
    def equity(self) -> float:
        return self.usd_free + self.usd_lock + self.coin_value + self.short_value

    def summary(self) -> dict[str, Any]:
        return {"side": self.side, "usd_free": self.usd_free, "usd_lock": self.usd_lock,
                "usd_short_collateral": self.usd_short_collateral,
                "coin_free": self.coin_free, "coin_lock": self.coin_lock,
                "coin_value": round(self.coin_value, 6), "short_qty": self.short_qty,
                "short_value": round(self.short_value, 6), "equity": round(self.equity, 6)}


# --------------------------------------------------------------------------- #
# Bot
# --------------------------------------------------------------------------- #

class Bot:
    def __init__(self, cfg: Config, force_flip_min: float | None, max_cycles: int | None) -> None:
        self.cfg = cfg
        self.force_flip_min = force_flip_min
        self.max_cycles = max_cycles
        self.logs = JsonlLogs(cfg.log_dir)
        self.history = PriceHistory(cfg.state_dir / "prices.json",
                                    keep_hours=max(SEED_HOURS, cfg.sma_hours) + 24)
        self.client: RoostooClient | None = None
        self.rules: dict[str, Any] = {}
        self.stop_requested = False
        self.cycle_no = 0
        self.started_at = time.time()
        self.last_action: dict[str, Any] | None = None
        self.last_pos: Position | None = None
        self.consecutive_net_errors = 0

    # ----- signals --------------------------------------------------------- #

    def install_signal_handlers(self) -> None:
        def handler(signum: int, _frame: Any) -> None:
            if self.stop_requested:  # second Ctrl+C: stop immediately
                raise KeyboardInterrupt
            self.stop_requested = True
            log.info("signal %s received: finishing current cycle, then exiting", signum)

        signal.signal(signal.SIGINT, handler)
        if hasattr(signal, "SIGTERM"):
            signal.signal(signal.SIGTERM, handler)

    def sleep(self, seconds: float) -> None:
        """Interruptible sleep: wakes within 1 s of a stop request."""
        end = time.monotonic() + seconds
        while not self.stop_requested and time.monotonic() < end:
            time.sleep(min(1.0, end - time.monotonic()))

    # ----- startup --------------------------------------------------------- #

    def build_client(self) -> RoostooClient:
        """Key-label safety gate. Returns a client allowed to sign requests."""
        probe = RoostooClient.from_env()
        label = probe.key_label
        if label == "testing":
            allowed: tuple[str, ...] = ("testing",)
        elif label == "competition":
            if not self.cfg.allow_competition:
                raise KeySafetyError("ROOSTOO_KEY_LABEL=competition but config has "
                                     "allow_competition: false. Refusing to start.")
            allowed = ("competition",)
            print("\n" + "!" * 70 + "\n  WARNING: COMPETITION KEY. Real scored account.\n"
                  "  Press Ctrl+C within 10 seconds to abort.\n" + "!" * 70, flush=True)
            for i in range(10, 0, -1):
                print(f"  starting in {i}...", flush=True)
                time.sleep(1)
        else:
            raise KeySafetyError(f"ROOSTOO_KEY_LABEL={label!r}: must be 'testing' "
                                 "(or 'competition' with allow_competition: true).")
        client = RoostooClient.from_env(allowed_labels=allowed,
                                        log_path=self.cfg.log_dir / "api_log.jsonl")
        client.assert_key_allowed()
        return client

    def startup(self) -> None:
        cfg = self.cfg
        self.client = self.build_client()
        c = self.client
        log.info("starting: pair=%s notional=$%s interval=%smin sma=%sh short=%s "
                 "dry_run=%s force_flip=%s key=%s label=%s", cfg.pair, cfg.notional_usd,
                 cfg.interval_min, cfg.sma_hours, cfg.allow_short, cfg.dry_run,
                 self.force_flip_min, mask_key(c.api_key), c.key_label)

        # Retry network problems at startup instead of dying (e.g. boot before network).
        delay = 5.0
        while not self.stop_requested:
            try:
                offset = c.sync_clock()
                info = c.exchange_info()
                break
            except requests.RequestException as exc:
                self.logs.error("startup", exc)
                log.warning("startup network error (%s); retry in %.0fs", exc, delay)
                self.sleep(delay)
                delay = min(delay * 2, 300)
        else:
            return
        rules = info.get("TradePairs", {}).get(cfg.pair)
        if not info.get("IsRunning") or not rules or not rules.get("CanTrade"):
            raise RuntimeError(f"exchange not usable: IsRunning={info.get('IsRunning')} "
                               f"rules={rules}")
        self.rules = rules
        log.info("clock offset %d ms; %s rules: %s", offset, cfg.pair, rules)

        try:
            host = self.history.seed_from_binance(cfg.binance_symbol,
                                                  max(SEED_HOURS, cfg.sma_hours + 1),
                                                  cfg.log_dir / "api_log.jsonl")
            self.history.save()
            log.info("seeded %d hourly closes from %s", len(self.history.buckets), host)
        except RuntimeError as exc:
            self.logs.error("seed_binance", exc)
            log.warning("Binance seed failed (%s); using %d stored hours", exc,
                        len(self.history.buckets))

        pos = self.read_position()
        self.logs.write("decisions", {"event": "startup_reconcile", "position": pos.summary(),
                                      "dry_run": cfg.dry_run, "key_label": c.key_label})
        log.info("reconciled position: %s", pos.summary())

    # ----- exchange reads -------------------------------------------------- #

    def read_position(self) -> Position:
        assert self.client is not None
        c, cfg = self.client, self.cfg
        t = c.ticker(cfg.pair)["Data"][cfg.pair]
        wallet = extract_wallet(c.balance())
        usd, coin = wallet.get("USD", {}), wallet.get(cfg.coin, {})
        short_qty = short_value = 0.0
        try:
            for p in c.short_positions().get("Positions") or []:
                if p.get("Pair") == cfg.pair:
                    short_qty += num(p, "ShortQty")
                    short_value += num(p, "PositionValue")
        except RoostooAPIError as exc:  # e.g. shorts disabled: treat as no short
            self.logs.error("short_positions", exc)
        bid = num(t, "MaxBid")
        coin_value = (num(coin, "Free") + num(coin, "Lock")) * bid
        if short_qty > 0:
            side = "SHORT"
        elif coin_value >= cfg.long_threshold_frac * cfg.notional_usd:
            side = "LONG"
        else:
            side = "FLAT"
        return Position(usd_free=num(usd, "Free"), usd_lock=num(usd, "Lock"),
                        usd_short_collateral=num(usd, "ShortCollateral"),
                        coin_free=num(coin, "Free"), coin_lock=num(coin, "Lock"),
                        short_qty=short_qty, short_value=short_value, bid=bid,
                        ask=num(t, "MinAsk"), last=num(t, "LastPrice"), side=side)

    # ----- decision -------------------------------------------------------- #

    def decide(self, pos: Position, sma: float | None) -> tuple[str, str]:
        """Return (target, reason)."""
        cfg = self.cfg
        if cfg.kill_file.exists():
            return "FLAT", "KILL file present"
        if self.force_flip_min:
            phase = int((time.time() - self.started_at) / (self.force_flip_min * 60))
            return ("LONG" if phase % 2 == 0 else "FLAT"), f"force-flip phase {phase}"
        if sma is None:
            return pos.side, "insufficient price history; holding"
        if pos.last > sma:
            return "LONG", f"last {pos.last} > sma {sma:.2f}"
        return ("SHORT" if cfg.allow_short else "FLAT"), f"last {pos.last} <= sma {sma:.2f}"

    # ----- execution ------------------------------------------------------- #

    def send(self, action: str, request: dict[str, Any],
             call: Callable[[], dict[str, Any]]) -> dict[str, Any] | None:
        """Send one order (or log it in dry run). Never resends on failure: the
        next cycle re-reads the real position from the exchange instead."""
        rec: dict[str, Any] = {"action": action, "request": request,
                               "dry_run": self.cfg.dry_run, "cycle": self.cycle_no}
        if self.cfg.dry_run:
            self.logs.write("orders", rec)
            log.info("[DRY RUN] would %s %s", action, request)
            return None
        try:
            resp = call()
            rec["response"] = resp
            self.logs.write("orders", rec)
            log.info("%s sent: %s -> %s", action, request, _order_brief(resp))
            return resp
        except RoostooAPIError as exc:
            rec["error"] = exc.err_msg
            rec["response"] = exc.response
            self.logs.write("orders", rec)
            self.logs.error(f"order:{action}", exc)
            log.error("%s rejected: %s", action, exc.err_msg)
            return None
        except requests.RequestException as exc:
            rec["error"] = f"UNKNOWN OUTCOME ({type(exc).__name__}: {exc}); not resent"
            self.logs.write("orders", rec)
            raise

    def execute(self, pos: Position, target: str) -> list[str]:
        """Move from pos.side to target with MARKET orders. Exits before entries."""
        assert self.client is not None
        c, cfg = self.client, self.cfg
        ap = int(self.rules["AmountPrecision"])
        mini = float(self.rules["MiniOrder"])
        done: list[str] = []

        if pos.side == "SHORT" and target != "SHORT":
            self.send("SHORT_CLOSE", {"pair": cfg.pair}, lambda: c.short_close(cfg.pair))
            done.append("SHORT_CLOSE")

        if pos.side == "LONG" and target != "LONG":
            # Sell the actual free balance, rounded DOWN to AmountPrecision.
            qty = round_to_precision(pos.coin_free, ap)
            if float(qty) * pos.bid > mini:
                req = {"pair": cfg.pair, "side": "SELL", "type": "MARKET",
                       "quantity": fmt_decimal(qty)}
                self.send("SELL", req, lambda: c.place_order(cfg.pair, "SELL", qty, "MARKET"))
                done.append("SELL")
            else:
                log.info("sell skipped: %s %s is below MiniOrder", qty, cfg.coin)

        if target == "LONG" and pos.side != "LONG":
            usd_needed = cfg.notional_usd - pos.coin_value
            budget = min(usd_needed, pos.usd_free / 1.002)  # leave room for the fee
            qty = round_to_precision(budget / pos.ask, ap) if pos.ask else 0
            if qty and float(qty) * pos.ask > mini:
                req = {"pair": cfg.pair, "side": "BUY", "type": "MARKET",
                       "quantity": fmt_decimal(qty)}
                self.send("BUY", req, lambda: c.place_order(cfg.pair, "BUY", qty, "MARKET"))
                done.append("BUY")
            else:
                log.warning("buy skipped: qty %s too small (usd_free=%.2f)", qty, pos.usd_free)

        if target == "SHORT" and pos.side != "SHORT":
            collateral = round(min(cfg.notional_usd, pos.usd_free / 1.002), 2)
            if collateral >= 1:
                req = {"pair": cfg.pair, "collateral": collateral}
                self.send("SHORT_OPEN", req, lambda: c.short_open(cfg.pair, collateral))
                done.append("SHORT_OPEN")
        return done

    # ----- one cycle ------------------------------------------------------- #

    def cycle(self) -> None:
        assert self.client is not None
        self.cycle_no += 1
        self.client.sync_clock()
        pos = self.read_position()
        self.history.add(int(time.time() * 1000), pos.last)
        self.history.save()
        sma = self.history.sma(self.cfg.sma_hours)
        target, reason = self.decide(pos, sma)
        kill = self.cfg.kill_file.exists()

        actions: list[str] = []
        if target != pos.side:
            actions = self.execute(pos, target)
        decision = {"cycle": self.cycle_no, "price": pos.last, "bid": pos.bid, "ask": pos.ask,
                    "sma": round(sma, 4) if sma else None, "sma_hours": self.cfg.sma_hours,
                    "history_hours": len(self.history.buckets), "current": pos.side,
                    "target": target, "reason": reason,
                    "action": "+".join(actions) if actions else
                    ("IDLE (KILL)" if kill else "HOLD"),
                    "dry_run": self.cfg.dry_run, "kill": kill}
        self.logs.write("decisions", decision)
        if actions:
            self.last_action = {"time": utc_iso(), "action": decision["action"],
                                "dry_run": self.cfg.dry_run}
            if not self.cfg.dry_run:
                time.sleep(1)
                pos = self.read_position()  # confirm the new state from the exchange
        log.info("cycle %d: price=%s sma=%s %s -> %s: %s | equity=%.2f", self.cycle_no,
                 pos.last, decision["sma"], decision["current"], target,
                 decision["action"], pos.equity)

        self.logs.write("equity", {"cycle": self.cycle_no, "usd": pos.usd_free + pos.usd_lock,
                                   "coin_qty": pos.coin_free + pos.coin_lock,
                                   "coin_value": round(pos.coin_value, 6),
                                   "short_value": round(pos.short_value, 6),
                                   "usd_short_collateral": pos.usd_short_collateral,
                                   "total_equity": round(pos.equity, 6),
                                   "position": pos.side, "price": pos.last})
        self.last_pos = pos
        self.heartbeat("running", pos)

    def heartbeat(self, status: str, pos: Position | None = None) -> None:
        write_json_atomic(self.cfg.state_dir / "heartbeat.json", {
            "time": utc_iso(), "ts": int(time.time() * 1000), "status": status,
            "pid": os.getpid(), "cycle": self.cycle_no, "interval_min": self.cfg.interval_min,
            "dry_run": self.cfg.dry_run, "force_flip_min": self.force_flip_min,
            "kill_active": self.cfg.kill_file.exists(),
            "key_label": self.client.key_label if self.client else None,
            "equity": round(pos.equity, 4) if pos else None,
            "position": pos.summary() if pos else None, "price": pos.last if pos else None,
            "last_action": self.last_action,
        })

    # ----- main loop ------------------------------------------------------- #

    def run(self) -> int:
        self.install_signal_handlers()
        self.startup()
        interval_s = self.cfg.interval_min * 60
        next_run = time.monotonic()
        while not self.stop_requested:
            self.sleep(next_run - time.monotonic())
            if self.stop_requested:
                break
            try:
                self.cycle()
                self.consecutive_net_errors = 0
                next_run += interval_s
            except requests.RequestException as exc:
                # Network trouble: retry sooner, backing off 15s, 30s, 60s ... <= interval.
                self.consecutive_net_errors += 1
                delay = min(15 * 2 ** (self.consecutive_net_errors - 1), interval_s)
                self.logs.error("cycle:network", exc)
                log.warning("network error (%s); retrying in %.0fs", exc, delay)
                next_run = time.monotonic() + delay
            except Exception as exc:  # never crash the loop
                self.logs.error("cycle", exc)
                log.exception("cycle %d failed; continuing", self.cycle_no)
                next_run += interval_s
            if self.max_cycles and self.cycle_no >= self.max_cycles:
                log.info("max cycles (%d) reached", self.max_cycles)
                break
            if next_run < time.monotonic():  # a cycle overran: don't burst to catch up
                next_run = time.monotonic()
        self.heartbeat("stopped", self.last_pos)
        log.info("stopped cleanly after %d cycles", self.cycle_no)
        return 0


def _order_brief(resp: dict[str, Any]) -> str:
    od = resp.get("OrderDetail") or resp
    keys = ("OrderID", "ID", "Status", "FilledQuantity", "FilledAverPrice",
            "CommissionChargeValue", "ShortQty", "EntryPrice", "ClosePrice", "ReturnAmount")
    return ", ".join(f"{k}={od[k]}" for k in keys if k in od)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", type=Path, default=HERE / "config.yaml")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--live", action="store_true", help="override config: dry_run=false")
    mode.add_argument("--dry-run", action="store_true", help="override config: dry_run=true")
    ap.add_argument("--interval-min", type=float, help="override interval_min")
    ap.add_argument("--force-flip-every", type=float, metavar="N",
                    help="TEST MODE: alternate LONG/FLAT every N minutes")
    ap.add_argument("--max-cycles", type=int, help="exit after N cycles (for tests)")
    args = ap.parse_args()

    cfg = load_config(args.config)
    if args.live:
        cfg.dry_run = False
    if args.dry_run:
        cfg.dry_run = True
    if args.interval_min:
        cfg.interval_min = args.interval_min
    setup_logging(cfg)
    try:
        return Bot(cfg, args.force_flip_every, args.max_cycles).run()
    except KeySafetyError as exc:
        log.error("SAFETY: %s", exc)
        return 2
    except KeyboardInterrupt:
        log.info("interrupted")
        return 130
    except Exception:  # startup failure (config, exchange not usable, ...)
        log.exception("fatal error during startup")
        return 1


if __name__ == "__main__":
    sys.exit(main())
