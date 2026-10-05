# Run: c20_r1_bo_near

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +141.62% | +14.83% | 1.05 | 1.48 | -19.98% | 0.74 | 1.13 |
| in_sample | 2020-02-15 → 2024-12-31 | +94.99% | +14.66% | 1.04 | 1.47 | -19.98% | 0.73 | 1.12 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +24.01% | +15.47% | 1.06 | 1.53 | -11.57% | 1.34 | 1.33 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.27% | +18.13% | 1.20 | 1.73 | -11.57% | 1.57 | 1.52 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.17% | 45% | -6.27% | -6.78% | -1.33 | 14 | 100% |
| out_of_sample | 532 | -0.22% | 44% | -6.27% | -6.78% | -1.43 | 14 | 100% |
| in_sample | 1768 | -0.14% | 46% | -5.64% | -5.98% | -1.20 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.179% | 55% | 2.88 | +34.01% |
| bull | 659 | 28% | +0.105% | 51% | 2.85 | +96.32% |
| bear | 399 | 17% | +0.013% | 48% | 0.44 | +4.73% |
| chop | 1099 | 47% | -0.007% | 43% | -0.20 | -10.25% |

## Turnover, fees, activity

- trades: 6543 (2.81/day); active days 100%
- turnover 42.4x equity/year; fees 4.24% of equity/year ($22,383 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.94
