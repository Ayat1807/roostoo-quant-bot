# Block 5: risk-adjusted profit and down markets (new team objective)

_Generated 2026-10-07 11:09 UTC. Rules: `variants_b5_shorts.yaml` (declared before any run). Data to 2026-06-30, both halves (IS 2020-02-15 to 2024-12-31, OOS 2025-01-01 to 2026-06-30); Jul-Oct 2026 informational._

**Trials:** 496 declared across all blocks; luck threshold about 2.9 standard errors.

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
| b6b_hmm2 | IS | +0.6% (422) | 52% | -0.7% (709) | +2.1% (637) | yes |
| b6b_hmm2 | OOS | +2.1% (141) | 73% | -0.1% (272) | +1.7% (119) | yes |
| b6b_hmm2 | INFO | -1.8% (1) | 0% | -2.3% (51) | +7.4% (30) |  |
| b6c_erc | IS | +1.4% (422) | 58% | -0.9% (709) | +2.1% (637) | yes |
| b6c_erc | OOS | +2.4% (141) | 76% | -0.2% (272) | +1.1% (119) | yes |
| b6c_erc | INFO | -3.8% (1) | 0% | -2.3% (51) | +7.6% (30) |  |
| b6a_A3_cusum4_c50 | IS | +0.9% (422) | 55% | -0.7% (709) | +1.8% (637) | yes |
| b6a_A3_cusum4_c50 | OOS | +1.5% (141) | 72% | -0.1% (272) | +1.7% (119) | yes |
| b6a_A3_cusum4_c50 | INFO | -2.6% (1) | 0% | -2.5% (51) | +6.6% (30) |  |
| b7_hmm2_cusum | IS | +0.9% (422) | 56% | -0.7% (709) | +1.7% (637) | yes |
| b7_hmm2_cusum | OOS | +1.5% (141) | 71% | -0.0% (272) | +1.7% (119) | yes |
| b7_hmm2_cusum | INFO | -2.1% (1) | 0% | -2.3% (51) | +6.1% (30) |  |
| b7_erc_cusum | IS | +1.2% (422) | 56% | -0.9% (709) | +1.6% (637) | yes |
| b7_erc_cusum | OOS | +1.5% (141) | 75% | -0.4% (272) | +0.8% (119) | yes |
| b7_erc_cusum | INFO | -3.4% (1) | 0% | -2.3% (51) | +6.1% (30) |  |
| b7_hmm2_erc | IS | +1.4% (422) | 60% | -0.9% (709) | +2.0% (637) | yes |
| b7_hmm2_erc | OOS | +2.5% (141) | 76% | -0.1% (272) | +1.1% (119) | yes |
| b7_hmm2_erc | INFO | -2.0% (1) | 0% | -2.2% (51) | +7.2% (30) |  |
| b7_hmm2_erc_cusum | IS | +1.3% (422) | 58% | -0.9% (709) | +1.5% (637) | yes |
| b7_hmm2_erc_cusum | OOS | +1.6% (141) | 74% | -0.3% (272) | +0.9% (119) | yes |
| b7_hmm2_erc_cusum | INFO | -2.9% (1) | 0% | -2.1% (51) | +5.8% (30) |  |

## Primary metric, risk limits, verdict

| run | half | median 14d composite | mean 14d | median 14d | P(<= -10%) | worst 14d | Sharpe | max DD | P(>= +10%) | fees/yr | trades/day | meets all | beats s3v2e_core10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| live xsmom R1 | IS | -1.77 | +1.7% | -0.9% | 3% | -19.1% | 1.06 | -60.2% | 15% | 17.5% | 6.0 |  |  |
| live xsmom R1 | OOS | -5.00 | -0.8% | -2.5% | 2% | -12.0% | -0.79 | -40.2% | 9% | 14.1% | 5.0 | no | no |
| live xsmom R1 | INFO | -2.70 | +1.1% | -1.3% | 0% | -6.4% | 0.89 | -11.7% | 15% | 17.3% | 5.9 |  |  |
| s3v2e_core10 | IS | -1.61 | +0.6% | -0.2% | 0% | -5.3% | 1.00 | -16.8% | 3% | 3.7% | 2.0 |  |  |
| s3v2e_core10 | OOS | -0.28 | +0.8% | -0.1% | 0% | -5.2% | 1.38 | -12.0% | 4% | 4.3% | 2.1 | **yes** |  |
| s3v2e_core10 | INFO | -6.40 | +1.6% | -0.9% | 0% | -6.0% | 1.35 | -10.4% | 16% | 7.3% | 3.1 |  |  |
| b6b_hmm2 | IS | -1.29 | +0.6% | -0.2% | 0% | -5.6% | 1.02 | -18.5% | 3% | 3.7% | 2.0 |  |  |
| b6b_hmm2 | OOS | -0.26 | +0.8% | -0.1% | 0% | -5.2% | 1.46 | -11.5% | 3% | 4.1% | 2.1 | **yes** | no |
| b6b_hmm2 | INFO | -5.70 | +1.3% | -1.0% | 0% | -6.0% | 1.20 | -10.4% | 16% | 7.3% | 3.1 |  |  |
| b6c_erc | IS | -1.96 | +0.7% | -0.2% | 0% | -7.4% | 1.07 | -18.6% | 4% | 4.3% | 2.2 |  |  |
| b6c_erc | OOS | 0.71 | +0.8% | +0.1% | 0% | -5.5% | 1.24 | -13.1% | 5% | 4.5% | 2.2 | **yes** | no |
| b6c_erc | INFO | -8.35 | +1.3% | -1.8% | 0% | -5.5% | 1.10 | -10.1% | 17% | 9.5% | 3.6 |  |  |
| b6a_A3_cusum4_c50 | IS | -1.61 | +0.6% | -0.2% | 0% | -6.5% | 1.09 | -17.5% | 2% | 3.8% | 2.3 |  |  |
| b6a_A3_cusum4_c50 | OOS | 0.18 | +0.7% | +0.0% | 0% | -3.7% | 1.45 | -8.4% | 2% | 4.3% | 2.5 | **yes** | no |
| b6a_A3_cusum4_c50 | INFO | -8.74 | +0.8% | -1.4% | 0% | -5.5% | 0.66 | -10.0% | 15% | 7.4% | 3.4 |  |  |
| b7_hmm2_cusum | IS | -1.33 | +0.6% | -0.1% | 0% | -6.5% | 1.04 | -17.5% | 2% | 3.8% | 2.3 |  |  |
| b7_hmm2_cusum | OOS | 0.18 | +0.8% | +0.0% | 0% | -3.7% | 1.55 | -8.1% | 2% | 4.2% | 2.4 | **yes** | no |
| b7_hmm2_cusum | INFO | -6.96 | +0.8% | -1.2% | 0% | -5.5% | 0.63 | -10.0% | 15% | 7.2% | 3.4 |  |  |
| b7_erc_cusum | IS | -1.72 | +0.5% | -0.2% | 0% | -6.7% | 0.78 | -19.7% | 1% | 4.4% | 2.5 |  |  |
| b7_erc_cusum | OOS | 0.54 | +0.4% | +0.1% | 0% | -5.0% | 0.85 | -11.3% | 1% | 4.6% | 2.5 | no | no |
| b7_erc_cusum | INFO | -9.10 | +0.8% | -1.8% | 0% | -5.2% | 0.65 | -8.8% | 16% | 9.8% | 4.1 |  |  |
| b7_hmm2_erc | IS | -1.64 | +0.7% | -0.2% | 0% | -7.4% | 1.05 | -18.6% | 4% | 4.2% | 2.1 |  |  |
| b7_hmm2_erc | OOS | 1.18 | +0.8% | +0.1% | 0% | -5.5% | 1.36 | -12.0% | 5% | 4.4% | 2.1 | **yes** | no |
| b7_hmm2_erc | INFO | -7.78 | +1.3% | -1.8% | 0% | -5.1% | 1.18 | -9.3% | 17% | 9.6% | 3.7 |  |  |
| b7_hmm2_erc_cusum | IS | -1.56 | +0.5% | -0.2% | 0% | -6.7% | 0.80 | -19.5% | 1% | 4.4% | 2.5 |  |  |
| b7_hmm2_erc_cusum | OOS | 0.77 | +0.5% | +0.1% | 0% | -4.8% | 1.04 | -10.3% | 1% | 4.5% | 2.4 | **yes** | no |
| b7_hmm2_erc_cusum | INFO | -7.90 | +0.8% | -1.8% | 0% | -5.2% | 0.73 | -8.2% | 16% | 9.4% | 4.1 |  |  |

## Regimes, analogs, long / short, correlation (OOS unless noted)

Regime slices: mean daily return (days) by BTC regime (config/lab.yaml), OOS. Analogs: mean 14d return after the 30 historical states nearest to today (outcomes to 2026-06-30). Long / short P&L: sum over the half / mean equity (runs with recorded positions); short hit = share of short episodes with P&L > 0.

| run | bull | bear | chop | shock | analogs 14d mean / P>=10% | long P&L OOS | short P&L OOS | short hit OOS | net short OOS | corr live | corr BTC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| live xsmom R1 | +0.18% (86) | -0.17% (108) | -0.09% (329) | +0.02% (22) | -0.4% / 17% | -14.5% | +0.0% |  | 0% |  | 0.45 |
| s3v2e_core10 | +0.20% (86) | +0.18% (108) | -0.01% (329) | -0.02% (22) | +0.4% / 0% | +17.0% | +21.0% | 40% | 47% | 0.32 | -0.09 |
| b6b_hmm2 | +0.19% (86) | +0.18% (108) | -0.01% (329) | -0.03% (22) | +0.4% / 0% | +16.3% | +22.8% | 42% | 48% | 0.32 | -0.09 |
| b6c_erc | +0.12% (86) | +0.22% (108) | -0.01% (329) | -0.04% (22) | +0.4% / 0% | +11.0% | +25.1% | 42% | 50% | 0.31 | -0.14 |
| b6a_A3_cusum4_c50 | +0.18% (86) | +0.13% (108) | -0.00% (329) | -0.07% (22) | +0.4% / 0% | +18.7% | +15.7% | 40% | 47% | 0.30 | -0.10 |
| b7_hmm2_cusum | +0.17% (86) | +0.14% (108) | +0.00% (329) | -0.07% (22) | +0.4% / 0% | +18.6% | +16.9% | 41% | 48% | 0.30 | -0.10 |
| b7_erc_cusum | +0.06% (86) | +0.14% (108) | -0.01% (329) | -0.08% (22) | +0.4% / 0% | +8.6% | +14.5% | 41% | 49% | 0.30 | -0.14 |
| b7_hmm2_erc | +0.12% (86) | +0.22% (108) | -0.01% (329) | -0.03% (22) | +0.4% / 0% | +11.6% | +27.1% | 46% | 49% | 0.30 | -0.14 |
| b7_hmm2_erc_cusum | +0.06% (86) | +0.15% (108) | -0.00% (329) | -0.08% (22) | +0.4% / 0% | +9.4% | +16.9% | 45% | 49% | 0.29 | -0.14 |

## Secondary: 3-day horizon (mean / median / P(> 0) / worst)

| run | IS | OOS | 30 analog windows |
|---|---|---|---|
| live xsmom R1 | +0.3% / -0.1% / 39% / -12.0% | -0.2% / -0.4% / 34% / -7.2% | -1.3% / -1.9% / 23% / -3.8% |
| s3v2e_core10 | +0.1% / -0.1% / 43% / -4.0% | +0.2% / -0.1% / 43% / -3.7% | -0.2% / -0.1% / 33% / -1.8% |
| b6b_hmm2 | +0.1% / -0.1% / 43% / -4.0% | +0.2% / -0.0% / 44% / -3.4% | -0.2% / -0.2% / 30% / -1.8% |
| b6c_erc | +0.2% / -0.1% / 43% / -4.8% | +0.2% / -0.1% / 42% / -4.0% | -0.3% / -0.2% / 23% / -1.8% |
| b6a_A3_cusum4_c50 | +0.1% / -0.1% / 43% / -4.0% | +0.2% / -0.1% / 42% / -3.1% | -0.2% / -0.2% / 33% / -1.6% |
| b7_hmm2_cusum | +0.1% / -0.1% / 43% / -4.0% | +0.2% / -0.0% / 42% / -3.1% | -0.2% / -0.2% / 30% / -1.6% |
| b7_erc_cusum | +0.1% / -0.1% / 43% / -4.6% | +0.1% / -0.1% / 40% / -3.0% | -0.3% / -0.2% / 23% / -1.6% |
| b7_hmm2_erc | +0.1% / -0.1% / 43% / -4.8% | +0.2% / -0.1% / 44% / -3.6% | -0.3% / -0.2% / 27% / -1.8% |
| b7_hmm2_erc_cusum | +0.1% / -0.1% / 43% / -4.6% | +0.1% / -0.1% / 43% / -2.8% | -0.3% / -0.2% / 23% / -1.6% |

## Margin vs the reference (b3_s3v2e_core10) and the luck threshold

t = margin / standard error (see variants_b7_combo.yaml). Luck threshold for 496 declared trials: about 2.9 SE. A margin is distinguishable from selection luck only if t exceeds it.

| run | half | mean 14d diff | t | median composite diff | t | beats on both (sign) | clears luck threshold on both |
|---|---|---|---|---|---|---|---|
| b6b_hmm2 | IS | -0.00% | -0.09 | +0.31 | +1.08 | no | no |
| b6b_hmm2 | OOS | +0.03% | +0.72 | +0.02 | +0.09 | yes | no |
| b6c_erc | IS | +0.12% | +0.77 | -0.36 | -0.51 | no | no |
| b6c_erc | OOS | -0.06% | -0.26 | +0.99 | +0.96 | no | no |
| b6a_A3_cusum4_c50 | IS | -0.03% | -0.34 | -0.00 | -0.00 | no | no |
| b6a_A3_cusum4_c50 | OOS | -0.09% | -0.60 | +0.46 | +0.76 | no | no |
| b7_hmm2_cusum | IS | -0.07% | -0.71 | +0.28 | +0.46 | no | no |
| b7_hmm2_cusum | OOS | -0.06% | -0.37 | +0.47 | +0.72 | no | no |
| b7_erc_cusum | IS | -0.15% | -1.13 | -0.11 | -0.16 | no | no |
| b7_erc_cusum | OOS | -0.41% | -1.49 | +0.83 | +0.90 | no | no |
| b7_hmm2_erc | IS | +0.09% | +0.61 | -0.03 | -0.04 | no | no |
| b7_hmm2_erc | OOS | +0.01% | +0.04 | +1.46 | +1.33 | yes | no |
| b7_hmm2_erc_cusum | IS | -0.14% | -1.09 | +0.05 | +0.07 | no | no |
| b7_hmm2_erc_cusum | OOS | -0.31% | -1.15 | +1.05 | +1.11 | no | no |
