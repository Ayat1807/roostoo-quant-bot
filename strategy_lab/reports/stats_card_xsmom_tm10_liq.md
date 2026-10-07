# Stats card: `b3_xsmom_tm10_liq`

_Generated 2026-10-07 03:19 UTC by `python -m lab.stats_card b3_xsmom_tm10_liq b3_xsmom_r1` at lab commit 82f6d83. Judged on data to 2026-06-30 (IS / OOS). **Jul-Oct 2026 is informational only.**_

**Luck threshold:** 276 trials declared across all blocks; the best of that many tries is expected to look about 2.7 standard errors better than its true value, so small differences between runs are noise.

**Constraints (each half):** P(14d <= -10%) <= 10% and worst 14d >= -20%. **Stress:** 100% taker fills and 7 bps slippage per fill (lab default 2 bps).


## IS

| metric | `b3_xsmom_tm10_liq` | `b3_xsmom_r1` |
|---|---|---|
| range | 2020-02-15 to 2024-12-31 | 2020-02-15 to 2024-12-31 |
| Total return | +61.0% | +414.4% |
| Sharpe | 0.51 | 1.06 |
| Sortino | 0.68 | 1.46 |
| Calmar | 0.29 | 0.66 |
| Composite, whole period | 0.51 | 1.10 |
| Composite, median of 14d windows | -1.23 | -1.77 |
| Max drawdown | -34.9% | -60.2% |
| 14d windows | 1768 | 1768 |
| P(14d >= +10%) | 6% | 15% |
| P(14d >= +8%) | 8% | 18% |
| P(14d <= -10%) | 0% | 3% |
| Median 14d | -0.3% | -0.9% |
| Worst 14d | -11.3% | -19.1% |
| % positive 14d | 44% | 42% |
| Constraints met | yes | yes |
| Fees / yr (of equity) | 7.5% | 17.5% |
| Trades / day | 2.9 | 6.0 |
| Active days per 14 | 10.5 | 11.5 |
| Stress: total return | +38.2% | +344.8% |
| Stress: P(14d >= +10%) | 6% | 15% |
| Stress: P(14d <= -10%) | 0% | 3% |
| Stress: median 14d | -0.4% | -1.1% |
| Stress: worst 14d | -11.4% | -19.4% |

## OOS

| metric | `b3_xsmom_tm10_liq` | `b3_xsmom_r1` |
|---|---|---|
| range | 2025-01-01 to 2026-06-30 | 2025-01-01 to 2026-06-30 |
| Total return | -11.5% | -32.3% |
| Sharpe | -0.18 | -0.79 |
| Sortino | -0.25 | -1.10 |
| Calmar | -0.34 | -0.57 |
| Composite, whole period | -0.25 | -0.85 |
| Composite, median of 14d windows | -4.92 | -5.00 |
| Max drawdown | -22.9% | -40.2% |
| 14d windows | 532 | 532 |
| P(14d >= +10%) | 6% | 9% |
| P(14d >= +8%) | 8% | 11% |
| P(14d <= -10%) | 1% | 2% |
| Median 14d | -1.7% | -2.5% |
| Worst 14d | -11.3% | -12.0% |
| % positive 14d | 39% | 35% |
| Constraints met | yes | yes |
| Fees / yr (of equity) | 10.7% | 14.1% |
| Trades / day | 4.3 | 5.0 |
| Active days per 14 | 12.2 | 11.5 |
| Stress: total return | -21.4% | -38.8% |
| Stress: P(14d >= +10%) | 5% | 7% |
| Stress: P(14d <= -10%) | 1% | 2% |
| Stress: median 14d | -1.9% | -2.6% |
| Stress: worst 14d | -11.7% | -12.1% |

## Jul-Oct 2026 (info only)

| metric | `b3_xsmom_tm10_liq` | `b3_xsmom_r1` |
|---|---|---|
| range | 2026-07-01 to 2026-10-04 | 2026-07-01 to 2026-10-04 |
| Total return | +71.8% | +6.1% |
| Sharpe | 5.61 | 0.89 |
| Sortino | 9.04 | 1.26 |
| Calmar | 55.30 | 2.16 |
| Composite, whole period | 21.89 | 1.42 |
| Composite, median of 14d windows | 25.56 | -2.70 |
| Max drawdown | -12.5% | -11.7% |
| 14d windows | 82 | 82 |
| P(14d >= +10%) | 20% | 15% |
| P(14d >= +8%) | 24% | 16% |
| P(14d <= -10%) | 0% | 0% |
| Median 14d | +4.7% | -1.3% |
| Worst 14d | -7.6% | -6.4% |
| % positive 14d | 85% | 30% |
| Constraints met | yes | yes |
| Fees / yr (of equity) | 13.1% | 17.3% |
| Trades / day | 4.8 | 5.9 |
| Active days per 14 | 12.8 | 12.7 |
| Stress: total return | +67.0% | +2.3% |
| Stress: P(14d >= +10%) | 20% | 15% |
| Stress: P(14d <= -10%) | 0% | 0% |
| Stress: median 14d | +3.7% | -2.0% |
| Stress: worst 14d | -8.3% | -6.4% |

_Sharpe / Sortino / Calmar on hourly returns annualised x 24 x 365; Calmar = annualised return / |max drawdown|; composite = 0.4 Sortino + 0.3 Sharpe + 0.3 Calmar. 14-day windows step daily from 00:00 UTC and lie fully inside the period._
