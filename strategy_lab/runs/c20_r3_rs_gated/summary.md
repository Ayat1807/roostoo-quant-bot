# Run: c20_r3_rs_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +112.49% | +12.54% | 0.91 | 1.31 | -19.17% | 0.65 | 0.99 |
| in_sample | 2020-02-15 → 2024-12-31 | +63.98% | +10.66% | 0.82 | 1.17 | -19.17% | 0.56 | 0.88 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +29.70% | +18.99% | 1.20 | 1.73 | -13.84% | 1.37 | 1.46 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.68% | +18.70% | 1.11 | 1.62 | -13.84% | 1.35 | 1.39 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.18% | 45% | -7.14% | -7.73% | -1.51 | 14 | 100% |
| out_of_sample | 532 | -0.15% | 46% | -7.14% | -7.73% | -1.08 | 14 | 100% |
| in_sample | 1768 | -0.18% | 45% | -6.24% | -6.63% | -1.59 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.154% | 58% | 2.53 | +28.46% |
| bull | 659 | 28% | +0.090% | 55% | 2.75 | +78.73% |
| bear | 399 | 17% | +0.016% | 48% | 0.47 | +5.68% |
| chop | 1099 | 47% | -0.007% | 44% | -0.20 | -10.37% |

## Turnover, fees, activity

- trades: 5584 (2.40/day); active days 100%
- turnover 38.0x equity/year; fees 3.80% of equity/year ($18,451 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
