# Run: c30_r2_tr

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +118.38% | +13.03% | 0.85 | 1.19 | -23.19% | 0.56 | 0.90 |
| in_sample | 2020-02-15 → 2024-12-31 | +77.09% | +12.42% | 0.83 | 1.15 | -23.19% | 0.54 | 0.87 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +23.41% | +15.10% | 0.94 | 1.33 | -12.59% | 1.20 | 1.17 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +11.74% | +16.01% | 0.95 | 1.37 | -12.59% | 1.27 | 1.21 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.26% | 44% | -7.34% | -7.84% | -1.66 | 14 | 100% |
| out_of_sample | 532 | -0.30% | 44% | -7.34% | -7.84% | -1.37 | 14 | 100% |
| in_sample | 1768 | -0.25% | 44% | -7.29% | -7.64% | -1.73 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.173% | 58% | 2.70 | +32.45% |
| bull | 659 | 28% | +0.115% | 53% | 2.63 | +108.40% |
| bear | 399 | 17% | -0.025% | 46% | -0.77 | -10.01% |
| chop | 1099 | 47% | -0.007% | 45% | -0.16 | -10.28% |

## Turnover, fees, activity

- trades: 9402 (4.04/day); active days 100%
- turnover 48.9x equity/year; fees 4.89% of equity/year ($23,439 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.88
