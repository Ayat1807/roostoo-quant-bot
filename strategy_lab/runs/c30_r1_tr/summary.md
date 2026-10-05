# Run: c30_r1_tr

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +133.86% | +14.25% | 0.84 | 1.16 | -24.74% | 0.58 | 0.89 |
| in_sample | 2020-02-15 → 2024-12-31 | +93.87% | +14.52% | 0.86 | 1.17 | -24.74% | 0.59 | 0.90 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +20.71% | +13.41% | 0.79 | 1.11 | -12.96% | 1.04 | 0.99 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +5.20% | +7.02% | 0.49 | 0.70 | -11.71% | 0.60 | 0.61 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.36% | 44% | -7.05% | -7.63% | -1.90 | 14 | 100% |
| out_of_sample | 532 | -0.43% | 41% | -6.75% | -7.63% | -2.22 | 14 | 100% |
| in_sample | 1768 | -0.32% | 45% | -7.05% | -7.38% | -1.74 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.242% | 59% | 3.51 | +48.76% |
| bull | 659 | 28% | +0.117% | 54% | 2.38 | +110.04% |
| bear | 399 | 17% | -0.050% | 44% | -1.51 | -18.67% |
| chop | 1099 | 47% | -0.002% | 44% | -0.04 | -6.08% |

## Turnover, fees, activity

- trades: 11574 (4.97/day); active days 100%
- turnover 56.6x equity/year; fees 5.66% of equity/year ($29,126 total)
- average gross exposure 0.21; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.83
