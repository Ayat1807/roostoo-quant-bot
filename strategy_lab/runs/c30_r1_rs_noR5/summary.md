# Run: c30_r1_rs_noR5

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +164.80% | +16.50% | 0.91 | 1.25 | -28.50% | 0.58 | 0.95 |
| in_sample | 2020-02-15 → 2024-12-31 | +139.44% | +19.58% | 1.04 | 1.44 | -28.50% | 0.69 | 1.09 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +10.65% | +7.00% | 0.46 | 0.64 | -14.92% | 0.47 | 0.53 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -0.61% | -0.82% | 0.04 | 0.05 | -10.45% | -0.08 | 0.01 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.37% | 44% | -7.26% | -8.16% | -1.57 | 14 | 100% |
| out_of_sample | 532 | -0.29% | 45% | -6.23% | -7.28% | -1.17 | 14 | 100% |
| in_sample | 1768 | -0.37% | 44% | -7.26% | -8.16% | -1.53 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.248% | 58% | 3.42 | +50.03% |
| bull | 659 | 28% | +0.148% | 55% | 2.71 | +155.17% |
| bear | 399 | 17% | -0.085% | 45% | -2.32 | -29.34% |
| chop | 1099 | 47% | +0.004% | 45% | 0.08 | -0.10% |

## Turnover, fees, activity

- trades: 6674 (2.87/day); active days 100%
- turnover 41.3x equity/year; fees 4.13% of equity/year ($23,971 total)
- average gross exposure 0.22; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.73
