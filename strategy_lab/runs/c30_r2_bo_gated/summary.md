# Run: c30_r2_bo_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +104.80% | +11.90% | 0.92 | 1.31 | -18.06% | 0.66 | 1.00 |
| in_sample | 2020-02-15 → 2024-12-31 | +62.73% | +10.49% | 0.84 | 1.21 | -18.06% | 0.58 | 0.91 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +25.95% | +16.68% | 1.14 | 1.63 | -12.49% | 1.34 | 1.39 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +11.94% | +16.28% | 1.06 | 1.54 | -12.49% | 1.30 | 1.33 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.17% | 45% | -6.49% | -7.03% | -1.46 | 14 | 100% |
| out_of_sample | 532 | -0.13% | 46% | -6.49% | -7.03% | -1.05 | 14 | 100% |
| in_sample | 1768 | -0.17% | 45% | -5.80% | -6.15% | -1.58 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.138% | 58% | 2.48 | +25.17% |
| bull | 659 | 28% | +0.089% | 53% | 2.67 | +77.36% |
| bear | 399 | 17% | +0.013% | 47% | 0.44 | +4.76% |
| chop | 1099 | 47% | -0.008% | 44% | -0.22 | -10.13% |

## Turnover, fees, activity

- trades: 5570 (2.39/day); active days 100%
- turnover 36.4x equity/year; fees 3.64% of equity/year ($16,988 total)
- average gross exposure 0.16; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.96
