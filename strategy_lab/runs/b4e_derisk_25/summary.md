# Run: b4e_derisk_25

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +347.47% | +25.32% | 0.81 | 1.11 | -63.28% | 0.40 | 0.81 |
| in_sample | 2020-02-15 → 2024-12-31 | +434.86% | +40.98% | 1.09 | 1.49 | -63.28% | 0.65 | 1.11 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -16.62% | -9.82% | -0.23 | -0.32 | -31.79% | -0.31 | -0.29 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +0.29% | +0.29% | 0.14 | 0.19 | -24.75% | 0.01 | 0.12 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.19% | 40% | -20.63% | -20.63% | -2.55 | 12 | 32% |
| out_of_sample | 628 | -1.76% | 36% | -11.97% | -13.23% | -3.70 | 12 | 21% |
| in_sample | 1768 | -0.90% | 42% | -20.63% | -20.63% | -1.94 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.657% | 45% | 3.96 | +190.86% |
| bull | 687 | 28% | +0.271% | 49% | 2.40 | +448.50% |
| bear | 400 | 17% | -0.210% | 30% | -3.23 | -58.10% |
| chop | 1160 | 48% | -0.025% | 35% | -0.35 | -33.06% |

## Turnover, fees, activity

- trades: 14491 (5.98/day); active days 82%
- turnover 166.5x equity/year; fees 16.65% of equity/year ($241,734 total)
- average gross exposure 0.29; brake active 45.8% of hours
- correlation of daily returns with s3v2 baseline: 0.37
