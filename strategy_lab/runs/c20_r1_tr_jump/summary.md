# Run: c20_r1_tr_jump

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +136.56% | +14.45% | 0.97 | 1.38 | -21.37% | 0.68 | 1.05 |
| in_sample | 2020-02-15 → 2024-12-31 | +85.11% | +13.44% | 0.92 | 1.31 | -21.37% | 0.63 | 0.99 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +27.89% | +17.88% | 1.12 | 1.61 | -13.39% | 1.33 | 1.38 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +11.64% | +15.86% | 1.00 | 1.44 | -13.39% | 1.18 | 1.23 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.26% | 44% | -6.85% | -7.56% | -1.53 | 14 | 100% |
| out_of_sample | 532 | -0.29% | 44% | -6.85% | -7.56% | -1.30 | 14 | 100% |
| in_sample | 1768 | -0.25% | 45% | -6.68% | -7.05% | -1.52 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.188% | 57% | 3.12 | +36.08% |
| bull | 659 | 28% | +0.096% | 54% | 2.54 | +85.19% |
| bear | 399 | 17% | -0.015% | 46% | -0.46 | -6.75% |
| chop | 1099 | 47% | +0.006% | 46% | 0.14 | +3.03% |

## Turnover, fees, activity

- trades: 10640 (4.57/day); active days 100%
- turnover 51.1x equity/year; fees 5.11% of equity/year ($26,820 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.94
