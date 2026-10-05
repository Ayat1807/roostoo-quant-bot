# Run: c30_r1_rs_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +86.60% | +10.27% | 0.78 | 1.12 | -19.78% | 0.52 | 0.84 |
| in_sample | 2020-02-15 → 2024-12-31 | +45.47% | +7.98% | 0.65 | 0.93 | -19.78% | 0.40 | 0.69 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +28.39% | +18.18% | 1.15 | 1.65 | -13.84% | 1.31 | 1.40 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.61% | +17.21% | 1.04 | 1.51 | -13.84% | 1.24 | 1.29 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.22% | 44% | -7.11% | -7.69% | -1.80 | 14 | 100% |
| out_of_sample | 532 | -0.18% | 46% | -7.11% | -7.69% | -1.08 | 14 | 100% |
| in_sample | 1768 | -0.22% | 43% | -6.18% | -6.56% | -1.99 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.150% | 58% | 2.58 | +27.80% |
| bull | 659 | 28% | +0.077% | 54% | 2.35 | +64.38% |
| bear | 399 | 17% | +0.016% | 47% | 0.50 | +5.92% |
| chop | 1099 | 47% | -0.012% | 44% | -0.33 | -14.42% |

## Turnover, fees, activity

- trades: 5583 (2.40/day); active days 100%
- turnover 37.2x equity/year; fees 3.72% of equity/year ($16,612 total)
- average gross exposure 0.16; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.97
