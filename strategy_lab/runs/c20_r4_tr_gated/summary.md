# Run: c20_r4_tr_gated

Strategy `None`; universe `None`; params `{}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +115.01% | +12.75% | 0.94 | 1.35 | -18.34% | 0.70 | 1.03 |
| in_sample | 2020-02-15 → 2024-12-31 | +62.81% | +10.50% | 0.82 | 1.17 | -18.34% | 0.57 | 0.89 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +32.18% | +20.50% | 1.29 | 1.87 | -13.27% | 1.55 | 1.60 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.04% | +19.21% | 1.15 | 1.67 | -13.27% | 1.45 | 1.45 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.18% | 45% | -7.09% | -7.67% | -1.37 | 14 | 100% |
| out_of_sample | 532 | -0.12% | 47% | -7.09% | -7.67% | -0.71 | 14 | 100% |
| in_sample | 1768 | -0.18% | 44% | -6.27% | -6.66% | -1.40 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.156% | 58% | 2.61 | +28.91% |
| bull | 659 | 28% | +0.085% | 54% | 2.64 | +72.97% |
| bear | 399 | 17% | +0.016% | 48% | 0.48 | +5.72% |
| chop | 1099 | 47% | -0.004% | 44% | -0.10 | -6.65% |

## Turnover, fees, activity

- trades: 5757 (2.47/day); active days 100%
- turnover 38.2x equity/year; fees 3.82% of equity/year ($18,484 total)
- average gross exposure 0.17; brake active 10.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
