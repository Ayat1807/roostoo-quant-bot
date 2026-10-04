"""Per-coin trend capture: which Roostoo coins trend, and is it persistent?

    python -m lab.trend_capture

For each Roostoo crypto coin (data/roostoo_pairs.json, Binance history):
  * trend L/S: single-coin S3v2 signal, position = mean(sign of 24/72/168/336h returns)
    in [-1, 1], recomputed daily at 00:00 UTC, held 24h; 0.10% fee + 2 bps per unit
    of turnover
  * trend long-only: max(position, 0)
  * hold: buy and hold
  * efficiency ratio (Kaufman): |net move| / sum |hourly moves|, a strategy-free
    measure of how trendy the price path was
Periods: Jun-Oct 2026 (the team's quick test), OOS 2025-01 -> now, 2022-2024.
Persistence: Spearman rank correlation of coins' trend Sharpe between periods. If it
is near 0, "which coins trend best" in one period does not predict the next.
Writes reports/trend_capture.md.
"""

from __future__ import annotations

import sys

import numpy as np
import pandas as pd

from lab import ROOT
from lab.data import load_close
from lab.roostoo import binance_to_roostoo

HORIZONS = (24, 72, 168, 336)
COST = 0.001 + 0.0002
PERIODS = {"jun_oct_2026": ("2026-06-01", None), "oos_2025_26": ("2025-01-01", None),
           "is_2022_24": ("2022-01-01", "2024-12-31 23:00")}


def sharpe(r: pd.Series) -> float:
    r = r.dropna()
    return float(r.mean() / r.std() * np.sqrt(24 * 365)) if len(r) > 48 and r.std() > 0 else np.nan


def coin_table(c: pd.Series, start: str, end: str | None) -> dict[str, float]:
    sig = sum(np.sign(c / c.shift(h) - 1) for h in HORIZONS) / len(HORIZONS)
    daily = sig.where(sig.index.hour == 0).ffill()          # recompute at 00:00, hold 24h
    pos_ls, pos_lo = daily.shift(1), daily.clip(lower=0).shift(1)
    r = c.pct_change()
    s, e = pd.Timestamp(start, tz="UTC"), (pd.Timestamp(end, tz="UTC") if end else None)
    out = {}
    for name, pos in (("ls", pos_ls), ("lo", pos_lo)):
        net = (pos * r - pos.diff().abs() * COST).loc[s:e]
        out[f"{name}_ret"] = float((1 + net.fillna(0)).prod() - 1)
        out[f"{name}_sharpe"] = sharpe(net)
    rr = r.loc[s:e]
    out["hold_ret"] = float((1 + rr.fillna(0)).prod() - 1)
    out["hold_sharpe"] = sharpe(rr)
    px = c.loc[s:e].dropna()
    out["eff_ratio"] = float(abs(px.iloc[-1] - px.iloc[0]) / px.diff().abs().sum()) if len(px) > 48 else np.nan
    out["hours"] = int(len(px))
    return out


def main() -> int:
    pairs = binance_to_roostoo()
    assets = sorted(pairs)
    closes = load_close(assets, "2021-11-01")
    rows = []
    for a in assets:
        c = closes[a].dropna()
        for per, (s, e) in PERIODS.items():
            if len(c.loc[s:e]) < 24 * 60:
                continue
            rows.append({"coin": a.replace("USDT", ""), "period": per, **coin_table(c, s, e)})
    t = pd.DataFrame(rows)
    piv = t.pivot(index="coin", columns="period", values="ls_sharpe")
    L = ["# Per-coin trend capture (Roostoo crypto list)\n",
         "Single-coin S3v2 signal (mean sign of 24/72/168/336h returns), daily, 0.12% per unit turnover. "
         "`ER` = Kaufman efficiency ratio (trendiness, strategy-free). Sharpe annualised from hourly returns.\n"]
    L.append("## Persistence of 'which coins trend best'\n")
    L.append("| periods | coins | Spearman rank corr of trend L/S Sharpe |")
    L.append("|---|---|---|")
    for a_, b_ in (("is_2022_24", "oos_2025_26"), ("is_2022_24", "jun_oct_2026")):
        j = piv[[a_, b_]].dropna()
        L.append(f"| {a_} vs {b_} | {len(j)} | {j[a_].rank().corr(j[b_].rank()):+.2f} |")
    for per in ("jun_oct_2026", "oos_2025_26", "is_2022_24"):
        x = t[t.period == per].sort_values("ls_sharpe", ascending=False)
        L.append(f"\n## {per}: {len(x)} coins, sorted by trend L/S Sharpe\n")
        L.append(f"Median trend L/S Sharpe {x.ls_sharpe.median():.2f}; median hold Sharpe {x.hold_sharpe.median():.2f}; "
                 f"trend L/S beats hold on {(x.ls_sharpe > x.hold_sharpe).mean():.0%} of coins.\n")
        L.append("| coin | trend L/S ret | L/S Sharpe | long-only ret | LO Sharpe | hold ret | hold Sharpe | ER |")
        L.append("|---|---|---|---|---|---|---|---|")
        for _, r in x.iterrows():
            L.append(f"| {r.coin} | {r.ls_ret:+.1%} | {r.ls_sharpe:.2f} | {r.lo_ret:+.1%} | {r.lo_sharpe:.2f} | "
                     f"{r.hold_ret:+.1%} | {r.hold_sharpe:.2f} | {r.eff_ratio:.3f} |")
    path = ROOT / "reports" / "trend_capture.md"
    path.parent.mkdir(exist_ok=True)
    path.write_text("\n".join(L) + "\n", encoding="utf-8")
    t.to_csv(ROOT / "reports" / "trend_capture.csv", index=False)
    print("\n".join(L[:12]))
    focus = ["ENA", "ARB", "NEAR", "HBAR", "SEI", "LTC", "BTC", "ETH", "BNB", "DOGE"]
    print("\nTeam's quick-test coins, trend L/S Sharpe by period:")
    print(piv.reindex(focus)[["is_2022_24", "oos_2025_26", "jun_oct_2026"]].round(2).to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
