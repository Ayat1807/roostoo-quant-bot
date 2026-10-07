# Run: b4s_b4e_derisk_50_r2h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +50.80% | +6.38% | 0.35 | 0.49 | -84.10% | 0.08 | 0.32 |
| in_sample | 2020-02-15 → 2024-12-31 | +141.28% | +19.77% | 0.66 | 0.91 | -79.22% | 0.25 | 0.64 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -37.65% | -23.56% | -0.81 | -1.13 | -52.61% | -0.45 | -0.83 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -20.55% | -20.55% | -0.77 | -1.08 | -37.38% | -0.55 | -0.83 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.64% | 38% | -20.68% | -21.58% | -3.26 | 13 | 37% |
| out_of_sample | 628 | -2.42% | 32% | -12.92% | -13.65% | -5.10 | 13 | 28% |
| in_sample | 1768 | -1.30% | 40% | -20.68% | -21.58% | -2.57 | 13 | 40% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.812% | 52% | 4.60 | +276.84% |
| bull | 687 | 28% | +0.242% | 46% | 2.04 | +343.34% |
| bear | 400 | 17% | -0.268% | 30% | -3.93 | -66.92% |
| chop | 1160 | 48% | -0.102% | 35% | -1.42 | -72.71% |

## Turnover, fees, activity

- trades: 83841 (34.59/day); active days 85%
- turnover 406.3x equity/year; fees 40.63% of equity/year ($354,978 total)
- average gross exposure 0.29; brake active 51.2% of hours
- correlation of daily returns with s3v2 baseline: 0.37
