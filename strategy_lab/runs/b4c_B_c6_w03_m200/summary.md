# Run: b4c_B_c6_w03_m200

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 6, 'w': 0.3, 'swap_m': 2.0, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +207.09% | +18.41% | 0.66 | 0.91 | -65.42% | 0.28 | 0.65 |
| in_sample | 2020-02-15 → 2024-12-31 | +398.05% | +38.94% | 1.07 | 1.48 | -54.65% | 0.71 | 1.13 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -38.31% | -24.03% | -0.87 | -1.21 | -52.78% | -0.46 | -0.88 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -10.58% | -10.58% | -0.32 | -0.45 | -33.25% | -0.32 | -0.37 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.85% | 42% | -14.62% | -17.79% | -1.87 | 14 | 78% |
| out_of_sample | 628 | -1.92% | 35% | -11.17% | -12.53% | -4.16 | 14 | 82% |
| in_sample | 1768 | -0.46% | 45% | -14.62% | -17.79% | -1.02 | 14 | 76% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.766% | 56% | 4.84 | +254.29% |
| bull | 687 | 28% | +0.241% | 49% | 2.30 | +356.87% |
| bear | 400 | 17% | -0.153% | 43% | -2.32 | -47.49% |
| chop | 1160 | 48% | -0.079% | 38% | -1.11 | -63.87% |

## Turnover, fees, activity

- trades: 17864 (7.37/day); active days 96%
- turnover 223.6x equity/year; fees 22.36% of equity/year ($306,311 total)
- average gross exposure 0.30; brake active 52.4% of hours
- correlation of daily returns with s3v2 baseline: 0.50
