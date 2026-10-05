# Run: c20_r4_tr_gated_rfng

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +116.12% | +12.84% | 0.95 | 1.37 | -18.29% | 0.70 | 1.04 |
| in_sample | 2020-02-15 → 2024-12-31 | +63.96% | +10.66% | 0.83 | 1.20 | -18.29% | 0.58 | 0.90 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +31.93% | +20.35% | 1.29 | 1.87 | -13.21% | 1.54 | 1.60 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.92% | +19.04% | 1.14 | 1.66 | -13.21% | 1.44 | 1.44 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.14% | 45% | -7.05% | -7.63% | -1.18 | 14 | 100% |
| out_of_sample | 532 | -0.12% | 47% | -7.05% | -7.63% | -0.73 | 14 | 100% |
| in_sample | 1768 | -0.14% | 45% | -6.24% | -6.63% | -1.20 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.154% | 58% | 2.59 | +28.48% |
| bull | 659 | 28% | +0.086% | 53% | 2.70 | +74.38% |
| bear | 399 | 17% | +0.016% | 48% | 0.48 | +5.68% |
| chop | 1099 | 47% | -0.004% | 44% | -0.10 | -6.57% |

## Turnover, fees, activity

- trades: 5704 (2.45/day); active days 100%
- turnover 38.0x equity/year; fees 3.80% of equity/year ($18,493 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
