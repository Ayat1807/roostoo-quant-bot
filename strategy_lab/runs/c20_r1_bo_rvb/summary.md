# Run: c20_r1_bo_rvb

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +118.11% | +13.01% | 0.89 | 1.27 | -22.16% | 0.59 | 0.95 |
| in_sample | 2020-02-15 → 2024-12-31 | +73.04% | +11.89% | 0.84 | 1.19 | -22.16% | 0.54 | 0.89 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +26.15% | +16.80% | 1.07 | 1.54 | -12.90% | 1.30 | 1.33 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.76% | +17.42% | 1.04 | 1.51 | -12.90% | 1.35 | 1.32 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.23% | 45% | -7.06% | -7.63% | -1.61 | 14 | 100% |
| out_of_sample | 532 | -0.12% | 47% | -7.06% | -7.63% | -0.72 | 14 | 100% |
| in_sample | 1768 | -0.25% | 45% | -6.09% | -6.51% | -1.73 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.228% | 59% | 3.63 | +45.51% |
| bull | 659 | 28% | +0.100% | 52% | 2.65 | +89.75% |
| bear | 399 | 17% | -0.003% | 45% | -0.09 | -1.99% |
| chop | 1099 | 47% | -0.015% | 42% | -0.38 | -17.50% |

## Turnover, fees, activity

- trades: 6883 (2.96/day); active days 100%
- turnover 43.5x equity/year; fees 4.35% of equity/year ($21,528 total)
- average gross exposure 0.18; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.95
