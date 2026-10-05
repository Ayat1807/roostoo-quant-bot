# Run: c20_r4_bo_gated_rfng

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +116.57% | +12.88% | 0.95 | 1.37 | -18.21% | 0.71 | 1.04 |
| in_sample | 2020-02-15 → 2024-12-31 | +62.37% | +10.44% | 0.81 | 1.17 | -18.21% | 0.57 | 0.89 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +33.50% | +21.31% | 1.34 | 1.93 | -12.64% | 1.69 | 1.68 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.84% | +20.32% | 1.20 | 1.75 | -12.64% | 1.61 | 1.54 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.15% | 45% | -7.08% | -7.67% | -1.27 | 14 | 100% |
| out_of_sample | 532 | -0.10% | 48% | -7.08% | -7.67% | -0.61 | 14 | 100% |
| in_sample | 1768 | -0.15% | 45% | -6.34% | -6.73% | -1.31 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.152% | 58% | 2.54 | +27.99% |
| bull | 659 | 28% | +0.087% | 54% | 2.77 | +75.22% |
| bear | 399 | 17% | +0.015% | 48% | 0.44 | +5.25% |
| chop | 1099 | 47% | -0.003% | 44% | -0.09 | -6.09% |

## Turnover, fees, activity

- trades: 5448 (2.34/day); active days 100%
- turnover 38.1x equity/year; fees 3.81% of equity/year ($18,264 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
