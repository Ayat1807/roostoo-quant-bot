# Run: b4c_B_c4_w00_m125

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 4, 'w': 0.0, 'swap_m': 1.25, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +319.11% | +24.09% | 0.80 | 1.12 | -52.55% | 0.46 | 0.82 |
| in_sample | 2020-02-15 → 2024-12-31 | +491.21% | +43.91% | 1.17 | 1.63 | -52.07% | 0.84 | 1.26 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -29.08% | -17.75% | -0.62 | -0.87 | -39.63% | -0.45 | -0.67 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +3.92% | +3.92% | 0.28 | 0.40 | -23.28% | 0.17 | 0.30 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.79% | 42% | -14.87% | -18.19% | -1.70 | 14 | 68% |
| out_of_sample | 628 | -1.94% | 33% | -10.96% | -11.87% | -4.18 | 14 | 70% |
| in_sample | 1768 | -0.30% | 46% | -14.87% | -18.19% | -0.56 | 14 | 67% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.768% | 56% | 4.61 | +252.93% |
| bull | 687 | 28% | +0.279% | 48% | 2.63 | +491.90% |
| bear | 400 | 17% | -0.082% | 43% | -1.37 | -29.83% |
| chop | 1160 | 48% | -0.100% | 38% | -1.53 | -71.41% |

## Turnover, fees, activity

- trades: 17765 (7.33/day); active days 95%
- turnover 220.9x equity/year; fees 22.09% of equity/year ($318,535 total)
- average gross exposure 0.29; brake active 51.3% of hours
- correlation of daily returns with s3v2 baseline: 0.52
