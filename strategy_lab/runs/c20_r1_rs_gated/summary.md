# Run: c20_r1_rs_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +105.04% | +11.92% | 0.86 | 1.24 | -19.90% | 0.60 | 0.93 |
| in_sample | 2020-02-15 → 2024-12-31 | +55.55% | +9.47% | 0.73 | 1.05 | -19.90% | 0.48 | 0.78 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +31.94% | +20.36% | 1.23 | 1.78 | -14.14% | 1.44 | 1.52 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.19% | +19.41% | 1.11 | 1.62 | -14.14% | 1.37 | 1.39 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.20% | 44% | -7.41% | -8.02% | -1.59 | 14 | 100% |
| out_of_sample | 532 | -0.16% | 47% | -7.41% | -8.02% | -0.92 | 14 | 100% |
| in_sample | 1768 | -0.20% | 44% | -6.57% | -6.98% | -1.72 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.160% | 58% | 2.58 | +29.75% |
| bull | 659 | 28% | +0.083% | 53% | 2.52 | +70.70% |
| bear | 399 | 17% | +0.017% | 47% | 0.48 | +5.94% |
| chop | 1099 | 47% | -0.008% | 44% | -0.20 | -10.56% |

## Turnover, fees, activity

- trades: 5583 (2.40/day); active days 100%
- turnover 39.0x equity/year; fees 3.90% of equity/year ($18,325 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
