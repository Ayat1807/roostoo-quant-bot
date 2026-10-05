# Run: c30_r1_bo_rvb

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +106.20% | +12.02% | 0.83 | 1.16 | -23.28% | 0.52 | 0.87 |
| in_sample | 2020-02-15 → 2024-12-31 | +71.70% | +11.71% | 0.81 | 1.13 | -23.28% | 0.50 | 0.85 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +20.18% | +13.08% | 0.88 | 1.26 | -12.28% | 1.07 | 1.09 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +10.56% | +14.37% | 0.92 | 1.32 | -12.28% | 1.17 | 1.16 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.26% | 45% | -6.57% | -7.10% | -1.83 | 14 | 100% |
| out_of_sample | 532 | -0.19% | 45% | -6.57% | -7.10% | -1.37 | 14 | 100% |
| in_sample | 1768 | -0.26% | 45% | -5.92% | -6.84% | -1.92 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.254% | 60% | 4.12 | +52.17% |
| bull | 659 | 28% | +0.104% | 51% | 2.51 | +94.04% |
| bear | 399 | 17% | -0.014% | 45% | -0.44 | -5.98% |
| chop | 1099 | 47% | -0.023% | 42% | -0.61 | -24.20% |

## Turnover, fees, activity

- trades: 6883 (2.96/day); active days 100%
- turnover 44.3x equity/year; fees 4.43% of equity/year ($21,417 total)
- average gross exposure 0.18; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.89
