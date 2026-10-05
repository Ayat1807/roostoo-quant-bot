# Run: c20_r1_tr

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +136.55% | +14.45% | 0.90 | 1.26 | -21.77% | 0.66 | 0.98 |
| in_sample | 2020-02-15 → 2024-12-31 | +87.82% | +13.78% | 0.87 | 1.22 | -21.77% | 0.63 | 0.94 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +26.05% | +16.74% | 0.99 | 1.41 | -12.68% | 1.32 | 1.26 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +8.86% | +12.03% | 0.76 | 1.10 | -12.68% | 0.95 | 0.95 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.29% | 44% | -7.13% | -7.90% | -1.68 | 14 | 100% |
| out_of_sample | 532 | -0.34% | 43% | -7.13% | -7.90% | -1.78 | 14 | 100% |
| in_sample | 1768 | -0.28% | 45% | -7.11% | -7.48% | -1.58 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.221% | 58% | 3.30 | +43.48% |
| bull | 659 | 28% | +0.109% | 55% | 2.54 | +100.06% |
| bear | 399 | 17% | -0.028% | 43% | -0.84 | -11.25% |
| chop | 1099 | 47% | -0.001% | 44% | -0.03 | -4.96% |

## Turnover, fees, activity

- trades: 11574 (4.97/day); active days 100%
- turnover 51.7x equity/year; fees 5.17% of equity/year ($26,668 total)
- average gross exposure 0.20; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.92
