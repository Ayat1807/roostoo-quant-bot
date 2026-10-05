# Run: c30_r1_bo_noR5

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +125.10% | +13.57% | 0.83 | 1.17 | -27.96% | 0.49 | 0.86 |
| in_sample | 2020-02-15 → 2024-12-31 | +102.48% | +15.55% | 0.93 | 1.30 | -27.96% | 0.56 | 0.97 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +10.97% | +7.20% | 0.50 | 0.72 | -12.61% | 0.57 | 0.61 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +4.63% | +6.24% | 0.46 | 0.66 | -10.05% | 0.62 | 0.59 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.50% | 41% | -6.66% | -6.97% | -2.53 | 14 | 100% |
| out_of_sample | 532 | -0.72% | 36% | -5.89% | -6.64% | -3.05 | 14 | 100% |
| in_sample | 1768 | -0.42% | 42% | -6.66% | -6.97% | -2.24 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.287% | 53% | 4.09 | +60.24% |
| bull | 659 | 28% | +0.106% | 51% | 2.23 | +95.85% |
| bear | 399 | 17% | -0.039% | 44% | -1.19 | -14.99% |
| chop | 1099 | 47% | -0.010% | 44% | -0.25 | -13.89% |

## Turnover, fees, activity

- trades: 7583 (3.26/day); active days 100%
- turnover 49.4x equity/year; fees 4.94% of equity/year ($25,726 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.79
