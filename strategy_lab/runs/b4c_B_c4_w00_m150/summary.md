# Run: b4c_B_c4_w00_m150

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 4, 'w': 0.0, 'swap_m': 1.5, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +328.49% | +24.50% | 0.81 | 1.13 | -53.18% | 0.46 | 0.83 |
| in_sample | 2020-02-15 → 2024-12-31 | +513.44% | +45.00% | 1.19 | 1.66 | -53.18% | 0.85 | 1.28 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -30.12% | -18.44% | -0.65 | -0.91 | -43.63% | -0.42 | -0.69 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -2.57% | -2.57% | 0.01 | 0.01 | -27.30% | -0.09 | -0.02 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.67% | 43% | -15.29% | -17.67% | -1.38 | 14 | 70% |
| out_of_sample | 628 | -1.69% | 34% | -11.24% | -12.38% | -4.09 | 14 | 71% |
| in_sample | 1768 | -0.26% | 46% | -15.29% | -17.67% | -0.44 | 14 | 70% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.737% | 55% | 4.45 | +234.35% |
| bull | 687 | 28% | +0.257% | 47% | 2.45 | +409.75% |
| bear | 400 | 17% | -0.080% | 43% | -1.25 | -29.56% |
| chop | 1160 | 48% | -0.081% | 38% | -1.21 | -64.31% |

## Turnover, fees, activity

- trades: 17023 (7.02/day); active days 95%
- turnover 214.9x equity/year; fees 21.49% of equity/year ($300,038 total)
- average gross exposure 0.29; brake active 49.0% of hours
- correlation of daily returns with s3v2 baseline: 0.52
