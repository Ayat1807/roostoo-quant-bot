# Run: c20_r3_tr_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +118.02% | +13.00% | 0.96 | 1.39 | -18.31% | 0.71 | 1.06 |
| in_sample | 2020-02-15 → 2024-12-31 | +65.15% | +10.82% | 0.84 | 1.21 | -18.31% | 0.59 | 0.92 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +32.13% | +20.47% | 1.31 | 1.90 | -13.18% | 1.55 | 1.62 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.28% | +19.54% | 1.18 | 1.72 | -13.18% | 1.48 | 1.49 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.17% | 45% | -6.98% | -7.56% | -1.42 | 14 | 100% |
| out_of_sample | 532 | -0.12% | 47% | -6.98% | -7.56% | -0.70 | 14 | 100% |
| in_sample | 1768 | -0.17% | 45% | -6.21% | -6.59% | -1.52 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.150% | 58% | 2.50 | +27.61% |
| bull | 659 | 28% | +0.089% | 55% | 2.84 | +77.96% |
| bear | 399 | 17% | +0.015% | 47% | 0.45 | +5.29% |
| chop | 1099 | 47% | -0.004% | 44% | -0.11 | -6.68% |

## Turnover, fees, activity

- trades: 5759 (2.47/day); active days 100%
- turnover 37.7x equity/year; fees 3.77% of equity/year ($18,468 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
