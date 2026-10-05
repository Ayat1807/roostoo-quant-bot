# Run: c20_r1_rs

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +130.95% | +14.02% | 0.88 | 1.23 | -26.47% | 0.53 | 0.92 |
| in_sample | 2020-02-15 → 2024-12-31 | +87.81% | +13.78% | 0.87 | 1.21 | -26.47% | 0.52 | 0.90 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +23.07% | +14.89% | 0.93 | 1.31 | -11.05% | 1.35 | 1.21 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +8.14% | +11.03% | 0.72 | 1.02 | -11.05% | 1.00 | 0.92 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.35% | 44% | -7.17% | -7.92% | -1.72 | 14 | 100% |
| out_of_sample | 532 | -0.26% | 44% | -6.72% | -7.92% | -1.62 | 14 | 100% |
| in_sample | 1768 | -0.36% | 44% | -7.17% | -7.53% | -1.62 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.198% | 57% | 3.08 | +38.30% |
| bull | 659 | 28% | +0.118% | 55% | 2.76 | +113.00% |
| bear | 399 | 17% | -0.043% | 44% | -1.28 | -16.53% |
| chop | 1099 | 47% | -0.000% | 44% | -0.01 | -3.87% |

## Turnover, fees, activity

- trades: 6761 (2.90/day); active days 100%
- turnover 42.5x equity/year; fees 4.25% of equity/year ($22,249 total)
- average gross exposure 0.21; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.90
