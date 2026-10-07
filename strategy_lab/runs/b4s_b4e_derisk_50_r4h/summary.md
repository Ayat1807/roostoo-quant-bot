# Run: b4s_b4e_derisk_50_r4h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +228.43% | +19.61% | 0.67 | 0.93 | -66.56% | 0.29 | 0.66 |
| in_sample | 2020-02-15 → 2024-12-31 | +413.84% | +39.83% | 1.05 | 1.46 | -64.90% | 0.61 | 1.08 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -36.24% | -22.59% | -0.75 | -1.04 | -51.35% | -0.44 | -0.77 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -16.83% | -16.83% | -0.59 | -0.83 | -34.31% | -0.49 | -0.66 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.09% | 41% | -16.09% | -17.92% | -2.34 | 13 | 36% |
| out_of_sample | 628 | -2.12% | 36% | -12.20% | -13.39% | -4.44 | 12 | 27% |
| in_sample | 1768 | -0.63% | 44% | -16.09% | -17.92% | -1.24 | 13 | 39% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.751% | 50% | 4.46 | +241.55% |
| bull | 687 | 28% | +0.302% | 50% | 2.47 | +559.02% |
| bear | 400 | 17% | -0.278% | 29% | -4.20 | -68.14% |
| chop | 1160 | 48% | -0.058% | 36% | -0.79 | -54.20% |

## Turnover, fees, activity

- trades: 47371 (19.54/day); active days 85%
- turnover 307.9x equity/year; fees 30.79% of equity/year ($409,164 total)
- average gross exposure 0.30; brake active 48.4% of hours
- correlation of daily returns with s3v2 baseline: 0.37
