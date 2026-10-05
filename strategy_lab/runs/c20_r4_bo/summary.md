# Run: c20_r4_bo

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +125.53% | +13.60% | 0.92 | 1.30 | -19.17% | 0.71 | 1.01 |
| in_sample | 2020-02-15 → 2024-12-31 | +69.86% | +11.46% | 0.80 | 1.13 | -19.17% | 0.60 | 0.87 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +32.79% | +20.88% | 1.26 | 1.83 | -13.78% | 1.52 | 1.57 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +11.53% | +15.70% | 0.95 | 1.39 | -13.78% | 1.14 | 1.18 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.24% | 45% | -7.17% | -7.64% | -1.40 | 14 | 100% |
| out_of_sample | 532 | -0.29% | 45% | -7.17% | -7.64% | -1.69 | 14 | 100% |
| in_sample | 1768 | -0.19% | 45% | -6.96% | -7.35% | -1.24 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.188% | 55% | 3.11 | +36.05% |
| bull | 659 | 28% | +0.104% | 54% | 2.69 | +94.50% |
| bear | 399 | 17% | -0.010% | 45% | -0.30 | -4.67% |
| chop | 1099 | 47% | -0.005% | 43% | -0.13 | -8.50% |

## Turnover, fees, activity

- trades: 6895 (2.96/day); active days 100%
- turnover 43.7x equity/year; fees 4.37% of equity/year ($21,993 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.95
