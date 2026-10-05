# Run: c30_r1_bo_jump

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +90.01% | +10.59% | 0.78 | 1.11 | -21.11% | 0.50 | 0.83 |
| in_sample | 2020-02-15 → 2024-12-31 | +56.20% | +9.56% | 0.73 | 1.03 | -21.11% | 0.45 | 0.77 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +21.69% | +14.02% | 0.93 | 1.34 | -13.52% | 1.04 | 1.13 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +10.32% | +14.03% | 0.89 | 1.29 | -13.52% | 1.04 | 1.09 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.34% | 43% | -7.21% | -7.75% | -2.11 | 14 | 100% |
| out_of_sample | 532 | -0.42% | 42% | -7.21% | -7.75% | -2.04 | 14 | 100% |
| in_sample | 1768 | -0.32% | 44% | -6.26% | -6.61% | -2.02 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.186% | 56% | 3.05 | +35.53% |
| bull | 659 | 28% | +0.093% | 53% | 2.68 | +81.50% |
| bear | 399 | 17% | -0.016% | 41% | -0.46 | -6.81% |
| chop | 1099 | 47% | -0.013% | 44% | -0.35 | -15.42% |

## Turnover, fees, activity

- trades: 7275 (3.12/day); active days 100%
- turnover 46.7x equity/year; fees 4.67% of equity/year ($21,279 total)
- average gross exposure 0.19; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.95
