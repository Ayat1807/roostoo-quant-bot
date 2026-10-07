# Run: b4c_B_c6_w05_m125

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 6, 'w': 0.5, 'swap_m': 1.25, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +122.21% | +12.78% | 0.52 | 0.72 | -61.33% | 0.21 | 0.51 |
| in_sample | 2020-02-15 → 2024-12-31 | +231.56% | +27.83% | 0.84 | 1.17 | -56.05% | 0.50 | 0.87 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -32.91% | -20.31% | -0.72 | -1.00 | -45.19% | -0.45 | -0.75 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -11.92% | -11.92% | -0.40 | -0.56 | -31.73% | -0.38 | -0.46 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.82% | 43% | -15.71% | -17.74% | -1.59 | 14 | 75% |
| out_of_sample | 628 | -2.30% | 33% | -12.43% | -14.00% | -4.87 | 14 | 82% |
| in_sample | 1768 | -0.24% | 47% | -15.71% | -17.74% | -0.40 | 14 | 73% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.775% | 58% | 4.83 | +259.46% |
| bull | 687 | 28% | +0.215% | 48% | 2.08 | +283.38% |
| bear | 400 | 17% | -0.153% | 42% | -2.24 | -47.52% |
| chop | 1160 | 48% | -0.093% | 38% | -1.34 | -69.27% |

## Turnover, fees, activity

- trades: 19008 (7.84/day); active days 96%
- turnover 246.3x equity/year; fees 24.63% of equity/year ($228,468 total)
- average gross exposure 0.30; brake active 50.6% of hours
- correlation of daily returns with s3v2 baseline: 0.49
