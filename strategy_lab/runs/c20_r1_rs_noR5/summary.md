# Run: c20_r1_rs_noR5

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +157.18% | +15.96% | 0.96 | 1.34 | -25.90% | 0.62 | 1.01 |
| in_sample | 2020-02-15 → 2024-12-31 | +118.20% | +17.33% | 1.03 | 1.44 | -25.90% | 0.67 | 1.08 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +17.94% | +11.67% | 0.73 | 1.03 | -11.74% | 0.99 | 0.93 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +4.24% | +5.71% | 0.42 | 0.59 | -10.69% | 0.53 | 0.52 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.31% | 45% | -7.25% | -7.64% | -1.56 | 14 | 100% |
| out_of_sample | 532 | -0.25% | 46% | -6.16% | -7.64% | -1.10 | 14 | 100% |
| in_sample | 1768 | -0.31% | 45% | -7.25% | -7.57% | -1.53 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.226% | 59% | 3.30 | +44.75% |
| bull | 659 | 28% | +0.130% | 55% | 2.82 | +128.92% |
| bear | 399 | 17% | -0.054% | 45% | -1.59 | -20.00% |
| chop | 1099 | 47% | +0.003% | 45% | 0.06 | -0.71% |

## Turnover, fees, activity

- trades: 6674 (2.87/day); active days 100%
- turnover 41.5x equity/year; fees 4.15% of equity/year ($23,231 total)
- average gross exposure 0.21; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.85
