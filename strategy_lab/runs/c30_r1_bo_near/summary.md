# Run: c30_r1_bo_near

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +141.46% | +14.82% | 1.05 | 1.47 | -19.91% | 0.74 | 1.13 |
| in_sample | 2020-02-15 → 2024-12-31 | +104.63% | +15.80% | 1.10 | 1.54 | -19.91% | 0.79 | 1.19 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +18.08% | +11.75% | 0.87 | 1.25 | -10.51% | 1.12 | 1.10 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +11.61% | +15.82% | 1.16 | 1.68 | -10.51% | 1.51 | 1.47 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.13% | 46% | -5.66% | -6.59% | -1.09 | 14 | 100% |
| out_of_sample | 532 | -0.20% | 43% | -5.45% | -5.88% | -1.16 | 14 | 100% |
| in_sample | 1768 | -0.10% | 47% | -5.66% | -6.59% | -0.90 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.180% | 55% | 2.91 | +34.20% |
| bull | 659 | 28% | +0.111% | 50% | 2.72 | +103.38% |
| bear | 399 | 17% | +0.011% | 48% | 0.44 | +4.16% |
| chop | 1099 | 47% | -0.011% | 43% | -0.32 | -13.32% |

## Turnover, fees, activity

- trades: 6543 (2.81/day); active days 100%
- turnover 42.5x equity/year; fees 4.25% of equity/year ($22,698 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.86
