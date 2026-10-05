# Run: c30_r1_rs_rfng

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +113.77% | +12.65% | 0.80 | 1.12 | -27.94% | 0.45 | 0.82 |
| in_sample | 2020-02-15 → 2024-12-31 | +77.11% | +12.42% | 0.79 | 1.10 | -27.94% | 0.44 | 0.81 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +20.79% | +13.46% | 0.84 | 1.19 | -13.04% | 1.03 | 1.04 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +6.60% | +8.93% | 0.61 | 0.86 | -13.04% | 0.68 | 0.73 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.35% | 43% | -7.16% | -7.49% | -2.09 | 14 | 100% |
| out_of_sample | 532 | -0.29% | 43% | -6.45% | -7.04% | -1.71 | 14 | 100% |
| in_sample | 1768 | -0.35% | 43% | -7.16% | -7.49% | -2.05 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.191% | 58% | 3.12 | +36.77% |
| bull | 659 | 28% | +0.115% | 54% | 2.66 | +107.91% |
| bear | 399 | 17% | -0.042% | 46% | -1.25 | -16.28% |
| chop | 1099 | 47% | -0.005% | 44% | -0.11 | -8.36% |

## Turnover, fees, activity

- trades: 6667 (2.86/day); active days 100%
- turnover 42.1x equity/year; fees 4.21% of equity/year ($20,864 total)
- average gross exposure 0.21; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.85
