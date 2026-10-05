# Run: c30_r4_tr_gated_jump

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +97.03% | +11.22% | 0.90 | 1.29 | -17.55% | 0.64 | 0.98 |
| in_sample | 2020-02-15 → 2024-12-31 | +51.44% | +8.87% | 0.76 | 1.09 | -17.55% | 0.51 | 0.81 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +30.22% | +19.30% | 1.28 | 1.86 | -12.76% | 1.51 | 1.58 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.46% | +18.39% | 1.15 | 1.68 | -12.76% | 1.44 | 1.45 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.16% | 45% | -6.76% | -7.32% | -1.47 | 14 | 100% |
| out_of_sample | 532 | -0.11% | 47% | -6.76% | -7.32% | -0.70 | 14 | 100% |
| in_sample | 1768 | -0.16% | 44% | -5.92% | -6.28% | -1.60 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.141% | 58% | 2.55 | +25.81% |
| bull | 659 | 28% | +0.076% | 53% | 2.54 | +62.86% |
| bear | 399 | 17% | +0.015% | 48% | 0.49 | +5.57% |
| chop | 1099 | 47% | -0.005% | 44% | -0.13 | -7.05% |

## Turnover, fees, activity

- trades: 5499 (2.36/day); active days 100%
- turnover 35.6x equity/year; fees 3.56% of equity/year ($16,259 total)
- average gross exposure 0.16; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
