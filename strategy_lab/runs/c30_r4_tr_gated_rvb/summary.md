# Run: c30_r4_tr_gated_rvb

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +99.84% | +11.47% | 0.90 | 1.28 | -17.48% | 0.66 | 0.98 |
| in_sample | 2020-02-15 → 2024-12-31 | +54.58% | +9.33% | 0.77 | 1.10 | -17.48% | 0.53 | 0.83 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +29.38% | +18.79% | 1.25 | 1.81 | -12.56% | 1.50 | 1.55 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.68% | +17.30% | 1.10 | 1.61 | -12.56% | 1.38 | 1.39 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.16% | 45% | -6.67% | -7.22% | -1.42 | 14 | 100% |
| out_of_sample | 532 | -0.12% | 46% | -6.67% | -7.22% | -0.85 | 14 | 100% |
| in_sample | 1768 | -0.15% | 45% | -5.80% | -6.16% | -1.45 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.145% | 58% | 2.63 | +26.70% |
| bull | 659 | 28% | +0.081% | 54% | 2.53 | +67.98% |
| bear | 399 | 17% | +0.015% | 48% | 0.50 | +5.60% |
| chop | 1099 | 47% | -0.007% | 44% | -0.20 | -9.26% |

## Turnover, fees, activity

- trades: 5749 (2.47/day); active days 100%
- turnover 36.2x equity/year; fees 3.62% of equity/year ($16,764 total)
- average gross exposure 0.16; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.98
