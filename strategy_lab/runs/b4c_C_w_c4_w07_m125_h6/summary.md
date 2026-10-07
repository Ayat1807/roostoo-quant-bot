# Run: b4c_C_w_c4_w07_m125_h6

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 4, 'w': 0.7, 'swap_m': 1.25, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +178.93% | +16.71% | 0.62 | 0.87 | -69.19% | 0.24 | 0.60 |
| in_sample | 2020-02-15 → 2024-12-31 | +328.34% | +34.71% | 0.99 | 1.38 | -55.89% | 0.62 | 1.04 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -34.85% | -21.63% | -0.80 | -1.11 | -48.82% | -0.44 | -0.82 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -4.93% | -4.93% | -0.08 | -0.12 | -25.80% | -0.19 | -0.13 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.68% | 42% | -13.59% | -17.09% | -1.46 | 14 | 72% |
| out_of_sample | 628 | -1.45% | 37% | -12.71% | -13.70% | -3.94 | 14 | 77% |
| in_sample | 1768 | -0.46% | 44% | -13.59% | -17.09% | -0.96 | 14 | 70% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.632% | 54% | 3.84 | +178.52% |
| bull | 687 | 28% | +0.232% | 48% | 2.16 | +326.39% |
| bear | 400 | 17% | -0.100% | 42% | -1.43 | -35.19% |
| chop | 1160 | 48% | -0.079% | 37% | -1.20 | -63.76% |

## Turnover, fees, activity

- trades: 19496 (8.04/day); active days 96%
- turnover 266.2x equity/year; fees 26.62% of equity/year ($326,995 total)
- average gross exposure 0.29; brake active 49.5% of hours
- correlation of daily returns with s3v2 baseline: 0.52
