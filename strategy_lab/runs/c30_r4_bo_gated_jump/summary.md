# Run: c30_r4_bo_gated_jump

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +102.56% | +11.70% | 0.94 | 1.36 | -16.16% | 0.72 | 1.04 |
| in_sample | 2020-02-15 → 2024-12-31 | +54.63% | +9.34% | 0.80 | 1.15 | -16.16% | 0.58 | 0.88 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +31.11% | +19.85% | 1.35 | 1.96 | -12.12% | 1.64 | 1.68 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.65% | +18.65% | 1.19 | 1.74 | -12.12% | 1.54 | 1.52 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.16% | 45% | -6.60% | -7.15% | -1.43 | 14 | 100% |
| out_of_sample | 532 | -0.10% | 48% | -6.60% | -7.15% | -0.60 | 14 | 100% |
| in_sample | 1768 | -0.17% | 44% | -5.84% | -6.20% | -1.55 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.141% | 58% | 2.59 | +25.86% |
| bull | 659 | 28% | +0.080% | 54% | 2.74 | +67.48% |
| bear | 399 | 17% | +0.014% | 47% | 0.44 | +4.88% |
| chop | 1099 | 47% | -0.004% | 44% | -0.12 | -6.49% |

## Turnover, fees, activity

- trades: 5326 (2.29/day); active days 100%
- turnover 35.2x equity/year; fees 3.52% of equity/year ($16,243 total)
- average gross exposure 0.15; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
