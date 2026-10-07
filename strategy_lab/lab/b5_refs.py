"""Block 5 references re-scored with recorded positions (no trials): identical curves, saved as b5ref__<run>."""
import numpy as np

from lab.backtest import Backtest, RunConfig
from lab.combine import combine_many
from lab.runner import HCACHE, load_hourly, resolve_base

for n in ["b3_s3v2e_core10", "b3_s3v2e_tv06_core10", "b3_regime_core10"]:
    r = Backtest(RunConfig.from_dict({**resolve_base(n), "name": n, "record_positions": True})).run()
    ref = load_hourly(n)
    d = float(np.abs(r["hourly"]["equity"].values - ref["equity"].values).max())
    print(f"{n}: reproduction max |d equity| {d:.2e}", flush=True)
    assert d < 1e-6
    r["hourly"].to_pickle(HCACHE / f"b5ref__{n}.pkl")
    r["positions"].to_pickle(HCACHE / f"b5ref__{n}_pos.pkl")
c = combine_many([(load_hourly("b3_s3v2e_core10"), 0.5), (load_hourly("b3_xsmom_r1"), 0.5)])
c.to_pickle(HCACHE / "b5ref__c50_s3v2e_xsmom_r1.pkl")
print("50/50 s3v2e_core10 + xsmom_r1 combined")
