# Run: b4c_B_c2_w00_m150

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 2, 'w': 0.0, 'swap_m': 1.5, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +28.20% | +3.81% | 0.28 | 0.38 | -55.39% | 0.07 | 0.26 |
| in_sample | 2020-02-15 → 2024-12-31 | +60.55% | +10.18% | 0.45 | 0.63 | -55.39% | 0.18 | 0.44 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -20.05% | -11.95% | -0.38 | -0.54 | -35.11% | -0.34 | -0.43 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -6.90% | -6.90% | -0.20 | -0.29 | -27.11% | -0.25 | -0.25 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.97% | 41% | -15.47% | -17.87% | -2.15 | 14 | 62% |
| out_of_sample | 628 | -1.50% | 36% | -11.41% | -11.73% | -3.75 | 14 | 58% |
| in_sample | 1768 | -0.70% | 42% | -15.47% | -17.87% | -1.40 | 14 | 64% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.557% | 53% | 3.56 | +146.55% |
| bull | 687 | 28% | +0.154% | 47% | 1.58 | +156.38% |
| bear | 400 | 17% | -0.084% | 42% | -1.28 | -30.61% |
| chop | 1160 | 48% | -0.099% | 36% | -1.58 | -70.77% |

## Turnover, fees, activity

- trades: 16040 (6.62/day); active days 94%
- turnover 206.6x equity/year; fees 20.66% of equity/year ($100,189 total)
- average gross exposure 0.26; brake active 52.9% of hours
- correlation of daily returns with s3v2 baseline: 0.50
