# Run: c20_r4_rs

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +117.43% | +12.95% | 0.85 | 1.19 | -23.42% | 0.55 | 0.90 |
| in_sample | 2020-02-15 → 2024-12-31 | +66.26% | +10.97% | 0.74 | 1.03 | -23.42% | 0.47 | 0.78 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +30.90% | +19.72% | 1.18 | 1.69 | -12.99% | 1.52 | 1.49 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.22% | +18.06% | 1.05 | 1.52 | -12.99% | 1.39 | 1.34 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.30% | 43% | -7.03% | -7.69% | -1.47 | 14 | 100% |
| out_of_sample | 532 | -0.24% | 43% | -6.94% | -7.69% | -1.14 | 14 | 100% |
| in_sample | 1768 | -0.32% | 43% | -7.03% | -7.39% | -1.52 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.143% | 56% | 2.22 | +25.97% |
| bull | 659 | 28% | +0.125% | 55% | 3.10 | +123.21% |
| bear | 399 | 17% | -0.022% | 45% | -0.64 | -9.38% |
| chop | 1099 | 47% | -0.009% | 44% | -0.22 | -12.67% |

## Turnover, fees, activity

- trades: 6367 (2.73/day); active days 100%
- turnover 40.7x equity/year; fees 4.07% of equity/year ($20,476 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.94
