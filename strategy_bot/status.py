"""Health check for strategy_bot. Read-only: no API calls, no writes.

    python status.py                                   # config.yaml (testing bot)
    python status.py --config config_competition.yaml  # the competition bot

Heartbeat age (WARN if older than 2 intervals, where an interval is one poll plus one
limit-order wait), equity and brake, a target-vs-actual weight table, the last 5
decisions, the last 5 orders and the error count over the last 24h.

Sleeve mode (config `sleeves:`): one block per sleeve (weight, execution, last and next
decision, book equity, targets vs book weights), and the table lists only the active
universe (each sleeve's universe, for R1 the month's list in state/universe_r1.json, plus
anything still held).

"Actual" = the latest account snapshot (logs/equity.jsonl) plus the fills logged in
logs/orders.jsonl after that snapshot was taken. The bot snapshots the account before it
trades, so without the fills the table would show the pre-trade book until the next hour.
"""

from __future__ import annotations

import json
import sys
import time
from collections import deque
from pathlib import Path
from typing import Any

import pandas as pd
import yaml

HERE = Path(__file__).resolve().parent


def tail_jsonl(path: Path, n: int, pred: Any = None) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    out: deque = deque(maxlen=n)
    with path.open(encoding="utf-8") as fh:
        for ln in fh:
            try:
                rec = json.loads(ln)
            except ValueError:
                continue
            if pred is None or pred(rec):
                out.append(rec)
    return list(out)


def count_recent(path: Path, since_ms: int) -> int:
    return len(tail_jsonl(path, 10**9, lambda r: r.get("ts", 0) >= since_ms))


def read_json(path: Path) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def fmt_w(w: float | None) -> str:
    return "   -   " if w is None else f"{w:+7.2%}"


def _f(x: Any) -> float:
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def fills_usd(orders: list[dict[str, Any]]) -> dict[str, float]:
    """Signed USD of the fills in these order records (buy +, sell -), per pair.

    Live quirk: PENDING / CANCELED responses report FilledQuantity == Quantity, so only
    FILLED responses count. A limit order that rested is counted from its LIMIT_TIMEOUT
    record (filled qty measured from the balance, priced at the limit) or from its
    LIMIT_LATE_FILL 'filled while resting' record; a late fill 'before cancel took effect'
    is already inside LIMIT_TIMEOUT.filled. Dry-run and failed orders never filled."""
    out: dict[str, float] = {}
    placed: dict[Any, dict[str, Any]] = {}     # order_id -> request (side, price) of a resting limit

    def add(pair: str, side: str, qty: float, price: float) -> None:
        if pair and qty > 0 and price > 0:
            out[pair] = out.get(pair, 0.0) + (qty * price if side == "BUY" else -qty * price)

    for o in orders:
        if o.get("dry_run") or o.get("error"):
            continue
        a, req = o.get("action", ""), o.get("request") or {}
        r = o.get("response") or {}
        od = r.get("OrderDetail") or {}
        if a in ("OPEN_SHORT", "CLOSE_SHORT"):
            d = r.get("OrderDetail") or r
            if a == "OPEN_SHORT":
                add(req.get("pair"), "SELL", _f(d.get("ShortQty")), _f(d.get("EntryPrice")))
            else:
                add(req.get("pair"), "BUY", _f(d.get("ClosedQty") or d.get("ShortQty")), _f(d.get("ClosePrice")))
        elif a == "LIMIT_TIMEOUT":
            rq = placed.get(o.get("order_id"), {})
            add(o.get("pair"), rq.get("side", ""), _f(o.get("filled")), _f(rq.get("price")))
        elif a == "LIMIT_LATE_FILL":
            if o.get("status") == "FILLED" and o.get("how") == "filled while resting":
                add(o.get("pair"), o.get("side", ""), _f(o.get("filled_qty")), _f(o.get("avg_price")))
        elif od:
            if od.get("Status") == "FILLED":
                add(req.get("pair"), req.get("side", od.get("Side", "")), _f(od.get("FilledQuantity")),
                    _f(od.get("FilledAverPrice")))
            elif od.get("Status") == "PENDING":
                placed[od.get("OrderID")] = req
    return out


def actual_weights(log_dir: Path, sleeve_mode: bool) -> dict[str, Any]:
    """Latest account snapshot + fills since it was taken (see module docstring).

    Sleeve mode writes the step's equity record AFTER its orders (the snapshot itself is
    taken before them), so the fills to add are those after the PREVIOUS equity record;
    single-strategy mode writes the equity record before its orders."""
    eq = tail_jsonl(log_dir / "equity.jsonl", 2)
    if not eq:
        return {}
    last = eq[-1]
    if sleeve_mode:
        since = pd.Timestamp(eq[-2]["time"]) if len(eq) > 1 else None
        keep = (lambda r: since is None or pd.Timestamp(r["time"]) > since)
    else:
        since = pd.Timestamp(last["time"])
        keep = (lambda r: pd.Timestamp(r["time"]) >= since)
    orders = tail_jsonl(log_dir / "orders.jsonl", 10**9, lambda r: "time" in r and keep(r))
    fills = fills_usd(orders)
    expo = {p: _f(v) for p, v in (last.get("exposure") or {}).items()}
    for p, v in fills.items():
        expo[p] = expo.get(p, 0.0) + v
    sizing = _f(last.get("sizing_equity")) or _f(last.get("equity"))
    w = {p: (v / sizing if sizing else 0.0) for p, v in expo.items()}
    return {"snapshot_time": last.get("time"), "weights": w, "fills": fills, "n_fill_records": len(orders),
            "sizing_equity": sizing, "equity_record": last}


def next_decision(now: pd.Timestamp, hour: int) -> pd.Timestamp:
    t = now.floor("D") + pd.Timedelta(hours=hour)
    return t if t > now else t + pd.Timedelta(days=1)


def sleeve_view(cfg: dict[str, Any], state_dir: Path, log_dir: Path, act: dict[str, Any],
                mult: float, now: pd.Timestamp) -> dict[str, Any]:
    """Per-sleeve books/targets/decisions and the active universe (display data only)."""
    books = (read_json(state_dir / "sleeves.json") or {}).get("books", {})
    r1 = read_json(state_dir / "universe_r1.json")
    eq_rec = act.get("equity_record") or {}
    book_eq = eq_rec.get("sleeves") or {}
    last_dec: dict[str, dict] = {}
    for d in tail_jsonl(log_dir / "decisions.jsonl", 10**9,
                        lambda r: r.get("event") == "targets" and r.get("sleeve") and r.get("reason") != "restored"):
        last_dec[d["sleeve"]] = d
    sizing = act.get("sizing_equity") or 0.0
    total = sum(_f(b.get("equity")) for b in book_eq.values())
    cap = cfg.get("capital_cap_usd")
    scale = min(1.0, float(cap) / total) if cap and total > 0 else 1.0
    sleeves, universe, combined = [], [], {}
    for s in cfg["sleeves"]:
        name = str(s["name"])
        b = books.get(name) or {}
        if s.get("universe_rule"):
            uni = list((r1 or {}).get("selected") or [])
            src = (f"R1 list for {r1.get('month')} (as of {r1.get('as_of')}, selected {r1.get('selected_at')})"
                   if r1 else "R1 list not selected yet (state/universe_r1.json missing)")
        else:
            uni = list(s.get("universe") or cfg["universe"])
            src = "fixed list"
        strat = dict(s.get("strategy") or cfg["strategy"])
        if strat.get("btc_pair") and strat["btc_pair"] not in uni:
            uni.append(strat["btc_pair"])
        universe += [p for p in uni if p not in universe]
        tgt = {p: _f(w) for p, w in (b.get("target") or {}).items()}
        e = _f((book_eq.get(name) or {}).get("equity"))
        for p, w in tgt.items():
            if w and sizing:
                combined[p] = combined.get(p, 0.0) + w * mult * e * scale / sizing
        hour = int(s.get("decision_hour_utc", cfg.get("rebalance_hour_utc", 0)))
        ld = last_dec.get(name) or {}
        sleeves.append({
            "name": name, "weight": _f(s["weight"]), "strategy": strat.get("name"),
            "execution": s.get("execution", "band"), "decision_hour_utc": hour,
            "universe": uni, "universe_source": src, "target": tgt,
            "book_weights": (book_eq.get(name) or {}).get("weights") or {},
            "book_equity": e, "book_cash": (book_eq.get(name) or {}).get("cash"),
            "slot": b.get("slot"), "computed_at": b.get("computed_at"),
            "last_decision": {"time": ld.get("time"), "reason": ld.get("reason"), "bar_time": ld.get("bar_time"),
                              "skipped": ld.get("liquidity_skipped") or {}} if ld else None,
            "next_decision": str(next_decision(now, hour)),
        })
    held = sorted(p for p, w in (act.get("weights") or {}).items() if abs(w) > 1e-4 and p not in universe)
    held += sorted(p for b in books.values() for p in (b.get("units") or {})
                   if p not in universe and p not in held)
    return {"sleeves": sleeves, "universe": universe, "held_outside": held, "target": combined}


def build(cfg: dict[str, Any], base: Path = HERE, now: pd.Timestamp | None = None) -> dict[str, Any] | None:
    """Everything status shows, as data (tests use this). None if the bot never ran."""
    paths = cfg.get("paths", {})
    log_dir = base / paths.get("log_dir", "logs")
    state_dir = base / paths.get("state_dir", "state")
    hb = read_json(state_dir / "heartbeat.json")
    if hb is None:
        return None
    now = now if now is not None else pd.Timestamp.now(tz="UTC")
    sleeve_mode = bool(cfg.get("sleeves"))
    act = actual_weights(log_dir, sleeve_mode)
    actual = act.get("weights") if act else (hb.get("actual") or {})
    mult = _f(hb.get("mult")) if hb.get("mult") is not None else 1.0
    out: dict[str, Any] = {"hb": hb, "sleeve_mode": sleeve_mode, "actual": actual, "act": act, "mult": mult,
                           "kill": (base / paths.get("kill_file", "KILL")).exists(),
                           "log_dir": log_dir}
    if sleeve_mode:
        sv = sleeve_view(cfg, state_dir, log_dir, act, mult, now)
        out.update(sv)
        out["pairs"] = sv["universe"] + sv["held_outside"]
        out["target_x"] = sv["target"]                  # already x brake
    else:
        tgt = hb.get("target") or {}
        out["target_raw"] = tgt
        out["target_x"] = {p: w * mult for p, w in tgt.items()}
        out["pairs"] = hb.get("pairs") or sorted(set(tgt) | set(actual))
    return out


def render(cfg: dict[str, Any], d: dict[str, Any]) -> tuple[list[str], int]:
    hb, lines, rc = d["hb"], [], 0
    pr = lines.append
    age = time.time() - hb["ts"] / 1000
    interval = float(hb.get("poll_s") or 60) + float(hb.get("limit_wait_s") or 0)
    stale = age > 2 * interval and str(hb.get("status", "")).startswith("running")
    if stale:
        rc = 1
    pr(f"Heartbeat: {hb['time']}  age {age/60:.1f} min  [{'WARN: STALE' if stale else 'ok'}]  "
       f"status={hb.get('status')}  poll #{hb.get('cycle')}")
    mode = (", ".join(f"{s['name']} {s['weight']:g} ({s['strategy']}, {s['execution']} "
                      f"{s['decision_hour_utc']:02d}:00 UTC)" for s in d["sleeves"])
            if d["sleeve_mode"] else f"strategy={hb.get('strategy')}")
    pr(f"Mode: {'sleeves: ' if d['sleeve_mode'] else ''}{mode}  dry_run={hb.get('dry_run')} "
       f"key={hb.get('key_label')} cap=${hb.get('capital_cap_usd')} allow_short={hb.get('allow_short')} "
       f"KILL={'PRESENT' if d['kill'] else 'absent'}")
    eq, se = hb.get("equity"), hb.get("sizing_equity")
    if eq is not None:
        pr(f"Equity: ${eq:,.2f} (sizing ${se:,.2f})  USD ${hb.get('usd') or 0:,.2f}  "
           f"brake: x{hb.get('mult')} ({hb.get('brake')})  last trade day: {hb.get('last_trade_day')}")
    act = d["act"]
    if act:
        nf = len(act["fills"])
        pr(f"Actual: account snapshot {act['snapshot_time']}"
           f"{f' + fills since on {nf} pair(s)' if nf else ' (no fills since)'}")
    if not d["sleeve_mode"]:
        pr(f"Targets computed: {hb.get('target_time')}")
    rg = hb.get("regime")
    if rg:
        pr(f"HMM regime: p_crisis {float(rg.get('p_crisis', 0)):.1%} on {rg.get('day')} "
           f"(model {rg.get('month_model', rg.get('reason', ''))}) -> targets x {1 - 0.5 * float(rg.get('p_crisis', 0)):.2f}, "
           f"short scale in bull {0.5 + 0.5 * float(rg.get('p_crisis', 0)):.2f}")
    nw = hb.get("news")
    if nw:
        pr(f"News layer ({'SHADOW' if nw.get('shadow') else 'LIVE'}): gross actual {nw.get('gross_actual', 0):.1%} vs "
           f"would-be {nw.get('gross_would', 0):.1%}; rules: {', '.join(nw.get('fired') or []) or 'none'}")
        shadow = tail_jsonl(d["log_dir"] / "news_shadow.jsonl", 10**9,
                            lambda r: r.get("event") in ("item", "daily_summary", "cost_cap", "llm_invalid")
                            or (r.get("event") == "step" and r.get("fired")))[-5:]
        for r in shadow:
            if r["event"] == "item":
                o = r.get("llm") or {}
                pr(f"  {r['time'][:16]} {r.get('source')}: {r.get('headline', '')[:70]} -> {o.get('coin')} {o.get('event_type')} "
                   f"{o.get('direction')} sev {o.get('severity')} conf {o.get('confidence')}"
                   f"{' => ' + r['rule'] if r.get('rule') else ''}")
            elif r["event"] == "step":
                pr(f"  {r['time'][:16]} would: {', '.join(r.get('fired') or [])}; gross {r.get('gross_actual', 0):.1%} -> "
                   f"{r.get('gross_would', 0):.1%}; extra trades {r.get('would_trade_extra')}")
            else:
                pr(f"  {r['time'][:16]} {r['event']}: " + ", ".join(f"{k}={v}" for k, v in r.items()
                                                                   if k not in ("time", "ts", "event"))[:150])
    if hb.get("cuts") is not None:
        cuts = hb.get("cuts") or {}
        pr(f"CUSUM cuts since bar {hb.get('cut_reset_bar')}: "
           + (", ".join(f"{p} x{f:g}" for p, f in cuts.items()) if cuts else "none active"))
    for s in d.get("sleeves", []):
        ld = s["last_decision"]
        pr(f"\nSleeve {s['name']}: weight {s['weight']:g}, {s['strategy']}, {s['execution']}, "
           f"book equity ${s['book_equity']:,.2f} (cash ${_f(s['book_cash']):,.2f})")
        pr(f"  last decision: {ld['time'] + ' (' + str(ld['reason']) + ', bar ' + str(ld['bar_time']) + ')' if ld else 'none logged'}"
           f"; targets in force: slot {s['slot']}, computed {s['computed_at']}")
        if ld and ld["skipped"]:
            pr(f"  liquidity guard skipped: {ld['skipped']}")
        pr(f"  next decision: {s['next_decision']}")
        pr(f"  universe ({len(s['universe'])}): {s['universe_source']}: {', '.join(s['universe'])}")
        nz = {p: w for p, w in s["target"].items() if abs(w) > 1e-9}
        pr(f"  target (gross {sum(abs(w) for w in nz.values()):.0%}): "
           + (", ".join(f"{p} {w:+.1%}" for p, w in sorted(nz.items(), key=lambda x: -abs(x[1]))) or "all cash"))
        bw = {p: _f(w) for p, w in s["book_weights"].items() if abs(_f(w)) > 1e-6}
        pr(f"  book    (gross {sum(abs(w) for w in bw.values()):.0%}): "
           + (", ".join(f"{p} {w:+.1%}" for p, w in sorted(bw.items(), key=lambda x: -abs(x[1]))) or "all cash"))
    if d.get("held_outside"):
        pr(f"\nHeld outside the active universe: {', '.join(d['held_outside'])}")

    tx, actual = d["target_x"], d["actual"]
    band = float(cfg.get("band", 0.06))
    band_pairs = ({p for s in d["sleeves"] if s["execution"] == "band" for p in s["universe"]}
                  if d["sleeve_mode"] else set(d["pairs"]))
    if d["sleeve_mode"]:
        pr(f"\n{'pair':<12}{'target':>9}{'actual':>9}{'diff':>9}  note   (target = sleeves' targets x brake, "
           f"share of sizing equity)")
    else:
        pr(f"\n{'pair':<12}{'target':>9}{'x brake':>9}{'actual':>9}{'diff':>9}  note")
    for p in d["pairs"]:
        te, a = tx.get(p, 0.0 if d["sleeve_mode"] else None), actual.get(p)
        a = 0.0 if a is None and d["sleeve_mode"] else a
        dd = None if te is None or a is None else a - te
        note = "outside band" if dd is not None and abs(dd) > band and p in band_pairs else ""
        if d["sleeve_mode"] and p in d.get("held_outside", []):
            note = (note + " held, not in universe").strip()
        if d["sleeve_mode"]:
            pr(f"{p:<12}{fmt_w(te):>9}{fmt_w(a):>9}{fmt_w(dd):>9}  {note}")
        else:
            t = d["target_raw"].get(p)
            pr(f"{p:<12}{fmt_w(t):>9}{fmt_w(te):>9}{fmt_w(a):>9}{fmt_w(dd):>9}  {note}")
    gt = sum(abs(v) for p, v in tx.items() if p in d["pairs"])
    ga = sum(abs(v) for p, v in actual.items() if p in d["pairs"] or abs(v) > 1e-4)
    if d["sleeve_mode"]:
        pr(f"{'gross':<12}{gt:>+8.2%}{ga:>+9.2%}")
    else:
        g0 = sum(abs(v) for v in d["target_raw"].values())
        pr(f"{'gross':<12}{g0:>+8.2%}{gt:>+9.2%}{ga:>+9.2%}")

    log_dir = d["log_dir"]
    pr("\nLast 5 decisions:")
    for x in tail_jsonl(log_dir / "decisions.jsonl", 5):
        ev = x.get("event")
        if ev == "rebalance":
            plan = ", ".join(f"{y['action']} {y['pair']} ${y['usd']:,.0f}" for y in x.get("plan", []))
            pr(f"  {x['time']}  rebalance [{x.get('reason')}] band={x.get('band')} "
               f"orders={x.get('orders')}  {plan or 'no trades needed'}")
        elif ev == "targets":
            nz = {p: round(w, 3) for p, w in x.get("target", {}).items() if w}
            sl = f" sleeve={x['sleeve']}" if x.get("sleeve") else ""
            pr(f"  {x['time']}  targets{sl} [{x.get('reason')}] gross={x.get('gross')} {nz}")
        elif ev == "universe_reselect":
            pr(f"  {x['time']}  universe_reselect as of {x.get('as_of')}: {len(x.get('selected') or [])} coins")
        else:
            pr(f"  {x['time']}  {ev}")

    pr("\nLast 5 orders:")
    orders = tail_jsonl(log_dir / "orders.jsonl", 5)
    if not orders:
        pr("  none")
    for o in orders:
        req = o.get("request") or {}
        r = o.get("response") or {}
        od = r.get("OrderDetail") or r
        if o.get("action") in ("LIMIT_TIMEOUT", "LIMIT_LATE_FILL", "CANCEL_STALE"):
            pr(f"  {o['time']}  {o['action']} {o.get('pair', '')} order {o.get('order_id')} "
               f"filled={o.get('filled', o.get('filled_qty', ''))} {o.get('final_status', o.get('status', ''))}")
            continue
        res = (f"{od.get('Status', '')} filled={od.get('FilledQuantity', od.get('ShortQty', ''))} "
               f"@ {od.get('FilledAverPrice', od.get('EntryPrice', od.get('ClosePrice', '')))}") if od else ""
        pr(f"  {o['time']}  {o.get('action')} {req.get('pair', o.get('pair', ''))} "
           f"qty={req.get('quantity', req.get('close_qty', ''))} coll={req.get('collateral', '')} "
           f"{'[DRY RUN]' if o.get('dry_run') else res}"
           f"{'  ERROR: ' + str(o['error'])[:80] if o.get('error') else ''}")

    n_err = count_recent(log_dir / "errors.jsonl", int((time.time() - 86400) * 1000))
    pr(f"\nErrors in last 24h: {n_err}")
    if n_err:
        last = tail_jsonl(log_dir / "errors.jsonl", 1)[0]
        pr(f"  latest: {last['time']} [{last.get('where')}] {last.get('type')}: "
           f"{str(last.get('message', ''))[:150]}")
        rc = max(rc, 1)
    return lines, rc


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    cfg = yaml.safe_load((HERE / ap.parse_args().config).read_text(encoding="utf-8"))
    d = build(cfg)
    if d is None:
        print("NO HEARTBEAT: the bot has never run here (heartbeat.json missing in the state dir)")
        return 2
    lines, rc = render(cfg, d)
    print("\n".join(lines))
    return rc


if __name__ == "__main__":
    sys.exit(main())
