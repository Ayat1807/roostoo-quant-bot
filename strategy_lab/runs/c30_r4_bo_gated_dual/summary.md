# Run: c30_r4_bo_gated_dual

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +103.80% | +11.81% | 0.93 | 1.34 | -16.62% | 0.71 | 1.03 |
| in_sample | 2020-02-15 → 2024-12-31 | +55.42% | +9.45% | 0.79 | 1.14 | -16.62% | 0.57 | 0.86 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +31.24% | +19.93% | 1.33 | 1.93 | -11.71% | 1.70 | 1.68 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.59% | +18.58% | 1.18 | 1.72 | -11.71% | 1.59 | 1.52 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.16% | 44% | -6.59% | -7.14% | -1.41 | 14 | 100% |
| out_of_sample | 532 | -0.10% | 48% | -6.59% | -7.14% | -0.62 | 14 | 100% |
| in_sample | 1768 | -0.17% | 44% | -5.82% | -6.18% | -1.49 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.145% | 58% | 2.65 | +26.69% |
| bull | 659 | 28% | +0.082% | 54% | 2.66 | +69.48% |
| bear | 399 | 17% | +0.014% | 48% | 0.45 | +4.99% |
| chop | 1099 | 47% | -0.005% | 44% | -0.15 | -7.74% |

## Turnover, fees, activity

- trades: 5581 (2.40/day); active days 100%
- turnover 36.5x equity/year; fees 3.65% of equity/year ($16,876 total)
- average gross exposure 0.15; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.98
