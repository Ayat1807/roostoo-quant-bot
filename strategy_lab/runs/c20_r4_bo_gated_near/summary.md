# Run: c20_r4_bo_gated_near

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +118.42% | +13.03% | 0.98 | 1.41 | -17.44% | 0.75 | 1.08 |
| in_sample | 2020-02-15 → 2024-12-31 | +64.78% | +10.77% | 0.86 | 1.23 | -17.44% | 0.62 | 0.94 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +32.67% | +20.80% | 1.33 | 1.94 | -12.65% | 1.64 | 1.67 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +15.03% | +20.59% | 1.23 | 1.79 | -12.65% | 1.63 | 1.57 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.12% | 46% | -7.01% | -7.59% | -1.12 | 14 | 100% |
| out_of_sample | 532 | -0.09% | 48% | -7.01% | -7.59% | -0.55 | 14 | 100% |
| in_sample | 1768 | -0.12% | 46% | -6.18% | -6.56% | -1.16 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.151% | 58% | 2.57 | +27.89% |
| bull | 659 | 28% | +0.085% | 54% | 2.78 | +72.90% |
| bear | 399 | 17% | +0.016% | 48% | 0.48 | +5.66% |
| chop | 1099 | 47% | -0.002% | 44% | -0.04 | -4.31% |

## Turnover, fees, activity

- trades: 5349 (2.30/day); active days 100%
- turnover 37.1x equity/year; fees 3.71% of equity/year ($18,167 total)
- average gross exposure 0.16; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
