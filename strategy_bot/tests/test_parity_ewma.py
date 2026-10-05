"""(a2) Parity: live s3v2 with vol_method=ewma == strategy_lab's e_ewma_vol (block 2 trial 50).

    python -m tests.test_parity_ewma

The live bot holds up to 2000 hourly bars; the lab backtest hands the strategy its last
800. The live strategy limits EWMA to the last `ewma_window` (800) returns, so both must
give identical weights. The lab strategy (strategy_lab/strategies/s3v2x.py) is imported
directly, with the params of trial e_ewma_vol from strategy_lab/variants_b2.yaml.
Also checks that config.yaml uses ewma and that std mode is unchanged (reference path).
Requirement: max |diff| < 1e-9 on every date.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import yaml

from bot import load_config
from strategies import get_strategy
from tests.hist_data import load_closes

HERE = Path(__file__).resolve().parent.parent
LAB = HERE.parent / "strategy_lab"


def lab_params() -> dict:
    doc = yaml.safe_load((LAB / "variants_b2.yaml").read_text(encoding="utf-8"))
    run = next(r for r in doc["runs"] if r["name"] == "e_ewma_vol")
    return {**doc["defaults"]["params"], **run["params"], "btc_pair": "BTC/USD"}


def main() -> int:
    sys.path.insert(0, str(LAB))
    from lab.strategies import get_strategy as lab_get  # noqa: E402

    cfg = load_config(HERE / "config.yaml")["strategy"]
    lp = lab_params()
    c = load_closes()
    live, lab = get_strategy("s3v2"), lab_get("s3v2x")
    worst, n = 0.0, 0
    for ts in c.index[2000::97]:
        hist = c.loc[:ts]
        a = pd.Series(live.target_weights(hist.iloc[-2000:], cfg))
        b = pd.Series(lab.target_weights(hist.iloc[-800:], lp))
        worst = max(worst, float((a - b.reindex(a.index)).abs().max()))
        n += 1
    ok_cfg = cfg.get("vol_method") == "ewma" and float(cfg.get("ewma_halflife")) == float(lp["ewma_halflife"])
    ok_par = worst < 1e-9 and n > 10
    std_cfg = {**cfg, "vol_method": "std"}
    old = pd.Series(live.target_weights(c.iloc[-800:], std_cfg))
    ref = pd.Series(lab.target_weights(c.iloc[-800:], {**lp, "vol_method": "std"}))
    ok_std = float((old - ref).abs().max()) < 1e-9
    diff_now = float((pd.Series(live.target_weights(c.iloc[-2000:], cfg)) - old).abs().max())
    print(f"[{'PASS' if ok_cfg else 'FAIL'}] config.yaml: vol_method={cfg.get('vol_method')} "
          f"halflife={cfg.get('ewma_halflife')} (lab e_ewma_vol: {lp['vol_method']} {lp['ewma_halflife']})")
    print(f"[{'PASS' if ok_par else 'FAIL'}] live s3v2 (ewma, 2000-bar history) == lab e_ewma_vol "
          f"(800-bar window) on {n} dates: max diff {worst:.1e}")
    print(f"[{'PASS' if ok_std else 'FAIL'}] vol_method=std unchanged vs lab std")
    print(f"[info] latest bar: max weight change ewma vs std = {diff_now:.4f}")
    ok = ok_cfg and ok_par and ok_std
    print(f"\n(a2) ewma parity: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
