# Run: c30_r1_rs

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +125.47% | +13.60% | 0.81 | 1.11 | -29.47% | 0.46 | 0.83 |
| in_sample | 2020-02-15 → 2024-12-31 | +93.85% | +14.52% | 0.84 | 1.16 | -29.47% | 0.49 | 0.87 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +16.38% | +10.68% | 0.68 | 0.95 | -11.23% | 0.95 | 0.87 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +4.03% | +5.43% | 0.40 | 0.57 | -10.14% | 0.53 | 0.51 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.37% | 43% | -7.15% | -7.65% | -1.79 | 14 | 100% |
| out_of_sample | 532 | -0.30% | 45% | -6.16% | -7.65% | -1.13 | 14 | 100% |
| in_sample | 1768 | -0.39% | 43% | -7.15% | -7.46% | -1.90 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.209% | 57% | 3.23 | +40.72% |
| bull | 659 | 28% | +0.131% | 55% | 2.65 | +130.42% |
| bear | 399 | 17% | -0.073% | 44% | -2.13 | -25.80% |
| chop | 1099 | 47% | -0.000% | 45% | -0.01 | -4.36% |

## Turnover, fees, activity

- trades: 6761 (2.90/day); active days 100%
- turnover 42.8x equity/year; fees 4.28% of equity/year ($22,499 total)
- average gross exposure 0.22; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.80
