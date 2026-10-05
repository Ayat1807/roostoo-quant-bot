# Run: c20_r4_tr_gated_jump

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +111.99% | +12.50% | 0.92 | 1.34 | -18.47% | 0.68 | 1.02 |
| in_sample | 2020-02-15 → 2024-12-31 | +59.53% | +10.04% | 0.79 | 1.14 | -18.47% | 0.54 | 0.86 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +33.01% | +21.01% | 1.31 | 1.91 | -13.46% | 1.56 | 1.62 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.68% | +20.10% | 1.18 | 1.72 | -13.46% | 1.49 | 1.49 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.17% | 45% | -7.19% | -7.78% | -1.47 | 14 | 100% |
| out_of_sample | 532 | -0.12% | 47% | -7.19% | -7.78% | -0.66 | 14 | 100% |
| in_sample | 1768 | -0.17% | 45% | -6.40% | -6.79% | -1.63 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.154% | 58% | 2.55 | +28.42% |
| bull | 659 | 28% | +0.082% | 54% | 2.62 | +69.50% |
| bear | 399 | 17% | +0.016% | 48% | 0.47 | +5.72% |
| chop | 1099 | 47% | -0.003% | 44% | -0.08 | -5.71% |

## Turnover, fees, activity

- trades: 5499 (2.36/day); active days 100%
- turnover 37.9x equity/year; fees 3.79% of equity/year ($18,090 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 1.00
