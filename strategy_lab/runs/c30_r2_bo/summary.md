# Run: c30_r2_bo

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +139.95% | +14.71% | 0.95 | 1.34 | -20.68% | 0.71 | 1.03 |
| in_sample | 2020-02-15 → 2024-12-31 | +83.70% | +13.27% | 0.89 | 1.24 | -20.68% | 0.64 | 0.95 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +30.71% | +19.61% | 1.14 | 1.64 | -11.46% | 1.71 | 1.51 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.18% | +16.61% | 1.01 | 1.45 | -9.90% | 1.68 | 1.39 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.27% | 44% | -7.24% | -7.57% | -1.95 | 14 | 100% |
| out_of_sample | 532 | -0.34% | 44% | -6.36% | -6.66% | -1.80 | 14 | 100% |
| in_sample | 1768 | -0.26% | 44% | -7.24% | -7.57% | -2.02 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.184% | 56% | 2.83 | +34.94% |
| bull | 659 | 28% | +0.114% | 53% | 2.68 | +106.85% |
| bear | 399 | 17% | -0.027% | 43% | -0.91 | -10.77% |
| chop | 1099 | 47% | +0.001% | 43% | 0.04 | -1.69% |

## Turnover, fees, activity

- trades: 7088 (3.04/day); active days 100%
- turnover 46.5x equity/year; fees 4.65% of equity/year ($22,814 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.86
