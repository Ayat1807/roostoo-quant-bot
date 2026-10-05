# Run: c30_r1_tr_noR5

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +117.47% | +12.95% | 0.79 | 1.10 | -23.30% | 0.56 | 0.84 |
| in_sample | 2020-02-15 → 2024-12-31 | +77.84% | +12.52% | 0.77 | 1.06 | -23.30% | 0.54 | 0.82 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +22.38% | +14.45% | 0.86 | 1.22 | -11.65% | 1.24 | 1.12 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +6.84% | +9.26% | 0.61 | 0.88 | -11.65% | 0.79 | 0.77 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.34% | 44% | -7.23% | -7.58% | -1.71 | 14 | 100% |
| out_of_sample | 532 | -0.43% | 41% | -6.66% | -7.49% | -2.00 | 14 | 100% |
| in_sample | 1768 | -0.30% | 45% | -7.23% | -7.58% | -1.55 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.201% | 55% | 3.03 | +38.92% |
| bull | 659 | 28% | +0.115% | 54% | 2.45 | +107.13% |
| bear | 399 | 17% | -0.043% | 45% | -1.26 | -16.51% |
| chop | 1099 | 47% | -0.004% | 44% | -0.09 | -7.62% |

## Turnover, fees, activity

- trades: 11699 (5.03/day); active days 100%
- turnover 54.9x equity/year; fees 5.49% of equity/year ($27,138 total)
- average gross exposure 0.21; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.85
