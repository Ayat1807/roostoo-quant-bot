"""Daily check: the testing bots and the live competition bot side by side. Read-only (no API calls, no writes).

    python daily_check.py                      # default: config.yaml, config_testing_hmm_cusum.yaml, config_competition_s3v2e.yaml
    python daily_check.py --config a.yaml b.yaml

Per bot: heartbeat age / status, key label, equity now / 24h ago / at its first record, positions (actual weights from the
latest snapshot + fills), HMM p_crisis and CUSUM cuts (if enabled), cuts fired, orders and errors in the last 24h.
Exit code 1 if any bot has a stale heartbeat or errors in the last 24h.
"""

from __future__ import annotations

import argparse
import sys
import time

import pandas as pd
import yaml

import status
from status import HERE, count_recent, tail_jsonl

DEFAULT = ["config.yaml", "config_testing_hmm_cusum.yaml", "config_competition_s3v2e.yaml"]


def equity_points(log_dir) -> tuple[float | None, float | None, float | None, str | None]:
    recs = tail_jsonl(log_dir / "equity.jsonl", 10**9)
    if not recs:
        return None, None, None, None
    now = recs[-1]
    ago = [r for r in recs if r["ts"] <= now["ts"] - 86400 * 1000]
    return now.get("equity"), (ago[-1].get("equity") if ago else None), recs[0].get("equity"), recs[0].get("time")


def row(cfg_name: str) -> dict:
    p = HERE / cfg_name
    if not p.exists():
        return {"config": cfg_name, "note": "config missing"}
    cfg = yaml.safe_load(p.read_text(encoding="utf-8"))
    d = status.build(cfg)
    if d is None:
        return {"config": cfg_name, "note": "never ran here (no heartbeat)"}
    hb, log_dir = d["hb"], d["log_dir"]
    age = (time.time() - hb["ts"] / 1000) / 60
    interval = (float(hb.get("poll_s") or 60) + float(hb.get("limit_wait_s") or 0)) / 60
    since = int((time.time() - 86400) * 1000)
    eq, eq24, eq0, t0 = equity_points(log_dir)
    pos = {k: v for k, v in (d["actual"] or {}).items() if abs(v) > 1e-3}
    cuts24 = tail_jsonl(log_dir / "decisions.jsonl", 10**9,
                        lambda r: r.get("event") == "changepoint_cut" and r.get("ts", 0) >= since)
    orders24 = count_recent(log_dir / "orders.jsonl", since)
    errs24 = count_recent(log_dir / "errors.jsonl", since)
    rg = hb.get("regime") or {}
    return {"config": cfg_name, "status": hb.get("status"), "age_min": age,
            "stale": age > 2 * interval and str(hb.get("status", "")).startswith("running"),
            "key": hb.get("key_label"), "dry": hb.get("dry_run"), "equity": eq, "eq24": eq24, "eq0": eq0, "t0": t0,
            "gross": sum(abs(v) for v in pos.values()), "net": sum(pos.values()), "pos": pos,
            "p_crisis": rg.get("p_crisis"), "cuts": hb.get("cuts"), "cuts24": sum(len(c.get("pairs", {})) for c in cuts24),
            "orders24": orders24, "errors24": errs24, "kill": d["kill"], "brake": hb.get("brake")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", nargs="+", default=DEFAULT)
    rows = [row(c) for c in ap.parse_args().config]
    pct = lambda a, b: "n/a" if a is None or not b else f"{a / b - 1:+.2%}"
    print(f"Daily check {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC\n")
    w = 34
    print(f"{'':22}" + "".join(f"{r['config'][:w-2]:<{w}}" for r in rows))
    lines = [
        ("heartbeat", lambda r: f"{r['status']} {r['age_min']:.0f} min{' STALE' if r['stale'] else ''}"),
        ("key / dry run / KILL", lambda r: f"{r['key']} / {r['dry']} / {'PRESENT' if r['kill'] else 'absent'}"),
        ("equity", lambda r: "n/a" if r["equity"] is None else f"${r['equity']:,.2f}"),
        ("24h change", lambda r: pct(r["equity"], r["eq24"])),
        ("since first record", lambda r: f"{pct(r['equity'], r['eq0'])} (from {str(r['t0'])[:10]})"),
        ("gross / net exposure", lambda r: f"{r['gross']:.0%} / {r['net']:+.0%}"),
        ("brake", lambda r: str(r["brake"])),
        ("HMM p_crisis", lambda r: "off" if r["p_crisis"] is None else f"{r['p_crisis']:.1%}"),
        ("CUSUM cuts active", lambda r: "off" if r["cuts"] is None else (", ".join(r["cuts"]) or "none")),
        ("cuts fired 24h", lambda r: "off" if r["cuts"] is None else str(r["cuts24"])),
        ("orders / errors 24h", lambda r: f"{r['orders24']} / {r['errors24']}"),
    ]
    for name, f in lines:
        print(f"{name:22}" + "".join(f"{(f(r) if 'note' not in r else r['note'] if name == 'heartbeat' else ''):<{w}}"
                                     for r in rows))
    print("\nPositions (weight of sizing equity):")
    for r in rows:
        if "note" in r:
            continue
        print(f"  {r['config']}: " + (", ".join(f"{p} {v:+.1%}" for p, v in sorted(r["pos"].items(), key=lambda x: -abs(x[1])))
                                      or "flat"))
    bad = any(r.get("stale") or r.get("errors24") for r in rows if "note" not in r)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
