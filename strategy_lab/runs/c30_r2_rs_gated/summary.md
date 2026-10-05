# Run: c30_r2_rs_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +94.83% | +11.02% | 0.84 | 1.19 | -17.00% | 0.65 | 0.92 |
| in_sample | 2020-02-15 → 2024-12-31 | +55.10% | +9.41% | 0.75 | 1.07 | -17.00% | 0.55 | 0.82 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +25.72% | +16.53% | 1.08 | 1.55 | -13.13% | 1.26 | 1.32 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +11.75% | +16.02% | 1.01 | 1.46 | -13.13% | 1.22 | 1.25 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.19% | 43% | -6.82% | -7.39% | -1.70 | 14 | 100% |
| out_of_sample | 532 | -0.17% | 46% | -6.82% | -7.39% | -1.10 | 14 | 100% |
| in_sample | 1768 | -0.19% | 43% | -5.96% | -6.33% | -1.82 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.159% | 58% | 2.82 | +29.75% |
| bull | 659 | 28% | +0.081% | 53% | 2.31 | +68.02% |
| bear | 399 | 17% | +0.016% | 47% | 0.49 | +5.65% |
| chop | 1099 | 47% | -0.011% | 44% | -0.31 | -13.67% |

## Turnover, fees, activity

- trades: 5480 (2.35/day); active days 100%
- turnover 36.3x equity/year; fees 3.63% of equity/year ($16,642 total)
- average gross exposure 0.16; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.95
