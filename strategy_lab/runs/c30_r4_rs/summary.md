# Run: c30_r4_rs

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +105.18% | +11.93% | 0.76 | 1.05 | -24.99% | 0.48 | 0.79 |
| in_sample | 2020-02-15 → 2024-12-31 | +61.53% | +10.32% | 0.67 | 0.92 | -24.99% | 0.41 | 0.69 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +27.13% | +17.40% | 1.05 | 1.51 | -12.42% | 1.40 | 1.34 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +11.25% | +15.33% | 0.93 | 1.34 | -12.42% | 1.23 | 1.19 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.36% | 43% | -6.92% | -7.25% | -1.97 | 14 | 100% |
| out_of_sample | 532 | -0.27% | 43% | -6.39% | -7.23% | -1.77 | 14 | 100% |
| in_sample | 1768 | -0.38% | 43% | -6.92% | -7.25% | -1.97 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.127% | 55% | 1.98 | +22.44% |
| bull | 659 | 28% | +0.141% | 55% | 3.11 | +147.23% |
| bear | 399 | 17% | -0.043% | 46% | -1.23 | -16.42% |
| chop | 1099 | 47% | -0.014% | 44% | -0.33 | -17.24% |

## Turnover, fees, activity

- trades: 6367 (2.73/day); active days 100%
- turnover 40.0x equity/year; fees 4.00% of equity/year ($19,838 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.87
