"""Core + satellite as two sub-books of one account (research block 2, part C).

At the start the account is split (1 - share) / share; each book then runs its own rules
on its own capital (core: live s3v2 config; satellite: its run's rules incl. its -8% loss
limit) and the books are NOT rebalanced against each other. The combined hourly frame is
the sum of the two scaled equity curves; fees, turnover and trade counts add up. The
satellite's per-coin cap (10% of total equity) never binds: a satellite position is at
most 1/k = 25% of its book = 5% / 7.5% of the account at 20% / 30%.
"""

from __future__ import annotations

import pandas as pd


def combine_hourly(core: pd.DataFrame, sat: pd.DataFrame, share: float, initial: float = 50_000.0) -> pd.DataFrame:
    idx = core.index.intersection(sat.index)
    c, s = core.loc[idx], sat.loc[idx]
    kc = initial * (1 - share) / c["equity"].iloc[0]
    ks = initial * share / s["equity"].iloc[0]
    out = pd.DataFrame(index=idx)
    out["equity"] = c["equity"] * kc + s["equity"] * ks
    out["cash"] = c["cash"] * kc + s["cash"] * ks
    out["long"] = c["long"] * kc + s["long"] * ks
    out["short"] = c["short"] * kc + s["short"] * ks
    out["gross"] = (out["long"] + out["short"]) / out["equity"]
    out["turnover"] = c["turnover"] * kc + s["turnover"] * ks
    out["fees"] = c["fees"] * kc + s["fees"] * ks
    out["trades"] = c["trades"] + s["trades"]
    out["mult"] = c["mult"]
    return out
