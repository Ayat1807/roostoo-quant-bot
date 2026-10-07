# Run: b4s_b4d_resistance_r4h

Strategy `xsmom_entry`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'entry_filter': 'resistance'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +152.94% | +15.00% | 0.56 | 0.78 | -73.02% | 0.21 | 0.54 |
| in_sample | 2020-02-15 → 2024-12-31 | +353.33% | +36.29% | 0.98 | 1.36 | -63.30% | 0.57 | 1.01 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -44.34% | -28.34% | -1.02 | -1.41 | -56.97% | -0.50 | -1.02 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -23.48% | -23.48% | -0.93 | -1.30 | -38.90% | -0.60 | -0.98 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.20% | 41% | -16.34% | -17.93% | -2.67 | 13 | 36% |
| out_of_sample | 628 | -2.47% | 32% | -12.20% | -13.40% | -4.99 | 12 | 27% |
| in_sample | 1768 | -0.67% | 44% | -16.34% | -17.93% | -1.26 | 13 | 39% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.724% | 48% | 4.22 | +224.89% |
| bull | 687 | 28% | +0.293% | 48% | 2.41 | +520.72% |
| bear | 400 | 17% | -0.276% | 28% | -4.13 | -67.99% |
| chop | 1160 | 48% | -0.071% | 34% | -0.98 | -60.81% |

## Turnover, fees, activity

- trades: 47342 (19.53/day); active days 85%
- turnover 309.5x equity/year; fees 30.95% of equity/year ($380,330 total)
- average gross exposure 0.30; brake active 49.6% of hours
- correlation of daily returns with s3v2 baseline: 0.37
