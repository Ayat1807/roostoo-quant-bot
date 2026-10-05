# Run: c20_r3_bo

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +127.25% | +13.74% | 0.93 | 1.31 | -19.39% | 0.71 | 1.01 |
| in_sample | 2020-02-15 → 2024-12-31 | +93.59% | +14.49% | 0.97 | 1.37 | -19.39% | 0.75 | 1.06 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +17.47% | +11.37% | 0.78 | 1.11 | -13.46% | 0.84 | 0.93 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +10.70% | +14.56% | 0.92 | 1.33 | -13.46% | 1.08 | 1.13 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.21% | 45% | -7.05% | -7.55% | -1.29 | 14 | 100% |
| out_of_sample | 532 | -0.42% | 40% | -7.05% | -7.55% | -2.27 | 14 | 100% |
| in_sample | 1768 | -0.16% | 47% | -5.91% | -6.28% | -1.01 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.213% | 55% | 3.38 | +41.96% |
| bull | 659 | 28% | +0.112% | 55% | 2.99 | +105.93% |
| bear | 399 | 17% | -0.014% | 45% | -0.42 | -6.01% |
| chop | 1099 | 47% | -0.012% | 43% | -0.32 | -15.35% |

## Turnover, fees, activity

- trades: 7018 (3.01/day); active days 100%
- turnover 44.1x equity/year; fees 4.41% of equity/year ($23,192 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.93
