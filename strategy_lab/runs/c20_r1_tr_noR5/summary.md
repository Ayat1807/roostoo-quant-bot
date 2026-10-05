# Run: c20_r1_tr_noR5

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +125.62% | +13.61% | 0.87 | 1.22 | -22.19% | 0.61 | 0.93 |
| in_sample | 2020-02-15 → 2024-12-31 | +77.13% | +12.42% | 0.81 | 1.14 | -22.19% | 0.56 | 0.87 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +27.48% | +17.63% | 1.05 | 1.51 | -12.69% | 1.39 | 1.33 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +10.18% | +13.84% | 0.85 | 1.23 | -12.69% | 1.09 | 1.07 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.26% | 45% | -7.23% | -7.83% | -1.43 | 14 | 100% |
| out_of_sample | 532 | -0.33% | 43% | -7.09% | -7.83% | -1.49 | 14 | 100% |
| in_sample | 1768 | -0.22% | 45% | -7.23% | -7.61% | -1.37 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.193% | 55% | 2.94 | +37.01% |
| bull | 659 | 28% | +0.107% | 54% | 2.60 | +98.17% |
| bear | 399 | 17% | -0.023% | 46% | -0.67 | -9.43% |
| chop | 1099 | 47% | -0.002% | 44% | -0.06 | -6.09% |

## Turnover, fees, activity

- trades: 11699 (5.03/day); active days 100%
- turnover 50.5x equity/year; fees 5.05% of equity/year ($25,342 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.93
