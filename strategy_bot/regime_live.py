"""HMM2 regime + CUSUM changepoint cut for s3v2 (strategy_lab blocks 6 / 7, run b7_hmm2_cusum). Off unless configured.

Both mirror strategy_lab exactly (tests/test_hmm_cusum.py checks parity with lab/regime_hmm.py, data/regime/hmm2.csv and
lab/changepoint.py):

HMM2 (config `regime_hmm`): Gaussian HMM (hmmlearn, full covariance, 2 states, 10 seeds, best log-likelihood) on daily BTC
features [log return of daily closes, 7-day realised vol of hourly log returns x sqrt(8760)], BTC hourly closes from Binance
since 2020-01-01 (cached in the state dir). The model for month M is fitted once on days < (first day of M - 1 day); the
probability for day d is the FILTERED probability (forward pass, data up to the end of d) of the crisis state (= highest mean
vol). A target computed on the bar opening at day D uses the row of day D - 1. Mapping (declared in block 6 track B):
short_scale_bull_eff = short_scale_bull + (1 - short_scale_bull) x p_crisis; target x (1 - crisis_cut x p_crisis).

CUSUM cut (config `changepoint_cut`): z_t = hourly return / EWMA std (halflife 168h) of the previous bar; down_t = max(0,
down_{t-1} - z_t - k), up_t = max(0, up_{t-1} + z_t - k), both reset at the bar of the daily target and accumulated from it
(that bar included). A held long with down > threshold (short with up > threshold), not yet cut since the daily target, gets
its target x cut until the next daily target; the cut trades at once.
"""

from __future__ import annotations

import json
import logging
import warnings
from pathlib import Path
from typing import Any, Callable

import numpy as np
import pandas as pd

from infra import write_json_atomic

log = logging.getLogger("strategy_bot.regime")
HMM_START = pd.Timestamp("2020-01-01", tz="UTC")


def features(btc: pd.Series) -> pd.DataFrame:
    r = np.log(btc).diff()
    daily = btc.resample("1D").last()
    ret = np.log(daily).diff()
    vol = r.rolling(168).std().resample("1D").last() * np.sqrt(24 * 365)
    return pd.DataFrame({"ret": ret, "vol": vol}).dropna()


def fit(X: np.ndarray, n: int = 2):
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


def filtered_last(startprob, transmat, means, covars, X: np.ndarray) -> np.ndarray:
    """Filtered state probabilities for every row of X (forward pass), Gaussian full-covariance emissions."""
    n = len(startprob)
    logB = np.zeros((len(X), n))
    for k in range(n):
        d = X - means[k]
        inv = np.linalg.inv(covars[k])
        _, logdet = np.linalg.slogdet(covars[k])
        logB[:, k] = -0.5 * (np.einsum("ij,jk,ik->i", d, inv, d) + logdet + X.shape[1] * np.log(2 * np.pi))
    a = np.log(np.maximum(startprob, 1e-300)) + logB[0]
    out = np.zeros_like(logB)
    out[0] = np.exp(a - np.logaddexp.reduce(a))
    logA = np.log(np.maximum(transmat, 1e-300))
    for t in range(1, len(X)):
        a = np.logaddexp.reduce(a[:, None] + logA, axis=0) + logB[t]
        a -= np.logaddexp.reduce(a)
        out[t] = np.exp(a)
    return out


class RegimeHMM:
    """Point-in-time p_crisis per day; the month's model is fitted once and cached in <state>/hmm2_model.json."""

    def __init__(self, state_dir: Path, fetch: Callable[[pd.Timestamp], pd.Series | None], n: int = 2) -> None:
        self.dir, self.fetch, self.n = Path(state_dir), fetch, n
        self.model_file = self.dir / f"hmm{n}_model.json"
        self.btc_file = self.dir / "btc_1h_since_2020.csv"
        self.model: dict[str, Any] | None = None
        if self.model_file.exists():
            try:
                self.model = json.loads(self.model_file.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                self.model = None
        self.btc: pd.Series | None = None

    def _history(self, now: pd.Timestamp) -> pd.Series:
        s = None
        if self.btc_file.exists():
            s = pd.read_csv(self.btc_file, index_col=0).iloc[:, 0]
            s.index = pd.to_datetime(s.index, utc=True)
        if s is None or s.index[-1] < now.floor("h") - pd.Timedelta(hours=2):
            new = self.fetch(now)
            if new is None:
                if s is None:
                    raise RuntimeError("regime_hmm: no BTC history (Binance unreachable)")
            else:
                s = new if s is None else pd.concat([s[s.index < new.index[0]], new])
                s = s[s.index >= HMM_START]
                self.dir.mkdir(parents=True, exist_ok=True)
                s.to_frame("BTC").to_csv(self.btc_file)
        full = pd.date_range(s.index[0], s.index[-1], freq="1h", tz="UTC")
        return s.reindex(full).ffill()

    def p_crisis(self, day: pd.Timestamp, now: pd.Timestamp) -> tuple[float, dict]:
        """p_crisis of `day` (data up to the end of `day`), using the model of day's calendar month."""
        day = day.floor("D")
        btc = self._history(now)
        f = features(btc.loc[:day + pd.Timedelta(hours=23)])
        if day not in f.index:
            return 0.0, {"reason": f"no features for {day.date()}"}
        ms = day.replace(day=1)
        if ms < f.index[0] + pd.DateOffset(months=6):
            return 0.0, {"reason": "before the first walk-forward fit"}
        key = str(ms.date())
        if not self.model or self.model.get("month") != key:
            train = f[f.index < ms - pd.Timedelta(days=1)]
            mu, sd = train.mean().values, train.std().values
            m = fit((train.values - mu) / sd, self.n)
            self.model = {"month": key, "fit_days": int(len(train)), "mu": mu.tolist(), "sd": sd.tolist(),
                          "startprob": m.startprob_.tolist(), "transmat": m.transmat_.tolist(),
                          "means": m.means_.tolist(), "covars": m.covars_.tolist(),
                          "crisis": int(np.argmax(m.means_[:, 1])), "fitted_at": str(now)}
            write_json_atomic(self.model_file, self.model)
            log.info("regime_hmm: fitted the %s model on %d days (crisis state %d)", key, len(train), self.model["crisis"])
        md = self.model
        X = (f.loc[:day].values - np.array(md["mu"])) / np.array(md["sd"])
        P = filtered_last(np.array(md["startprob"]), np.array(md["transmat"]), np.array(md["means"]),
                          np.array(md["covars"]), X)
        return float(P[-1, md["crisis"]]), {"month_model": md["month"], "fit_days": md["fit_days"]}


def cusum_scores(close: pd.DataFrame, reset_bar: pd.Timestamp, k: float = 0.5,
                 halflife: float = 168) -> tuple[pd.Series, pd.Series]:
    """(down, up) CUSUM per pair at the last bar, accumulated from reset_bar (included)."""
    r = close.pct_change()
    sd = r.ewm(halflife=halflife).std().shift(1)
    z = (r / sd).replace([np.inf, -np.inf], np.nan).fillna(0.0)
    z = z.loc[reset_bar:]
    d = pd.Series(0.0, index=close.columns)
    u = pd.Series(0.0, index=close.columns)
    for _, row in z.iterrows():
        d = np.maximum(0.0, d - row - k)
        u = np.maximum(0.0, u + row - k)
    return d, u
