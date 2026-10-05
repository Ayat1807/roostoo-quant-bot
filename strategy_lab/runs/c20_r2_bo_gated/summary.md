# Run: c20_r2_bo_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +117.18% | +12.93% | 0.94 | 1.36 | -18.80% | 0.69 | 1.03 |
| in_sample | 2020-02-15 → 2024-12-31 | +67.06% | +11.08% | 0.85 | 1.22 | -18.80% | 0.59 | 0.92 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +30.11% | +19.24% | 1.23 | 1.77 | -13.28% | 1.45 | 1.51 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.67% | +18.68% | 1.13 | 1.64 | -13.28% | 1.41 | 1.42 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.18% | 45% | -7.01% | -7.59% | -1.44 | 14 | 100% |
| out_of_sample | 532 | -0.13% | 46% | -7.01% | -7.59% | -0.73 | 14 | 100% |
| in_sample | 1768 | -0.17% | 45% | -6.31% | -6.70% | -1.58 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.152% | 58% | 2.52 | +28.00% |
| bull | 659 | 28% | +0.090% | 53% | 2.75 | +79.03% |
| bear | 399 | 17% | +0.015% | 47% | 0.44 | +5.18% |
| chop | 1099 | 47% | -0.005% | 44% | -0.13 | -7.77% |

## Turnover, fees, activity

- trades: 5570 (2.39/day); active days 100%
- turnover 38.4x equity/year; fees 3.84% of equity/year ($18,576 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.98
