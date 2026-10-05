# Run: c30_r2_rs

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +92.27% | +10.79% | 0.71 | 0.99 | -27.03% | 0.40 | 0.73 |
| in_sample | 2020-02-15 → 2024-12-31 | +45.95% | +8.05% | 0.56 | 0.77 | -27.03% | 0.30 | 0.57 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +31.85% | +20.30% | 1.21 | 1.73 | -11.47% | 1.77 | 1.58 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.99% | +19.14% | 1.11 | 1.60 | -11.47% | 1.67 | 1.47 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.35% | 42% | -7.12% | -7.62% | -2.26 | 14 | 100% |
| out_of_sample | 532 | -0.16% | 45% | -6.53% | -7.62% | -0.82 | 14 | 100% |
| in_sample | 1768 | -0.41% | 42% | -7.12% | -7.50% | -2.85 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.195% | 56% | 2.94 | +37.32% |
| bull | 659 | 28% | +0.116% | 55% | 2.65 | +109.29% |
| bear | 399 | 17% | -0.042% | 44% | -1.17 | -16.18% |
| chop | 1099 | 47% | -0.016% | 44% | -0.37 | -18.55% |

## Turnover, fees, activity

- trades: 6420 (2.76/day); active days 100%
- turnover 41.0x equity/year; fees 4.10% of equity/year ($18,886 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.89
