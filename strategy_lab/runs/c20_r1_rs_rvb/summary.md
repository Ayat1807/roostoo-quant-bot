# Run: c20_r1_rs_rvb

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +104.62% | +11.88% | 0.82 | 1.16 | -22.37% | 0.53 | 0.87 |
| in_sample | 2020-02-15 → 2024-12-31 | +55.99% | +9.53% | 0.69 | 0.97 | -22.37% | 0.43 | 0.72 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +31.30% | +19.97% | 1.20 | 1.74 | -13.66% | 1.46 | 1.50 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.35% | +18.25% | 1.05 | 1.52 | -13.66% | 1.34 | 1.33 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.21% | 45% | -7.34% | -8.05% | -1.44 | 14 | 100% |
| out_of_sample | 532 | -0.12% | 47% | -7.34% | -8.05% | -0.51 | 14 | 100% |
| in_sample | 1768 | -0.25% | 44% | -6.49% | -6.89% | -1.67 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.182% | 57% | 2.87 | +34.49% |
| bull | 659 | 28% | +0.096% | 54% | 2.63 | +85.68% |
| bear | 399 | 17% | -0.002% | 45% | -0.05 | -1.53% |
| chop | 1099 | 47% | -0.012% | 43% | -0.29 | -14.84% |

## Turnover, fees, activity

- trades: 6333 (2.72/day); active days 100%
- turnover 41.1x equity/year; fees 4.11% of equity/year ($19,592 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.97
