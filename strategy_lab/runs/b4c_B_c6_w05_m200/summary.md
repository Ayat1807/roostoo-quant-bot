# Run: b4c_B_c6_w05_m200

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 6, 'w': 0.5, 'swap_m': 2.0, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +251.68% | +20.85% | 0.72 | 1.00 | -59.17% | 0.35 | 0.72 |
| in_sample | 2020-02-15 → 2024-12-31 | +400.57% | +39.08% | 1.07 | 1.49 | -40.09% | 0.97 | 1.21 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -29.71% | -18.17% | -0.61 | -0.85 | -43.68% | -0.42 | -0.65 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -3.28% | -3.28% | -0.01 | -0.01 | -26.56% | -0.12 | -0.04 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.59% | 45% | -13.95% | -16.16% | -1.07 | 14 | 79% |
| out_of_sample | 628 | -2.12% | 34% | -13.95% | -14.48% | -4.78 | 14 | 88% |
| in_sample | 1768 | +0.00% | 48% | -13.44% | -16.16% | 0.00 | 14 | 76% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.801% | 59% | 4.89 | +274.48% |
| bull | 687 | 28% | +0.223% | 49% | 2.13 | +303.53% |
| bear | 400 | 17% | -0.105% | 45% | -1.58 | -36.51% |
| chop | 1160 | 48% | -0.078% | 37% | -1.10 | -63.35% |

## Turnover, fees, activity

- trades: 17918 (7.39/day); active days 96%
- turnover 230.5x equity/year; fees 23.05% of equity/year ($321,385 total)
- average gross exposure 0.30; brake active 50.9% of hours
- correlation of daily returns with s3v2 baseline: 0.50
