# Run: c20_r1_bo_jump

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +107.32% | +12.11% | 0.86 | 1.23 | -20.74% | 0.58 | 0.92 |
| in_sample | 2020-02-15 → 2024-12-31 | +62.70% | +10.48% | 0.77 | 1.11 | -20.74% | 0.51 | 0.83 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +27.49% | +17.63% | 1.10 | 1.60 | -13.94% | 1.26 | 1.35 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.72% | +17.37% | 1.02 | 1.49 | -13.94% | 1.25 | 1.28 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.30% | 43% | -7.47% | -8.04% | -1.92 | 14 | 100% |
| out_of_sample | 532 | -0.35% | 42% | -7.47% | -8.04% | -1.77 | 14 | 100% |
| in_sample | 1768 | -0.27% | 43% | -6.62% | -7.01% | -1.84 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.183% | 56% | 2.90 | +34.82% |
| bull | 659 | 28% | +0.093% | 54% | 2.73 | +81.81% |
| bear | 399 | 17% | -0.004% | 42% | -0.11 | -2.43% |
| chop | 1099 | 47% | -0.008% | 44% | -0.21 | -11.28% |

## Turnover, fees, activity

- trades: 7275 (3.12/day); active days 100%
- turnover 45.0x equity/year; fees 4.50% of equity/year ($21,436 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.98
