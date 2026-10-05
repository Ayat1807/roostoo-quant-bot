# Run: c30_r1_bo_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +104.54% | +11.87% | 0.91 | 1.30 | -18.72% | 0.63 | 0.99 |
| in_sample | 2020-02-15 → 2024-12-31 | +61.64% | +10.34% | 0.83 | 1.18 | -18.72% | 0.55 | 0.89 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +26.64% | +17.11% | 1.17 | 1.68 | -12.26% | 1.40 | 1.44 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.60% | +17.19% | 1.12 | 1.62 | -12.26% | 1.40 | 1.40 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.18% | 44% | -6.52% | -7.06% | -1.70 | 14 | 100% |
| out_of_sample | 532 | -0.13% | 46% | -6.52% | -7.06% | -0.80 | 14 | 100% |
| in_sample | 1768 | -0.18% | 43% | -5.84% | -6.20% | -1.85 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.170% | 58% | 2.96 | +32.10% |
| bull | 659 | 28% | +0.086% | 53% | 2.58 | +73.69% |
| bear | 399 | 17% | +0.013% | 48% | 0.43 | +4.64% |
| chop | 1099 | 47% | -0.011% | 43% | -0.31 | -13.06% |

## Turnover, fees, activity

- trades: 5710 (2.45/day); active days 100%
- turnover 37.0x equity/year; fees 3.70% of equity/year ($17,339 total)
- average gross exposure 0.16; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.96
