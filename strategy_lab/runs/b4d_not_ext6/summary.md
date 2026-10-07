# Run: b4d_not_ext6

Strategy `xsmom_entry`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'entry_filter': 'not_extended', 'ext': 0.06}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +161.74% | +15.59% | 0.78 | 1.07 | -38.14% | 0.41 | 0.78 |
| in_sample | 2020-02-15 → 2024-12-31 | +223.11% | +27.15% | 1.17 | 1.60 | -31.41% | 0.86 | 1.25 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -19.19% | -11.42% | -0.58 | -0.82 | -30.78% | -0.37 | -0.61 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +0.48% | +0.48% | 0.12 | 0.17 | -21.80% | 0.02 | 0.11 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.82% | 38% | -8.28% | -10.31% | -3.19 | 9 | 10% |
| out_of_sample | 628 | -1.31% | 33% | -7.49% | -7.79% | -5.23 | 10 | 8% |
| in_sample | 1768 | -0.61% | 40% | -8.28% | -10.31% | -2.46 | 9 | 11% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.379% | 32% | 3.64 | +88.28% |
| bull | 687 | 28% | +0.197% | 43% | 2.63 | +259.73% |
| bear | 400 | 17% | -0.119% | 19% | -3.09 | -38.62% |
| chop | 1160 | 48% | -0.036% | 31% | -0.75 | -37.04% |

## Turnover, fees, activity

- trades: 6764 (2.79/day); active days 64%
- turnover 84.8x equity/year; fees 8.48% of equity/year ($74,288 total)
- average gross exposure 0.19; brake active 30.9% of hours
- correlation of daily returns with s3v2 baseline: 0.44
