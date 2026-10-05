# Run: c30_r3_rs

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +120.41% | +13.19% | 0.80 | 1.09 | -27.98% | 0.47 | 0.82 |
| in_sample | 2020-02-15 → 2024-12-31 | +96.56% | +14.85% | 0.86 | 1.18 | -27.98% | 0.53 | 0.89 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +12.21% | +8.01% | 0.56 | 0.79 | -10.92% | 0.73 | 0.71 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +7.95% | +10.78% | 0.74 | 1.05 | -10.10% | 1.07 | 0.96 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.37% | 44% | -7.40% | -7.71% | -1.81 | 14 | 100% |
| out_of_sample | 532 | -0.45% | 40% | -5.95% | -6.85% | -2.12 | 14 | 100% |
| in_sample | 1768 | -0.32% | 45% | -7.40% | -7.71% | -1.62 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.169% | 56% | 2.68 | +31.69% |
| bull | 659 | 28% | +0.158% | 55% | 3.16 | +174.76% |
| bear | 399 | 17% | -0.071% | 43% | -2.05 | -25.24% |
| chop | 1099 | 47% | -0.013% | 45% | -0.31 | -16.85% |

## Turnover, fees, activity

- trades: 6518 (2.80/day); active days 100%
- turnover 39.9x equity/year; fees 3.99% of equity/year ($21,932 total)
- average gross exposure 0.21; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.81
