# Run: c30_r1_bo_dual

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +105.79% | +11.98% | 0.83 | 1.18 | -20.39% | 0.59 | 0.90 |
| in_sample | 2020-02-15 → 2024-12-31 | +66.36% | +10.99% | 0.77 | 1.08 | -20.39% | 0.54 | 0.83 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +23.67% | +15.26% | 1.04 | 1.49 | -10.92% | 1.40 | 1.33 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.15% | +17.96% | 1.14 | 1.66 | -10.92% | 1.64 | 1.50 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.27% | 45% | -6.79% | -7.32% | -1.72 | 14 | 100% |
| out_of_sample | 532 | -0.29% | 45% | -6.79% | -7.32% | -1.60 | 14 | 100% |
| in_sample | 1768 | -0.24% | 45% | -6.25% | -6.60% | -1.58 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.205% | 56% | 3.38 | +40.05% |
| bull | 659 | 28% | +0.089% | 50% | 2.26 | +76.90% |
| bear | 399 | 17% | -0.020% | 44% | -0.65 | -8.36% |
| chop | 1099 | 47% | -0.005% | 43% | -0.12 | -7.50% |

## Turnover, fees, activity

- trades: 8425 (3.62/day); active days 100%
- turnover 55.1x equity/year; fees 5.51% of equity/year ($26,484 total)
- average gross exposure 0.18; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.91
