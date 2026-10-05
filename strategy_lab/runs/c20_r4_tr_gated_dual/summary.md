# Run: c20_r4_tr_gated_dual

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +116.70% | +12.89% | 0.95 | 1.37 | -18.09% | 0.71 | 1.05 |
| in_sample | 2020-02-15 → 2024-12-31 | +63.75% | +10.63% | 0.83 | 1.19 | -18.09% | 0.59 | 0.90 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +32.45% | +20.67% | 1.31 | 1.89 | -13.21% | 1.57 | 1.62 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.81% | +18.88% | 1.14 | 1.66 | -13.21% | 1.43 | 1.43 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.17% | 45% | -7.03% | -7.61% | -1.30 | 14 | 100% |
| out_of_sample | 532 | -0.12% | 47% | -7.03% | -7.61% | -0.70 | 14 | 100% |
| in_sample | 1768 | -0.16% | 45% | -6.26% | -6.64% | -1.38 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.153% | 57% | 2.59 | +28.40% |
| bull | 659 | 28% | +0.087% | 54% | 2.69 | +74.89% |
| bear | 399 | 17% | +0.016% | 48% | 0.47 | +5.61% |
| chop | 1099 | 47% | -0.004% | 44% | -0.10 | -6.47% |

## Turnover, fees, activity

- trades: 5719 (2.46/day); active days 100%
- turnover 38.0x equity/year; fees 3.80% of equity/year ($18,470 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
