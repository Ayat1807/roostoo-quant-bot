# Run: b4c_B_c4_w03_m200

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 4, 'w': 0.3, 'swap_m': 2.0, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +198.62% | +17.91% | 0.65 | 0.91 | -59.60% | 0.30 | 0.65 |
| in_sample | 2020-02-15 → 2024-12-31 | +316.50% | +33.94% | 0.98 | 1.36 | -59.54% | 0.57 | 1.01 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -28.27% | -17.22% | -0.60 | -0.84 | -41.70% | -0.41 | -0.64 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -9.17% | -9.17% | -0.29 | -0.42 | -29.50% | -0.31 | -0.35 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.62% | 44% | -15.15% | -17.44% | -1.36 | 14 | 69% |
| out_of_sample | 628 | -1.52% | 36% | -11.38% | -12.23% | -3.60 | 14 | 73% |
| in_sample | 1768 | -0.17% | 47% | -15.15% | -17.44% | -0.24 | 14 | 67% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.730% | 56% | 4.64 | +233.18% |
| bull | 687 | 28% | +0.226% | 49% | 2.18 | +313.26% |
| bear | 400 | 17% | -0.111% | 44% | -1.72 | -37.71% |
| chop | 1160 | 48% | -0.083% | 38% | -1.30 | -65.18% |

## Turnover, fees, activity

- trades: 17114 (7.06/day); active days 95%
- turnover 220.3x equity/year; fees 22.03% of equity/year ($249,318 total)
- average gross exposure 0.29; brake active 50.4% of hours
- correlation of daily returns with s3v2 baseline: 0.52
