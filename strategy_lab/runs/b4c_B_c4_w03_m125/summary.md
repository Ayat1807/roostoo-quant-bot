# Run: b4c_B_c4_w03_m125

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 4, 'w': 0.3, 'swap_m': 1.25, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +180.14% | +16.78% | 0.62 | 0.87 | -63.08% | 0.27 | 0.61 |
| in_sample | 2020-02-15 → 2024-12-31 | +302.94% | +33.04% | 0.96 | 1.33 | -61.17% | 0.54 | 0.98 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -30.44% | -18.66% | -0.67 | -0.94 | -39.87% | -0.47 | -0.72 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -5.72% | -5.72% | -0.12 | -0.17 | -30.38% | -0.19 | -0.16 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.92% | 42% | -17.11% | -17.56% | -1.91 | 14 | 74% |
| out_of_sample | 628 | -1.85% | 35% | -11.39% | -12.18% | -4.45 | 14 | 78% |
| in_sample | 1768 | -0.52% | 44% | -17.11% | -17.56% | -1.10 | 14 | 72% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.769% | 57% | 5.06 | +258.24% |
| bull | 687 | 28% | +0.212% | 48% | 2.02 | +273.67% |
| bear | 400 | 17% | -0.103% | 43% | -1.58 | -35.74% |
| chop | 1160 | 48% | -0.088% | 36% | -1.32 | -67.43% |

## Turnover, fees, activity

- trades: 18663 (7.70/day); active days 95%
- turnover 237.9x equity/year; fees 23.79% of equity/year ($267,500 total)
- average gross exposure 0.28; brake active 51.7% of hours
- correlation of daily returns with s3v2 baseline: 0.49
