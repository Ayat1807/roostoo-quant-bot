# Run: b4d_pullback

Strategy `xsmom_entry`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'entry_filter': 'pullback'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +11.03% | +1.59% | 0.19 | 0.26 | -71.10% | 0.02 | 0.17 |
| in_sample | 2020-02-15 → 2024-12-31 | +127.94% | +18.38% | 0.73 | 1.00 | -48.10% | 0.38 | 0.73 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -51.29% | -33.58% | -2.05 | -2.75 | -54.89% | -0.61 | -1.90 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -27.40% | -27.40% | -1.83 | -2.49 | -35.05% | -0.78 | -1.78 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.24% | 32% | -14.14% | -15.91% | -3.74 | 9 | 11% |
| out_of_sample | 628 | -1.89% | 23% | -8.47% | -10.11% | -6.24 | 9 | 2% |
| in_sample | 1768 | -0.99% | 36% | -14.14% | -15.91% | -2.76 | 10 | 14% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.366% | 43% | 3.18 | +82.50% |
| bull | 687 | 28% | +0.124% | 43% | 1.46 | +114.13% |
| bear | 400 | 17% | -0.188% | 23% | -4.13 | -53.61% |
| chop | 1160 | 48% | -0.036% | 30% | -0.63 | -38.75% |

## Turnover, fees, activity

- trades: 8152 (3.36/day); active days 66%
- turnover 101.0x equity/year; fees 10.10% of equity/year ($70,405 total)
- average gross exposure 0.18; brake active 38.7% of hours
- correlation of daily returns with s3v2 baseline: 0.36
