# Run: c30_r4_bo

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +117.33% | +12.94% | 0.86 | 1.21 | -20.20% | 0.64 | 0.93 |
| in_sample | 2020-02-15 → 2024-12-31 | +66.94% | +11.07% | 0.76 | 1.05 | -20.20% | 0.55 | 0.81 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +30.15% | +19.26% | 1.18 | 1.71 | -13.84% | 1.39 | 1.45 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +8.83% | +11.98% | 0.78 | 1.13 | -13.84% | 0.87 | 0.94 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.28% | 44% | -6.82% | -7.17% | -1.78 | 14 | 100% |
| out_of_sample | 532 | -0.34% | 45% | -6.78% | -7.16% | -1.84 | 14 | 100% |
| in_sample | 1768 | -0.26% | 44% | -6.82% | -7.17% | -1.64 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.193% | 54% | 3.33 | +37.37% |
| bull | 659 | 28% | +0.109% | 54% | 2.58 | +101.19% |
| bear | 399 | 17% | -0.024% | 44% | -0.76 | -9.73% |
| chop | 1099 | 47% | -0.008% | 43% | -0.20 | -11.10% |

## Turnover, fees, activity

- trades: 6895 (2.96/day); active days 100%
- turnover 44.6x equity/year; fees 4.46% of equity/year ($22,114 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.89
