# Run: b4c_C_h_c4_w05_m125_h12

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 4, 'w': 0.5, 'swap_m': 1.25, 'min_hold_h': 12}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +276.64% | +22.11% | 0.75 | 1.04 | -54.33% | 0.41 | 0.76 |
| in_sample | 2020-02-15 → 2024-12-31 | +387.42% | +38.33% | 1.05 | 1.46 | -51.48% | 0.74 | 1.12 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -22.69% | -13.62% | -0.42 | -0.59 | -40.82% | -0.33 | -0.46 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +2.93% | +2.93% | 0.24 | 0.34 | -26.95% | 0.11 | 0.24 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.79% | 43% | -13.67% | -18.23% | -1.64 | 14 | 75% |
| out_of_sample | 628 | -1.78% | 38% | -12.36% | -13.07% | -4.13 | 14 | 83% |
| in_sample | 1768 | -0.44% | 45% | -13.67% | -18.23% | -0.81 | 14 | 72% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.636% | 55% | 4.00 | +181.87% |
| bull | 687 | 28% | +0.252% | 50% | 2.37 | +391.14% |
| bear | 400 | 17% | -0.114% | 42% | -1.67 | -38.85% |
| chop | 1160 | 48% | -0.061% | 37% | -0.89 | -55.51% |

## Turnover, fees, activity

- trades: 18318 (7.56/day); active days 96%
- turnover 240.8x equity/year; fees 24.08% of equity/year ($300,655 total)
- average gross exposure 0.29; brake active 48.7% of hours
- correlation of daily returns with s3v2 baseline: 0.49
