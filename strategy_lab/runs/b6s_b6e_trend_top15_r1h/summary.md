# Run: b6s_b6e_trend_top15_r1h

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'TREND', 'n_liquid': 15, 'min_history_days': 180, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -4.15% | -0.64% | 0.04 | 0.06 | -43.11% | -0.01 | 0.03 |
| in_sample | 2020-02-15 → 2024-12-31 | +2.46% | +0.50% | 0.11 | 0.17 | -43.11% | 0.01 | 0.11 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -6.44% | -3.71% | -0.23 | -0.33 | -22.51% | -0.16 | -0.25 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +5.34% | +5.34% | 0.41 | 0.61 | -22.51% | 0.24 | 0.44 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.37% | 41% | -7.57% | -8.47% | -3.31 | 14 | 99% |
| out_of_sample | 628 | -0.40% | 34% | -5.53% | -6.33% | -4.96 | 14 | 100% |
| in_sample | 1768 | -0.34% | 44% | -7.57% | -8.47% | -2.59 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.480% | 56% | 5.26 | +126.30% |
| bull | 687 | 28% | -0.000% | 41% | -0.00 | -2.33% |
| bear | 400 | 17% | -0.016% | 42% | -0.44 | -7.06% |
| chop | 1160 | 48% | -0.062% | 33% | -1.53 | -52.63% |

## Turnover, fees, activity

- trades: 11716 (4.83/day); active days 100%
- turnover 178.4x equity/year; fees 17.84% of equity/year ($61,986 total)
- average gross exposure 0.17; brake active 22.6% of hours
- correlation of daily returns with s3v2 baseline: 0.61
