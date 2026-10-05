# Run: c20_r4_bo_gated_dual

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +116.51% | +12.88% | 0.95 | 1.37 | -17.89% | 0.72 | 1.05 |
| in_sample | 2020-02-15 → 2024-12-31 | +62.18% | +10.41% | 0.81 | 1.17 | -17.89% | 0.58 | 0.89 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +33.62% | +21.38% | 1.34 | 1.95 | -12.74% | 1.68 | 1.69 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.74% | +20.18% | 1.20 | 1.74 | -12.74% | 1.58 | 1.53 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.17% | 45% | -7.08% | -7.66% | -1.44 | 14 | 100% |
| out_of_sample | 532 | -0.10% | 48% | -7.08% | -7.66% | -0.57 | 14 | 100% |
| in_sample | 1768 | -0.17% | 44% | -6.33% | -6.72% | -1.59 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.156% | 58% | 2.62 | +29.00% |
| bull | 659 | 28% | +0.086% | 54% | 2.71 | +73.86% |
| bear | 399 | 17% | +0.015% | 48% | 0.45 | +5.33% |
| chop | 1099 | 47% | -0.003% | 44% | -0.09 | -6.20% |

## Turnover, fees, activity

- trades: 5581 (2.40/day); active days 100%
- turnover 38.5x equity/year; fees 3.85% of equity/year ($18,501 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
