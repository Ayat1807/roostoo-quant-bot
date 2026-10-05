# Run: c20_r1_bo_rfng

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +117.12% | +12.93% | 0.88 | 1.26 | -21.15% | 0.61 | 0.95 |
| in_sample | 2020-02-15 → 2024-12-31 | +73.83% | +11.99% | 0.84 | 1.20 | -21.15% | 0.57 | 0.90 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +24.86% | +16.00% | 1.00 | 1.45 | -12.87% | 1.24 | 1.26 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.79% | +18.85% | 1.10 | 1.61 | -12.87% | 1.46 | 1.42 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.32% | 43% | -7.08% | -7.65% | -2.21 | 14 | 100% |
| out_of_sample | 532 | -0.41% | 44% | -7.08% | -7.65% | -2.12 | 14 | 100% |
| in_sample | 1768 | -0.31% | 43% | -7.06% | -7.45% | -2.19 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.189% | 56% | 2.97 | +36.12% |
| bull | 659 | 28% | +0.101% | 53% | 2.74 | +90.81% |
| bear | 399 | 17% | -0.009% | 43% | -0.26 | -4.33% |
| chop | 1099 | 47% | -0.007% | 43% | -0.18 | -10.57% |

## Turnover, fees, activity

- trades: 7442 (3.20/day); active days 100%
- turnover 45.1x equity/year; fees 4.51% of equity/year ($21,574 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.96
