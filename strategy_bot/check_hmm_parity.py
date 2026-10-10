"""Quick parity check of the bot's HMM2 regime model against strategy_lab (run on EC2 after installing the packages):

    .venv/bin/python check_hmm_parity.py

Downloads BTC hourly closes since 2020 from Binance (about 60 requests, into a temporary folder; no keys, nothing written to
the bot's state), fits the walk-forward HMM exactly as the live bot does (regime_live.RegimeHMM) for a few fixed past dates,
and compares the filtered crisis probability with the committed lab file ../strategy_lab/data/regime/hmm2.csv.
PASS if every difference is <= 0.01 (identical package versions give ~1e-12; this tolerance allows other scipy / sklearn
builds while still catching a wrong model). Exit code 0 = PASS, 1 = FAIL.
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
LAB = HERE.parent / "strategy_lab" / "data" / "regime" / "hmm2.csv"
DATES = ["2025-03-15", "2025-08-05", "2025-11-20", "2026-02-10", "2026-05-20", "2026-06-28"]
TOL = 0.01


def main() -> int:
    import hmmlearn
    import numpy
    import scipy
    import sklearn

    from market_data import fetch_binance_hourly
    from regime_live import HMM_START, RegimeHMM
    print(f"versions: numpy {numpy.__version__}, pandas {pd.__version__}, scipy {scipy.__version__}, "
          f"scikit-learn {sklearn.__version__}, hmmlearn {hmmlearn.__version__}")
    lab = pd.read_csv(LAB, index_col=0)
    lab.index = pd.to_datetime(lab.index, utc=True)
    with tempfile.TemporaryDirectory() as d:
        rh = RegimeHMM(Path(d), lambda now: fetch_binance_hourly(
            "BTC/USD", int((now - HMM_START) / pd.Timedelta(hours=1)) + 2, None, now), 2)
        worst = 0.0
        for ds in DATES:
            day = pd.Timestamp(ds, tz="UTC")
            p, info = rh.p_crisis(day, pd.Timestamp.now(tz="UTC"))
            ref = float(lab.at[day, "p_crisis"])
            worst = max(worst, abs(p - ref))
            print(f"  {ds}: bot p_crisis {p:.6f}  lab {ref:.6f}  diff {abs(p - ref):.2e}  ({info})")
    ok = worst <= TOL
    print(f"HMM parity: {'PASS' if ok else 'FAIL'} (max diff {worst:.2e}, tolerance {TOL})")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
