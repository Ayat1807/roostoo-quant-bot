# Run: b4c_A_g_S3_G75

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 3, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d'}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +183.67% | +17.00% | 0.60 | 0.84 | -73.05% | 0.23 | 0.59 |
| in_sample | 2020-02-15 → 2024-12-31 | +459.51% | +42.29% | 1.07 | 1.49 | -59.51% | 0.71 | 1.13 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -49.30% | -32.05% | -1.14 | -1.58 | -55.54% | -0.58 | -1.15 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -18.70% | -18.70% | -0.64 | -0.90 | -38.72% | -0.48 | -0.70 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.08% | 41% | -21.46% | -23.19% | -1.87 | 14 | 76% |
| out_of_sample | 628 | -2.40% | 31% | -12.83% | -14.96% | -4.60 | 14 | 68% |
| in_sample | 1768 | -0.50% | 44% | -21.46% | -23.19% | -0.78 | 14 | 79% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.731% | 53% | 3.92 | +223.87% |
| bull | 687 | 28% | +0.262% | 48% | 2.29 | +413.72% |
| bear | 400 | 17% | -0.134% | 44% | -1.75 | -43.94% |
| chop | 1160 | 48% | -0.093% | 38% | -1.25 | -69.59% |

## Turnover, fees, activity

- trades: 19281 (7.95/day); active days 95%
- turnover 232.4x equity/year; fees 23.24% of equity/year ($357,565 total)
- average gross exposure 0.38; brake active 52.5% of hours
- correlation of daily returns with s3v2 baseline: 0.53
