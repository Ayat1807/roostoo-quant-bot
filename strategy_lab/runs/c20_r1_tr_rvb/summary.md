# Run: c20_r1_tr_rvb

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +106.60% | +12.05% | 0.82 | 1.16 | -21.32% | 0.57 | 0.88 |
| in_sample | 2020-02-15 → 2024-12-31 | +60.10% | +10.12% | 0.71 | 1.00 | -21.32% | 0.47 | 0.76 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +29.16% | +18.66% | 1.13 | 1.63 | -13.35% | 1.40 | 1.41 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.10% | +19.29% | 1.09 | 1.59 | -13.35% | 1.44 | 1.40 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.27% | 43% | -7.40% | -8.06% | -1.89 | 14 | 100% |
| out_of_sample | 532 | -0.16% | 45% | -7.40% | -8.06% | -0.93 | 14 | 100% |
| in_sample | 1768 | -0.30% | 43% | -6.26% | -6.65% | -2.19 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.214% | 58% | 3.34 | +42.09% |
| bull | 659 | 28% | +0.087% | 53% | 2.28 | +73.83% |
| bear | 399 | 17% | +0.001% | 46% | 0.02 | -0.69% |
| chop | 1099 | 47% | -0.011% | 44% | -0.26 | -13.79% |

## Turnover, fees, activity

- trades: 9230 (3.96/day); active days 100%
- turnover 45.0x equity/year; fees 4.50% of equity/year ($21,911 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.96
