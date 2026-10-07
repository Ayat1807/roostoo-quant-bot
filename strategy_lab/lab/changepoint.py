"""Changepoint scores per coin and hour (block 6 track A3), computed once from the closes, used by the backtester.

z_t = r_t / sigma_{t-1}: hourly return over the EWMA std (halflife 168h) of the previous bar (no look-ahead).
Scores are directional, "against the position": `down` is evidence of a downward break (cuts longs), `up` of an upward
break (cuts shorts).

  cusum  two-sided CUSUM with slack k (0.5): down_t = max(0, down_{t-1} - z_t - k), up_t = max(0, up_{t-1} + z_t - k);
         both reset to 0 at every daily target refresh (the bar where a new daily target is computed).
  bocpd  Bayesian online changepoint detection (Adams & MacKay 2007) on z with a Gaussian likelihood of known variance 1
         and a N(0, 1) prior on the segment mean; constant hazard 1/168 (one change a week on average); run length
         truncated at 720h. Score = P(run length <= 6h) (a change within the last 6 hours), assigned to `down` if the mean
         z of the last 6 bars is negative, else to `up`.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def standardized(c: pd.DataFrame, halflife: float = 168) -> np.ndarray:
    r = c.pct_change()
    sd = r.ewm(halflife=halflife).std().shift(1)
    z = (r / sd).replace([np.inf, -np.inf], np.nan)
    return z.fillna(0.0).values


def cusum(z: np.ndarray, reset: np.ndarray, k: float = 0.5) -> tuple[np.ndarray, np.ndarray]:
    T, A = z.shape
    dn, up = np.zeros((T, A)), np.zeros((T, A))
    d, u = np.zeros(A), np.zeros(A)
    for t in range(T):
        if reset[t]:
            d[:], u[:] = 0.0, 0.0
        d = np.maximum(0.0, d - z[t] - k)
        u = np.maximum(0.0, u + z[t] - k)
        dn[t], up[t] = d, u
    return dn, up


def bocpd(z: np.ndarray, hazard: float = 1 / 168, rmax: int = 720, recent: int = 6) -> tuple[np.ndarray, np.ndarray]:
    T, A = z.shape
    R = np.zeros((A, rmax + 1))
    R[:, 0] = 1.0
    n = np.zeros(rmax + 1)                # observations in a run of length r (same for every coin)
    S = np.zeros((A, rmax + 1))           # sum of z in that run
    n[:] = np.arange(rmax + 1)
    score = np.zeros((T, A))
    for t in range(T):
        x = z[t][:, None]
        mu = S / (1.0 + n)                # posterior mean, prior N(0, 1), known variance 1
        var = 1.0 + 1.0 / (1.0 + n)
        pred = np.exp(-0.5 * (x - mu) ** 2 / var) / np.sqrt(2 * np.pi * var)
        g = R * pred
        cp = (g * hazard).sum(axis=1)
        growth = g * (1 - hazard)
        newR = np.zeros_like(R)
        newR[:, 0] = cp
        newR[:, 1:] = growth[:, :-1]
        newR[:, -1] += growth[:, -1]       # truncation: the longest run absorbs the tail
        tot = newR.sum(axis=1, keepdims=True)
        R = np.where(tot > 0, newR / np.where(tot > 0, tot, 1.0), R)
        newS = np.zeros_like(S)
        newS[:, 1:] = S[:, :-1] + x
        newS[:, -1] = S[:, -1] + x[:, 0]   # (approximation for the absorbed tail)
        S = newS
        score[t] = R[:, :recent + 1].sum(axis=1)
    rm = pd.DataFrame(z).rolling(recent, min_periods=1).mean().values
    return np.where(rm < 0, score, 0.0), np.where(rm >= 0, score, 0.0)


def scores(c: pd.DataFrame, method: str, reset: np.ndarray, k: float = 0.5) -> tuple[np.ndarray, np.ndarray]:
    z = standardized(c)
    if method == "cusum":
        return cusum(z, reset, k)
    if method == "bocpd":
        return bocpd(z)
    raise ValueError(f"changepoint method must be cusum|bocpd, got {method!r}")
