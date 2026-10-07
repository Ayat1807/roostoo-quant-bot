# Run: b4c_B_c6_w00_m125

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 6, 'w': 0.0, 'swap_m': 1.25, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +155.09% | +15.15% | 0.58 | 0.80 | -68.15% | 0.22 | 0.56 |
| in_sample | 2020-02-15 → 2024-12-31 | +359.12% | +36.64% | 1.02 | 1.41 | -56.56% | 0.65 | 1.06 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -44.41% | -28.40% | -1.14 | -1.58 | -52.83% | -0.54 | -1.13 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -10.74% | -10.74% | -0.35 | -0.51 | -31.95% | -0.34 | -0.41 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.79% | 43% | -15.74% | -17.63% | -1.81 | 14 | 77% |
| out_of_sample | 628 | -2.22% | 31% | -12.35% | -13.32% | -4.80 | 14 | 79% |
| in_sample | 1768 | -0.04% | 48% | -15.74% | -17.63% | 0.00 | 14 | 76% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.670% | 55% | 4.18 | +198.86% |
| bull | 687 | 28% | +0.239% | 49% | 2.24 | +347.33% |
| bear | 400 | 17% | -0.136% | 43% | -2.05 | -43.88% |
| chop | 1160 | 48% | -0.084% | 36% | -1.18 | -66.00% |

## Turnover, fees, activity

- trades: 18223 (7.52/day); active days 95%
- turnover 229.6x equity/year; fees 22.96% of equity/year ($282,799 total)
- average gross exposure 0.30; brake active 50.7% of hours
- correlation of daily returns with s3v2 baseline: 0.50
