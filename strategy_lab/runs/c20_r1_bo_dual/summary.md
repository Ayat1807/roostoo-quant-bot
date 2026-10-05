# Run: c20_r1_bo_dual

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +117.84% | +12.98% | 0.90 | 1.28 | -20.29% | 0.64 | 0.97 |
| in_sample | 2020-02-15 → 2024-12-31 | +69.48% | +11.41% | 0.81 | 1.15 | -20.29% | 0.56 | 0.87 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +28.56% | +18.29% | 1.17 | 1.69 | -11.95% | 1.53 | 1.49 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.44% | +19.77% | 1.18 | 1.72 | -11.95% | 1.65 | 1.54 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.23% | 45% | -7.20% | -7.76% | -1.46 | 14 | 100% |
| out_of_sample | 532 | -0.18% | 45% | -7.20% | -7.76% | -0.99 | 14 | 100% |
| in_sample | 1768 | -0.23% | 45% | -6.60% | -6.98% | -1.48 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.196% | 57% | 3.12 | +37.72% |
| bull | 659 | 28% | +0.091% | 51% | 2.47 | +78.89% |
| bear | 399 | 17% | -0.007% | 44% | -0.22 | -3.64% |
| chop | 1099 | 47% | -0.003% | 43% | -0.08 | -6.09% |

## Turnover, fees, activity

- trades: 8425 (3.62/day); active days 100%
- turnover 50.5x equity/year; fees 5.05% of equity/year ($24,907 total)
- average gross exposure 0.18; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.96
