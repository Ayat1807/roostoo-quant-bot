# Run: c20_r2_rs

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +108.82% | +12.24% | 0.81 | 1.15 | -23.74% | 0.52 | 0.86 |
| in_sample | 2020-02-15 → 2024-12-31 | +55.87% | +9.52% | 0.67 | 0.94 | -23.74% | 0.40 | 0.69 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +34.10% | +21.67% | 1.27 | 1.83 | -12.43% | 1.74 | 1.64 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +15.03% | +20.59% | 1.16 | 1.68 | -12.43% | 1.66 | 1.52 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.29% | 43% | -7.16% | -7.98% | -2.14 | 14 | 100% |
| out_of_sample | 532 | -0.14% | 47% | -7.06% | -7.98% | -0.78 | 14 | 100% |
| in_sample | 1768 | -0.34% | 42% | -7.16% | -7.56% | -2.52 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.189% | 57% | 2.85 | +35.91% |
| bull | 659 | 28% | +0.108% | 56% | 2.74 | +99.74% |
| bear | 399 | 17% | -0.021% | 44% | -0.59 | -8.96% |
| chop | 1099 | 47% | -0.010% | 44% | -0.24 | -13.53% |

## Turnover, fees, activity

- trades: 6420 (2.76/day); active days 100%
- turnover 41.3x equity/year; fees 4.13% of equity/year ($19,841 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.95
