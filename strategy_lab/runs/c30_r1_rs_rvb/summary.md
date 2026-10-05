# Run: c30_r1_rs_rvb

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +85.96% | +10.22% | 0.71 | 0.99 | -23.59% | 0.43 | 0.74 |
| in_sample | 2020-02-15 → 2024-12-31 | +46.12% | +8.08% | 0.59 | 0.81 | -23.59% | 0.34 | 0.61 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +27.38% | +17.56% | 1.10 | 1.57 | -13.05% | 1.35 | 1.36 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +11.27% | +15.34% | 0.93 | 1.34 | -13.05% | 1.18 | 1.17 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.24% | 45% | -6.99% | -7.78% | -1.60 | 14 | 100% |
| out_of_sample | 532 | -0.11% | 48% | -6.99% | -7.78% | -0.63 | 14 | 100% |
| in_sample | 1768 | -0.26% | 44% | -6.05% | -6.43% | -1.72 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.184% | 57% | 3.01 | +35.09% |
| bull | 659 | 28% | +0.098% | 54% | 2.50 | +87.30% |
| bear | 399 | 17% | -0.012% | 45% | -0.36 | -5.56% |
| chop | 1099 | 47% | -0.018% | 43% | -0.47 | -20.59% |

## Turnover, fees, activity

- trades: 6333 (2.72/day); active days 100%
- turnover 40.5x equity/year; fees 4.05% of equity/year ($18,512 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.92
