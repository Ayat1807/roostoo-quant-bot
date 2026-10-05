# Run: c20_r4_tr_gated_rvb

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +113.87% | +12.66% | 0.93 | 1.34 | -18.42% | 0.69 | 1.02 |
| in_sample | 2020-02-15 → 2024-12-31 | +61.63% | +10.33% | 0.80 | 1.15 | -18.42% | 0.56 | 0.87 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +32.44% | +20.66% | 1.30 | 1.88 | -13.33% | 1.55 | 1.61 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.17% | +19.38% | 1.15 | 1.68 | -13.33% | 1.45 | 1.45 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.18% | 45% | -7.13% | -7.71% | -1.40 | 14 | 100% |
| out_of_sample | 532 | -0.12% | 47% | -7.13% | -7.71% | -0.70 | 14 | 100% |
| in_sample | 1768 | -0.18% | 44% | -6.32% | -6.71% | -1.45 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.156% | 58% | 2.61 | +29.00% |
| bull | 659 | 28% | +0.085% | 54% | 2.63 | +72.85% |
| bear | 399 | 17% | +0.016% | 48% | 0.48 | +5.74% |
| chop | 1099 | 47% | -0.004% | 44% | -0.11 | -7.16% |

## Turnover, fees, activity

- trades: 5749 (2.47/day); active days 100%
- turnover 38.3x equity/year; fees 3.83% of equity/year ($18,427 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
