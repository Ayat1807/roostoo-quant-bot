# Run: c30_r3_bo

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +119.91% | +13.15% | 0.87 | 1.21 | -20.56% | 0.64 | 0.94 |
| in_sample | 2020-02-15 → 2024-12-31 | +102.53% | +15.55% | 0.99 | 1.38 | -20.56% | 0.76 | 1.08 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +8.65% | +5.70% | 0.44 | 0.63 | -13.19% | 0.43 | 0.51 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +7.65% | +10.36% | 0.72 | 1.03 | -13.19% | 0.79 | 0.86 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.30% | 44% | -6.58% | -7.01% | -1.56 | 14 | 100% |
| out_of_sample | 532 | -0.56% | 39% | -6.58% | -7.01% | -3.22 | 14 | 100% |
| in_sample | 1768 | -0.17% | 46% | -5.48% | -6.43% | -0.85 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.231% | 55% | 3.65 | +46.22% |
| bull | 659 | 28% | +0.122% | 54% | 2.92 | +118.38% |
| bear | 399 | 17% | -0.028% | 44% | -0.93 | -11.34% |
| chop | 1099 | 47% | -0.018% | 43% | -0.48 | -20.73% |

## Turnover, fees, activity

- trades: 7018 (3.01/day); active days 100%
- turnover 45.2x equity/year; fees 4.52% of equity/year ($23,913 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.85
