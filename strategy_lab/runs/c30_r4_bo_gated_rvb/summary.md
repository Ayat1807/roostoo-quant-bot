# Run: c30_r4_bo_gated_rvb

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +99.94% | +11.47% | 0.90 | 1.29 | -17.33% | 0.66 | 0.98 |
| in_sample | 2020-02-15 → 2024-12-31 | +51.96% | +8.95% | 0.75 | 1.07 | -17.33% | 0.52 | 0.81 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +31.69% | +20.20% | 1.32 | 1.91 | -11.94% | 1.69 | 1.67 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.03% | +19.19% | 1.20 | 1.74 | -11.94% | 1.61 | 1.54 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.17% | 44% | -6.73% | -7.29% | -1.51 | 14 | 100% |
| out_of_sample | 532 | -0.10% | 48% | -6.73% | -7.29% | -0.59 | 14 | 100% |
| in_sample | 1768 | -0.17% | 44% | -5.92% | -6.29% | -1.67 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.145% | 58% | 2.61 | +26.81% |
| bull | 659 | 28% | +0.081% | 54% | 2.61 | +68.46% |
| bear | 399 | 17% | +0.014% | 48% | 0.45 | +5.05% |
| chop | 1099 | 47% | -0.007% | 43% | -0.19 | -9.08% |

## Turnover, fees, activity

- trades: 5479 (2.35/day); active days 100%
- turnover 36.3x equity/year; fees 3.63% of equity/year ($16,453 total)
- average gross exposure 0.16; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.98
