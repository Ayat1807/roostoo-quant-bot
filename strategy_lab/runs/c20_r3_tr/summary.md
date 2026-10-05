# Run: c20_r3_tr

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +136.23% | +14.43% | 0.97 | 1.37 | -22.53% | 0.64 | 1.03 |
| in_sample | 2020-02-15 → 2024-12-31 | +84.48% | +13.36% | 0.91 | 1.28 | -22.53% | 0.59 | 0.96 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +28.15% | +18.04% | 1.17 | 1.68 | -11.84% | 1.52 | 1.48 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.83% | +20.30% | 1.25 | 1.81 | -11.84% | 1.71 | 1.61 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.21% | 45% | -6.57% | -7.02% | -1.29 | 14 | 100% |
| out_of_sample | 532 | -0.23% | 44% | -6.57% | -7.02% | -1.38 | 14 | 100% |
| in_sample | 1768 | -0.19% | 46% | -6.34% | -6.70% | -1.22 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.160% | 56% | 2.56 | +29.71% |
| bull | 659 | 28% | +0.115% | 55% | 3.02 | +110.25% |
| bear | 399 | 17% | -0.010% | 47% | -0.32 | -4.65% |
| chop | 1099 | 47% | -0.004% | 45% | -0.10 | -7.02% |

## Turnover, fees, activity

- trades: 8577 (3.68/day); active days 100%
- turnover 46.2x equity/year; fees 4.62% of equity/year ($24,060 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.95
