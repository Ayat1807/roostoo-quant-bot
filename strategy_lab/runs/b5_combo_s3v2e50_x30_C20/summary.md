# Run: b5_combo_s3v2e50_x30_C20

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +165.35% | +15.83% | 0.74 | 1.02 | -45.03% | 0.35 | 0.74 |
| in_sample | 2020-02-15 → 2024-12-31 | +167.68% | +22.35% | 0.92 | 1.27 | -45.03% | 0.50 | 0.93 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -1.02% | -0.58% | 0.06 | 0.08 | -19.62% | -0.03 | 0.04 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +8.51% | +8.51% | 0.57 | 0.82 | -16.85% | 0.51 | 0.65 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.70% | 42% | -14.03% | -14.43% | -2.33 | 14 | 100% |
| out_of_sample | 628 | -1.07% | 39% | -7.16% | -9.09% | -3.48 | 14 | 100% |
| in_sample | 1768 | -0.58% | 43% | -14.03% | -14.43% | -1.90 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.391% | 55% | 3.56 | +91.27% |
| bull | 687 | 28% | +0.179% | 52% | 2.52 | +220.22% |
| bear | 400 | 17% | -0.099% | 42% | -2.41 | -33.63% |
| chop | 1160 | 48% | -0.031% | 41% | -0.63 | -33.79% |

## Turnover, fees, activity

- trades: 22515 (9.29/day); active days 100%
- turnover 110.9x equity/year; fees 11.09% of equity/year ($85,651 total)
- average gross exposure 0.24; brake active 9.5% of hours
- correlation of daily returns with s3v2 baseline: 0.57
