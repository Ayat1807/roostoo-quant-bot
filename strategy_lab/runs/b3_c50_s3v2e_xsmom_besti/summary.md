# Run: b3_c50_s3v2e_xsmom_besti

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +226.83% | +19.52% | 0.77 | 1.06 | -51.77% | 0.38 | 0.77 |
| in_sample | 2020-02-15 → 2024-12-31 | +256.12% | +29.71% | 1.00 | 1.38 | -51.77% | 0.57 | 1.03 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -8.43% | -4.89% | -0.13 | -0.18 | -24.12% | -0.20 | -0.17 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +4.85% | +4.85% | 0.35 | 0.49 | -19.58% | 0.25 | 0.37 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.90% | 41% | -16.45% | -16.48% | -2.34 | 14 | 100% |
| out_of_sample | 628 | -1.30% | 38% | -8.76% | -11.11% | -3.66 | 14 | 100% |
| in_sample | 1768 | -0.77% | 43% | -16.45% | -16.48% | -2.07 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.482% | 54% | 3.64 | +120.69% |
| bull | 687 | 28% | +0.216% | 52% | 2.49 | +302.52% |
| bear | 400 | 17% | -0.145% | 40% | -2.93 | -45.05% |
| chop | 1160 | 48% | -0.027% | 41% | -0.46 | -32.10% |

## Turnover, fees, activity

- trades: 19113 (7.88/day); active days 100%
- turnover 131.7x equity/year; fees 13.17% of equity/year ($132,829 total)
- average gross exposure 0.27; brake active 9.5% of hours
- correlation of daily returns with s3v2 baseline: 0.49
