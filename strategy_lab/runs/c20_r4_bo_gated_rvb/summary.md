# Run: c20_r4_bo_gated_rvb

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +113.93% | +12.66% | 0.93 | 1.34 | -18.35% | 0.69 | 1.02 |
| in_sample | 2020-02-15 → 2024-12-31 | +59.87% | +10.09% | 0.78 | 1.13 | -18.35% | 0.55 | 0.85 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +33.94% | +21.57% | 1.34 | 1.94 | -12.85% | 1.68 | 1.68 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +15.03% | +20.59% | 1.20 | 1.76 | -12.85% | 1.60 | 1.54 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.18% | 45% | -7.16% | -7.76% | -1.43 | 14 | 100% |
| out_of_sample | 532 | -0.11% | 48% | -7.16% | -7.76% | -0.59 | 14 | 100% |
| in_sample | 1768 | -0.18% | 44% | -6.40% | -6.80% | -1.64 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.157% | 58% | 2.60 | +29.09% |
| bull | 659 | 28% | +0.085% | 54% | 2.68 | +73.21% |
| bear | 399 | 17% | +0.015% | 48% | 0.45 | +5.37% |
| chop | 1099 | 47% | -0.004% | 44% | -0.11 | -7.07% |

## Turnover, fees, activity

- trades: 5479 (2.35/day); active days 100%
- turnover 38.4x equity/year; fees 3.84% of equity/year ($18,219 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
