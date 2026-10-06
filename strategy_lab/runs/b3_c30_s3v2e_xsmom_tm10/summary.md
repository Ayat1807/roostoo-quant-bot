# Run: b3_c30_s3v2e_xsmom_tm10

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +184.60% | +17.06% | 1.10 | 1.56 | -17.09% | 1.00 | 1.25 |
| in_sample | 2020-02-15 → 2024-12-31 | +81.45% | +12.98% | 0.89 | 1.25 | -17.09% | 0.76 | 1.00 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +56.93% | +29.22% | 1.64 | 2.35 | -8.99% | 3.25 | 2.41 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +45.57% | +45.57% | 2.15 | 3.09 | -8.99% | 5.07 | 3.40 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.24% | 45% | -5.12% | -7.60% | -1.43 | 14 | 100% |
| out_of_sample | 628 | -0.17% | 47% | -5.12% | -7.60% | -0.64 | 14 | 100% |
| in_sample | 1768 | -0.25% | 44% | -4.75% | -5.98% | -1.72 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.209% | 53% | 2.86 | +42.07% |
| bull | 687 | 28% | +0.122% | 53% | 3.17 | +126.60% |
| bear | 400 | 17% | +0.011% | 47% | 0.37 | +3.71% |
| chop | 1160 | 48% | -0.009% | 43% | -0.23 | -12.56% |

## Turnover, fees, activity

- trades: 13727 (5.66/day); active days 100%
- turnover 54.7x equity/year; fees 5.47% of equity/year ($28,817 total)
- average gross exposure 0.19; brake active 9.5% of hours
- correlation of daily returns with s3v2 baseline: 0.88
