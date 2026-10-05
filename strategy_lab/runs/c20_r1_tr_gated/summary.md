# Run: c20_r1_tr_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +120.52% | +13.20% | 0.95 | 1.37 | -18.60% | 0.71 | 1.05 |
| in_sample | 2020-02-15 → 2024-12-31 | +70.28% | +11.52% | 0.87 | 1.24 | -18.60% | 0.62 | 0.94 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +29.61% | +18.94% | 1.20 | 1.73 | -13.31% | 1.42 | 1.48 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.58% | +17.17% | 1.06 | 1.55 | -13.31% | 1.29 | 1.32 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.19% | 44% | -6.88% | -7.45% | -1.60 | 14 | 100% |
| out_of_sample | 532 | -0.14% | 46% | -6.88% | -7.45% | -1.08 | 14 | 100% |
| in_sample | 1768 | -0.19% | 44% | -6.17% | -6.55% | -1.85 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.179% | 58% | 2.95 | +34.03% |
| bull | 659 | 28% | +0.091% | 54% | 2.61 | +78.95% |
| bear | 399 | 17% | +0.014% | 47% | 0.43 | +4.90% |
| chop | 1099 | 47% | -0.007% | 44% | -0.20 | -10.29% |

## Turnover, fees, activity

- trades: 6644 (2.85/day); active days 100%
- turnover 38.9x equity/year; fees 3.89% of equity/year ($19,281 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.98
