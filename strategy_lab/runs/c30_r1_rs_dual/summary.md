# Run: c30_r1_rs_dual

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +102.76% | +11.72% | 0.78 | 1.09 | -22.31% | 0.53 | 0.83 |
| in_sample | 2020-02-15 → 2024-12-31 | +66.48% | +11.00% | 0.74 | 1.03 | -22.31% | 0.49 | 0.78 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +21.89% | +14.15% | 0.91 | 1.30 | -12.78% | 1.11 | 1.12 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +10.58% | +14.39% | 0.91 | 1.31 | -12.78% | 1.13 | 1.13 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.31% | 44% | -7.04% | -7.38% | -1.74 | 14 | 100% |
| out_of_sample | 532 | -0.24% | 46% | -6.76% | -7.30% | -1.09 | 14 | 100% |
| in_sample | 1768 | -0.32% | 44% | -7.04% | -7.38% | -1.82 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.163% | 54% | 2.57 | +30.24% |
| bull | 659 | 28% | +0.115% | 54% | 2.70 | +108.80% |
| bear | 399 | 17% | -0.039% | 43% | -1.14 | -15.16% |
| chop | 1099 | 47% | -0.007% | 44% | -0.18 | -10.32% |

## Turnover, fees, activity

- trades: 7315 (3.14/day); active days 100%
- turnover 47.3x equity/year; fees 4.73% of equity/year ($22,978 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.89
