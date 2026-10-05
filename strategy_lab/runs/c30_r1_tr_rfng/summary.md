# Run: c30_r1_tr_rfng

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +117.51% | +12.96% | 0.83 | 1.16 | -22.12% | 0.59 | 0.89 |
| in_sample | 2020-02-15 → 2024-12-31 | +75.05% | +12.15% | 0.80 | 1.11 | -22.12% | 0.55 | 0.85 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +24.35% | +15.68% | 0.93 | 1.32 | -13.73% | 1.14 | 1.15 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +7.45% | +10.08% | 0.67 | 0.96 | -13.73% | 0.73 | 0.80 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.30% | 44% | -7.08% | -7.43% | -2.00 | 14 | 100% |
| out_of_sample | 532 | -0.40% | 41% | -6.50% | -6.99% | -2.05 | 14 | 100% |
| in_sample | 1768 | -0.28% | 44% | -7.08% | -7.43% | -1.87 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.197% | 60% | 3.23 | +38.20% |
| bull | 659 | 28% | +0.110% | 54% | 2.55 | +101.56% |
| bear | 399 | 17% | -0.029% | 46% | -0.91 | -11.73% |
| chop | 1099 | 47% | -0.006% | 44% | -0.14 | -9.73% |

## Turnover, fees, activity

- trades: 10908 (4.69/day); active days 100%
- turnover 51.7x equity/year; fees 5.17% of equity/year ($24,784 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.89
