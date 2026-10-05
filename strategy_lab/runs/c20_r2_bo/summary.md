# Run: c20_r2_bo

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +140.61% | +14.76% | 0.98 | 1.39 | -20.47% | 0.72 | 1.07 |
| in_sample | 2020-02-15 → 2024-12-31 | +81.04% | +12.93% | 0.89 | 1.26 | -20.47% | 0.63 | 0.96 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +33.01% | +21.01% | 1.25 | 1.80 | -11.20% | 1.88 | 1.66 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.66% | +18.68% | 1.11 | 1.61 | -11.20% | 1.67 | 1.48 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.26% | 43% | -7.23% | -7.61% | -1.74 | 14 | 100% |
| out_of_sample | 532 | -0.28% | 43% | -6.76% | -7.31% | -1.37 | 14 | 100% |
| in_sample | 1768 | -0.25% | 43% | -7.23% | -7.61% | -1.87 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.181% | 55% | 2.81 | +34.36% |
| bull | 659 | 28% | +0.106% | 53% | 2.78 | +97.56% |
| bear | 399 | 17% | -0.012% | 44% | -0.38 | -5.39% |
| chop | 1099 | 47% | +0.001% | 44% | 0.03 | -1.95% |

## Turnover, fees, activity

- trades: 7088 (3.04/day); active days 100%
- turnover 44.9x equity/year; fees 4.49% of equity/year ($22,460 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.94
