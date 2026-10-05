# Run: c20_r1_tr_dual

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +110.83% | +12.41% | 0.85 | 1.21 | -20.95% | 0.59 | 0.92 |
| in_sample | 2020-02-15 → 2024-12-31 | +61.95% | +10.38% | 0.74 | 1.05 | -20.95% | 0.50 | 0.79 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +30.30% | +19.36% | 1.20 | 1.74 | -12.76% | 1.52 | 1.51 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.69% | +18.71% | 1.10 | 1.60 | -12.76% | 1.47 | 1.41 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.29% | 44% | -7.59% | -8.18% | -1.67 | 14 | 100% |
| out_of_sample | 532 | -0.15% | 46% | -7.59% | -8.18% | -0.93 | 14 | 100% |
| in_sample | 1768 | -0.31% | 44% | -7.12% | -7.50% | -2.01 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.177% | 56% | 2.77 | +33.34% |
| bull | 659 | 28% | +0.100% | 53% | 2.67 | +90.55% |
| bear | 399 | 17% | -0.017% | 43% | -0.48 | -7.33% |
| chop | 1099 | 47% | -0.005% | 44% | -0.13 | -8.36% |

## Turnover, fees, activity

- trades: 9483 (4.07/day); active days 100%
- turnover 46.9x equity/year; fees 4.69% of equity/year ($23,076 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.96
