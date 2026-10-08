"""Block 8 (universe breadth / exposure, the last block): report and sweep resolver. Rules: variants_b8_breadth.yaml.

    python -m lab.b8 --resolve-sweep
    python -m lab.b8                 # leaderboard_b8.md

Each family is judged against its own core10 baseline: b8_s_* vs b3_s3v2e_core10, b8_h_* vs b7_hmm2_cusum.
"""

from __future__ import annotations

import argparse
import sys

import numpy as np
import pandas as pd

from lab import ROOT
from lab.b3 import IS_END, OOS0, OOS_END, fwd, windows
from lab.b4c import ls_detail
from lab.b5 import HALVES, beats_ref, btc, judge, rank
from lab.b6 import append, doc
from lab.b7 import margins
from lab.leaderboard import N01, declared_total
from lab.runner import HCACHE, load_hourly

FILE = "variants_b8_breadth.yaml"
BASE = {"s": "b3_s3v2e_core10", "h": "b7_hmm2_cusum"}
LABEL = {"s": "s3v2e (live)", "h": "HMM2 + CUSUM (forward test)"}


def broad_down_starts() -> pd.DatetimeIndex:
    """Window starts (daily) where BTC 14d < -5% AND > 70% of the Roostoo pool coins (>= 90 days of history) fell."""
    from lab.universe import Universe, _daily, stock_tokens
    close = _daily()["close"]
    u = Universe({"type": "satellite", "rule": "R1"})
    stocks = set(stock_tokens())
    pool = [a for a in close.columns if "~" not in a and a in u._roostoo and a not in stocks]
    c = close[pool]
    hist = c.notna().cumsum()
    r14 = c.shift(-14) / c - 1
    ok = (hist >= 90) & r14.notna()
    share_down = ((r14 < 0) & ok).sum(axis=1) / ok.sum(axis=1).replace(0, np.nan)
    b = btc().resample("1D").last()
    b14 = b.shift(-14) / b - 1
    df = pd.concat([share_down.rename("down"), b14.rename("btc")], axis=1).dropna()
    return df.index[(df["btc"] < -0.05) & (df["down"] > 0.70)]


def broad_down(name: str, starts: pd.DatetimeIndex) -> dict:
    h = load_hourly(name)
    out = {}
    for k, (a, b) in HALVES.items():
        w = windows(h, a, b)
        if w.empty:
            continue
        w = w[w["start"].isin(starts)]
        g = [float(h["gross"].loc[s:s + pd.Timedelta(days=14)].mean()) for s in w["start"]]
        out[k] = {"n": int(len(w)), "mean": float(w["ret"].mean()) if len(w) else None,
                  "pos": float((w["ret"] > 0).mean()) if len(w) else None, "gross": float(np.mean(g)) if g else None}
    return out


def floor_days() -> pd.DatetimeIndex:
    """Daily decisions (00:00 bar, core10) where the U6 floor fires: >= 7 of 10 coins share the signal sign and the s3v2e
    gross (floor off) is in (0, 50%). Data-determined, identical for both families."""
    from lab.data import load_close
    from lab.runner import resolve_base
    from lab.strategies import get_strategy
    p = resolve_base("b3_s3v2e_core10")
    assets = p["universe"]["assets"]
    c = load_close(assets)
    s3 = get_strategy("s3v2x")
    hz = p["params"]["horizons"]
    fired = []
    for i in np.where(c.index.hour == 0)[0]:
        if i < 800:
            continue
        win = c.iloc[i - 799:i + 1].dropna(axis=1, how="any")
        if len(win.columns) < 10:
            continue
        w = s3.target_weights(win, p["params"])
        last = win.iloc[-1]
        sig = sum(np.sign(last / win.iloc[-1 - h] - 1) for h in hz) / len(hz)
        agree = max(int((sig > 0).sum()), int((sig < 0).sum()))
        g = sum(abs(v) for v in w.values())
        if agree >= 7 and 0 < g < 0.5:
            fired.append(c.index[i])
    return pd.DatetimeIndex(fired)


def next24(name: str, days: pd.DatetimeIndex) -> pd.Series:
    eq = load_hourly(name)["equity"]
    return pd.Series({d: eq.asof(d + pd.Timedelta(hours=25)) / eq.asof(d + pd.Timedelta(hours=1)) - 1 for d in days
                      if d + pd.Timedelta(hours=25) <= min(eq.index[-1], OOS_END)}, dtype=float)


def resolve_sweep() -> int:
    if "trial: 511," in (ROOT / FILE).read_text(encoding="utf-8"):
        print("already resolved")
        return 0
    names = [r["name"] for r in doc(FILE)["runs"] if r.get("group") != "sweep"]
    J = {n: judge(n) for n in names}
    best2 = rank(names, J)[:2]
    L = [f"  # resolved {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC by lab/b8.py --resolve-sweep: best 2 = {best2}"]
    t = 511
    for n in best2:
        for e in (1, 2, 4, 6, 12):
            L.append(f"  - {{name: b8s_{n}_r{e}h, trial: {t}, group: sweep, base: {n}, rebalance_every_h: {e}}}")
            t += 1
    append(FILE, L)
    return 0


def main_report() -> int:
    from lab.analogs import features, find_analogs
    runs = doc(FILE)["runs"]
    have = [r["name"] for r in runs if load_hourly(r["name"]) is not None]
    fam = {r["name"]: (r.get("group") if r.get("group") in BASE else r["name"].split("_b8_")[1][0]) for r in runs}
    J = {n: judge(n) for n in have + list(BASE.values())}
    lt = N01.inv_cdf(1 - 1 / declared_total())
    starts = broad_down_starts()
    f = features()
    today = f[["btc_ret_30d"]].dropna().index[-1]
    f2 = f[(f.index <= OOS_END - pd.Timedelta(days=14)) | (f.index == today)]
    analog_days = [d + pd.Timedelta(hours=23) for d in find_analogs(f2, today, k=30)[0].index]
    pct = lambda x: "" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:+.1%}"
    pr = lambda x: "" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:.0%}"
    L = ["# Block 8 (last block): universe breadth and exposure\n",
         f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC. Rules: `{FILE}` (declared before any run). Data to 2026-06-30, "
         "both halves; Jul-Oct 2026 informational. Each family vs its own core10 baseline._\n",
         f"**Trials:** {declared_total()} declared (ledger frozen after this block); luck threshold about {lt:.1f} SE.\n",
         f"**Broad-down windows** (BTC 14d < -5% AND > 70% of pool coins down): {len(starts)} window starts in total.\n"]
    adopted = []
    for g in ("s", "h"):
        base = BASE[g]
        names = [base] + [n for n in have if fam.get(n) == g]
        L += [f"\n## {LABEL[g]} family (baseline `{base}`)\n",
              "| run | median 14d comp IS / OOS | mean 14d IS / OOS | down mean IS / OOS | broad-down mean IS / OOS (n) | "
              "broad-down gross IS / OOS | worst 14d IS / OOS | P(<=-10%) IS / OOS | OOS Sharpe | meets all | beats baseline both "
              "halves | t mean / t comp (min of halves) |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for n in names:
            j = J[n]
            bd = broad_down(n, starts)
            bi, bo = bd.get("IS", {}), bd.get("OOS", {})
            beat = n != base and beats_ref(j, J[base])
            if n != base:
                m = margins(n, base)
                tm = min(m["IS"]["t_mean"], m["OOS"]["t_mean"])
                tc = min(m["IS"]["t_med"], m["OOS"]["t_med"])
                tt = f"{tm:+.2f} / {tc:+.2f}"
            else:
                tt = "baseline"
            if beat and j["meets"]:
                adopted.append(n)
            L.append(f"| {n} | {j['IS']['comp']:.2f} / {j['OOS']['comp']:.2f} | {pct(j['IS']['mean'])} / {pct(j['OOS']['mean'])} | "
                     f"{pct(j['IS']['down'])} / {pct(j['OOS']['down'])} | {pct(bi.get('mean'))} / {pct(bo.get('mean'))} "
                     f"({bi.get('n', 0)} / {bo.get('n', 0)}) | {pr(bi.get('gross'))} / {pr(bo.get('gross'))} | "
                     f"{pct(j['IS']['worst'])} / {pct(j['OOS']['worst'])} | {pr(j['IS']['pm10'])} / {pr(j['OOS']['pm10'])} | "
                     f"{j['OOS']['sharpe']:.2f} | {'yes' if j['meets'] else '**no**'} | "
                     f"{'' if n == base else ('**yes**' if beat else 'no')} | {tt} |")
        L += [f"\n### {LABEL[g]}: exposure, positions, costs, analogs (OOS)\n",
              "| run | avg gross | avg positions | net short share | fees/yr | trades/day | analogs 14d mean / P(>0) |",
              "|---|---|---|---|---|---|---|"]
        for n in names:
            h = load_hourly(n)
            ho = h.loc[OOS0:OOS_END]
            alias = "b5ref__b3_s3v2e_core10" if n == "b3_s3v2e_core10" else n      # baseline positions recorded there
            d = ls_detail(alias).get("OOS") if (HCACHE / f"{alias}_pos.pkl").exists() else None
            an = fwd(h, analog_days)
            eq = h["equity"]
            ar = pd.Series([eq.asof(x + pd.Timedelta(days=14)) / eq.asof(x) - 1 for x in analog_days
                            if x + pd.Timedelta(days=14) <= OOS_END], dtype=float)
            L.append(f"| {n} | {ho['gross'].mean():.0%} | {d['coins']:.1f} | {pr(d['net_short'])} | "
                     f"{J[n]['OOS']['fees_yr']:.1%} | {J[n]['OOS']['trades_day']:.1f} | {pct(an.get('mean'))} / {pr((ar > 0).mean())} |"
                     if d else f"| {n} | {ho['gross'].mean():.0%} | n/a | n/a | {J[n]['OOS']['fees_yr']:.1%} | "
                               f"{J[n]['OOS']['trades_day']:.1f} | {pct(an.get('mean'))} / {pr((ar > 0).mean())} |")
    fd = floor_days()
    n_dec = len(pd.date_range("2020-03-01", OOS_END, freq="1D"))
    L += ["\n## U6 exposure floor: when it fires\n",
          f"The floor fires on {len(fd)} daily decisions ({len(fd) / n_dec:.0%} of days; IS {int((fd <= IS_END).sum())}, OOS "
          f"{int(((fd >= OOS0) & (fd <= OOS_END)).sum())}). Next-24h return on those days (mean / worst / P(>0)):\n",
          "| run | IS | OOS | baseline on the same days IS | OOS |", "|---|---|---|---|---|"]
    for g in ("s", "h"):
        n, base = f"b8_{g}_U6", BASE[g]
        if load_hourly(n) is None:
            continue
        c = lambda r: f"{r.mean():+.2%} / {r.min():+.2%} / {(r > 0).mean():.0%}" if len(r) else ""
        a, b = next24(n, fd), next24(base, fd)
        L.append(f"| {n} | {c(a[a.index <= IS_END])} | {c(a[a.index >= OOS0])} | {c(b[b.index <= IS_END])} | {c(b[b.index >= OOS0])} |")
    L.insert(4, f"**Adopted: {', '.join('`' + a + '`' for a in adopted) if adopted else 'none'}** (all requirements + beats its own "
                "baseline on both primary metrics in both halves).\n")
    (ROOT / "leaderboard_b8.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"adopted: {adopted}")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--resolve-sweep", action="store_true")
    a = ap.parse_args()
    sys.exit(resolve_sweep() if a.resolve_sweep else main_report())
