"""Scorecard: the same report for every run.

Sections: full period / in-sample (2020-2024) / out-of-sample (2025-2026); every rolling
14-day window stepping daily (median, % positive, worst return, worst DD, median
composite); competition composite 0.4*Sortino + 0.3*Sharpe + 0.3*Calmar on 14-day
windows; results by BTC regime (rules in config/lab.yaml); turnover, fees, trades and
active days per 14 days; correlation of daily returns with the s3v2 baseline.

Metric definitions match the reference research/engine.py::metrics (hourly returns,
annualised with 24*365; Calmar = annualised return / |max DD|).
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from lab import load_config

HPY = 24 * 365
CFG = load_config()


def metrics(eq: pd.Series | np.ndarray) -> dict[str, float]:
    e = np.asarray(eq, dtype=float)
    if len(e) < 3:
        return {}
    r = e[1:] / e[:-1] - 1
    n = len(r)
    total = e[-1] / e[0] - 1
    ann = (1 + total) ** (HPY / n) - 1 if total > -1 else -1.0
    sd = r.std(ddof=1)
    sharpe = r.mean() / sd * np.sqrt(HPY) if sd > 0 else 0.0
    dd_sd = np.sqrt((np.minimum(r, 0) ** 2).mean())
    sortino = r.mean() / dd_sd * np.sqrt(HPY) if dd_sd > 0 else 0.0
    peak = np.maximum.accumulate(e)
    mdd = float((e / peak - 1).min())
    calmar = ann / abs(mdd) if mdd < 0 else 0.0
    return {"return": float(total), "ann_ret": float(ann), "vol": float(sd * np.sqrt(HPY)),
            "sharpe": float(sharpe), "sortino": float(sortino), "mdd": mdd,
            "calmar": float(calmar),
            "composite": float(0.4 * sortino + 0.3 * sharpe + 0.3 * calmar)}


def _slice(h: pd.DataFrame, start: str | None, end: str | None) -> pd.DataFrame:
    s = pd.Timestamp(start, tz="UTC") if start else None
    e = pd.Timestamp(end, tz="UTC") if end else None
    return h.loc[s:e]


def rolling_14d(h: pd.DataFrame, days: int = 14) -> pd.DataFrame:
    """Every `days`-day window stepping one day (the competition horizon)."""
    eq, tr = h["equity"], h["trades"]
    starts = pd.date_range(eq.index[0].ceil("D"), eq.index[-1] - pd.Timedelta(days=days), freq="1D")
    if not len(starts):
        return pd.DataFrame()
    eqv, idx = eq.values, eq.index
    act_day = (tr.groupby(tr.index.floor("D")).sum() > 0)
    out = []
    for s in starts:
        a, b = idx.searchsorted(s), idx.searchsorted(s + pd.Timedelta(days=days))
        m = metrics(eqv[a:b + 1])
        if not m:
            continue
        m["start"] = s
        m["active_days"] = int(act_day.loc[s:s + pd.Timedelta(days=days - 1)].sum())
        out.append(m)
    return pd.DataFrame(out)


def summarize_windows(w: pd.DataFrame) -> dict[str, float]:
    if w.empty:
        return {}
    return {"n_windows": int(len(w)), "median_return": float(w["return"].median()),
            "pct_positive": float((w["return"] > 0).mean()),
            "worst_return": float(w["return"].min()), "best_return": float(w["return"].max()),
            "worst_dd": float(w["mdd"].min()), "median_dd": float(w["mdd"].median()),
            "median_composite": float(w["composite"].median()),
            "mean_composite": float(w["composite"].clip(-50, 50).mean()),
            "median_sharpe": float(w["sharpe"].median()),
            "median_active_days": float(w["active_days"].median()),
            "min_active_days": int(w["active_days"].min()),
            "pct_windows_all_days_active": float((w["active_days"] >= 14).mean())}


# --------------------------------------------------------------------------- #
# BTC regimes
# --------------------------------------------------------------------------- #

def btc_daily_features(btc_close_hourly: pd.Series) -> pd.DataFrame:
    d = btc_close_hourly.resample("1D").last().dropna()
    r1 = d.pct_change()
    vol7 = r1.rolling(7).std()
    f = pd.DataFrame({
        "btc_ret_1d": r1,
        "btc_ret_30d": d / d.shift(30) - 1,
        "btc_above_ma50": d > d.rolling(50).mean(),
        "btc_vol_7d_pct": vol7.rolling(365, min_periods=90).rank(pct=True),
    })
    return f


def classify_regimes(feat: pd.DataFrame) -> pd.Series:
    rules = CFG["regimes"]
    out = pd.Series("chop", index=feat.index, dtype=object)
    assigned = pd.Series(False, index=feat.index)
    for name, expr in rules.items():
        mask = pd.Series([bool(eval(expr, {"__builtins__": {}, "abs": abs}, row.to_dict()))
                          if row.notna().all() else False for _, row in feat.iterrows()],
                         index=feat.index)
        hit = mask & ~assigned
        out[hit] = name
        assigned |= hit
    return out


def by_regime(h: pd.DataFrame, regimes: pd.Series) -> dict[str, dict[str, float]]:
    deq = h["equity"].resample("1D").last()
    dr = deq.pct_change().dropna()
    reg = regimes.reindex(dr.index.floor("D")).values
    out = {}
    for name in CFG["regimes"]:
        x = dr[reg == name]
        if len(x) < 2:
            continue
        out[name] = {"days": int(len(x)), "share_days": float(len(x) / len(dr)),
                     "mean_daily": float(x.mean()), "hit_rate": float((x > 0).mean()),
                     "ann_sharpe": float(x.mean() / x.std() * np.sqrt(365)) if x.std() > 0 else 0.0,
                     "cum_return": float((1 + x).prod() - 1)}
    return out


# --------------------------------------------------------------------------- #
# Full scorecard
# --------------------------------------------------------------------------- #

def scorecard(h: pd.DataFrame, btc_hourly: pd.Series, baseline: pd.DataFrame | None = None,
              initial_equity: float | None = None) -> dict[str, Any]:
    per = CFG["periods"]
    out: dict[str, Any] = {"periods": {}, "rolling_14d": {}}
    for name, (s, e) in per.items():
        hs = _slice(h, s, e)
        if len(hs) > 48:
            out["periods"][name] = {**metrics(hs["equity"].values),
                                    "start": str(hs.index[0]), "end": str(hs.index[-1])}
    for name in ("full", "out_of_sample", "in_sample"):
        s, e = per[name]
        out["rolling_14d"][name] = summarize_windows(rolling_14d(_slice(h, s, e)))
    regimes = classify_regimes(btc_daily_features(btc_hourly))
    out["regimes"] = by_regime(h, regimes)
    out["regime_share_oos"] = regimes.loc[pd.Timestamp(per["out_of_sample"][0], tz="UTC"):] \
        .value_counts(normalize=True).round(3).to_dict()
    years = (h.index[-1] - h.index[0]) / pd.Timedelta(days=365)
    avg_eq = float(h["equity"].mean())
    days = h["trades"].groupby(h.index.floor("D")).sum()
    out["activity"] = {
        "trades_total": int(h["trades"].sum()), "trades_per_day": float(days.mean()),
        "active_day_share": float((days > 0).mean()),
        "turnover_per_year_x_equity": float(h["turnover"].sum() / avg_eq / years),
        "fees_total_usd": float(h["fees"].sum()),
        "fees_per_year_pct_equity": float(h["fees"].sum() / avg_eq / years),
        "avg_gross_exposure": float(h["gross"].mean()),
        "time_brake_active": float((h["mult"] < 1).mean()),
    }
    if baseline is not None:
        a = h["equity"].resample("1D").last().pct_change()
        b = baseline["equity"].resample("1D").last().pct_change()
        j = pd.concat([a, b], axis=1).dropna()
        out["corr_daily_vs_s3v2"] = float(j.iloc[:, 0].corr(j.iloc[:, 1])) if len(j) > 10 else None
    return out


# --------------------------------------------------------------------------- #
# Markdown
# --------------------------------------------------------------------------- #

def _pct(x: float | None) -> str:
    return "n/a" if x is None else f"{x:+.2%}"


def to_markdown(name: str, spec: dict[str, Any], sc: dict[str, Any]) -> str:
    L = [f"# Run: {name}\n", f"Strategy `{spec.get('strategy')}`; universe `{spec.get('universe')}`; "
         f"params `{spec.get('params', {})}`; band {spec.get('band', 0.06)}; brake "
         f"{spec.get('brake', True)}; shorts {spec.get('allow_short', True)}; guard "
         f"{spec.get('activity_guard', 'full')}\n"]
    L.append("## Periods\n")
    L.append("| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for k, m in sc["periods"].items():
        L.append(f"| {k} | {m['start'][:10]} → {m['end'][:10]} | {_pct(m['return'])} | {_pct(m['ann_ret'])} | "
                 f"{m['sharpe']:.2f} | {m['sortino']:.2f} | {_pct(m['mdd'])} | {m['calmar']:.2f} | "
                 f"{m['composite']:.2f} |")
    L.append("\n## Rolling 14-day windows (competition horizon)\n")
    L.append("| period | windows | median ret | % positive | worst ret | worst DD | median composite | "
             "median active days /14 | % windows 14/14 active |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for k, w in sc["rolling_14d"].items():
        if w:
            L.append(f"| {k} | {w['n_windows']} | {_pct(w['median_return'])} | {w['pct_positive']:.0%} | "
                     f"{_pct(w['worst_return'])} | {_pct(w['worst_dd'])} | {w['median_composite']:.2f} | "
                     f"{w['median_active_days']:.0f} | {w['pct_windows_all_days_active']:.0%} |")
    L.append("\n## By BTC regime (daily returns, full period)\n")
    L.append("| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |")
    L.append("|---|---|---|---|---|---|---|")
    for k, r in sc["regimes"].items():
        L.append(f"| {k} | {r['days']} | {r['share_days']:.0%} | {r['mean_daily']:+.3%} | {r['hit_rate']:.0%} | "
                 f"{r['ann_sharpe']:.2f} | {_pct(r['cum_return'])} |")
    a = sc["activity"]
    L.append("\n## Turnover, fees, activity\n")
    L.append(f"- trades: {a['trades_total']} ({a['trades_per_day']:.2f}/day); active days {a['active_day_share']:.0%}")
    L.append(f"- turnover {a['turnover_per_year_x_equity']:.1f}x equity/year; fees {a['fees_per_year_pct_equity']:.2%} "
             f"of equity/year (${a['fees_total_usd']:,.0f} total)")
    L.append(f"- average gross exposure {a['avg_gross_exposure']:.2f}; brake active {a['time_brake_active']:.1%} of hours")
    if sc.get("corr_daily_vs_s3v2") is not None:
        L.append(f"- correlation of daily returns with s3v2 baseline: {sc['corr_daily_vs_s3v2']:.2f}")
    return "\n".join(L) + "\n"
