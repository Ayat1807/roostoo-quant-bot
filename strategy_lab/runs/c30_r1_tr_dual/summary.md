# Run: c30_r1_tr_dual

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +95.28% | +11.06% | 0.77 | 1.08 | -21.39% | 0.52 | 0.82 |
| in_sample | 2020-02-15 → 2024-12-31 | +55.06% | +9.40% | 0.67 | 0.93 | -21.39% | 0.44 | 0.71 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +26.04% | +16.74% | 1.09 | 1.57 | -12.01% | 1.39 | 1.37 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +11.88% | +16.20% | 1.02 | 1.47 | -12.01% | 1.35 | 1.30 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.32% | 43% | -7.41% | -7.96% | -1.81 | 14 | 100% |
| out_of_sample | 532 | -0.22% | 45% | -7.41% | -7.96% | -1.04 | 14 | 100% |
| in_sample | 1768 | -0.36% | 43% | -7.06% | -7.41% | -2.03 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.176% | 55% | 2.82 | +33.32% |
| bull | 659 | 28% | +0.104% | 53% | 2.57 | +94.64% |
| bear | 399 | 17% | -0.035% | 43% | -1.03 | -13.70% |
| chop | 1099 | 47% | -0.008% | 44% | -0.21 | -11.01% |

## Turnover, fees, activity

- trades: 9483 (4.07/day); active days 100%
- turnover 49.5x equity/year; fees 4.95% of equity/year ($23,738 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.91
