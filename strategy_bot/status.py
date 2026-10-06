"""Health check for strategy_bot. Read-only: no API calls.

    python status.py                                   # config.yaml (testing bot)
    python status.py --config config_competition.yaml  # the competition bot

Heartbeat age (WARN if older than 2 intervals, where an interval is one poll plus one
limit-order wait), equity and brake, a target-vs-actual weight table per pair, the last
5 decisions, the last 5 orders and the error count over the last 24h.
"""

from __future__ import annotations

import json
import sys
import time
from collections import deque
from pathlib import Path
from typing import Any

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


def fmt_w(w: float | None) -> str:
    return "   -   " if w is None else f"{w:+7.2%}"


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    cfg = yaml.safe_load((HERE / ap.parse_args().config).read_text(encoding="utf-8"))
    paths = cfg.get("paths", {})
    log_dir = HERE / paths.get("log_dir", "logs")
    state_dir = HERE / paths.get("state_dir", "state")
    kill = HERE / paths.get("kill_file", "KILL")
    hb_path = state_dir / "heartbeat.json"
    if not hb_path.exists():
        print("NO HEARTBEAT: the bot has never run here (state/heartbeat.json missing)")
        return 2
    hb = json.loads(hb_path.read_text(encoding="utf-8"))
    rc = 0

    age = time.time() - hb["ts"] / 1000
    interval = float(hb.get("poll_s") or 60) + float(hb.get("limit_wait_s") or 0)
    stale = age > 2 * interval and str(hb.get("status", "")).startswith("running")
    if stale:
        rc = 1
    print(f"Heartbeat: {hb['time']}  age {age/60:.1f} min  [{'WARN: STALE' if stale else 'ok'}]  "
          f"status={hb.get('status')}  poll #{hb.get('cycle')}")
    print(f"Mode: strategy={hb.get('strategy')} dry_run={hb.get('dry_run')} key={hb.get('key_label')} "
          f"cap=${hb.get('capital_cap_usd')} allow_short={hb.get('allow_short')} "
          f"KILL={'PRESENT' if kill.exists() else 'absent'}")
    eq, se = hb.get("equity"), hb.get("sizing_equity")
    if eq is not None:
        print(f"Equity: ${eq:,.2f} (sizing ${se:,.2f})  USD ${hb.get('usd') or 0:,.2f}  "
              f"brake: x{hb.get('mult')} ({hb.get('brake')})  last trade day: {hb.get('last_trade_day')}")
    print(f"Targets computed: {hb.get('target_time')}")

    tgt, act = hb.get("target") or {}, hb.get("actual") or {}
    mult = hb.get("mult") or 0
    band = float(cfg.get("band", 0.06))
    print(f"\n{'pair':<10}{'target':>9}{'x brake':>9}{'actual':>9}{'diff':>9}  note")
    for p in hb.get("pairs") or sorted(set(tgt) | set(act)):
        t, a = tgt.get(p), act.get(p)
        te = None if t is None else t * mult
        d = None if te is None or a is None else a - te
        note = "outside band" if d is not None and abs(d) > band else ""
        print(f"{p:<10}{fmt_w(t):>9}{fmt_w(te):>9}{fmt_w(a):>9}{fmt_w(d):>9}  {note}")
    gt = sum(abs(v) for v in tgt.values()) if tgt else 0
    ga = sum(abs(v) for v in act.values()) if act else 0
    print(f"{'gross':<10}{gt:>+8.2%}{gt*mult:>+9.2%}{ga:>+9.2%}")

    print("\nLast 5 decisions:")
    for d in tail_jsonl(log_dir / "decisions.jsonl", 5):
        ev = d.get("event")
        if ev == "rebalance":
            plan = ", ".join(f"{x['action']} {x['pair']} ${x['usd']:,.0f}" for x in d.get("plan", []))
            print(f"  {d['time']}  rebalance [{d.get('reason')}] band={d.get('band')} "
                  f"orders={d.get('orders')}  {plan or 'no trades needed'}")
        elif ev == "targets":
            nz = {p: round(w, 3) for p, w in d.get("target", {}).items() if w}
            print(f"  {d['time']}  targets [{d.get('reason')}] gross={d.get('gross')} {nz}")
        else:
            print(f"  {d['time']}  {ev}")

    print("\nLast 5 orders:")
    orders = tail_jsonl(log_dir / "orders.jsonl", 5)
    if not orders:
        print("  none")
    for o in orders:
        req = o.get("request") or {}
        r = o.get("response") or {}
        od = r.get("OrderDetail") or r
        res = (f"{od.get('Status', '')} filled={od.get('FilledQuantity', od.get('ShortQty', ''))} "
               f"@ {od.get('FilledAverPrice', od.get('EntryPrice', od.get('ClosePrice', '')))}") if od else ""
        print(f"  {o['time']}  {o.get('action')} {req.get('pair', o.get('pair', ''))} "
              f"qty={req.get('quantity', req.get('close_qty', ''))} coll={req.get('collateral', '')} "
              f"{'[DRY RUN]' if o.get('dry_run') else res}"
              f"{'  ERROR: ' + str(o['error'])[:80] if o.get('error') else ''}")

    n_err = count_recent(log_dir / "errors.jsonl", int((time.time() - 86400) * 1000))
    print(f"\nErrors in last 24h: {n_err}")
    if n_err:
        last = tail_jsonl(log_dir / "errors.jsonl", 1)[0]
        print(f"  latest: {last['time']} [{last.get('where')}] {last.get('type')}: "
              f"{str(last.get('message', ''))[:150]}")
        rc = max(rc, 1)
    return rc


if __name__ == "__main__":
    sys.exit(main())
