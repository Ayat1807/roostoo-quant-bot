# Run: c20_r1_rs_near

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +119.79% | +13.14% | 0.92 | 1.30 | -20.93% | 0.63 | 0.98 |
| in_sample | 2020-02-15 → 2024-12-31 | +75.99% | +12.28% | 0.87 | 1.23 | -20.93% | 0.59 | 0.93 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +24.99% | +16.08% | 1.06 | 1.53 | -12.02% | 1.34 | 1.33 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.00% | +16.37% | 1.04 | 1.50 | -12.02% | 1.36 | 1.32 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.17% | 45% | -7.01% | -7.52% | -1.38 | 14 | 100% |
| out_of_sample | 532 | -0.20% | 45% | -7.01% | -7.52% | -1.23 | 14 | 100% |
| in_sample | 1768 | -0.16% | 45% | -5.88% | -6.28% | -1.29 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.149% | 56% | 2.38 | +27.23% |
| bull | 659 | 28% | +0.106% | 56% | 2.84 | +97.85% |
| bear | 399 | 17% | +0.007% | 49% | 0.22 | +2.03% |
| chop | 1099 | 47% | -0.010% | 43% | -0.25 | -12.41% |

## Turnover, fees, activity

- trades: 6072 (2.61/day); active days 100%
- turnover 39.3x equity/year; fees 3.93% of equity/year ($19,915 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.95
