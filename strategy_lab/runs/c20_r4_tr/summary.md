# Run: c20_r4_tr

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +112.02% | +12.50% | 0.85 | 1.20 | -21.96% | 0.57 | 0.91 |
| in_sample | 2020-02-15 → 2024-12-31 | +58.49% | +9.89% | 0.71 | 1.00 | -21.96% | 0.45 | 0.75 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +33.90% | +21.55% | 1.27 | 1.85 | -14.07% | 1.53 | 1.58 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.45% | +18.38% | 1.06 | 1.55 | -14.07% | 1.31 | 1.33 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.26% | 44% | -7.25% | -7.74% | -1.55 | 14 | 100% |
| out_of_sample | 532 | -0.24% | 45% | -7.15% | -7.74% | -1.12 | 14 | 100% |
| in_sample | 1768 | -0.26% | 44% | -7.25% | -7.65% | -1.67 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.152% | 55% | 2.46 | +28.03% |
| bull | 659 | 28% | +0.096% | 53% | 2.57 | +85.22% |
| bear | 399 | 17% | +0.000% | 45% | 0.01 | -0.78% |
| chop | 1099 | 47% | -0.004% | 44% | -0.11 | -7.78% |

## Turnover, fees, activity

- trades: 8290 (3.56/day); active days 100%
- turnover 44.3x equity/year; fees 4.43% of equity/year ($21,320 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.97
