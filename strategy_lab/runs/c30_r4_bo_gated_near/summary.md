# Run: c30_r4_bo_gated_near

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +106.66% | +12.05% | 0.98 | 1.41 | -15.98% | 0.75 | 1.09 |
| in_sample | 2020-02-15 → 2024-12-31 | +59.31% | +10.01% | 0.87 | 1.24 | -15.98% | 0.63 | 0.94 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +29.83% | +19.07% | 1.32 | 1.91 | -11.54% | 1.65 | 1.66 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.06% | +19.24% | 1.24 | 1.80 | -11.54% | 1.67 | 1.59 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.11% | 46% | -6.50% | -7.04% | -1.06 | 14 | 100% |
| out_of_sample | 532 | -0.09% | 48% | -6.50% | -7.04% | -0.56 | 14 | 100% |
| in_sample | 1768 | -0.11% | 46% | -5.60% | -5.94% | -1.06 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.137% | 58% | 2.57 | +25.08% |
| bull | 659 | 28% | +0.080% | 53% | 2.77 | +68.13% |
| bear | 399 | 17% | +0.015% | 48% | 0.50 | +5.47% |
| chop | 1099 | 47% | -0.003% | 44% | -0.08 | -4.92% |

## Turnover, fees, activity

- trades: 5349 (2.30/day); active days 100%
- turnover 34.4x equity/year; fees 3.44% of equity/year ($16,375 total)
- average gross exposure 0.15; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.98
