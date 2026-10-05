# Run: c30_r4_bo_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +101.92% | +11.65% | 0.91 | 1.31 | -17.18% | 0.68 | 1.00 |
| in_sample | 2020-02-15 → 2024-12-31 | +53.84% | +9.22% | 0.77 | 1.10 | -17.18% | 0.54 | 0.83 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +31.37% | +20.01% | 1.32 | 1.91 | -11.83% | 1.69 | 1.67 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.89% | +18.99% | 1.20 | 1.74 | -11.83% | 1.61 | 1.54 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.17% | 44% | -6.66% | -7.22% | -1.45 | 14 | 100% |
| out_of_sample | 532 | -0.10% | 48% | -6.66% | -7.22% | -0.60 | 14 | 100% |
| in_sample | 1768 | -0.18% | 44% | -5.86% | -6.22% | -1.61 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.145% | 58% | 2.62 | +26.68% |
| bull | 659 | 28% | +0.081% | 53% | 2.62 | +68.86% |
| bear | 399 | 17% | +0.014% | 48% | 0.45 | +4.99% |
| chop | 1099 | 47% | -0.006% | 43% | -0.17 | -8.24% |

## Turnover, fees, activity

- trades: 5484 (2.36/day); active days 100%
- turnover 36.1x equity/year; fees 3.61% of equity/year ($16,530 total)
- average gross exposure 0.16; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.98
