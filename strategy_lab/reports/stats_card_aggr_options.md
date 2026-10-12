# Stats card: `b12_hmm_cusum_aggr`

_Generated 2026-10-10 09:47 UTC by `python -m lab.stats_card b12_hmm_cusum_aggr b3_s3v2e_core10 b3_s3v2e_tv06_core10 b12_aggr_mid b12_aggr_15` at lab commit d728bf5. Judged on data to 2026-06-30 (IS / OOS). **Jul-Oct 2026 is informational only.**_

**Luck threshold:** 524 trials declared across all blocks; the best of that many tries is expected to look about 2.9 standard errors better than its true value, so small differences between runs are noise.

**Constraints (each half):** P(14d <= -10%) <= 10% and worst 14d >= -20%. **Stress:** 100% taker fills and 7 bps slippage per fill (lab default 2 bps).


## IS

| metric | `b12_hmm_cusum_aggr` | `b3_s3v2e_core10` | `b3_s3v2e_tv06_core10` | `b12_aggr_mid` | `b12_aggr_15` |
|---|---|---|---|---|---|
| range | 2020-02-15 to 2024-12-31 | 2020-02-15 to 2024-12-31 | 2020-02-15 to 2024-12-31 | 2020-02-15 to 2024-12-31 | 2020-02-15 to 2024-12-31 |
| Total return | +107.0% | +97.8% | +116.0% | +96.1% | +125.9% |
| Sharpe | 0.59 | 1.00 | 0.77 | 0.72 | 0.89 |
| Sortino | 0.84 | 1.48 | 1.11 | 1.04 | 1.29 |
| Calmar | 0.38 | 0.89 | 0.54 | 0.66 | 0.85 |
| Composite, whole period | 0.63 | 1.16 | 0.83 | 0.83 | 1.04 |
| Composite, median of 14d windows | -1.36 | -1.61 | -1.47 | -1.73 | -0.30 |
| Max drawdown | -42.0% | -16.8% | -31.9% | -22.3% | -21.3% |
| 14d windows | 1768 | 1768 | 1768 | 1768 | 1768 |
| P(14d >= +10%) | 11% | 3% | 7% | 6% | 5% |
| P(14d >= +8%) | 15% | 4% | 10% | 9% | 7% |
| P(14d <= -10%) | 1% | 0% | 0% | 0% | 0% |
| Mean 14d | +0.8% | +0.6% | +0.8% | +0.7% | +0.7% |
| Median 14d | -0.8% | -0.2% | -0.4% | -0.4% | -0.1% |
| Worst 14d | -12.3% | -5.3% | -8.9% | -7.1% | -6.7% |
| % positive 14d | 45% | 46% | 44% | 43% | 49% |
| Constraints met | yes | yes | yes | yes | yes |
| Fees / yr (of equity) | 19.9% | 3.7% | 7.3% | 8.2% | 7.0% |
| Trades / day | 9.9 | 2.0 | 3.1 | 4.1 | 3.4 |
| Active days per 14 | 14.0 | 14.0 | 14.0 | 14.0 | 14.0 |
| Stress: total return | +15.6% | +73.7% | +77.1% | +24.6% | +78.0% |
| Stress: P(14d >= +10%) | 11% | 3% | 7% | 5% | 5% |
| Stress: P(14d <= -10%) | 1% | 0% | 0% | 0% | 0% |
| Stress: median 14d | -1.4% | -0.2% | -0.5% | -0.7% | -0.2% |
| Stress: worst 14d | -11.7% | -5.4% | -9.4% | -8.9% | -11.0% |

## OOS

| metric | `b12_hmm_cusum_aggr` | `b3_s3v2e_core10` | `b3_s3v2e_tv06_core10` | `b12_aggr_mid` | `b12_aggr_15` |
|---|---|---|---|---|---|
| range | 2025-01-01 to 2026-06-30 | 2025-01-01 to 2026-06-30 | 2025-01-01 to 2026-06-30 | 2025-01-01 to 2026-06-30 | 2025-01-01 to 2026-06-30 |
| Total return | -2.7% | +34.5% | +19.7% | +25.6% | +23.8% |
| Sharpe | 0.10 | 1.38 | 0.59 | 0.72 | 0.76 |
| Sortino | 0.15 | 2.00 | 0.85 | 1.05 | 1.10 |
| Calmar | -0.05 | 1.83 | 0.59 | 0.82 | 0.78 |
| Composite, whole period | 0.08 | 1.77 | 0.70 | 0.88 | 0.90 |
| Composite, median of 14d windows | -2.41 | -0.28 | -2.15 | -0.79 | 0.27 |
| Max drawdown | -34.4% | -12.0% | -21.6% | -20.0% | -19.7% |
| 14d windows | 532 | 532 | 532 | 532 | 532 |
| P(14d >= +10%) | 8% | 4% | 5% | 6% | 4% |
| P(14d >= +8%) | 12% | 6% | 7% | 9% | 7% |
| P(14d <= -10%) | 0% | 0% | 0% | 1% | 0% |
| Mean 14d | +0.1% | +0.8% | +0.6% | +0.8% | +0.6% |
| Median 14d | -1.4% | -0.1% | -0.6% | -0.3% | +0.1% |
| Worst 14d | -10.4% | -5.2% | -13.0% | -11.2% | -8.0% |
| % positive 14d | 43% | 48% | 42% | 47% | 51% |
| Constraints met | yes | yes | yes | yes | yes |
| Fees / yr (of equity) | 23.1% | 4.3% | 8.3% | 9.0% | 9.9% |
| Trades / day | 11.4 | 2.1 | 3.4 | 4.4 | 4.3 |
| Active days per 14 | 13.9 | 14.0 | 13.8 | 13.9 | 14.0 |
| Stress: total return | -31.9% | +31.2% | +17.6% | +24.8% | +16.9% |
| Stress: P(14d >= +10%) | 7% | 3% | 6% | 6% | 4% |
| Stress: P(14d <= -10%) | 3% | 0% | 0% | 0% | 0% |
| Stress: median 14d | -2.3% | -0.1% | -0.7% | -0.3% | -0.1% |
| Stress: worst 14d | -14.6% | -4.2% | -13.3% | -10.5% | -7.8% |

## Jul-Oct 2026 (info only)

| metric | `b12_hmm_cusum_aggr` | `b3_s3v2e_core10` | `b3_s3v2e_tv06_core10` | `b12_aggr_mid` | `b12_aggr_15` |
|---|---|---|---|---|---|
| range | 2026-07-01 to 2026-10-04 | 2026-07-01 to 2026-10-04 | 2026-07-01 to 2026-10-04 | 2026-07-01 to 2026-10-04 | 2026-07-01 to 2026-10-04 |
| Total return | -10.9% | +6.4% | -1.7% | -3.3% | -4.2% |
| Sharpe | -1.87 | 1.35 | -0.14 | -0.52 | -0.92 |
| Sortino | -2.68 | 2.05 | -0.20 | -0.74 | -1.32 |
| Calmar | -2.20 | 2.56 | -0.47 | -0.90 | -1.34 |
| Composite, whole period | -2.29 | 1.99 | -0.26 | -0.72 | -1.20 |
| Composite, median of 14d windows | -8.65 | -6.40 | -6.07 | -7.74 | -9.75 |
| Max drawdown | -16.3% | -10.4% | -13.5% | -13.4% | -11.4% |
| 14d windows | 82 | 82 | 82 | 82 | 82 |
| P(14d >= +10%) | 15% | 16% | 16% | 16% | 15% |
| P(14d >= +8%) | 16% | 16% | 17% | 17% | 16% |
| P(14d <= -10%) | 0% | 0% | 0% | 0% | 0% |
| Mean 14d | -0.8% | +1.6% | +0.3% | -0.1% | -0.3% |
| Median 14d | -3.5% | -0.9% | -2.5% | -2.9% | -2.7% |
| Worst 14d | -6.9% | -6.0% | -6.3% | -6.2% | -5.1% |
| % positive 14d | 20% | 38% | 22% | 22% | 20% |
| Constraints met | yes | yes | yes | yes | yes |
| Fees / yr (of equity) | 30.1% | 7.3% | 14.0% | 13.3% | 15.6% |
| Trades / day | 13.0 | 3.1 | 5.2 | 5.9 | 5.7 |
| Active days per 14 | 14.0 | 14.0 | 13.8 | 14.0 | 14.0 |
| Stress: total return | -13.0% | +5.5% | -3.3% | -4.3% | -4.9% |
| Stress: P(14d >= +10%) | 15% | 16% | 16% | 16% | 15% |
| Stress: P(14d <= -10%) | 0% | 0% | 0% | 0% | 0% |
| Stress: median 14d | -3.7% | -1.1% | -2.8% | -2.9% | -2.8% |
| Stress: worst 14d | -7.4% | -6.1% | -6.6% | -6.4% | -5.2% |

_Sharpe / Sortino / Calmar on hourly returns annualised x 24 x 365; Calmar = annualised return / |max drawdown|; composite = 0.4 Sortino + 0.3 Sharpe + 0.3 Calmar. 14-day windows step daily from 00:00 UTC and lie fully inside the period._
