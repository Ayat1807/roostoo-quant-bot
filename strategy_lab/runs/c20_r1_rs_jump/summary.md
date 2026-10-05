# Run: c20_r1_rs_jump

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +112.05% | +12.51% | 0.88 | 1.25 | -20.19% | 0.62 | 0.95 |
| in_sample | 2020-02-15 → 2024-12-31 | +63.09% | +10.54% | 0.77 | 1.09 | -20.19% | 0.52 | 0.83 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +30.13% | +19.25% | 1.20 | 1.73 | -13.62% | 1.41 | 1.48 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.26% | +16.73% | 1.01 | 1.47 | -13.62% | 1.23 | 1.26 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.24% | 45% | -7.29% | -7.96% | -1.66 | 14 | 100% |
| out_of_sample | 532 | -0.14% | 47% | -7.29% | -7.96% | -0.57 | 14 | 100% |
| in_sample | 1768 | -0.25% | 45% | -6.90% | -7.31% | -1.75 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.192% | 58% | 3.13 | +37.04% |
| bull | 659 | 28% | +0.100% | 55% | 2.75 | +90.77% |
| bear | 399 | 17% | -0.021% | 44% | -0.62 | -8.97% |
| chop | 1099 | 47% | -0.006% | 44% | -0.14 | -8.81% |

## Turnover, fees, activity

- trades: 6725 (2.89/day); active days 100%
- turnover 42.7x equity/year; fees 4.27% of equity/year ($20,932 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.96
