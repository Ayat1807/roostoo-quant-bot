# Run: b4d_patient_limit

Strategy `xsmom_entry`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'entry_filter': 'none'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +138.06% | +13.95% | 0.55 | 0.76 | -71.44% | 0.20 | 0.53 |
| in_sample | 2020-02-15 → 2024-12-31 | +347.42% | +35.92% | 1.01 | 1.39 | -61.98% | 0.58 | 1.04 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -46.98% | -30.30% | -1.35 | -1.82 | -51.97% | -0.58 | -1.31 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -27.98% | -27.98% | -1.41 | -1.89 | -34.83% | -0.80 | -1.42 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.14% | 41% | -18.83% | -18.83% | -2.46 | 12 | 24% |
| out_of_sample | 628 | -2.43% | 34% | -11.81% | -13.59% | -5.85 | 11 | 13% |
| in_sample | 1768 | -0.63% | 43% | -18.83% | -18.83% | -1.35 | 12 | 28% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.556% | 45% | 3.42 | +144.47% |
| bull | 687 | 28% | +0.204% | 50% | 1.95 | +254.88% |
| bear | 400 | 17% | -0.230% | 32% | -3.87 | -61.15% |
| chop | 1160 | 48% | -0.022% | 35% | -0.33 | -29.36% |

## Turnover, fees, activity

- trades: 12418 (5.12/day); active days 79%
- turnover 156.9x equity/year; fees 13.04% of equity/year ($166,403 total)
- average gross exposure 0.25; brake active 42.6% of hours
- correlation of daily returns with s3v2 baseline: 0.34
