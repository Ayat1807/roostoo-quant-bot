# Run: b3_c50_s3v2e_xsmom_tm10

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +185.79% | +17.13% | 0.99 | 1.37 | -21.43% | 0.80 | 1.09 |
| in_sample | 2020-02-15 → 2024-12-31 | +70.54% | +11.55% | 0.74 | 1.02 | -21.43% | 0.54 | 0.79 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +67.60% | +34.15% | 1.57 | 2.25 | -10.90% | 3.13 | 2.31 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +62.76% | +62.76% | 2.30 | 3.28 | -10.90% | 5.76 | 3.73 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.30% | 45% | -6.60% | -10.90% | -1.45 | 14 | 100% |
| out_of_sample | 628 | -0.21% | 47% | -5.98% | -10.90% | -0.91 | 14 | 100% |
| in_sample | 1768 | -0.31% | 44% | -6.60% | -7.54% | -1.66 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.177% | 54% | 2.35 | +34.14% |
| bull | 687 | 28% | +0.135% | 53% | 2.89 | +146.43% |
| bear | 400 | 17% | -0.014% | 46% | -0.45 | -6.06% |
| chop | 1160 | 48% | -0.002% | 44% | -0.04 | -5.77% |

## Turnover, fees, activity

- trades: 13727 (5.66/day); active days 100%
- turnover 65.0x equity/year; fees 6.50% of equity/year ($32,433 total)
- average gross exposure 0.19; brake active 9.5% of hours
- correlation of daily returns with s3v2 baseline: 0.68
