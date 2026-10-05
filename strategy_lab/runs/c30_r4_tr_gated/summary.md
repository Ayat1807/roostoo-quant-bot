# Run: c30_r4_tr_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +101.55% | +11.62% | 0.91 | 1.30 | -17.36% | 0.67 | 1.00 |
| in_sample | 2020-02-15 → 2024-12-31 | +56.36% | +9.59% | 0.80 | 1.13 | -17.36% | 0.55 | 0.86 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +29.01% | +18.56% | 1.25 | 1.80 | -12.47% | 1.49 | 1.54 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.49% | +17.05% | 1.10 | 1.60 | -12.47% | 1.37 | 1.38 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.16% | 45% | -6.61% | -7.16% | -1.40 | 14 | 100% |
| out_of_sample | 532 | -0.12% | 46% | -6.61% | -7.16% | -0.89 | 14 | 100% |
| in_sample | 1768 | -0.15% | 45% | -5.74% | -6.09% | -1.42 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.144% | 58% | 2.64 | +26.58% |
| bull | 659 | 28% | +0.081% | 54% | 2.53 | +68.19% |
| bear | 399 | 17% | +0.015% | 48% | 0.50 | +5.56% |
| chop | 1099 | 47% | -0.006% | 44% | -0.18 | -8.48% |

## Turnover, fees, activity

- trades: 5757 (2.47/day); active days 100%
- turnover 36.0x equity/year; fees 3.60% of equity/year ($16,850 total)
- average gross exposure 0.16; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.97
