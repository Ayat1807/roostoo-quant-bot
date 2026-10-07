# Run: b4c_B_c2_w05_m200

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 2, 'w': 0.5, 'swap_m': 2.0, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +320.34% | +24.14% | 0.82 | 1.16 | -50.93% | 0.47 | 0.85 |
| in_sample | 2020-02-15 → 2024-12-31 | +385.41% | +38.21% | 1.10 | 1.54 | -39.46% | 0.97 | 1.23 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -13.30% | -7.80% | -0.19 | -0.28 | -30.12% | -0.26 | -0.25 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -3.06% | -3.06% | -0.01 | -0.02 | -28.19% | -0.11 | -0.05 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.60% | 43% | -13.08% | -14.03% | -1.39 | 14 | 63% |
| out_of_sample | 628 | -1.38% | 36% | -12.36% | -12.36% | -3.22 | 14 | 68% |
| in_sample | 1768 | -0.21% | 46% | -13.08% | -14.03% | -0.37 | 14 | 62% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.716% | 55% | 4.86 | +228.27% |
| bull | 687 | 28% | +0.225% | 48% | 2.19 | +311.84% |
| bear | 400 | 17% | -0.037% | 42% | -0.55 | -16.44% |
| chop | 1160 | 48% | -0.077% | 37% | -1.18 | -62.79% |

## Turnover, fees, activity

- trades: 16591 (6.84/day); active days 95%
- turnover 222.8x equity/year; fees 22.28% of equity/year ($335,370 total)
- average gross exposure 0.26; brake active 50.7% of hours
- correlation of daily returns with s3v2 baseline: 0.50
