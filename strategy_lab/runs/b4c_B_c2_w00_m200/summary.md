# Run: b4c_B_c2_w00_m200

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 2, 'w': 0.0, 'swap_m': 2.0, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +113.94% | +12.14% | 0.51 | 0.72 | -52.95% | 0.23 | 0.51 |
| in_sample | 2020-02-15 → 2024-12-31 | +138.44% | +19.48% | 0.69 | 0.95 | -52.95% | 0.37 | 0.70 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -10.22% | -5.95% | -0.11 | -0.16 | -30.09% | -0.20 | -0.16 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -4.19% | -4.19% | -0.07 | -0.10 | -29.36% | -0.14 | -0.11 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.86% | 42% | -14.45% | -16.63% | -1.85 | 14 | 64% |
| out_of_sample | 628 | -1.27% | 37% | -12.24% | -12.95% | -3.43 | 14 | 67% |
| in_sample | 1768 | -0.54% | 43% | -14.45% | -16.63% | -1.27 | 14 | 63% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.579% | 53% | 3.73 | +156.39% |
| bull | 687 | 28% | +0.197% | 48% | 2.02 | +243.76% |
| bear | 400 | 17% | -0.120% | 42% | -1.87 | -39.87% |
| chop | 1160 | 48% | -0.071% | 38% | -1.11 | -59.63% |

## Turnover, fees, activity

- trades: 15365 (6.34/day); active days 94%
- turnover 197.3x equity/year; fees 19.73% of equity/year ($138,190 total)
- average gross exposure 0.26; brake active 51.8% of hours
- correlation of daily returns with s3v2 baseline: 0.50
