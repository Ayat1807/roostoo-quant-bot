# Run: b4c_B_c2_w03_m200

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 2, 'w': 0.3, 'swap_m': 2.0, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +157.08% | +15.28% | 0.60 | 0.84 | -44.47% | 0.34 | 0.62 |
| in_sample | 2020-02-15 → 2024-12-31 | +204.32% | +25.60% | 0.83 | 1.15 | -44.47% | 0.58 | 0.88 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -15.42% | -9.09% | -0.24 | -0.34 | -31.28% | -0.29 | -0.30 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -0.83% | -0.83% | 0.08 | 0.12 | -27.01% | -0.03 | 0.06 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.77% | 43% | -14.97% | -18.33% | -1.77 | 14 | 65% |
| out_of_sample | 628 | -1.25% | 39% | -11.57% | -11.74% | -3.31 | 14 | 66% |
| in_sample | 1768 | -0.43% | 45% | -14.97% | -18.33% | -0.97 | 14 | 64% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.663% | 53% | 4.49 | +198.88% |
| bull | 687 | 28% | +0.232% | 48% | 2.27 | +331.83% |
| bear | 400 | 17% | -0.101% | 42% | -1.61 | -35.23% |
| chop | 1160 | 48% | -0.095% | 37% | -1.53 | -69.25% |

## Turnover, fees, activity

- trades: 15909 (6.56/day); active days 95%
- turnover 208.3x equity/year; fees 20.83% of equity/year ($179,312 total)
- average gross exposure 0.26; brake active 51.9% of hours
- correlation of daily returns with s3v2 baseline: 0.49
