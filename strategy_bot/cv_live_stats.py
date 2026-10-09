"""Live statistics from the bots' own logs (read-only; run on the machine that holds the logs, i.e. EC2).

    python cv_live_stats.py                      # print
    python cv_live_stats.py --json live_stats.json   # also write the numbers for strategy_lab/lab/cv_stats.py

Return and max drawdown from <logs>/equity.jsonl (account equity at each hourly step; max drawdown = worst fall from a
running peak); trades = order records with an exchange response in <logs>/orders.jsonl (fills of resting limit orders are
counted once, at placement). Nothing is estimated; a missing log is reported as "not computed".
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
S3V2E_START = pd.Timestamp("2026-10-07 10:04", tz="UTC")
ACCOUNT_START = pd.Timestamp("2026-10-06 15:30", tz="UTC")
XSMOM_END = pd.Timestamp("2026-10-07 10:00", tz="UTC")


def read(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for ln in path.read_text(encoding="utf-8").splitlines():
        try:
            out.append(json.loads(ln))
        except ValueError:
            continue
    return out


def stats(eq: pd.Series, trades: int) -> dict | None:
    eq = eq.dropna()
    if len(eq) < 2:
        return None
    return {"from": f"{eq.index[0]:%Y-%m-%d %H:%M}", "to": f"{eq.index[-1]:%Y-%m-%d %H:%M}",
            "days": (eq.index[-1] - eq.index[0]) / pd.Timedelta(days=1), "start_equity": float(eq.iloc[0]),
            "end_equity": float(eq.iloc[-1]), "return": float(eq.iloc[-1] / eq.iloc[0] - 1),
            "mdd": float((eq / eq.cummax() - 1).min()), "trades": int(trades)}


def series(log_dir: str, start: pd.Timestamp, end: pd.Timestamp | None = None) -> tuple[pd.Series, int]:
    eq = read(HERE / log_dir / "equity.jsonl")
    s = pd.Series({pd.Timestamp(r["time"]): float(r["equity"]) for r in eq if "equity" in r}, dtype=float).sort_index()
    if s.empty:
        return s, 0
    s = s[(s.index >= start) & ((s.index <= end) if end is not None else True)]
    od = [r for r in read(HERE / log_dir / "orders.jsonl") if "response" in r and not r.get("dry_run")]
    n = sum(1 for r in od if pd.Timestamp(r["time"]) >= start and (end is None or pd.Timestamp(r["time"]) <= end))
    return s, n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", type=Path)
    a = ap.parse_args()
    out = {}
    s, n = series("logs_competition_s3v2e", S3V2E_START)
    out["s3v2e_competition"] = stats(s, n)
    h, nh = series("logs_testing_hmm", pd.Timestamp("2000-01-01", tz="UTC"))
    out["hmm_testing"] = stats(h, nh)
    x, nx = series("logs_competition", ACCOUNT_START, XSMOM_END)
    acct = pd.concat([x, s]).sort_index()
    out["competition_account"] = stats(acct, nx + n) if len(x) and len(s) else None
    labels = {"s3v2e_competition": "s3v2e_core10, competition key (from 2026-10-07 10:04 UTC)",
              "hmm_testing": "HMM2 + CUSUM, testing key (from its start)",
              "competition_account": "whole competition account since 2026-10-06 15:30 UTC (xsmom until 10-07 10:00, then s3v2e)"}
    for k, d in out.items():
        print(f"{labels[k]}: " + ("not computed (log missing here)" if not d else
              f"{d['from']} to {d['to']} UTC ({d['days']:.1f} days), equity ${d['start_equity']:,.2f} -> "
              f"${d['end_equity']:,.2f}, return {d['return']:+.2%}, max drawdown {d['mdd']:.2%}, trades {d['trades']}"))
    if a.json:
        a.json.write_text(json.dumps({k: v for k, v in out.items() if v}, indent=1))
        print(f"wrote {a.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
