# Run: c20_r1_bo_noR5

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +130.71% | +14.01% | 0.91 | 1.28 | -20.74% | 0.68 | 0.99 |
| in_sample | 2020-02-15 → 2024-12-31 | +93.56% | +14.48% | 0.93 | 1.32 | -20.74% | 0.70 | 1.02 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +19.08% | +12.38% | 0.81 | 1.16 | -11.28% | 1.10 | 1.04 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +8.56% | +11.61% | 0.76 | 1.09 | -11.28% | 1.03 | 0.97 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.39% | 43% | -6.84% | -7.28% | -2.28 | 14 | 100% |
| out_of_sample | 532 | -0.53% | 39% | -6.59% | -7.28% | -2.45 | 14 | 100% |
| in_sample | 1768 | -0.35% | 44% | -6.84% | -7.20% | -1.99 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.251% | 53% | 3.74 | +51.02% |
| bull | 659 | 28% | +0.102% | 52% | 2.46 | +91.37% |
| bear | 399 | 17% | -0.021% | 44% | -0.63 | -8.60% |
| chop | 1099 | 47% | -0.007% | 44% | -0.17 | -10.61% |

## Turnover, fees, activity

- trades: 7583 (3.26/day); active days 100%
- turnover 46.9x equity/year; fees 4.69% of equity/year ($24,401 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.90
