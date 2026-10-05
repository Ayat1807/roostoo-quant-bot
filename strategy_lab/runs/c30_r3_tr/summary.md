# Run: c30_r3_tr

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +133.38% | +14.21% | 0.94 | 1.31 | -23.68% | 0.60 | 0.98 |
| in_sample | 2020-02-15 → 2024-12-31 | +88.87% | +13.91% | 0.91 | 1.26 | -23.68% | 0.59 | 0.95 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +23.65% | +15.25% | 1.03 | 1.48 | -10.89% | 1.40 | 1.32 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +13.87% | +18.96% | 1.25 | 1.80 | -10.89% | 1.74 | 1.62 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.24% | 45% | -5.89% | -6.51% | -1.38 | 14 | 100% |
| out_of_sample | 532 | -0.30% | 43% | -5.87% | -6.24% | -1.55 | 14 | 100% |
| in_sample | 1768 | -0.20% | 45% | -5.89% | -6.51% | -1.35 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.151% | 56% | 2.47 | +27.84% |
| bull | 659 | 28% | +0.127% | 55% | 3.02 | +125.83% |
| bear | 399 | 17% | -0.023% | 47% | -0.77 | -9.39% |
| chop | 1099 | 47% | -0.006% | 45% | -0.16 | -8.96% |

## Turnover, fees, activity

- trades: 8577 (3.68/day); active days 100%
- turnover 48.3x equity/year; fees 4.83% of equity/year ($25,214 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.89
