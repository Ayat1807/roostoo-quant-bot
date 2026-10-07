"""Block 6 track B: point-in-time regime probabilities (walk-forward), cached in data/regime/.

    python -m lab.regime_hmm      # writes data/regime/hmm2.csv, hmm3.csv, corr.csv

HMM: Gaussian HMM (hmmlearn, full covariance) on daily BTC features [log return 00:00->00:00 UTC, 7-day realised vol of
hourly returns (annualised)], 2 and 3 states. Expanding-window walk-forward: for every calendar month M from the first
month with >= 6 months of history, the model is fitted on days < (first day of M - 1 day embargo) (10 random starts,
best log-likelihood), then the FILTERED state probabilities (forward pass only, no smoothing, no future data) are written
for each day of M. State labels per fit (declared rule): crisis = highest mean vol; 3 states: of the other two, trend =
larger |mean return|, the third = chop; 2 states: the other = calm (p_trend 0). Row for day d uses data up to the end of d.
Correlation state: average pairwise correlation of the 10 core coins' hourly returns over the last 720 hours, per day;
flag = above the 80th percentile of its own history up to that day (expanding, >= 180 days of history).
"""

from __future__ import annotations

import sys
import warnings

import numpy as np
import pandas as pd

from lab import ROOT
from lab.data import load_close

OUT = ROOT / "data" / "regime"
CORE = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT", "DOGEUSDT", "AVAXUSDT", "LINKUSDT", "DOTUSDT"]


def features(btc: pd.Series) -> pd.DataFrame:
    r = np.log(btc).diff()
    daily = btc.resample("1D").last()
    ret = np.log(daily).diff()
    vol = r.rolling(168).std().resample("1D").last() * np.sqrt(24 * 365)
    return pd.DataFrame({"ret": ret, "vol": vol}).dropna()


def filtered(model, X: np.ndarray) -> np.ndarray:
    """Forward-filtered state probabilities P(s_t | x_1..t)."""
    logB = model._compute_log_likelihood(X)
    a = np.log(np.maximum(model.startprob_, 1e-300)) + logB[0]
    out = np.zeros_like(logB)
    out[0] = np.exp(a - np.logaddexp.reduce(a))
    logA = np.log(np.maximum(model.transmat_, 1e-300))
    for t in range(1, len(X)):
        a = np.logaddexp.reduce(a[:, None] + logA, axis=0) + logB[t]
        a -= np.logaddexp.reduce(a)
        out[t] = np.exp(a)
    return out


def fit(X: np.ndarray, n: int):
    from hmmlearn.hmm import GaussianHMM
    best, ll = None, -np.inf
    for seed in range(10):
        m = GaussianHMM(n_components=n, covariance_type="full", n_iter=200, random_state=seed)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            m.fit(X)
            s = m.score(X)
        if np.isfinite(s) and s > ll:
            best, ll = m, s
    return best


def labels(m, n: int) -> tuple[int, int | None]:
    mu = m.means_
    crisis = int(np.argmax(mu[:, 1]))
    if n == 2:
        return crisis, None
    rest = [k for k in range(n) if k != crisis]
    trend = max(rest, key=lambda k: abs(mu[k, 0]))
    return crisis, trend


def hmm_probs(f: pd.DataFrame, n: int) -> pd.DataFrame:
    Xall = f[["ret", "vol"]].values
    mu, sd = None, None
    rows = []
    months = pd.date_range(f.index[0] + pd.DateOffset(months=6), f.index[-1], freq="MS")
    for ms in months:
        train = f[f.index < ms - pd.Timedelta(days=1)]
        mu, sd = train.mean().values, train.std().values
        m = fit((train.values - mu) / sd, n)
        crisis, trend = labels(m, n)
        upto = f[f.index < ms + pd.DateOffset(months=1)]
        P = filtered(m, (upto.values - mu) / sd)
        sel = upto.index >= ms
        for d, p in zip(upto.index[sel], P[sel]):
            rows.append({"date": d, "p_crisis": float(p[crisis]), "p_trend": float(p[trend]) if trend is not None else 0.0,
                         "fit_end": str((ms - pd.Timedelta(days=1)).date())})
        print(f"  hmm{n} {ms:%Y-%m}: fitted on {len(train)} days", flush=True)
    return pd.DataFrame(rows).set_index("date")


def corr_state(c: pd.DataFrame) -> pd.DataFrame:
    r = c.pct_change()
    days = pd.date_range(r.index[0].ceil("D") + pd.Timedelta(days=30), r.index[-1].floor("D"), freq="1D")
    vals = {}
    for d in days:
        w = r.loc[d - pd.Timedelta(hours=720):d - pd.Timedelta(hours=1)].dropna(axis=1, how="any")
        if w.shape[1] < 3:
            continue
        cm = w.corr().values
        vals[d] = float(cm[np.triu_indices_from(cm, 1)].mean())
    s = pd.Series(vals)
    p80 = s.expanding(min_periods=180).quantile(0.8)
    return pd.DataFrame({"avg_corr": s, "p80": p80, "high": (s > p80) & p80.notna()})


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    c = load_close(CORE)
    f = features(c["BTCUSDT"])
    for n in (2, 3):
        hmm_probs(f, n).to_csv(OUT / f"hmm{n}.csv")
    corr_state(c).to_csv(OUT / "corr.csv")
    print("wrote", OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
