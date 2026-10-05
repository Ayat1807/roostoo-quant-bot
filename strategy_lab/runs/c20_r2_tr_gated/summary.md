# Run: c20_r2_tr_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +118.73% | +13.06% | 0.95 | 1.36 | -18.78% | 0.70 | 1.04 |
| in_sample | 2020-02-15 → 2024-12-31 | +68.28% | +11.25% | 0.86 | 1.23 | -18.78% | 0.60 | 0.93 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +30.10% | +19.23% | 1.21 | 1.75 | -13.19% | 1.46 | 1.50 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.01% | +17.77% | 1.08 | 1.58 | -13.19% | 1.35 | 1.36 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.18% | 44% | -6.96% | -7.53% | -1.54 | 14 | 100% |
| out_of_sample | 532 | -0.13% | 46% | -6.96% | -7.53% | -0.78 | 14 | 100% |
| in_sample | 1768 | -0.18% | 44% | -6.29% | -6.68% | -1.74 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.160% | 58% | 2.68 | +29.75% |
| bull | 659 | 28% | +0.090% | 53% | 2.62 | +78.84% |
| bear | 399 | 17% | +0.015% | 48% | 0.46 | +5.47% |
| chop | 1099 | 47% | -0.006% | 44% | -0.15 | -8.52% |

## Turnover, fees, activity

- trades: 6148 (2.64/day); active days 100%
- turnover 38.6x equity/year; fees 3.86% of equity/year ($18,863 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.98
