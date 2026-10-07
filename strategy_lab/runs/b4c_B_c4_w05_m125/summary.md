# Run: b4c_B_c4_w05_m125

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 4, 'w': 0.5, 'swap_m': 1.25, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +239.02% | +20.19% | 0.70 | 0.98 | -54.03% | 0.37 | 0.71 |
| in_sample | 2020-02-15 → 2024-12-31 | +319.16% | +34.12% | 0.97 | 1.35 | -52.84% | 0.65 | 1.03 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -19.08% | -11.35% | -0.32 | -0.45 | -36.72% | -0.31 | -0.37 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +3.01% | +3.01% | 0.24 | 0.35 | -25.52% | 0.12 | 0.25 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.75% | 43% | -14.00% | -18.23% | -1.63 | 14 | 73% |
| out_of_sample | 628 | -1.73% | 37% | -11.54% | -12.95% | -3.78 | 14 | 79% |
| in_sample | 1768 | -0.33% | 46% | -14.00% | -18.23% | -0.75 | 14 | 71% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.617% | 54% | 3.81 | +171.93% |
| bull | 687 | 28% | +0.263% | 51% | 2.44 | +426.68% |
| bear | 400 | 17% | -0.118% | 41% | -1.76 | -39.60% |
| chop | 1160 | 48% | -0.073% | 36% | -1.08 | -60.81% |

## Turnover, fees, activity

- trades: 18581 (7.67/day); active days 96%
- turnover 244.8x equity/year; fees 24.48% of equity/year ($273,887 total)
- average gross exposure 0.29; brake active 49.5% of hours
- correlation of daily returns with s3v2 baseline: 0.50
