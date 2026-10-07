# Run: b4b_best_breadth

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'score', 'exposure': 'breadth'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +439.07% | +28.88% | 0.91 | 1.26 | -51.23% | 0.56 | 0.95 |
| in_sample | 2020-02-15 → 2024-12-31 | +543.42% | +46.42% | 1.21 | 1.68 | -51.23% | 0.91 | 1.31 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -16.30% | -9.63% | -0.26 | -0.37 | -29.88% | -0.32 | -0.33 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -7.51% | -7.51% | -0.24 | -0.35 | -24.08% | -0.31 | -0.30 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.90% | 40% | -15.32% | -18.39% | -2.72 | 12 | 33% |
| out_of_sample | 628 | -1.61% | 35% | -12.66% | -12.96% | -5.24 | 12 | 21% |
| in_sample | 1768 | -0.61% | 42% | -15.32% | -18.39% | -1.80 | 12 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.683% | 43% | 3.92 | +202.67% |
| bull | 687 | 28% | +0.251% | 49% | 2.28 | +382.86% |
| bear | 400 | 17% | -0.212% | 31% | -3.75 | -58.16% |
| chop | 1160 | 48% | -0.003% | 34% | -0.04 | -11.85% |

## Turnover, fees, activity

- trades: 13606 (5.61/day); active days 83%
- turnover 139.9x equity/year; fees 13.99% of equity/year ($221,785 total)
- average gross exposure 0.24; brake active 43.9% of hours
- correlation of daily returns with s3v2 baseline: 0.39
