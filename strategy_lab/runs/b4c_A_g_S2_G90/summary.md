# Run: b4c_A_g_S2_G90

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.9, 'short_gate': 'btc_below_30d'}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +53.05% | +6.62% | 0.36 | 0.49 | -80.79% | 0.08 | 0.33 |
| in_sample | 2020-02-15 → 2024-12-31 | +229.62% | +27.67% | 0.82 | 1.13 | -65.36% | 0.42 | 0.83 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -53.60% | -35.40% | -1.38 | -1.91 | -59.47% | -0.60 | -1.35 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -22.19% | -22.19% | -0.84 | -1.17 | -38.15% | -0.58 | -0.89 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.45% | 39% | -19.92% | -23.11% | -2.62 | 14 | 76% |
| out_of_sample | 628 | -2.67% | 30% | -11.84% | -14.96% | -5.06 | 14 | 68% |
| in_sample | 1768 | -0.86% | 42% | -19.92% | -23.11% | -1.52 | 14 | 79% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.591% | 53% | 3.41 | +157.04% |
| bull | 687 | 28% | +0.242% | 48% | 2.16 | +352.01% |
| bear | 400 | 17% | -0.161% | 44% | -2.47 | -49.05% |
| chop | 1160 | 48% | -0.107% | 38% | -1.48 | -74.14% |

## Turnover, fees, activity

- trades: 18461 (7.62/day); active days 95%
- turnover 228.3x equity/year; fees 22.83% of equity/year ($234,286 total)
- average gross exposure 0.36; brake active 51.5% of hours
- correlation of daily returns with s3v2 baseline: 0.51
