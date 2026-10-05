# Run: c30_r1_tr_near

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +136.84% | +14.48% | 1.00 | 1.38 | -20.31% | 0.71 | 1.07 |
| in_sample | 2020-02-15 → 2024-12-31 | +107.79% | +16.16% | 1.08 | 1.50 | -20.31% | 0.80 | 1.16 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +14.05% | +9.19% | 0.70 | 0.98 | -10.89% | 0.84 | 0.85 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +11.47% | +15.62% | 1.13 | 1.63 | -10.54% | 1.48 | 1.44 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.22% | 45% | -5.95% | -6.37% | -1.60 | 14 | 100% |
| out_of_sample | 532 | -0.53% | 38% | -5.95% | -6.37% | -3.29 | 14 | 100% |
| in_sample | 1768 | -0.12% | 47% | -5.59% | -6.33% | -0.84 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.171% | 55% | 2.71 | +32.02% |
| bull | 659 | 28% | +0.122% | 53% | 2.80 | +118.08% |
| bear | 399 | 17% | +0.006% | 48% | 0.23 | +1.94% |
| chop | 1099 | 47% | -0.016% | 43% | -0.46 | -17.65% |

## Turnover, fees, activity

- trades: 7958 (3.42/day); active days 100%
- turnover 43.9x equity/year; fees 4.39% of equity/year ($23,756 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.86
