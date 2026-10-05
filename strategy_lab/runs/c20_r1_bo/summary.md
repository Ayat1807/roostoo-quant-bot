# Run: c20_r1_bo

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +135.39% | +14.36% | 0.93 | 1.32 | -21.76% | 0.66 | 1.00 |
| in_sample | 2020-02-15 → 2024-12-31 | +94.38% | +14.58% | 0.95 | 1.34 | -21.76% | 0.67 | 1.02 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +20.98% | +13.58% | 0.88 | 1.26 | -12.49% | 1.09 | 1.09 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.69% | +18.71% | 1.12 | 1.64 | -12.49% | 1.50 | 1.44 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.37% | 43% | -7.00% | -7.36% | -2.12 | 14 | 100% |
| out_of_sample | 532 | -0.40% | 42% | -6.52% | -7.22% | -2.28 | 14 | 100% |
| in_sample | 1768 | -0.35% | 43% | -7.00% | -7.36% | -1.98 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.235% | 55% | 3.51 | +47.13% |
| bull | 659 | 28% | +0.114% | 53% | 2.77 | +107.09% |
| bear | 399 | 17% | -0.024% | 42% | -0.75 | -9.87% |
| chop | 1099 | 47% | -0.009% | 44% | -0.22 | -12.27% |

## Turnover, fees, activity

- trades: 7682 (3.30/day); active days 100%
- turnover 47.6x equity/year; fees 4.76% of equity/year ($24,481 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.91
