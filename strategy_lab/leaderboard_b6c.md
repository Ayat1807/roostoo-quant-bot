# Block 5: risk-adjusted profit and down markets (new team objective)

_Generated 2026-10-07 10:47 UTC. Rules: `variants_b5_shorts.yaml` (declared before any run). Data to 2026-06-30, both halves (IS 2020-02-15 to 2024-12-31, OOS 2025-01-01 to 2026-06-30); Jul-Oct 2026 informational._

**Trials:** 482 declared across all blocks; luck threshold about 2.9 standard errors.

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
| b6c_erc | IS | +1.4% (422) | 58% | -0.9% (709) | +2.1% (637) | yes |
| b6c_erc | OOS | +2.4% (141) | 76% | -0.2% (272) | +1.1% (119) | yes |
| b6c_erc | INFO | -3.8% (1) | 0% | -2.3% (51) | +7.6% (30) |  |
| b6c_hrp | IS | +0.7% (422) | 51% | -0.8% (709) | +2.3% (637) | yes |
| b6c_hrp | OOS | +1.8% (141) | 64% | -0.4% (272) | +0.9% (119) | yes |
| b6c_hrp | INFO | -3.7% (1) | 0% | -2.4% (51) | +5.6% (30) |  |
| b6c_kelly | IS | +0.5% (422) | 46% | -0.4% (709) | +1.9% (637) | yes |
| b6c_kelly | OOS | +1.8% (141) | 70% | -0.8% (272) | +0.6% (119) | yes |
| b6c_kelly | INFO | -3.8% (1) | 0% | -2.3% (51) | +5.7% (30) |  |

## Primary metric, risk limits, verdict

| run | half | median 14d composite | mean 14d | median 14d | P(<= -10%) | worst 14d | Sharpe | max DD | P(>= +10%) | fees/yr | trades/day | meets all | beats s3v2e_core10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| live xsmom R1 | IS | -1.77 | +1.7% | -0.9% | 3% | -19.1% | 1.06 | -60.2% | 15% | 17.5% | 6.0 |  |  |
| live xsmom R1 | OOS | -5.00 | -0.8% | -2.5% | 2% | -12.0% | -0.79 | -40.2% | 9% | 14.1% | 5.0 | no | no |
| live xsmom R1 | INFO | -2.70 | +1.1% | -1.3% | 0% | -6.4% | 0.89 | -11.7% | 15% | 17.3% | 5.9 |  |  |
| s3v2e_core10 | IS | -1.61 | +0.6% | -0.2% | 0% | -5.3% | 1.00 | -16.8% | 3% | 3.7% | 2.0 |  |  |
| s3v2e_core10 | OOS | -0.28 | +0.8% | -0.1% | 0% | -5.2% | 1.38 | -12.0% | 4% | 4.3% | 2.1 | **yes** |  |
| s3v2e_core10 | INFO | -6.40 | +1.6% | -0.9% | 0% | -6.0% | 1.35 | -10.4% | 16% | 7.3% | 3.1 |  |  |
| b6c_erc | IS | -1.96 | +0.7% | -0.2% | 0% | -7.4% | 1.07 | -18.6% | 4% | 4.3% | 2.2 |  |  |
| b6c_erc | OOS | 0.71 | +0.8% | +0.1% | 0% | -5.5% | 1.24 | -13.1% | 5% | 4.5% | 2.2 | **yes** | no |
| b6c_erc | INFO | -8.35 | +1.3% | -1.8% | 0% | -5.5% | 1.10 | -10.1% | 17% | 9.5% | 3.6 |  |  |
| b6c_hrp | IS | -1.37 | +0.7% | -0.2% | 0% | -5.2% | 1.09 | -15.4% | 3% | 5.2% | 2.2 |  |  |
| b6c_hrp | OOS | -0.41 | +0.5% | -0.1% | 0% | -4.5% | 0.80 | -13.2% | 2% | 6.5% | 2.4 | no | no |
| b6c_hrp | INFO | -9.97 | +0.5% | -1.8% | 0% | -5.1% | 0.36 | -10.8% | 15% | 8.2% | 3.0 |  |  |
| b6c_kelly | IS | -0.73 | +0.7% | -0.1% | 0% | -7.0% | 0.97 | -17.5% | 2% | 4.1% | 2.1 |  |  |
| b6c_kelly | OOS | -2.32 | +0.2% | -0.3% | 0% | -5.6% | 0.33 | -17.5% | 4% | 4.3% | 2.1 | no | no |
| b6c_kelly | INFO | -3.39 | +0.6% | -0.6% | 0% | -5.6% | 0.24 | -10.8% | 13% | 7.3% | 3.0 |  |  |

## Regimes, analogs, long / short, correlation (OOS unless noted)

Regime slices: mean daily return (days) by BTC regime (config/lab.yaml), OOS. Analogs: mean 14d return after the 30 historical states nearest to today (outcomes to 2026-06-30). Long / short P&L: sum over the half / mean equity (runs with recorded positions); short hit = share of short episodes with P&L > 0.

| run | bull | bear | chop | shock | analogs 14d mean / P>=10% | long P&L OOS | short P&L OOS | short hit OOS | net short OOS | corr live | corr BTC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| live xsmom R1 | +0.18% (86) | -0.17% (108) | -0.09% (329) | +0.02% (22) | -0.4% / 17% | -14.5% | +0.0% |  | 0% |  | 0.45 |
| s3v2e_core10 | +0.20% (86) | +0.18% (108) | -0.01% (329) | -0.02% (22) | +0.4% / 0% | +17.0% | +21.0% | 40% | 47% | 0.32 | -0.09 |
| b6c_erc | +0.12% (86) | +0.22% (108) | -0.01% (329) | -0.04% (22) | +0.4% / 0% | +11.0% | +25.1% | 42% | 50% | 0.31 | -0.14 |
| b6c_hrp | +0.11% (86) | +0.18% (108) | -0.02% (329) | -0.12% (22) | +0.2% / 0% | +7.3% | +21.3% | 43% | 44% | 0.34 | -0.09 |
| b6c_kelly | +0.09% (86) | +0.18% (108) | -0.05% (329) | -0.14% (22) | +0.2% / 0% | +0.1% | +13.7% | 41% | 48% | 0.34 | -0.04 |

## Secondary: 3-day horizon (mean / median / P(> 0) / worst)

| run | IS | OOS | 30 analog windows |
|---|---|---|---|
| live xsmom R1 | +0.3% / -0.1% / 39% / -12.0% | -0.2% / -0.4% / 34% / -7.2% | -1.3% / -1.9% / 23% / -3.8% |
| s3v2e_core10 | +0.1% / -0.1% / 43% / -4.0% | +0.2% / -0.1% / 43% / -3.7% | -0.2% / -0.1% / 33% / -1.8% |
| b6c_erc | +0.2% / -0.1% / 43% / -4.8% | +0.2% / -0.1% / 42% / -4.0% | -0.3% / -0.2% / 23% / -1.8% |
| b6c_hrp | +0.1% / -0.1% / 43% / -5.1% | +0.1% / -0.1% / 42% / -4.4% | -0.2% / -0.2% / 33% / -1.8% |
| b6c_kelly | +0.1% / -0.0% / 45% / -6.6% | +0.0% / -0.1% / 39% / -4.9% | -0.3% / -0.1% / 43% / -3.2% |
