# Run: b4c_B_c6_w05_m150

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 6, 'w': 0.5, 'swap_m': 1.5, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +150.89% | +14.86% | 0.57 | 0.79 | -58.02% | 0.26 | 0.57 |
| in_sample | 2020-02-15 → 2024-12-31 | +252.93% | +29.47% | 0.88 | 1.22 | -47.06% | 0.63 | 0.94 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -28.88% | -17.62% | -0.59 | -0.83 | -39.91% | -0.44 | -0.64 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -9.22% | -9.22% | -0.27 | -0.38 | -31.03% | -0.30 | -0.32 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.77% | 43% | -13.31% | -17.64% | -1.45 | 14 | 79% |
| out_of_sample | 628 | -2.46% | 32% | -12.43% | -13.87% | -5.27 | 14 | 86% |
| in_sample | 1768 | -0.21% | 47% | -13.31% | -17.64% | -0.26 | 14 | 76% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.757% | 59% | 4.66 | +247.50% |
| bull | 687 | 28% | +0.204% | 48% | 1.99 | +257.08% |
| bear | 400 | 17% | -0.133% | 42% | -1.97 | -43.27% |
| chop | 1160 | 48% | -0.080% | 38% | -1.18 | -64.36% |

## Turnover, fees, activity

- trades: 18469 (7.62/day); active days 96%
- turnover 238.5x equity/year; fees 23.85% of equity/year ($246,005 total)
- average gross exposure 0.30; brake active 50.2% of hours
- correlation of daily returns with s3v2 baseline: 0.49
