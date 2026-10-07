# Run: b4s_b4c_A_g_S2_G75_r2h

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d'}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -70.56% | -16.82% | -0.31 | -0.43 | -95.49% | -0.18 | -0.32 |
| in_sample | 2020-02-15 → 2024-12-31 | -9.64% | -2.05% | 0.15 | 0.20 | -86.62% | -0.02 | 0.12 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -67.34% | -47.09% | -2.06 | -2.85 | -72.93% | -0.65 | -1.95 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -45.92% | -45.92% | -2.20 | -3.03 | -55.13% | -0.83 | -2.12 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -2.32% | 35% | -18.48% | -21.48% | -3.85 | 14 | 86% |
| out_of_sample | 628 | -3.50% | 25% | -15.11% | -15.55% | -6.07 | 14 | 84% |
| in_sample | 1768 | -1.85% | 38% | -18.48% | -21.48% | -2.89 | 14 | 86% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.926% | 59% | 5.15 | +358.19% |
| bull | 687 | 28% | +0.200% | 45% | 1.71 | +233.73% |
| bear | 400 | 17% | -0.344% | 34% | -4.79 | -75.71% |
| chop | 1160 | 48% | -0.209% | 35% | -2.85 | -92.07% |

## Turnover, fees, activity

- trades: 105566 (43.55/day); active days 97%
- turnover 567.3x equity/year; fees 56.73% of equity/year ($265,002 total)
- average gross exposure 0.35; brake active 52.5% of hours
- correlation of daily returns with s3v2 baseline: 0.50
