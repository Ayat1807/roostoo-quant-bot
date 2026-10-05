# Run: c20_r4_rs_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +110.29% | +12.36% | 0.90 | 1.29 | -19.19% | 0.64 | 0.98 |
| in_sample | 2020-02-15 → 2024-12-31 | +60.09% | +10.12% | 0.78 | 1.12 | -19.19% | 0.53 | 0.84 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +31.47% | +20.07% | 1.24 | 1.78 | -13.48% | 1.49 | 1.53 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.26% | +19.51% | 1.13 | 1.65 | -13.48% | 1.45 | 1.43 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.17% | 45% | -7.25% | -7.85% | -1.42 | 14 | 100% |
| out_of_sample | 532 | -0.12% | 47% | -7.25% | -7.85% | -0.76 | 14 | 100% |
| in_sample | 1768 | -0.17% | 45% | -6.37% | -6.77% | -1.45 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.152% | 58% | 2.45 | +27.98% |
| bull | 659 | 28% | +0.088% | 54% | 2.66 | +75.92% |
| bear | 399 | 17% | +0.017% | 48% | 0.49 | +6.02% |
| chop | 1099 | 47% | -0.007% | 44% | -0.18 | -9.84% |

## Turnover, fees, activity

- trades: 5536 (2.38/day); active days 100%
- turnover 38.5x equity/year; fees 3.85% of equity/year ($18,325 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
