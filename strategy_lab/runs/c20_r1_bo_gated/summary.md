# Run: c20_r1_bo_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +117.00% | +12.92% | 0.94 | 1.35 | -19.22% | 0.67 | 1.02 |
| in_sample | 2020-02-15 → 2024-12-31 | +66.33% | +10.98% | 0.84 | 1.20 | -19.22% | 0.57 | 0.90 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +30.58% | +19.53% | 1.25 | 1.80 | -13.13% | 1.49 | 1.54 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.10% | +19.28% | 1.16 | 1.69 | -13.13% | 1.47 | 1.46 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.18% | 44% | -7.03% | -7.61% | -1.52 | 14 | 100% |
| out_of_sample | 532 | -0.12% | 47% | -7.03% | -7.61% | -0.69 | 14 | 100% |
| in_sample | 1768 | -0.18% | 44% | -6.34% | -6.73% | -1.73 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.173% | 58% | 2.83 | +32.60% |
| bull | 659 | 28% | +0.088% | 53% | 2.69 | +76.65% |
| bear | 399 | 17% | +0.015% | 48% | 0.43 | +5.10% |
| chop | 1099 | 47% | -0.007% | 44% | -0.18 | -9.79% |

## Turnover, fees, activity

- trades: 5710 (2.45/day); active days 100%
- turnover 38.8x equity/year; fees 3.88% of equity/year ($18,810 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.98
