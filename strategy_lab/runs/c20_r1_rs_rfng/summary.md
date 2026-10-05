# Run: c20_r1_rs_rfng

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +123.16% | +13.41% | 0.88 | 1.24 | -25.29% | 0.53 | 0.92 |
| in_sample | 2020-02-15 → 2024-12-31 | +76.64% | +12.36% | 0.83 | 1.17 | -25.29% | 0.49 | 0.86 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +26.44% | +16.98% | 1.04 | 1.49 | -13.60% | 1.25 | 1.28 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +10.05% | +13.66% | 0.85 | 1.22 | -13.60% | 1.00 | 1.04 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.33% | 44% | -7.18% | -7.55% | -2.16 | 14 | 100% |
| out_of_sample | 532 | -0.33% | 44% | -6.96% | -7.53% | -1.84 | 14 | 100% |
| in_sample | 1768 | -0.32% | 44% | -7.18% | -7.55% | -2.16 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.187% | 59% | 2.96 | +35.62% |
| bull | 659 | 28% | +0.107% | 54% | 2.77 | +98.59% |
| bear | 399 | 17% | -0.022% | 47% | -0.64 | -9.22% |
| chop | 1099 | 47% | -0.003% | 44% | -0.07 | -6.58% |

## Turnover, fees, activity

- trades: 6667 (2.86/day); active days 100%
- turnover 42.1x equity/year; fees 4.21% of equity/year ($21,160 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.93
