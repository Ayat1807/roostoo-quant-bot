# Run: c20_r4_tr_gated_near

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +113.91% | +12.66% | 0.94 | 1.36 | -18.63% | 0.68 | 1.03 |
| in_sample | 2020-02-15 → 2024-12-31 | +61.48% | +10.31% | 0.82 | 1.18 | -18.63% | 0.55 | 0.88 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +32.59% | +20.75% | 1.31 | 1.89 | -13.21% | 1.57 | 1.62 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.94% | +20.47% | 1.20 | 1.76 | -13.21% | 1.55 | 1.53 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.14% | 46% | -7.14% | -7.72% | -1.16 | 14 | 100% |
| out_of_sample | 532 | -0.10% | 48% | -7.14% | -7.72% | -0.55 | 14 | 100% |
| in_sample | 1768 | -0.14% | 46% | -6.30% | -6.68% | -1.17 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.148% | 58% | 2.49 | +27.15% |
| bull | 659 | 28% | +0.083% | 54% | 2.67 | +70.40% |
| bear | 399 | 17% | +0.016% | 48% | 0.49 | +5.92% |
| chop | 1099 | 47% | -0.002% | 44% | -0.05 | -4.60% |

## Turnover, fees, activity

- trades: 5428 (2.33/day); active days 100%
- turnover 37.3x equity/year; fees 3.73% of equity/year ($18,034 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 1.00
