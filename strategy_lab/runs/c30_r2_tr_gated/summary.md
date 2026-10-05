# Run: c30_r2_tr_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +107.13% | +12.09% | 0.92 | 1.32 | -18.05% | 0.67 | 1.00 |
| in_sample | 2020-02-15 → 2024-12-31 | +64.56% | +10.74% | 0.86 | 1.22 | -18.05% | 0.60 | 0.93 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +25.97% | +16.69% | 1.11 | 1.59 | -12.37% | 1.35 | 1.38 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +10.95% | +14.91% | 0.99 | 1.44 | -12.37% | 1.21 | 1.23 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.17% | 44% | -6.42% | -6.95% | -1.57 | 14 | 100% |
| out_of_sample | 532 | -0.16% | 45% | -6.42% | -6.95% | -1.07 | 14 | 100% |
| in_sample | 1768 | -0.17% | 44% | -5.76% | -6.11% | -1.73 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.150% | 58% | 2.74 | +27.83% |
| bull | 659 | 28% | +0.089% | 53% | 2.46 | +77.16% |
| bear | 399 | 17% | +0.014% | 48% | 0.48 | +5.20% |
| chop | 1099 | 47% | -0.009% | 44% | -0.26 | -11.27% |

## Turnover, fees, activity

- trades: 6148 (2.64/day); active days 100%
- turnover 36.7x equity/year; fees 3.67% of equity/year ($17,420 total)
- average gross exposure 0.16; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.95
