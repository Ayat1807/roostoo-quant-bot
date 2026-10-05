# Run: c20_r2_tr

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +126.23% | +13.66% | 0.91 | 1.29 | -22.09% | 0.62 | 0.97 |
| in_sample | 2020-02-15 → 2024-12-31 | +76.63% | +12.36% | 0.85 | 1.20 | -22.09% | 0.56 | 0.90 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +28.19% | +18.06% | 1.11 | 1.58 | -13.08% | 1.38 | 1.38 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.47% | +18.41% | 1.06 | 1.54 | -13.08% | 1.41 | 1.36 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.24% | 44% | -7.53% | -8.09% | -1.42 | 14 | 100% |
| out_of_sample | 532 | -0.21% | 44% | -7.53% | -8.09% | -1.14 | 14 | 100% |
| in_sample | 1768 | -0.24% | 44% | -7.26% | -7.65% | -1.56 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.174% | 55% | 2.70 | +32.73% |
| bull | 659 | 28% | +0.107% | 54% | 2.73 | +98.55% |
| bear | 399 | 17% | -0.010% | 46% | -0.30 | -4.73% |
| chop | 1099 | 47% | -0.004% | 45% | -0.10 | -7.78% |

## Turnover, fees, activity

- trades: 9402 (4.04/day); active days 100%
- turnover 46.5x equity/year; fees 4.65% of equity/year ($22,876 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.95
