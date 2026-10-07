"""s3v2x_alloc: s3v2e signals with a different allocation across coins (block 6 track C, variants_b6c_alloc.yaml).

Signal and active set as s3v2x (s3v2e): sig_i = mean over the 4 horizons of sign(return), active = sig != 0. The s3v2e target
w0 (with its vol targeting, bull short scaling, caps) fixes the GROSS G = sum |w0|. The new weights only redistribute G:
  w_i = sign(sig_i) x a_i x |sig_i| / sum_j(a_j |sig_j|) x G, then shorts x short_scale_bull while BTC > its 14d mean,
  per-coin cap max_w, gross <= 1.
Allocation a (sum 1, a_i >= 0) on the active coins, hourly returns of the SIGNED positions:
  erc    equal risk contribution with the 30-day (720h) covariance (fixed-point iteration, 500 steps)
  hrp    hierarchical risk parity (Lopez de Prado 2016): single-linkage clusters on the 90-day (2160h) correlation distance
         sqrt((1 - rho) / 2), quasi-diagonal order, recursive bisection with inverse-variance cluster weights (90d covariance)
  kelly  shrunk Kelly: edge_i = alpha + beta x sig_i from a pooled OLS of the next-24h return on sig over the last 90 days of
         daily decisions (pairs whose 24h outcome ended before now: 24h purge, point-in-time, refit at every decision);
         f_i = max(edge_i x sign(sig_i), 0) / var_i with var_i = 24 x EWMA hourly variance (halflife 168h); a = 0.5 x f / sum f
         + 0.5 x equal; if every f is 0 -> equal
Needs lookback >= 2160 + 24 x 90 bars for kelly (lookback_bars 4400).
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from lab.strategies import Strategy


def _sig(c: pd.DataFrame, horizons, upto: int | None = None) -> pd.Series:
    x = c if upto is None else c.iloc[:upto + 1]
    last = x.iloc[-1]
    return sum(np.sign(last / x.iloc[-1 - h] - 1) for h in horizons) / len(horizons)


def erc(cov: np.ndarray, steps: int = 500) -> np.ndarray:
    n = len(cov)
    w = np.ones(n) / n
    for _ in range(steps):
        rc = w * (cov @ w)
        tot = rc.sum()
        if tot <= 0:
            break
        w = w * (tot / n / np.maximum(rc, 1e-18)) ** 0.5
        w /= w.sum()
    return w


def hrp(cov: np.ndarray, corr: np.ndarray) -> np.ndarray:
    from scipy.cluster.hierarchy import leaves_list, linkage
    from scipy.spatial.distance import squareform
    n = len(cov)
    if n == 1:
        return np.ones(1)
    d = np.sqrt(np.clip((1 - corr) / 2, 0, None))
    np.fill_diagonal(d, 0)
    order = list(leaves_list(linkage(squareform(d, checks=False), "single")))
    w = np.ones(n)
    clusters = [order]
    while clusters:
        nxt = []
        for cl in clusters:
            if len(cl) < 2:
                continue
            h = len(cl) // 2
            a, b = cl[:h], cl[h:]

            def cvar(ix):
                sub = cov[np.ix_(ix, ix)]
                iv = 1 / np.maximum(np.diag(sub), 1e-18)
                iv /= iv.sum()
                return float(iv @ sub @ iv)
            va, vb = cvar(a), cvar(b)
            alpha = 1 - va / (va + vb) if va + vb > 0 else 0.5
            w[a] *= alpha
            w[b] *= 1 - alpha
            nxt += [a, b]
        clusters = nxt
    return w / w.sum()


class S3v2xAlloc(Strategy):
    name = "s3v2x_alloc"
    DEF = {"alloc": "erc", "cov_h": 720, "hrp_h": 2160, "kelly_days": 90, "shrink": 0.5, "decision_hour": 0}

    def target_weights(self, closes: pd.DataFrame, cfg: dict[str, Any]) -> dict[str, float]:
        from lab.strategies import get_strategy
        import sys
        p = {**self.DEF, **(cfg or {})}
        base = {k: v for k, v in p.items() if k not in self.DEF}
        w0 = pd.Series(get_strategy("s3v2x").target_weights(closes, base))
        G = float(w0.abs().sum())
        c = closes.dropna(axis=1, how="any")
        dflt = sys.modules["live_strategies.s3v2"].DEFAULTS
        hz = tuple(base.get("horizons", dflt["horizons"]))
        sig = _sig(c, hz)
        act = [a for a in c.columns if sig[a] != 0]
        out = {a: 0.0 for a in closes.columns}
        if not act or G <= 0:
            return self.check(out)
        sgn = np.sign(sig[act]).values
        r = c[act].pct_change().iloc[1:] * sgn
        m = p["alloc"]
        if m == "erc":
            a = erc(r.iloc[-int(p["cov_h"]):].cov().values)
        elif m == "hrp":
            x = r.iloc[-int(p["hrp_h"]):]
            a = hrp(x.cov().values, x.corr().fillna(0).values)
        elif m == "kelly":
            a = self._kelly(c, act, sig, sgn, hz, p)
        else:
            raise ValueError(f"alloc {m!r}")
        mag = a * np.abs(sig[act].values)
        w = pd.Series(sgn * mag / mag.sum() * G, index=act)
        btc = c[base.get("btc_pair", "BTCUSDT")] if base.get("btc_pair", "BTCUSDT") in c.columns else None
        rw = int(base.get("regime_win", dflt["regime_win"]))
        if btc is not None and btc.iloc[-1] > btc.iloc[-rw:].mean():
            w[w < 0] *= float(base.get("short_scale_bull", dflt["short_scale_bull"]))
        w = w.clip(-float(base.get("max_w", dflt["max_w"])), float(base.get("max_w", dflt["max_w"])))
        g = w.abs().sum()
        if g > 1:
            w /= g
        for k, v in w.items():
            out[k] = float(v)
        return self.check(out)

    @staticmethod
    def _kelly(c, act, sig, sgn, hz, p) -> np.ndarray:
        n_days = int(p["kelly_days"])
        T = len(c)
        X, Y = [], []
        hour = c.index[-1].hour
        ends = [i for i in range(T - 25, T - 25 - 24 * n_days, -24) if i - max(hz) - 1 > 0]
        for i in ends:                       # decision at bar i, outcome i -> i + 24 (ends before now: purge)
            s = _sig(c, hz, i)
            fr = c.iloc[i + 24] / c.iloc[i] - 1
            X += list(s.values)
            Y += list(fr.values)
        X, Y = np.array(X), np.array(Y)
        ok = np.isfinite(X) & np.isfinite(Y)
        if ok.sum() < 50 or np.var(X[ok]) == 0:
            return np.ones(len(act)) / len(act)
        beta, alpha = np.polyfit(X[ok], Y[ok], 1)
        edge = (alpha + beta * sig[act].values) * sgn
        var = (c[act].pct_change().ewm(halflife=168).var().iloc[-1].values * 24)
        f = np.maximum(edge, 0) / np.maximum(var, 1e-12)
        eq = np.ones(len(act)) / len(act)
        if f.sum() <= 0:
            return eq
        return float(p["shrink"]) * eq + (1 - float(p["shrink"])) * f / f.sum()
