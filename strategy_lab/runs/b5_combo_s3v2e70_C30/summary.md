# Run: b5_combo_s3v2e70_C30

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +117.01% | +12.38% | 0.92 | 1.34 | -14.84% | 0.83 | 1.06 |
| in_sample | 2020-02-15 → 2024-12-31 | +60.14% | +10.13% | 0.79 | 1.16 | -14.84% | 0.68 | 0.91 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +35.70% | +18.97% | 1.23 | 1.80 | -12.54% | 1.51 | 1.54 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +23.02% | +23.02% | 1.32 | 1.95 | -12.54% | 1.84 | 1.73 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.20% | 44% | -5.42% | -6.60% | -1.52 | 14 | 100% |
| out_of_sample | 628 | -0.20% | 44% | -5.42% | -5.82% | -1.30 | 14 | 100% |
| in_sample | 1768 | -0.19% | 45% | -4.39% | -6.60% | -1.48 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.204% | 59% | 2.80 | +40.77% |
| bull | 687 | 28% | +0.085% | 52% | 3.10 | +77.40% |
| bear | 400 | 17% | +0.060% | 48% | 1.67 | +26.09% |
| chop | 1160 | 48% | -0.028% | 42% | -0.81 | -29.70% |

## Turnover, fees, activity

- trades: 8511 (3.51/day); active days 100%
- turnover 38.2x equity/year; fees 3.82% of equity/year ($18,288 total)
- average gross exposure 0.17; brake active 9.5% of hours
- correlation of daily returns with s3v2 baseline: 0.87
