# Run: b4c_B_c4_w03_m150

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 4, 'w': 0.3, 'swap_m': 1.5, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +235.26% | +19.98% | 0.70 | 0.98 | -58.02% | 0.34 | 0.71 |
| in_sample | 2020-02-15 → 2024-12-31 | +461.57% | +42.40% | 1.14 | 1.59 | -45.33% | 0.94 | 1.26 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -40.27% | -25.41% | -1.03 | -1.43 | -47.75% | -0.53 | -1.04 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -14.82% | -14.82% | -0.58 | -0.82 | -33.57% | -0.44 | -0.63 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.71% | 43% | -15.18% | -18.08% | -1.49 | 14 | 72% |
| out_of_sample | 628 | -2.11% | 32% | -11.83% | -11.94% | -4.70 | 14 | 75% |
| in_sample | 1768 | -0.11% | 48% | -15.18% | -18.08% | -0.07 | 14 | 70% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.735% | 56% | 4.71 | +236.55% |
| bull | 687 | 28% | +0.240% | 48% | 2.32 | +354.46% |
| bear | 400 | 17% | -0.103% | 43% | -1.54 | -35.77% |
| chop | 1160 | 48% | -0.085% | 38% | -1.27 | -65.87% |

## Turnover, fees, activity

- trades: 17756 (7.33/day); active days 95%
- turnover 223.0x equity/year; fees 22.30% of equity/year ($302,796 total)
- average gross exposure 0.29; brake active 51.5% of hours
- correlation of daily returns with s3v2 baseline: 0.52
