# Run: c30_r3_rs_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +97.77% | +11.28% | 0.86 | 1.23 | -18.65% | 0.60 | 0.93 |
| in_sample | 2020-02-15 → 2024-12-31 | +58.11% | +9.84% | 0.79 | 1.12 | -18.65% | 0.53 | 0.84 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +25.19% | +16.20% | 1.09 | 1.57 | -13.37% | 1.21 | 1.32 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +11.89% | +16.22% | 1.04 | 1.51 | -13.37% | 1.21 | 1.28 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.17% | 44% | -6.69% | -7.24% | -1.52 | 14 | 100% |
| out_of_sample | 532 | -0.17% | 45% | -6.69% | -7.24% | -1.28 | 14 | 100% |
| in_sample | 1768 | -0.17% | 44% | -5.69% | -6.04% | -1.59 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.141% | 58% | 2.49 | +25.89% |
| bull | 659 | 28% | +0.088% | 55% | 2.69 | +76.73% |
| bear | 399 | 17% | +0.015% | 48% | 0.49 | +5.48% |
| chop | 1099 | 47% | -0.012% | 44% | -0.33 | -14.01% |

## Turnover, fees, activity

- trades: 5584 (2.40/day); active days 100%
- turnover 35.8x equity/year; fees 3.58% of equity/year ($16,801 total)
- average gross exposure 0.16; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.96
