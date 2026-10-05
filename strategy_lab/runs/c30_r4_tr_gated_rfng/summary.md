# Run: c30_r4_tr_gated_rfng

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +103.22% | +11.76% | 0.93 | 1.33 | -17.29% | 0.68 | 1.01 |
| in_sample | 2020-02-15 → 2024-12-31 | +58.09% | +9.83% | 0.82 | 1.17 | -17.29% | 0.57 | 0.89 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +28.65% | +18.34% | 1.24 | 1.79 | -12.37% | 1.48 | 1.54 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.32% | +16.80% | 1.09 | 1.59 | -12.37% | 1.36 | 1.37 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.13% | 46% | -6.56% | -7.10% | -1.25 | 14 | 100% |
| out_of_sample | 532 | -0.12% | 46% | -6.56% | -7.10% | -0.89 | 14 | 100% |
| in_sample | 1768 | -0.12% | 46% | -5.70% | -6.05% | -1.23 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.141% | 58% | 2.60 | +25.94% |
| bull | 659 | 28% | +0.083% | 53% | 2.64 | +70.32% |
| bear | 399 | 17% | +0.015% | 48% | 0.49 | +5.49% |
| chop | 1099 | 47% | -0.006% | 44% | -0.17 | -8.36% |

## Turnover, fees, activity

- trades: 5704 (2.45/day); active days 100%
- turnover 35.8x equity/year; fees 3.58% of equity/year ($16,864 total)
- average gross exposure 0.15; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.98
