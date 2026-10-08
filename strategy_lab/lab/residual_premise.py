"""Block 9 STEP 0: residual-momentum premise test (definitions in variants_b9_residual.yaml). Report: reports/residual_premise.md

    python -m lab.residual_premise
"""

from __future__ import annotations

import sys

import numpy as np
import pandas as pd

from lab import ROOT
from lab.b3 import INFO0, IS_END, OOS0, OOS_END
from lab.universe import Universe, _daily, stock_tokens

COST = 0.0024        # one hedged leg round trip: 2 x (0.10% taker + 0.02% slippage)


def events() -> tuple[pd.DataFrame, pd.Series, pd.DataFrame]:
    d = _daily()
    close, qv = d["close"], d["quote_volume"]
    u = Universe({"type": "satellite", "rule": "R1"})
    stocks = set(stock_tokens())
    pool = [a for a in close.columns if "~" not in a and a in u._roostoo and a not in stocks and a != "BTCUSDT"]
    r = np.log(close[pool + ["BTCUSDT"]]).diff()
    rb = r["BTCUSDT"]
    r = r[pool]
    hist = close[pool].notna().cumsum()
    mqv = qv[pool].rolling(30, min_periods=30).mean()
    # point-in-time beta from the 30 days ending t-1
    cov = r.rolling(30, min_periods=25).cov(rb).shift(1)
    var = rb.rolling(30, min_periods=25).var().shift(1)
    beta = cov.div(var, axis=0)
    s3 = r.rolling(3).sum()
    b3 = rb.rolling(3).sum()
    R3 = s3 - beta.mul(b3, axis=0)
    f3 = r.rolling(3).sum().shift(-3)
    fb3 = rb.rolling(3).sum().shift(-3)
    F3 = f3 - beta.mul(fb3, axis=0)
    vol_ratio = qv[pool] / qv[pool].rolling(30, min_periods=30).mean().shift(1)
    spike = (np.exp(r).sub(1).abs() > 0.25).rolling(3).max().astype(bool)
    # monthly membership (selected on the 1st from data up to the previous day)
    member = pd.DataFrame(False, index=r.index, columns=pool)
    for ms in pd.date_range(r.index[0].ceil("D") + pd.Timedelta(days=95), r.index[-1], freq="MS"):
        prev = ms - pd.Timedelta(days=1)
        if prev not in r.index:
            continue
        ok = (hist.loc[prev] >= 90) & (mqv.loc[prev] >= 5e6)
        end = ms + pd.DateOffset(months=1)
        member.loc[(member.index >= ms) & (member.index < end), list(ok[ok].index)] = True
    calm = b3.abs() <= 0.03
    cand = (R3.abs() >= 0.10) & member & calm.values[:, None] & beta.notna() & F3.notna()
    rows = []
    for a in pool:
        dates = cand.index[cand[a].values]
        last = None
        for t in dates:
            if last is not None and t <= last + pd.Timedelta(days=3):
                continue
            last = t
            sg = float(np.sign(R3.at[t, a]))
            c = sg * float(F3.at[t, a])
            cost = COST * (1 + abs(float(beta.at[t, a])))
            rows.append({"date": t, "asset": a, "dir": "up" if sg > 0 else "down", "R3": float(R3.at[t, a]),
                         "beta": float(beta.at[t, a]), "C": c, "C_net": c - cost,
                         "vol2x": bool(vol_ratio.at[t, a] >= 2) if pd.notna(vol_ratio.at[t, a]) else False,
                         "spike": bool(spike.at[t, a])})
    ev = pd.DataFrame(rows)
    return ev, b3, member


def clustered(x: pd.DataFrame, col: str) -> dict:
    if len(x) < 5:
        return {"n": len(x)}
    m = x[col].mean()
    e = (x[col] - m).groupby(x["date"]).sum()
    se = float(np.sqrt((e ** 2).sum()) / len(x))
    return {"n": int(len(x)), "dates": int(x["date"].nunique()), "mean": float(m), "median": float(x[col].median()),
            "hit": float((x[col] > 0).mean()), "t": float(m / se) if se > 0 else np.nan}


def main() -> int:
    ev, b3, member = events()
    halves = {"IS (2020-2024)": (None, IS_END), "OOS (2025-01 to 2026-06)": (OOS0, OOS_END), "Jul-Oct 2026 (info)": (INFO0, None)}
    pct = lambda v: "" if v is None or (isinstance(v, float) and np.isnan(v)) else f"{v:+.2%}"
    L = ["# Block 9 STEP 0: residual-momentum premise test\n",
         f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by `python -m lab.residual_premise`; definitions in "
         "`variants_b9_residual.yaml` (declared before computing). Events: |residual 3-day move| >= 10% while BTC's 3-day move is "
         "within +/-3%; continuation C = next-3-day residual return in the direction of the move; C_net after a hedged round "
         "trip (0.24% x (1 + |beta|))._\n"]
    # frequency
    days = b3.dropna().index
    calm_days = days[(b3.loc[days].abs() <= 0.03).values]
    ev_days = set(ev["date"])
    wk = b3.groupby(b3.index.to_period("W")).sum()
    rb7 = np.log(_daily()["close"]["BTCUSDT"]).diff().groupby(b3.index.to_period("W")).sum()
    calm_weeks = rb7[rb7.abs() < 0.03].index
    per_week = ev.groupby(ev["date"].dt.to_period("W"))["asset"].nunique()
    L += ["## How often\n", "| period | days | days with >= 1 event | calm-BTC days with >= 1 event | calm weeks | median event coins per "
          "calm week | mean universe size |", "|---|---|---|---|---|---|---|"]
    for k, (a, b) in halves.items():
        dd = days[(days >= (a or days[0])) & (days <= (b or days[-1]))]
        cd = [d for d in calm_days if (a is None or d >= a) and (b is None or d <= b)]
        cw = [w for w in calm_weeks if (a is None or w.start_time.tz_localize("UTC") >= a)
              and (b is None or w.end_time.tz_localize("UTC") <= b + pd.Timedelta(days=1))]
        med = float(per_week.reindex(cw).fillna(0).median()) if cw else np.nan
        usize = float(member.loc[dd].sum(axis=1).mean())
        L.append(f"| {k} | {len(dd)} | {sum(d in ev_days for d in dd) / len(dd):.0%} | "
                 f"{sum(d in ev_days for d in cd) / max(len(cd), 1):.0%} | {len(cw)} | {med:.0f} | {usize:.0f} |")
    # continuation
    L += ["\n## Do the moves continue? (next-3-day residual return in the move's direction)\n",
          "| period | subset | events (dates) | mean C | median C | hit C > 0 | mean C_net (after costs) | t (C_net, clustered by date) |",
          "|---|---|---|---|---|---|---|---|"]
    subsets = {"all": lambda x: x, "volume >= 2x": lambda x: x[x.vol2x], "volume < 2x": lambda x: x[~x.vol2x],
               "single-day spike > 25%": lambda x: x[x.spike], "no spike": lambda x: x[~x.spike],
               "ATTENTION (vol >= 2x, no spike)": lambda x: x[x.vol2x & ~x.spike],
               "up moves": lambda x: x[x.dir == "up"], "down moves": lambda x: x[x.dir == "down"]}
    verdict = {}
    for k, (a, b) in halves.items():
        x = ev[(ev["date"] >= (a or ev["date"].min())) & (ev["date"] <= (b or ev["date"].max()))]
        for sn, f in subsets.items():
            y = f(x)
            sc, sn_ = clustered(y, "C"), clustered(y, "C_net")
            if sn_.get("n", 0) < 5:
                L.append(f"| {k} | {sn} | {len(y)} | | | | | |")
                continue
            L.append(f"| {k} | {sn} | {sn_['n']} ({sn_['dates']}) | {pct(sc['mean'])} | {pct(sc['median'])} | {sc['hit']:.0%} | "
                     f"{pct(sn_['mean'])} | {sn_['t']:+.2f} |")
            verdict[(k, sn)] = sn_
    ok = lambda sn: all(verdict.get((k, sn), {}).get("mean", -1) > 0 and verdict.get((k, sn), {}).get("t", 0) >= 2
                        for k in list(halves)[:2])
    go = ok("all") or ok("ATTENTION (vol >= 2x, no spike)")
    L.insert(2, f"**Verdict (declared rule: mean C_net > 0 with t >= 2 in BOTH halves, overall or in the attention subset): "
                f"{'GO' if go else 'NO-GO: continuation is not positive after costs; the block stops here'}**\n")
    (ROOT / "reports" / "residual_premise.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    ev.to_csv(ROOT / ".cache" / "residual_events.csv", index=False)
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
