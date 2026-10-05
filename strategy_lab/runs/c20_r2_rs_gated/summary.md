# Run: c20_r2_rs_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +110.53% | +12.38% | 0.89 | 1.29 | -18.12% | 0.68 | 0.99 |
| in_sample | 2020-02-15 → 2024-12-31 | +61.97% | +10.38% | 0.79 | 1.14 | -18.12% | 0.57 | 0.86 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +30.10% | +19.23% | 1.19 | 1.72 | -13.70% | 1.40 | 1.47 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.60% | +18.60% | 1.09 | 1.59 | -13.70% | 1.36 | 1.37 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.20% | 44% | -7.23% | -7.82% | -1.73 | 14 | 100% |
| out_of_sample | 532 | -0.15% | 46% | -7.23% | -7.82% | -0.94 | 14 | 100% |
| in_sample | 1768 | -0.20% | 43% | -6.43% | -6.83% | -1.93 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.166% | 58% | 2.73 | +31.02% |
| bull | 659 | 28% | +0.085% | 53% | 2.51 | +72.98% |
| bear | 399 | 17% | +0.016% | 47% | 0.47 | +5.77% |
| chop | 1099 | 47% | -0.007% | 44% | -0.19 | -10.10% |

## Turnover, fees, activity

- trades: 5480 (2.35/day); active days 100%
- turnover 38.4x equity/year; fees 3.84% of equity/year ($18,345 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.98
