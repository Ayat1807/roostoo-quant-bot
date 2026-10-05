# Run: c30_r4_tr_gated_dual

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +104.09% | +11.83% | 0.93 | 1.34 | -16.97% | 0.70 | 1.02 |
| in_sample | 2020-02-15 → 2024-12-31 | +57.77% | +9.79% | 0.82 | 1.17 | -16.97% | 0.58 | 0.89 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +29.46% | +18.84% | 1.27 | 1.83 | -12.38% | 1.52 | 1.57 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.15% | +16.57% | 1.08 | 1.58 | -12.38% | 1.34 | 1.36 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.15% | 45% | -6.53% | -7.07% | -1.35 | 14 | 100% |
| out_of_sample | 532 | -0.12% | 47% | -6.53% | -7.07% | -0.73 | 14 | 100% |
| in_sample | 1768 | -0.15% | 45% | -5.71% | -6.07% | -1.38 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.140% | 57% | 2.60 | +25.81% |
| bull | 659 | 28% | +0.083% | 54% | 2.62 | +71.13% |
| bear | 399 | 17% | +0.015% | 48% | 0.49 | +5.39% |
| chop | 1099 | 47% | -0.006% | 43% | -0.17 | -8.22% |

## Turnover, fees, activity

- trades: 5719 (2.46/day); active days 100%
- turnover 35.8x equity/year; fees 3.58% of equity/year ($16,830 total)
- average gross exposure 0.15; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.98
