# Run: c30_r1_rs_near

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +108.73% | +12.23% | 0.86 | 1.20 | -21.64% | 0.57 | 0.91 |
| in_sample | 2020-02-15 → 2024-12-31 | +76.13% | +12.29% | 0.87 | 1.19 | -21.64% | 0.57 | 0.91 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +18.59% | +12.07% | 0.86 | 1.23 | -10.73% | 1.13 | 1.09 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +9.44% | +12.82% | 0.90 | 1.29 | -10.73% | 1.19 | 1.15 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.22% | 45% | -6.51% | -6.95% | -1.63 | 14 | 100% |
| out_of_sample | 532 | -0.31% | 42% | -6.51% | -6.95% | -1.92 | 14 | 100% |
| in_sample | 1768 | -0.18% | 46% | -5.53% | -6.35% | -1.34 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.135% | 56% | 2.21 | +24.27% |
| bull | 659 | 28% | +0.113% | 55% | 2.75 | +105.88% |
| bear | 399 | 17% | +0.001% | 49% | 0.05 | -0.02% |
| chop | 1099 | 47% | -0.014% | 43% | -0.41 | -16.72% |

## Turnover, fees, activity

- trades: 6072 (2.61/day); active days 100%
- turnover 37.9x equity/year; fees 3.79% of equity/year ($18,997 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.89
