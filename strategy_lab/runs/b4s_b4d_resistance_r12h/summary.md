# Run: b4s_b4d_resistance_r12h

Strategy `xsmom_entry`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'entry_filter': 'resistance'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +86.36% | +9.83% | 0.44 | 0.60 | -83.84% | 0.12 | 0.41 |
| in_sample | 2020-02-15 → 2024-12-31 | +163.54% | +21.96% | 0.70 | 0.96 | -75.07% | 0.29 | 0.68 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -29.54% | -18.06% | -0.56 | -0.78 | -49.54% | -0.36 | -0.59 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -9.42% | -9.42% | -0.25 | -0.35 | -31.29% | -0.30 | -0.31 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.27% | 39% | -18.50% | -19.40% | -2.72 | 12 | 33% |
| out_of_sample | 628 | -2.12% | 36% | -11.82% | -14.14% | -4.56 | 12 | 23% |
| in_sample | 1768 | -0.94% | 41% | -18.50% | -19.40% | -2.16 | 13 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.516% | 44% | 3.05 | +126.05% |
| bull | 687 | 28% | +0.241% | 46% | 2.04 | +339.89% |
| bear | 400 | 17% | -0.276% | 27% | -3.91 | -68.01% |
| chop | 1160 | 48% | -0.037% | 34% | -0.50 | -41.41% |

## Turnover, fees, activity

- trades: 21701 (8.95/day); active days 83%
- turnover 219.2x equity/year; fees 21.92% of equity/year ($226,280 total)
- average gross exposure 0.30; brake active 49.4% of hours
- correlation of daily returns with s3v2 baseline: 0.36
