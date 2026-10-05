# Run: c30_r4_tr_gated_near

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +99.90% | +11.47% | 0.93 | 1.33 | -17.82% | 0.64 | 1.00 |
| in_sample | 2020-02-15 → 2024-12-31 | +54.36% | +9.30% | 0.80 | 1.15 | -17.82% | 0.52 | 0.86 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +29.61% | +18.93% | 1.27 | 1.84 | -12.36% | 1.53 | 1.58 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.89% | +19.00% | 1.20 | 1.75 | -12.36% | 1.54 | 1.52 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.12% | 46% | -6.68% | -7.24% | -1.10 | 14 | 100% |
| out_of_sample | 532 | -0.09% | 48% | -6.68% | -7.24% | -0.55 | 14 | 100% |
| in_sample | 1768 | -0.12% | 46% | -5.77% | -6.13% | -1.16 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.132% | 58% | 2.43 | +23.95% |
| bull | 659 | 28% | +0.077% | 54% | 2.61 | +64.27% |
| bear | 399 | 17% | +0.016% | 48% | 0.52 | +5.86% |
| chop | 1099 | 47% | -0.003% | 44% | -0.09 | -5.36% |

## Turnover, fees, activity

- trades: 5428 (2.33/day); active days 100%
- turnover 34.7x equity/year; fees 3.47% of equity/year ($16,175 total)
- average gross exposure 0.15; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
