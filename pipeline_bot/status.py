"""Quick health check for the pipeline bot. Read-only: makes no API calls.

    python status.py

Shows heartbeat age (WARN if older than 2 intervals), equity, position,
the last 5 decisions, the last 5 orders and the error count over the last 24h.
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


def tail_jsonl(path: Path, n: int) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        lines = deque((ln for ln in fh if ln.strip()), maxlen=n)
    out = []
    for ln in lines:
        try:
            out.append(json.loads(ln))
        except ValueError:
            pass
    return out


def count_recent(path: Path, since_ms: int) -> int:
    if not path.exists():
        return 0
    n = 0
    with path.open(encoding="utf-8") as fh:
        for ln in fh:
            try:
                if json.loads(ln).get("ts", 0) >= since_ms:
                    n += 1
            except ValueError:
                continue
    return n


def main() -> int:
    cfg = yaml.safe_load((HERE / "config.yaml").read_text(encoding="utf-8"))
    paths = cfg.get("paths", {})
    log_dir = HERE / paths.get("log_dir", "logs")
    state_dir = HERE / paths.get("state_dir", "state")
    kill = HERE / paths.get("kill_file", "KILL")
    rc = 0

    hb_path = state_dir / "heartbeat.json"
    if not hb_path.exists():
        print("NO HEARTBEAT: bot has never run here (state/heartbeat.json missing)")
        return 2
    hb = json.loads(hb_path.read_text(encoding="utf-8"))
    age_s = time.time() - hb["ts"] / 1000
    interval_s = float(hb.get("interval_min") or cfg["interval_min"]) * 60
    stale = age_s > 2 * interval_s and hb.get("status") == "running"
    flag = "WARN: STALE" if stale else "ok"
    if stale:
        rc = 1
    print(f"Heartbeat: {hb['time']}  age {age_s/60:.1f} min  [{flag}]  status={hb.get('status')} "
          f"cycle={hb.get('cycle')} pid={hb.get('pid')}")
    print(f"Mode: dry_run={hb.get('dry_run')} key={hb.get('key_label')} "
          f"interval={hb.get('interval_min')}min force_flip={hb.get('force_flip_min')} "
          f"KILL file={'PRESENT' if kill.exists() else 'absent'}")
    pos = hb.get("position") or {}
    if hb.get("equity") is not None:
        print(f"Equity: ${hb['equity']:,.2f}  position={pos.get('side')}  "
              f"USD={pos.get('usd_free', 0) + pos.get('usd_lock', 0):,.2f}  "
              f"coin={pos.get('coin_free', 0) + pos.get('coin_lock', 0):g} "
              f"(${pos.get('coin_value', 0):,.2f})  short=${pos.get('short_value', 0):,.2f}  "
              f"price={hb.get('price')}")
    print(f"Last action: {hb.get('last_action')}")

    print("\nLast 5 decisions:")
    for d in tail_jsonl(log_dir / "decisions.jsonl", 5):
        if d.get("event"):
            print(f"  {d['time']}  {d['event']}  {d.get('position', {}).get('side')}")
            continue
        print(f"  {d['time']}  #{d.get('cycle')} price={d.get('price')} sma={d.get('sma')} "
              f"{d.get('current')}->{d.get('target')}  {d.get('action')}"
              f"{'  [dry]' if d.get('dry_run') else ''}")

    print("\nLast 5 orders:")
    orders = tail_jsonl(log_dir / "orders.jsonl", 5)
    if not orders:
        print("  none")
    for o in orders:
        r = o.get("response") or {}
        od = r.get("OrderDetail") or r
        result = (f"{od.get('Status')} qty={od.get('FilledQuantity')} "
                  f"@ {od.get('FilledAverPrice')} fee={od.get('CommissionChargeValue')}"
                  if od else "")
        print(f"  {o['time']}  {o.get('action')} {o.get('request', {}).get('quantity', '')}  "
              f"{'[DRY RUN]' if o.get('dry_run') else result}"
              f"{'  ERROR: ' + str(o['error']) if o.get('error') else ''}")

    n_err = count_recent(log_dir / "errors.jsonl", int((time.time() - 86400) * 1000))
    print(f"\nErrors in last 24h: {n_err}")
    if n_err:
        last = tail_jsonl(log_dir / "errors.jsonl", 1)[0]
        print(f"  latest: {last['time']} [{last.get('where')}] {last.get('type')}: "
              f"{last.get('message', '')[:150]}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
