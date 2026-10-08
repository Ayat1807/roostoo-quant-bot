"""Block 10: intraday jump premise test (definitions in variants_b10_jumps.yaml). Report: reports/jump_premise.md

    python -m lab.jump_premise
"""

from __future__ import annotations

import sys

import numpy as np
import pandas as pd

from lab import ROOT
from lab.klines5m import OUT as K5
from lab.universe import Universe, _daily, stock_tokens

H = {"1h": 12, "3h": 36, "6h": 72, "12h": 144}
COST = 0.0025
IS0, IS1 = pd.Timestamp("2023-01-01", tz="UTC"), pd.Timestamp("2024-12-31 23:59", tz="UTC")
OOS0, OOS1 = pd.Timestamp("2025-01-01", tz="UTC"), pd.Timestamp("2026-06-30 23:59", tz="UTC")
INFO0 = pd.Timestamp("2026-07-01", tz="UTC")


def membership() -> pd.DataFrame:
    d = _daily()
    close, qv = d["close"], d["quote_volume"]
    u = Universe({"type": "satellite", "rule": "R1"})
    stocks = set(stock_tokens())
    pool = [a for a in close.columns if "~" not in a and a in u._roostoo and a not in stocks and a != "BTCUSDT"]
    hist = close[pool].notna().cumsum()
    mqv = qv[pool].rolling(30, min_periods=30).mean()
    mem = pd.DataFrame(False, index=close.index, columns=pool)
    tz = close.index.tz
    for ms in pd.date_range(pd.Timestamp("2022-12-01", tz=tz), close.index[-1], freq="MS"):
        prev = ms - pd.Timedelta(days=1)
        if prev not in close.index:
            continue
        ok = (hist.loc[prev] >= 90) & (mqv.loc[prev] >= 5e6)
        mem.loc[(mem.index >= ms) & (mem.index < ms + pd.DateOffset(months=1)), list(ok[ok].index)] = True
    return mem


def coin_events(sym: str, btc: pd.DataFrame, mem: pd.Series) -> list[dict]:
    p = K5 / f"{sym}.pkl"
    if not p.exists():
        return []
    df = pd.read_pickle(p)
    idx = btc.index
    c = df["close"].astype("float64").reindex(idx)
    first, last = df.index[0], df.index[-1]
    c = c.where((idx >= first) & (idx <= last)).ffill(limit=12)
    qv = df["qv"].astype("float64").reindex(idx).fillna(0.0)
    r = np.log(c).diff()
    rb = np.log(btc["close"].astype("float64")).diff()
    # hourly beta, 30 days ending at the previous full hour
    ch, bh = c.resample("1h").last(), btc["close"].astype("float64").resample("1h").last()
    rh, rbh = np.log(ch).diff(), np.log(bh).diff()
    beta_h = (rh.rolling(720, min_periods=600).cov(rbh) / rbh.rolling(720, min_periods=600).var()).shift(1)
    vavg_h = qv.resample("1h").sum().rolling(720, min_periods=600).mean().shift(1)
    hour = idx.floor("h")
    beta = pd.Series(beta_h.reindex(hour).values, index=idx)
    vavg = pd.Series(vavg_h.reindex(hour).values, index=idx)
    e = (r - beta * rb).fillna(0.0)
    R2 = e.rolling(24).sum()
    v2 = qv.rolling(24).sum()
    ratio = v2 / (2 * vavg)
    days = idx.floor("D") if mem.index.tz is not None else idx.floor("D").tz_localize(None)
    member = pd.Series(mem.reindex(days).values, index=idx).fillna(False).astype(bool)
    cand = (R2.abs() >= 0.05) & (ratio >= 3) & member & beta.notna() & c.notna()
    cs = e.cumsum().values
    qa = qv.values
    pos = np.where(cand.values)[0]
    out, nxt = [], -1
    n = len(idx)
    for i in pos:
        if i < nxt or i + 144 >= n:
            continue
        nxt = i + 144
        sg = float(np.sign(R2.iat[i]))
        row = {"time": idx[i], "asset": sym, "dir": "up" if sg > 0 else "down", "move": float(R2.iat[i]),
               "vol_ratio": float(ratio.iat[i]), "beta": float(beta.iat[i]),
               "capacity": float(0.05 * qa[i + 1:i + 4].sum())}
        for k, h in H.items():
            row[f"C_{k}"] = sg * float(cs[i + h] - cs[i])
        out.append(row)
    return out


def clustered(x: pd.DataFrame, col: str) -> dict:
    if len(x) < 10:
        return {"n": len(x)}
    m = x[col].mean()
    e = (x[col] - m).groupby(x["time"].dt.floor("D")).sum()
    se = float(np.sqrt((e ** 2).sum()) / len(x))
    return {"n": int(len(x)), "mean": float(m), "median": float(x[col].median()), "hit": float((x[col] > 0).mean()),
            "t": float(m / se) if se > 0 else np.nan}


def main() -> int:
    btc = pd.read_pickle(K5 / "BTCUSDT.pkl")
    btc = btc[~btc.index.duplicated()]
    full = pd.date_range(btc.index[0], btc.index[-1], freq="5min", tz="UTC")
    btc = btc.reindex(full).ffill()
    mem = membership()
    rows = []
    for sym in mem.columns:
        rows += coin_events(sym, btc, mem[sym])
        print(f"  {sym}: {len(rows)} events so far", flush=True)
    ev = pd.DataFrame(rows)
    ev.to_pickle(ROOT / ".cache" / "jump_events.pkl")
    for k in H:
        ev[f"N_{k}"] = ev[f"C_{k}"] - COST
        ev[f"Nh_{k}"] = ev[f"C_{k}"] - COST * (1 + ev["beta"].abs())
    halves = {"IS (2023-2024)": (IS0, IS1), "OOS (2025-01 to 2026-06)": (OOS0, OOS1), "Jul-Sep 2026 (info)": (INFO0, None)}
    tod = lambda x: pd.cut(x["time"].dt.hour, [0, 6, 12, 18, 24], right=False, labels=["00-06", "06-12", "12-18", "18-24"])
    subsets = {"ALL (bot subset)": lambda x: x, "volume >= 5x": lambda x: x[x.vol_ratio >= 5],
               "move 5-10%": lambda x: x[x.move.abs() < 0.10], "move 10-20%": lambda x: x[(x.move.abs() >= 0.10) & (x.move.abs() < 0.20)],
               "move >= 20%": lambda x: x[x.move.abs() >= 0.20], "up": lambda x: x[x.dir == "up"], "down": lambda x: x[x.dir == "down"],
               **{f"UTC {b}": (lambda b: lambda x: x[tod(x) == b])(b) for b in ["00-06", "06-12", "12-18", "18-24"]}}
    pct = lambda v: "" if v is None or (isinstance(v, float) and np.isnan(v)) else f"{v:+.2%}"
    L = ["# Block 10: intraday jump premise test\n",
         f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by `python -m lab.jump_premise`; definitions in "
         "`variants_b10_jumps.yaml` (declared before computing). Event: residual (beta-adjusted vs BTC) 2h move >= +/-5% with 2h "
         "volume >= 3x its 30-day hourly average; outcome = next-h-hour residual return in the move's direction, net of 0.25%. "
         "Cells: mean net / t (clustered by day)._\n"]
    weeks = lambda a, b: ((b or ev["time"].max()) - a).days / 7
    L += ["## How often, and capacity\n", "| period | events | events per week | median capacity (5% of the next 15 min volume) | "
          "10th percentile |", "|---|---|---|---|---|"]
    for k, (a, b) in halves.items():
        x = ev[(ev["time"] >= a) & (ev["time"] <= (b or ev["time"].max()))]
        L.append(f"| {k} | {len(x)} | {len(x) / weeks(a, b):.1f} | ${x['capacity'].median():,.0f} | ${x['capacity'].quantile(0.1):,.0f} |")
    verdict = {}
    for k, (a, b) in halves.items():
        x = ev[(ev["time"] >= a) & (ev["time"] <= (b or ev["time"].max()))]
        L += [f"\n## {k}: net residual return after the signal (cost 0.25%)\n",
              "| subset | n | 1h | 3h | 6h | 12h | 3h hit rate | 3h net with BTC hedge cost |", "|---|---|---|---|---|---|---|---|"]
        for sn, f in subsets.items():
            y = f(x)
            cells, n = [], len(y)
            for hk in H:
                s = clustered(y, f"N_{hk}")
                verdict[(k, sn, hk)] = s
                cells.append(f"{pct(s.get('mean'))} / {s.get('t', float('nan')):+.1f}" if s.get("n", 0) >= 10 else "")
            s3, sh = clustered(y, "C_3h"), clustered(y, "Nh_3h")
            L.append(f"| {sn} | {n} | " + " | ".join(cells) + f" | {s3.get('hit', float('nan')):.0%} | {pct(sh.get('mean'))} |")
    passing = [hk for hk in H if all(verdict.get((k, "ALL (bot subset)", hk), {}).get("mean", -1) > 0
                                     and verdict.get((k, "ALL (bot subset)", hk), {}).get("t", 0) >= 2 for k in list(halves)[:2])]
    go = bool(passing)
    L.insert(2, f"**Verdict (declared rule: the bot subset, at least one horizon, mean net > 0 with t >= 2 in BOTH halves): "
                f"{'GO at ' + ', '.join(passing) + ' (caveat: 4 horizons tested)' if go else 'NO-GO: recorded as a finding; no capture bot'}**\n")
    (ROOT / "reports" / "jump_premise.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
