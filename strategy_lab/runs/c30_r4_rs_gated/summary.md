# Run: c30_r4_rs_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +94.47% | +10.99% | 0.84 | 1.20 | -18.67% | 0.59 | 0.91 |
| in_sample | 2020-02-15 → 2024-12-31 | +52.28% | +9.00% | 0.73 | 1.04 | -18.67% | 0.48 | 0.78 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +27.81% | +17.82% | 1.15 | 1.65 | -12.78% | 1.39 | 1.42 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.78% | +17.44% | 1.08 | 1.56 | -12.78% | 1.36 | 1.36 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.16% | 45% | -6.86% | -7.43% | -1.38 | 14 | 100% |
| out_of_sample | 532 | -0.13% | 46% | -6.86% | -7.43% | -1.04 | 14 | 100% |
| in_sample | 1768 | -0.15% | 45% | -5.88% | -6.25% | -1.37 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.138% | 58% | 2.36 | +25.10% |
| bull | 659 | 28% | +0.085% | 54% | 2.56 | +72.58% |
| bear | 399 | 17% | +0.017% | 48% | 0.52 | +6.04% |
| chop | 1099 | 47% | -0.011% | 44% | -0.31 | -13.31% |

## Turnover, fees, activity

- trades: 5536 (2.38/day); active days 100%
- turnover 36.5x equity/year; fees 3.65% of equity/year ($16,612 total)
- average gross exposure 0.16; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.97
