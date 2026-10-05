# Run: c30_r4_tr

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +97.06% | +11.22% | 0.77 | 1.08 | -22.96% | 0.49 | 0.81 |
| in_sample | 2020-02-15 → 2024-12-31 | +49.88% | +8.64% | 0.62 | 0.86 | -22.96% | 0.38 | 0.64 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +31.59% | +20.15% | 1.21 | 1.75 | -13.74% | 1.47 | 1.50 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +11.53% | +15.71% | 0.95 | 1.39 | -13.74% | 1.14 | 1.18 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.31% | 43% | -7.27% | -7.64% | -1.75 | 14 | 100% |
| out_of_sample | 532 | -0.26% | 44% | -6.70% | -7.27% | -1.44 | 14 | 100% |
| in_sample | 1768 | -0.31% | 42% | -7.27% | -7.64% | -1.88 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.139% | 55% | 2.37 | +25.24% |
| bull | 659 | 28% | +0.098% | 54% | 2.43 | +86.75% |
| bear | 399 | 17% | -0.009% | 45% | -0.27 | -4.30% |
| chop | 1099 | 47% | -0.007% | 44% | -0.18 | -10.16% |

## Turnover, fees, activity

- trades: 8290 (3.56/day); active days 100%
- turnover 45.6x equity/year; fees 4.56% of equity/year ($21,105 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.93
