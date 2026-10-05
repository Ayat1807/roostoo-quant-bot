# Run: c30_r4_bo_gated_rfng

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +103.89% | +11.82% | 0.93 | 1.34 | -17.13% | 0.69 | 1.02 |
| in_sample | 2020-02-15 → 2024-12-31 | +55.70% | +9.49% | 0.80 | 1.14 | -17.13% | 0.55 | 0.86 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +31.06% | +19.82% | 1.32 | 1.90 | -11.72% | 1.69 | 1.67 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.75% | +18.80% | 1.19 | 1.74 | -11.72% | 1.60 | 1.53 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.16% | 45% | -6.60% | -7.15% | -1.30 | 14 | 100% |
| out_of_sample | 532 | -0.10% | 48% | -6.60% | -7.15% | -0.60 | 14 | 100% |
| in_sample | 1768 | -0.16% | 45% | -5.83% | -6.19% | -1.38 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.137% | 58% | 2.51 | +25.16% |
| bull | 659 | 28% | +0.084% | 53% | 2.75 | +71.56% |
| bear | 399 | 17% | +0.014% | 48% | 0.44 | +4.87% |
| chop | 1099 | 47% | -0.005% | 43% | -0.15 | -7.60% |

## Turnover, fees, activity

- trades: 5448 (2.34/day); active days 100%
- turnover 35.9x equity/year; fees 3.59% of equity/year ($16,521 total)
- average gross exposure 0.15; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.98
