# Run: b4e_derisk_50

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +333.74% | +24.73% | 0.79 | 1.09 | -62.14% | 0.40 | 0.79 |
| in_sample | 2020-02-15 → 2024-12-31 | +418.54% | +40.09% | 1.07 | 1.46 | -62.14% | 0.65 | 1.10 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -16.65% | -9.84% | -0.23 | -0.32 | -32.32% | -0.30 | -0.29 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -2.05% | -2.05% | 0.04 | 0.06 | -25.87% | -0.08 | 0.01 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.18% | 40% | -19.43% | -20.42% | -2.45 | 12 | 32% |
| out_of_sample | 628 | -1.91% | 36% | -11.97% | -13.23% | -3.96 | 12 | 21% |
| in_sample | 1768 | -0.93% | 42% | -19.43% | -20.42% | -1.94 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.645% | 52% | 3.89 | +184.62% |
| bull | 687 | 28% | +0.274% | 51% | 2.40 | +458.37% |
| bear | 400 | 17% | -0.224% | 41% | -3.42 | -60.52% |
| chop | 1160 | 48% | -0.022% | 41% | -0.31 | -30.87% |

## Turnover, fees, activity

- trades: 14349 (5.92/day); active days 82%
- turnover 166.4x equity/year; fees 16.64% of equity/year ($250,313 total)
- average gross exposure 0.30; brake active 46.5% of hours
- correlation of daily returns with s3v2 baseline: 0.37
