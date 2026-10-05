# Run: c30_r1_bo

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +132.12% | +14.11% | 0.87 | 1.23 | -27.32% | 0.52 | 0.91 |
| in_sample | 2020-02-15 → 2024-12-31 | +103.71% | +15.69% | 0.95 | 1.33 | -27.32% | 0.57 | 0.99 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +13.74% | +8.99% | 0.61 | 0.86 | -12.86% | 0.70 | 0.74 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.17% | +16.59% | 1.03 | 1.49 | -11.88% | 1.40 | 1.32 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.47% | 41% | -6.88% | -7.20% | -2.48 | 14 | 100% |
| out_of_sample | 532 | -0.69% | 39% | -5.80% | -6.55% | -3.09 | 14 | 100% |
| in_sample | 1768 | -0.41% | 42% | -6.88% | -7.20% | -2.11 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.263% | 55% | 3.74 | +53.90% |
| bull | 659 | 28% | +0.125% | 52% | 2.65 | +121.15% |
| bear | 399 | 17% | -0.044% | 43% | -1.45 | -16.82% |
| chop | 1099 | 47% | -0.013% | 44% | -0.32 | -16.34% |

## Turnover, fees, activity

- trades: 7682 (3.30/day); active days 100%
- turnover 50.5x equity/year; fees 5.05% of equity/year ($25,845 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.81
