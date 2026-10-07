# Run: b4b_live_conviction

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'exposure': 'conviction'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +93.54% | +10.46% | 0.45 | 0.62 | -75.61% | 0.14 | 0.43 |
| in_sample | 2020-02-15 → 2024-12-31 | +221.10% | +26.99% | 0.79 | 1.09 | -61.31% | 0.44 | 0.81 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -39.89% | -25.14% | -0.86 | -1.21 | -53.92% | -0.47 | -0.88 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -8.22% | -8.22% | -0.19 | -0.28 | -29.19% | -0.28 | -0.25 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.48% | 38% | -18.63% | -21.23% | -2.85 | 12 | 33% |
| out_of_sample | 628 | -2.58% | 33% | -12.86% | -15.18% | -5.78 | 12 | 21% |
| in_sample | 1768 | -0.99% | 40% | -18.63% | -21.23% | -2.23 | 12 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.777% | 45% | 4.43 | +255.51% |
| bull | 687 | 28% | +0.188% | 47% | 1.63 | +208.99% |
| bear | 400 | 17% | -0.231% | 28% | -3.66 | -61.50% |
| chop | 1160 | 48% | -0.057% | 34% | -0.75 | -54.24% |

## Turnover, fees, activity

- trades: 14939 (6.16/day); active days 83%
- turnover 188.8x equity/year; fees 18.88% of equity/year ($189,078 total)
- average gross exposure 0.29; brake active 49.4% of hours
- correlation of daily returns with s3v2 baseline: 0.37
