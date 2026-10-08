# Run: b6s_b6e_trend_top15_r2h

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'TREND', 'n_liquid': 15, 'min_history_days': 180, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +36.66% | +4.82% | 0.37 | 0.56 | -34.28% | 0.14 | 0.38 |
| in_sample | 2020-02-15 → 2024-12-31 | +38.34% | +6.87% | 0.47 | 0.71 | -34.28% | 0.20 | 0.49 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -1.20% | -0.68% | 0.01 | 0.02 | -19.68% | -0.03 | 0.00 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +7.29% | +7.29% | 0.52 | 0.78 | -19.68% | 0.37 | 0.58 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.36% | 42% | -7.45% | -7.45% | -3.02 | 14 | 98% |
| out_of_sample | 628 | -0.47% | 35% | -5.23% | -6.18% | -4.31 | 14 | 100% |
| in_sample | 1768 | -0.31% | 45% | -7.45% | -7.45% | -2.04 | 14 | 97% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.498% | 57% | 5.34 | +133.26% |
| bull | 687 | 28% | +0.020% | 43% | 0.48 | +12.29% |
| bear | 400 | 17% | -0.007% | 41% | -0.19 | -3.88% |
| chop | 1160 | 48% | -0.049% | 35% | -1.23 | -44.90% |

## Turnover, fees, activity

- trades: 9122 (3.76/day); active days 100%
- turnover 134.4x equity/year; fees 13.44% of equity/year ($57,693 total)
- average gross exposure 0.18; brake active 20.9% of hours
- correlation of daily returns with s3v2 baseline: 0.63
