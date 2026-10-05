# Run: c20_r1_rs_dual

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +115.82% | +12.82% | 0.86 | 1.22 | -21.55% | 0.59 | 0.92 |
| in_sample | 2020-02-15 → 2024-12-31 | +69.56% | +11.42% | 0.79 | 1.11 | -21.55% | 0.53 | 0.84 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +27.39% | +17.57% | 1.09 | 1.56 | -13.22% | 1.33 | 1.35 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.80% | +17.47% | 1.04 | 1.50 | -13.22% | 1.32 | 1.31 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.25% | 45% | -7.18% | -7.76% | -1.42 | 14 | 100% |
| out_of_sample | 532 | -0.13% | 47% | -7.18% | -7.76% | -0.63 | 14 | 100% |
| in_sample | 1768 | -0.28% | 44% | -7.10% | -7.48% | -1.57 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.168% | 55% | 2.61 | +31.27% |
| bull | 659 | 28% | +0.108% | 54% | 2.78 | +99.44% |
| bear | 399 | 17% | -0.020% | 43% | -0.57 | -8.37% |
| chop | 1099 | 47% | -0.005% | 43% | -0.12 | -7.92% |

## Turnover, fees, activity

- trades: 7315 (3.14/day); active days 100%
- turnover 45.5x equity/year; fees 4.55% of equity/year ($22,569 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.95
