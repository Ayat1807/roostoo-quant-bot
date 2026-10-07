# Run: b5_combo_s3v2e70_E30

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +126.97% | +13.14% | 1.06 | 1.55 | -12.88% | 1.02 | 1.24 |
| in_sample | 2020-02-15 → 2024-12-31 | +68.24% | +11.24% | 0.95 | 1.40 | -12.88% | 0.87 | 1.11 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +35.02% | +18.63% | 1.31 | 1.92 | -11.43% | 1.63 | 1.65 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +22.14% | +22.14% | 1.37 | 2.02 | -11.43% | 1.94 | 1.80 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.14% | 45% | -5.18% | -5.57% | -1.56 | 14 | 100% |
| out_of_sample | 628 | -0.13% | 46% | -5.18% | -5.57% | -0.89 | 14 | 100% |
| in_sample | 1768 | -0.14% | 45% | -3.89% | -5.34% | -1.63 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.207% | 59% | 3.19 | +41.98% |
| bull | 687 | 28% | +0.082% | 53% | 3.12 | +74.69% |
| bear | 400 | 17% | +0.035% | 46% | 1.19 | +14.52% |
| chop | 1160 | 48% | -0.016% | 43% | -0.49 | -18.49% |

## Turnover, fees, activity

- trades: 5191 (2.14/day); active days 100%
- turnover 33.2x equity/year; fees 3.32% of equity/year ($16,495 total)
- average gross exposure 0.15; brake active 9.5% of hours
- correlation of daily returns with s3v2 baseline: 0.86
