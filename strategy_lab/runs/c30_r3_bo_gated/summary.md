# Run: c30_r3_bo_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +104.60% | +11.88% | 0.94 | 1.35 | -17.51% | 0.68 | 1.03 |
| in_sample | 2020-02-15 → 2024-12-31 | +59.27% | +10.00% | 0.83 | 1.19 | -17.51% | 0.57 | 0.90 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +28.56% | +18.29% | 1.26 | 1.82 | -12.30% | 1.49 | 1.55 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.94% | +17.67% | 1.15 | 1.68 | -12.30% | 1.44 | 1.45 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.15% | 46% | -6.51% | -7.05% | -1.43 | 14 | 100% |
| out_of_sample | 532 | -0.11% | 47% | -6.51% | -7.05% | -0.66 | 14 | 100% |
| in_sample | 1768 | -0.15% | 45% | -5.65% | -6.00% | -1.53 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.143% | 58% | 2.61 | +26.31% |
| bull | 659 | 28% | +0.086% | 54% | 2.86 | +73.94% |
| bear | 399 | 17% | +0.014% | 47% | 0.45 | +4.94% |
| chop | 1099 | 47% | -0.007% | 44% | -0.21 | -9.44% |

## Turnover, fees, activity

- trades: 5493 (2.36/day); active days 100%
- turnover 35.0x equity/year; fees 3.50% of equity/year ($16,648 total)
- average gross exposure 0.15; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.97
