# Run: c20_r4_bo_gated_jump

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +115.69% | +12.81% | 0.95 | 1.38 | -17.59% | 0.73 | 1.06 |
| in_sample | 2020-02-15 → 2024-12-31 | +61.66% | +10.34% | 0.82 | 1.18 | -17.59% | 0.59 | 0.89 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +33.54% | +21.33% | 1.35 | 1.96 | -13.05% | 1.63 | 1.68 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.78% | +20.24% | 1.20 | 1.75 | -13.05% | 1.55 | 1.53 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.18% | 45% | -7.08% | -7.67% | -1.43 | 14 | 100% |
| out_of_sample | 532 | -0.10% | 48% | -7.08% | -7.67% | -0.58 | 14 | 100% |
| in_sample | 1768 | -0.19% | 45% | -6.34% | -6.73% | -1.56 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.154% | 58% | 2.58 | +28.45% |
| bull | 659 | 28% | +0.085% | 54% | 2.75 | +72.54% |
| bear | 399 | 17% | +0.015% | 47% | 0.44 | +5.26% |
| chop | 1099 | 47% | -0.003% | 44% | -0.07 | -5.37% |

## Turnover, fees, activity

- trades: 5326 (2.29/day); active days 100%
- turnover 37.6x equity/year; fees 3.76% of equity/year ($18,079 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 1.00
