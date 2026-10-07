# Run: b4c_B_c4_w00_m200

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 4, 'w': 0.0, 'swap_m': 2.0, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +511.64% | +31.36% | 0.96 | 1.35 | -51.10% | 0.61 | 1.01 |
| in_sample | 2020-02-15 → 2024-12-31 | +699.82% | +53.09% | 1.34 | 1.87 | -51.10% | 1.04 | 1.46 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -23.49% | -14.13% | -0.45 | -0.63 | -40.01% | -0.35 | -0.49 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +1.68% | +1.68% | 0.19 | 0.27 | -26.60% | 0.06 | 0.18 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.56% | 44% | -15.06% | -18.53% | -1.19 | 14 | 71% |
| out_of_sample | 628 | -1.46% | 35% | -11.00% | -12.15% | -3.47 | 14 | 76% |
| in_sample | 1768 | -0.16% | 47% | -15.06% | -18.53% | -0.15 | 14 | 69% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.782% | 56% | 4.66 | +260.93% |
| bull | 687 | 28% | +0.253% | 48% | 2.37 | +392.22% |
| bear | 400 | 17% | -0.095% | 43% | -1.49 | -33.77% |
| chop | 1160 | 48% | -0.048% | 40% | -0.70 | -48.02% |

## Turnover, fees, activity

- trades: 16400 (6.77/day); active days 95%
- turnover 205.3x equity/year; fees 20.53% of equity/year ($370,731 total)
- average gross exposure 0.29; brake active 49.6% of hours
- correlation of daily returns with s3v2 baseline: 0.52
