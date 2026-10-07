# Run: b4s_b4d_resistance_r2h

Strategy `xsmom_entry`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'entry_filter': 'resistance'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +13.45% | +1.92% | 0.24 | 0.33 | -87.64% | 0.02 | 0.21 |
| in_sample | 2020-02-15 → 2024-12-31 | +126.93% | +18.28% | 0.63 | 0.87 | -78.95% | 0.23 | 0.60 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -50.12% | -32.68% | -1.24 | -1.72 | -61.49% | -0.53 | -1.22 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -25.94% | -25.94% | -1.02 | -1.43 | -41.70% | -0.62 | -1.07 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.81% | 37% | -18.70% | -19.63% | -3.46 | 13 | 37% |
| out_of_sample | 628 | -2.71% | 27% | -12.92% | -13.65% | -5.19 | 13 | 28% |
| in_sample | 1768 | -1.30% | 40% | -18.70% | -19.63% | -2.59 | 13 | 40% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.799% | 52% | 4.56 | +268.89% |
| bull | 687 | 28% | +0.242% | 45% | 2.03 | +341.57% |
| bear | 400 | 17% | -0.277% | 31% | -4.11 | -68.14% |
| chop | 1160 | 48% | -0.122% | 33% | -1.70 | -78.14% |

## Turnover, fees, activity

- trades: 83184 (34.32/day); active days 85%
- turnover 404.8x equity/year; fees 40.48% of equity/year ($324,261 total)
- average gross exposure 0.29; brake active 52.3% of hours
- correlation of daily returns with s3v2 baseline: 0.36
