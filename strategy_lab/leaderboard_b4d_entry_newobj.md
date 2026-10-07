# Block 5: risk-adjusted profit and down markets (new team objective)

_Generated 2026-10-07 08:44 UTC. Rules: `variants_b5_shorts.yaml` (declared before any run). Data to 2026-06-30, both halves (IS 2020-02-15 to 2024-12-31, OOS 2025-01-01 to 2026-06-30); Jul-Oct 2026 informational._

**Trials:** 408 declared across all blocks; luck threshold about 2.8 standard errors.

**Requirements (both halves):** mean 14d return > 0 in DOWN windows (BTC 14d < -5%), P(14d <= -10%) <= 5%, worst 14d >= -15%; OOS Sharpe >= 1.0. **Adopt:** all requirements AND higher median 14d composite AND higher mean 14d return than s3v2e_core10 in both halves.

**Adopted: none**


## Down-market results first (mean 14d return by BTC 14d move; n windows)

| run | half | DOWN (BTC < -5%) | % of down windows > 0 | FLAT | UP (BTC > +5%) | down-market req. |
|---|---|---|---|---|---|---|
| live xsmom R1 | IS | -2.8% (422) | 15% | -0.4% (709) | +7.2% (637) | **no** |
| live xsmom R1 | OOS | -3.2% (141) | 23% | -1.8% (272) | +4.2% (119) | **no** |
| live xsmom R1 | INFO | -0.8% (1) | 0% | -1.9% (51) | +6.3% (30) |  |
| s3v2e_core10 | IS | +0.6% (422) | 50% | -0.7% (709) | +2.0% (637) | yes |
| s3v2e_core10 | OOS | +2.0% (141) | 72% | -0.2% (272) | +1.8% (119) | yes |
| s3v2e_core10 | INFO | -2.1% (1) | 0% | -2.3% (51) | +8.3% (30) |  |
| b4d_pullback | IS | -2.0% (422) | 17% | -0.5% (709) | +4.5% (637) | **no** |
| b4d_pullback | OOS | -2.5% (141) | 9% | -2.5% (272) | +1.0% (119) | **no** |
| b4d_pullback | INFO | -4.1% (1) | 0% | -1.8% (51) | +3.3% (30) |  |
| b4d_not_ext6 | IS | -1.3% (422) | 15% | -0.9% (709) | +4.9% (637) | **no** |
| b4d_not_ext6 | OOS | -1.7% (141) | 15% | -1.2% (272) | +1.6% (119) | **no** |
| b4d_not_ext6 | INFO | -3.3% (1) | 0% | -1.6% (51) | +8.9% (30) |  |
| b4d_not_ext10 | IS | -1.7% (422) | 16% | -0.7% (709) | +5.1% (637) | **no** |
| b4d_not_ext10 | OOS | -3.0% (141) | 11% | -1.6% (272) | +2.2% (119) | **no** |
| b4d_not_ext10 | INFO | -0.7% (1) | 0% | -1.2% (51) | +8.9% (30) |  |
| b4d_resistance | IS | -2.8% (422) | 15% | -0.5% (709) | +7.1% (637) | **no** |
| b4d_resistance | OOS | -3.3% (141) | 23% | -1.7% (272) | +4.5% (119) | **no** |
| b4d_resistance | INFO | -1.4% (1) | 0% | -2.3% (51) | +6.6% (30) |  |
| b4d_patient_limit | IS | -2.4% (422) | 17% | -0.4% (709) | +6.3% (637) | **no** |
| b4d_patient_limit | OOS | -3.6% (141) | 16% | -1.9% (272) | +1.7% (119) | **no** |
| b4d_patient_limit | INFO | -2.6% (1) | 0% | -1.9% (51) | +2.7% (30) |  |

## Primary metric, risk limits, verdict

| run | half | median 14d composite | mean 14d | median 14d | P(<= -10%) | worst 14d | Sharpe | max DD | P(>= +10%) | fees/yr | trades/day | meets all | beats s3v2e_core10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| live xsmom R1 | IS | -1.77 | +1.7% | -0.9% | 3% | -19.1% | 1.06 | -60.2% | 15% | 17.5% | 6.0 |  |  |
| live xsmom R1 | OOS | -5.00 | -0.8% | -2.5% | 2% | -12.0% | -0.79 | -40.2% | 9% | 14.1% | 5.0 | no | no |
| live xsmom R1 | INFO | -2.70 | +1.1% | -1.3% | 0% | -6.4% | 0.89 | -11.7% | 15% | 17.3% | 5.9 |  |  |
| s3v2e_core10 | IS | -1.61 | +0.6% | -0.2% | 0% | -5.3% | 1.00 | -16.8% | 3% | 3.7% | 2.0 |  |  |
| s3v2e_core10 | OOS | -0.28 | +0.8% | -0.1% | 0% | -5.2% | 1.38 | -12.0% | 4% | 4.3% | 2.1 | **yes** |  |
| s3v2e_core10 | INFO | -6.40 | +1.6% | -0.9% | 0% | -6.0% | 1.35 | -10.4% | 16% | 7.3% | 3.1 |  |  |
| b4d_pullback | IS | -2.76 | +0.9% | -1.0% | 1% | -14.1% | 0.73 | -48.1% | 8% | 10.5% | 3.5 |  |  |
| b4d_pullback | OOS | -7.01 | -1.7% | -2.2% | 0% | -8.5% | -2.30 | -52.6% | 2% | 8.5% | 2.8 | no | no |
| b4d_pullback | INFO | -1.55 | +0.1% | -0.6% | 0% | -4.3% | -0.56 | -9.7% | 2% | 8.9% | 2.9 |  |  |
| b4d_not_ext6 | IS | -2.46 | +1.1% | -0.6% | 0% | -8.3% | 1.17 | -31.4% | 9% | 8.2% | 2.7 |  |  |
| b4d_not_ext6 | OOS | -5.71 | -0.7% | -1.6% | 0% | -7.5% | -1.10 | -29.4% | 2% | 8.9% | 3.0 | no | no |
| b4d_not_ext6 | INFO | -1.93 | +2.2% | -0.5% | 0% | -3.9% | 1.83 | -9.1% | 17% | 10.8% | 3.1 |  |  |
| b4d_not_ext10 | IS | -2.93 | +1.2% | -1.1% | 0% | -9.6% | 0.89 | -59.2% | 10% | 13.6% | 4.9 |  |  |
| b4d_not_ext10 | OOS | -6.22 | -1.1% | -2.5% | 0% | -11.7% | -1.31 | -44.6% | 6% | 12.5% | 4.3 | no | no |
| b4d_not_ext10 | INFO | -0.99 | +2.5% | -0.3% | 0% | -5.3% | 2.39 | -8.8% | 15% | 13.2% | 4.5 |  |  |
| b4d_resistance | IS | -1.80 | +1.7% | -0.9% | 2% | -19.1% | 1.04 | -60.7% | 14% | 17.7% | 6.0 |  |  |
| b4d_resistance | OOS | -4.81 | -0.7% | -2.5% | 2% | -12.0% | -0.66 | -37.3% | 9% | 13.9% | 4.9 | no | no |
| b4d_resistance | INFO | -3.16 | +1.0% | -1.5% | 0% | -6.5% | 0.78 | -12.6% | 15% | 16.7% | 5.7 |  |  |
| b4d_patient_limit | IS | -1.35 | +1.6% | -0.6% | 2% | -18.8% | 1.01 | -62.0% | 13% | 13.7% | 5.4 |  |  |
| b4d_patient_limit | OOS | -6.33 | -1.5% | -3.0% | 1% | -11.8% | -1.60 | -50.9% | 3% | 10.4% | 4.4 | no | no |
| b4d_patient_limit | INFO | -1.83 | -0.2% | -0.7% | 0% | -6.2% | -0.04 | -11.6% | 0% | 12.4% | 5.1 |  |  |

## Regimes, analogs, long / short, correlation (OOS unless noted)

Regime slices: mean daily return (days) by BTC regime (config/lab.yaml), OOS. Analogs: mean 14d return after the 30 historical states nearest to today (outcomes to 2026-06-30). Long / short P&L: sum over the half / mean equity (runs with recorded positions); short hit = share of short episodes with P&L > 0.

| run | bull | bear | chop | shock | analogs 14d mean / P>=10% | long P&L OOS | short P&L OOS | short hit OOS | net short OOS | corr live | corr BTC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| live xsmom R1 | +0.18% (86) | -0.17% (108) | -0.09% (329) | +0.02% (22) | -0.4% / 17% | -14.5% | +0.0% |  | 0% |  | 0.45 |
| s3v2e_core10 | +0.20% (86) | +0.18% (108) | -0.01% (329) | -0.02% (22) | +0.4% / 0% | +17.0% | +21.0% | 40% | 47% | 0.32 | -0.09 |
| b4d_pullback | -0.11% (86) | -0.24% (108) | -0.10% (329) | +0.11% (22) | -1.5% / 3% | -55.3% | +0.0% |  | 0% | 0.70 | 0.39 |
| b4d_not_ext6 | -0.04% (86) | -0.09% (108) | -0.03% (329) | -0.19% (22) | -0.7% / 3% | -16.2% | +0.0% |  | 0% | 0.66 | 0.38 |
| b4d_not_ext10 | +0.08% (86) | -0.22% (108) | -0.07% (329) | -0.17% (22) | -0.7% / 13% | -26.8% | +0.0% |  | 0% | 0.77 | 0.42 |
| b4d_resistance | +0.18% (86) | -0.16% (108) | -0.08% (329) | +0.04% (22) | -0.6% / 13% | -9.5% | +0.0% |  | 0% | 1.00 | 0.45 |
| b4d_patient_limit | -0.02% (86) | -0.27% (108) | -0.08% (329) | +0.05% (22) | -0.6% / 13% | -31.3% | +0.0% |  | 0% | 0.89 | 0.42 |
