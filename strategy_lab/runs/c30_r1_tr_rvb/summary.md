# Run: c30_r1_tr_rvb

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +88.94% | +10.49% | 0.71 | 0.99 | -23.06% | 0.45 | 0.75 |
| in_sample | 2020-02-15 → 2024-12-31 | +52.29% | +9.00% | 0.63 | 0.87 | -21.96% | 0.41 | 0.66 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +24.17% | +15.57% | 0.98 | 1.40 | -12.97% | 1.20 | 1.22 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.48% | +17.04% | 1.01 | 1.46 | -12.97% | 1.31 | 1.28 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.29% | 43% | -7.09% | -7.76% | -2.01 | 14 | 100% |
| out_of_sample | 532 | -0.18% | 45% | -7.09% | -7.76% | -0.90 | 14 | 100% |
| in_sample | 1768 | -0.33% | 42% | -6.19% | -6.62% | -2.38 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.234% | 58% | 3.68 | +46.86% |
| bull | 659 | 28% | +0.083% | 53% | 2.01 | +69.52% |
| bear | 399 | 17% | -0.008% | 47% | -0.24 | -4.18% |
| chop | 1099 | 47% | -0.017% | 44% | -0.42 | -19.18% |

## Turnover, fees, activity

- trades: 9230 (3.96/day); active days 100%
- turnover 46.6x equity/year; fees 4.66% of equity/year ($21,991 total)
- average gross exposure 0.18; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.90
