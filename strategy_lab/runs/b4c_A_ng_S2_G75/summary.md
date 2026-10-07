# Run: b4c_A_ng_S2_G75

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'none'}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +51.63% | +6.47% | 0.35 | 0.49 | -73.14% | 0.09 | 0.33 |
| in_sample | 2020-02-15 → 2024-12-31 | +205.65% | +25.72% | 0.81 | 1.12 | -57.98% | 0.44 | 0.82 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -50.47% | -32.95% | -1.26 | -1.78 | -55.14% | -0.60 | -1.27 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -18.53% | -18.53% | -0.67 | -0.95 | -36.91% | -0.50 | -0.73 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.02% | 42% | -19.94% | -22.83% | -1.89 | 14 | 98% |
| out_of_sample | 628 | -2.02% | 34% | -14.29% | -17.27% | -4.19 | 14 | 100% |
| in_sample | 1768 | -0.50% | 45% | -19.94% | -22.83% | -0.86 | 14 | 97% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.543% | 53% | 3.41 | +139.78% |
| bull | 687 | 28% | +0.173% | 50% | 1.59 | +184.13% |
| bear | 400 | 17% | -0.122% | 45% | -1.91 | -40.45% |
| chop | 1160 | 48% | -0.076% | 41% | -1.08 | -62.63% |

## Turnover, fees, activity

- trades: 20383 (8.41/day); active days 98%
- turnover 236.5x equity/year; fees 23.65% of equity/year ($205,021 total)
- average gross exposure 0.39; brake active 51.1% of hours
- correlation of daily returns with s3v2 baseline: 0.48
