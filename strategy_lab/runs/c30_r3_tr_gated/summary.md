# Run: c30_r3_tr_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +106.06% | +12.00% | 0.95 | 1.36 | -17.33% | 0.69 | 1.04 |
| in_sample | 2020-02-15 → 2024-12-31 | +59.87% | +10.09% | 0.84 | 1.20 | -17.33% | 0.58 | 0.91 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +29.00% | +18.56% | 1.27 | 1.84 | -12.34% | 1.50 | 1.57 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.90% | +17.61% | 1.16 | 1.69 | -12.34% | 1.43 | 1.45 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.17% | 45% | -6.46% | -6.99% | -1.46 | 14 | 100% |
| out_of_sample | 532 | -0.12% | 47% | -6.46% | -6.99% | -0.89 | 14 | 100% |
| in_sample | 1768 | -0.17% | 45% | -5.64% | -5.99% | -1.65 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.135% | 58% | 2.45 | +24.67% |
| bull | 659 | 28% | +0.087% | 55% | 2.85 | +75.71% |
| bear | 399 | 17% | +0.014% | 47% | 0.45 | +4.91% |
| chop | 1099 | 47% | -0.006% | 44% | -0.18 | -8.49% |

## Turnover, fees, activity

- trades: 5759 (2.47/day); active days 100%
- turnover 35.4x equity/year; fees 3.54% of equity/year ($16,827 total)
- average gross exposure 0.15; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.98
