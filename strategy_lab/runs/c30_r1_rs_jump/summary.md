# Run: c30_r1_rs_jump

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +97.11% | +11.23% | 0.80 | 1.13 | -21.04% | 0.53 | 0.85 |
| in_sample | 2020-02-15 → 2024-12-31 | +56.78% | +9.65% | 0.71 | 1.00 | -21.04% | 0.46 | 0.75 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +25.82% | +16.60% | 1.08 | 1.55 | -13.03% | 1.27 | 1.33 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +9.69% | +13.16% | 0.86 | 1.25 | -13.03% | 1.01 | 1.06 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.26% | 45% | -6.93% | -7.67% | -1.64 | 14 | 100% |
| out_of_sample | 532 | -0.16% | 46% | -6.93% | -7.67% | -1.07 | 14 | 100% |
| in_sample | 1768 | -0.28% | 45% | -6.72% | -7.10% | -1.75 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.200% | 58% | 3.40 | +38.95% |
| bull | 659 | 28% | +0.104% | 54% | 2.68 | +95.27% |
| bear | 399 | 17% | -0.042% | 43% | -1.26 | -15.99% |
| chop | 1099 | 47% | -0.009% | 44% | -0.23 | -11.76% |

## Turnover, fees, activity

- trades: 6725 (2.89/day); active days 100%
- turnover 43.1x equity/year; fees 4.31% of equity/year ($20,522 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.91
