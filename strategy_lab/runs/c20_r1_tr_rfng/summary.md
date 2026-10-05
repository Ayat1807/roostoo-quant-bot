# Run: c20_r1_tr_rfng

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +125.65% | +13.61% | 0.89 | 1.27 | -21.39% | 0.64 | 0.97 |
| in_sample | 2020-02-15 → 2024-12-31 | +75.27% | +12.18% | 0.83 | 1.17 | -21.39% | 0.57 | 0.89 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +28.85% | +18.47% | 1.09 | 1.57 | -14.04% | 1.32 | 1.35 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +10.59% | +14.41% | 0.88 | 1.28 | -14.04% | 1.03 | 1.09 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.29% | 44% | -7.13% | -7.52% | -1.74 | 14 | 100% |
| out_of_sample | 532 | -0.35% | 43% | -6.99% | -7.52% | -1.77 | 14 | 100% |
| in_sample | 1768 | -0.25% | 45% | -7.13% | -7.52% | -1.71 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.190% | 58% | 3.01 | +36.43% |
| bull | 659 | 28% | +0.104% | 55% | 2.67 | +94.34% |
| bear | 399 | 17% | -0.013% | 45% | -0.39 | -5.93% |
| chop | 1099 | 47% | -0.004% | 45% | -0.09 | -7.40% |

## Turnover, fees, activity

- trades: 10908 (4.69/day); active days 100%
- turnover 48.3x equity/year; fees 4.83% of equity/year ($23,773 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.95
