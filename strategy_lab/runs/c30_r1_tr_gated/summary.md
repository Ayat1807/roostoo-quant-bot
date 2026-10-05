# Run: c30_r1_tr_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +109.81% | +12.32% | 0.93 | 1.31 | -17.78% | 0.69 | 1.01 |
| in_sample | 2020-02-15 → 2024-12-31 | +67.56% | +11.15% | 0.87 | 1.23 | -17.78% | 0.63 | 0.94 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +25.31% | +16.28% | 1.10 | 1.57 | -12.56% | 1.30 | 1.35 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +10.32% | +14.04% | 0.96 | 1.39 | -12.56% | 1.12 | 1.18 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.19% | 44% | -6.31% | -6.84% | -1.74 | 14 | 100% |
| out_of_sample | 532 | -0.17% | 45% | -6.31% | -6.84% | -1.26 | 14 | 100% |
| in_sample | 1768 | -0.18% | 44% | -5.59% | -5.96% | -1.83 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.180% | 58% | 3.12 | +34.29% |
| bull | 659 | 28% | +0.089% | 54% | 2.45 | +77.33% |
| bear | 399 | 17% | +0.012% | 47% | 0.41 | +4.33% |
| chop | 1099 | 47% | -0.011% | 44% | -0.34 | -13.82% |

## Turnover, fees, activity

- trades: 6644 (2.85/day); active days 100%
- turnover 37.3x equity/year; fees 3.73% of equity/year ($18,046 total)
- average gross exposure 0.16; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.94
