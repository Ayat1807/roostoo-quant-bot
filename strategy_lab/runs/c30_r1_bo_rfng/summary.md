# Run: c30_r1_bo_rfng

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +104.71% | +11.89% | 0.81 | 1.15 | -21.78% | 0.55 | 0.87 |
| in_sample | 2020-02-15 → 2024-12-31 | +72.89% | +11.87% | 0.82 | 1.16 | -21.78% | 0.54 | 0.87 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +18.28% | +11.88% | 0.78 | 1.12 | -12.24% | 0.97 | 0.98 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.12% | +16.53% | 1.02 | 1.49 | -12.24% | 1.35 | 1.30 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.38% | 41% | -6.98% | -7.33% | -2.38 | 14 | 100% |
| out_of_sample | 532 | -0.53% | 41% | -6.61% | -7.14% | -2.46 | 14 | 100% |
| in_sample | 1768 | -0.35% | 42% | -6.98% | -7.33% | -2.30 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.195% | 57% | 3.13 | +37.63% |
| bull | 659 | 28% | +0.105% | 52% | 2.65 | +96.03% |
| bear | 399 | 17% | -0.023% | 44% | -0.73 | -9.62% |
| chop | 1099 | 47% | -0.011% | 43% | -0.28 | -14.32% |

## Turnover, fees, activity

- trades: 7442 (3.20/day); active days 100%
- turnover 46.8x equity/year; fees 4.68% of equity/year ($21,486 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.91
