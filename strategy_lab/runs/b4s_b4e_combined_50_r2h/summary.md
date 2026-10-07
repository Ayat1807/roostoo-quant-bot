# Run: b4s_b4e_combined_50_r2h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +50.74% | +6.38% | 0.35 | 0.49 | -83.80% | 0.08 | 0.32 |
| in_sample | 2020-02-15 → 2024-12-31 | +144.47% | +20.09% | 0.66 | 0.92 | -78.88% | 0.25 | 0.64 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -38.48% | -24.15% | -0.83 | -1.16 | -52.94% | -0.46 | -0.85 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -21.78% | -21.78% | -0.83 | -1.16 | -37.86% | -0.58 | -0.89 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.63% | 38% | -20.68% | -21.58% | -3.26 | 13 | 37% |
| out_of_sample | 628 | -2.47% | 32% | -12.92% | -13.65% | -5.13 | 13 | 28% |
| in_sample | 1768 | -1.29% | 40% | -20.68% | -21.58% | -2.55 | 13 | 40% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.814% | 52% | 4.61 | +278.15% |
| bull | 687 | 28% | +0.243% | 45% | 2.05 | +344.90% |
| bear | 400 | 17% | -0.272% | 28% | -4.00 | -67.48% |
| chop | 1160 | 48% | -0.101% | 33% | -1.39 | -72.45% |

## Turnover, fees, activity

- trades: 83837 (34.59/day); active days 85%
- turnover 407.8x equity/year; fees 40.78% of equity/year ($357,050 total)
- average gross exposure 0.29; brake active 51.1% of hours
- correlation of daily returns with s3v2 baseline: 0.37
