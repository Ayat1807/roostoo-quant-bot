# Run: c20_r3_bo_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +117.04% | +12.92% | 0.96 | 1.38 | -18.43% | 0.70 | 1.05 |
| in_sample | 2020-02-15 → 2024-12-31 | +64.75% | +10.77% | 0.84 | 1.21 | -18.43% | 0.58 | 0.91 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +31.85% | +20.31% | 1.30 | 1.88 | -13.16% | 1.54 | 1.61 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.32% | +19.59% | 1.18 | 1.72 | -13.16% | 1.49 | 1.49 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.14% | 45% | -7.02% | -7.60% | -1.29 | 14 | 100% |
| out_of_sample | 532 | -0.10% | 47% | -7.02% | -7.60% | -0.59 | 14 | 100% |
| in_sample | 1768 | -0.15% | 45% | -6.21% | -6.60% | -1.39 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.155% | 58% | 2.60 | +28.70% |
| bull | 659 | 28% | +0.088% | 54% | 2.85 | +76.87% |
| bear | 399 | 17% | +0.015% | 47% | 0.45 | +5.32% |
| chop | 1099 | 47% | -0.004% | 44% | -0.12 | -7.34% |

## Turnover, fees, activity

- trades: 5493 (2.36/day); active days 100%
- turnover 37.5x equity/year; fees 3.75% of equity/year ($18,349 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
