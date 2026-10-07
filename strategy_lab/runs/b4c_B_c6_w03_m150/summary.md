# Run: b4c_B_c6_w03_m150

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 6, 'w': 0.3, 'swap_m': 1.5, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +200.37% | +18.01% | 0.65 | 0.90 | -64.39% | 0.28 | 0.64 |
| in_sample | 2020-02-15 → 2024-12-31 | +407.97% | +39.50% | 1.08 | 1.49 | -48.71% | 0.81 | 1.16 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -40.84% | -25.82% | -1.00 | -1.38 | -50.07% | -0.52 | -1.01 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -10.72% | -10.72% | -0.33 | -0.47 | -32.01% | -0.33 | -0.39 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.75% | 43% | -14.20% | -18.08% | -1.41 | 14 | 78% |
| out_of_sample | 628 | -2.17% | 35% | -14.20% | -14.75% | -4.67 | 14 | 85% |
| in_sample | 1768 | -0.28% | 46% | -14.07% | -18.08% | -0.44 | 14 | 76% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.782% | 57% | 4.93 | +264.35% |
| bull | 687 | 28% | +0.224% | 49% | 2.15 | +307.15% |
| bear | 400 | 17% | -0.126% | 45% | -1.85 | -41.60% |
| chop | 1160 | 48% | -0.083% | 37% | -1.19 | -65.33% |

## Turnover, fees, activity

- trades: 18097 (7.47/day); active days 96%
- turnover 225.7x equity/year; fees 22.57% of equity/year ($315,381 total)
- average gross exposure 0.30; brake active 52.7% of hours
- correlation of daily returns with s3v2 baseline: 0.51
