# Run: b4c_B_c6_w03_m125

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 6, 'w': 0.3, 'swap_m': 1.25, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +194.30% | +17.65% | 0.64 | 0.89 | -59.93% | 0.29 | 0.63 |
| in_sample | 2020-02-15 → 2024-12-31 | +405.97% | +39.39% | 1.07 | 1.49 | -41.59% | 0.95 | 1.20 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -41.81% | -26.51% | -1.02 | -1.41 | -49.65% | -0.53 | -1.03 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -20.17% | -20.17% | -0.80 | -1.12 | -34.42% | -0.59 | -0.87 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.79% | 43% | -15.50% | -18.20% | -1.47 | 14 | 77% |
| out_of_sample | 628 | -2.21% | 32% | -12.37% | -13.50% | -4.85 | 14 | 82% |
| in_sample | 1768 | -0.06% | 48% | -15.50% | -18.20% | -0.06 | 14 | 75% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.775% | 57% | 4.83 | +259.40% |
| bull | 687 | 28% | +0.216% | 47% | 2.05 | +285.35% |
| bear | 400 | 17% | -0.119% | 43% | -1.75 | -39.96% |
| chop | 1160 | 48% | -0.081% | 37% | -1.14 | -64.60% |

## Turnover, fees, activity

- trades: 18426 (7.60/day); active days 96%
- turnover 229.4x equity/year; fees 22.94% of equity/year ($314,736 total)
- average gross exposure 0.30; brake active 52.6% of hours
- correlation of daily returns with s3v2 baseline: 0.48
