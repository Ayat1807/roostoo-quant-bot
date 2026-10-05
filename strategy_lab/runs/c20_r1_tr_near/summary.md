# Run: c20_r1_tr_near

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +138.54% | +14.60% | 1.01 | 1.42 | -20.08% | 0.73 | 1.09 |
| in_sample | 2020-02-15 → 2024-12-31 | +97.10% | +14.91% | 1.03 | 1.45 | -20.08% | 0.74 | 1.11 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +21.11% | +13.66% | 0.94 | 1.35 | -11.71% | 1.17 | 1.17 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.19% | +18.02% | 1.18 | 1.70 | -11.71% | 1.54 | 1.50 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.21% | 45% | -6.61% | -7.10% | -1.59 | 14 | 100% |
| out_of_sample | 532 | -0.41% | 41% | -6.61% | -7.10% | -2.60 | 14 | 100% |
| in_sample | 1768 | -0.16% | 46% | -5.62% | -5.96% | -1.14 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.172% | 56% | 2.75 | +32.40% |
| bull | 659 | 28% | +0.112% | 54% | 2.89 | +105.99% |
| bear | 399 | 17% | +0.010% | 47% | 0.32 | +3.24% |
| chop | 1099 | 47% | -0.011% | 44% | -0.29 | -13.29% |

## Turnover, fees, activity

- trades: 7958 (3.42/day); active days 100%
- turnover 43.3x equity/year; fees 4.33% of equity/year ($23,088 total)
- average gross exposure 0.18; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.94
