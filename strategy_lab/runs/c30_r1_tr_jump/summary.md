# Run: c30_r1_tr_jump

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +133.87% | +14.25% | 0.94 | 1.32 | -22.08% | 0.65 | 1.00 |
| in_sample | 2020-02-15 → 2024-12-31 | +89.81% | +14.03% | 0.94 | 1.30 | -22.08% | 0.64 | 0.99 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +23.30% | +15.03% | 0.97 | 1.38 | -13.13% | 1.14 | 1.18 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +9.17% | +12.45% | 0.85 | 1.21 | -13.13% | 0.95 | 1.02 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.32% | 44% | -6.39% | -7.06% | -1.79 | 14 | 100% |
| out_of_sample | 532 | -0.47% | 42% | -6.32% | -7.06% | -2.16 | 14 | 100% |
| in_sample | 1768 | -0.29% | 45% | -6.39% | -6.72% | -1.62 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.194% | 55% | 3.36 | +37.55% |
| bull | 659 | 28% | +0.098% | 53% | 2.35 | +86.73% |
| bear | 399 | 17% | -0.031% | 45% | -0.94 | -12.28% |
| chop | 1099 | 47% | +0.008% | 46% | 0.20 | +5.93% |

## Turnover, fees, activity

- trades: 10640 (4.57/day); active days 100%
- turnover 55.5x equity/year; fees 5.55% of equity/year ($29,355 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.87
