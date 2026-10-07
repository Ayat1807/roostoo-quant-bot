# Run: b4c_B_c2_w05_m125

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 2, 'w': 0.5, 'swap_m': 1.25, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +234.34% | +19.93% | 0.71 | 1.01 | -45.24% | 0.44 | 0.75 |
| in_sample | 2020-02-15 → 2024-12-31 | +286.63% | +31.92% | 0.96 | 1.35 | -45.24% | 0.71 | 1.04 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -13.42% | -7.87% | -0.18 | -0.26 | -32.20% | -0.24 | -0.23 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +4.27% | +4.27% | 0.29 | 0.42 | -26.29% | 0.16 | 0.31 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.61% | 43% | -19.25% | -23.15% | -1.38 | 14 | 67% |
| out_of_sample | 628 | -1.39% | 40% | -12.36% | -12.36% | -3.65 | 14 | 71% |
| in_sample | 1768 | -0.38% | 44% | -19.25% | -23.15% | -0.81 | 14 | 65% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.707% | 56% | 4.82 | +223.04% |
| bull | 687 | 28% | +0.211% | 48% | 2.14 | +276.56% |
| bear | 400 | 17% | -0.080% | 42% | -1.22 | -29.70% |
| chop | 1160 | 48% | -0.073% | 37% | -1.08 | -60.91% |

## Turnover, fees, activity

- trades: 17749 (7.32/day); active days 95%
- turnover 240.1x equity/year; fees 24.01% of equity/year ($233,061 total)
- average gross exposure 0.26; brake active 51.6% of hours
- correlation of daily returns with s3v2 baseline: 0.50
