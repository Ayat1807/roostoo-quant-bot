# Run: c20_r4_bo_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +115.26% | +12.77% | 0.94 | 1.35 | -18.25% | 0.70 | 1.03 |
| in_sample | 2020-02-15 → 2024-12-31 | +61.13% | +10.26% | 0.80 | 1.15 | -18.25% | 0.56 | 0.87 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +33.72% | +21.44% | 1.34 | 1.94 | -12.74% | 1.68 | 1.68 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.93% | +20.45% | 1.20 | 1.75 | -12.74% | 1.60 | 1.54 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.18% | 45% | -7.12% | -7.71% | -1.43 | 14 | 100% |
| out_of_sample | 532 | -0.11% | 48% | -7.12% | -7.71% | -0.60 | 14 | 100% |
| in_sample | 1768 | -0.18% | 44% | -6.36% | -6.75% | -1.60 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.156% | 58% | 2.60 | +29.00% |
| bull | 659 | 28% | +0.085% | 54% | 2.69 | +73.45% |
| bear | 399 | 17% | +0.015% | 48% | 0.45 | +5.33% |
| chop | 1099 | 47% | -0.004% | 44% | -0.10 | -6.52% |

## Turnover, fees, activity

- trades: 5484 (2.36/day); active days 100%
- turnover 38.2x equity/year; fees 3.82% of equity/year ($18,270 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
