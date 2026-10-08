# Run: b6s_b6e_trend_top15_r6h

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'TREND', 'n_liquid': 15, 'min_history_days': 180, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +67.34% | +8.06% | 0.56 | 0.83 | -27.73% | 0.29 | 0.59 |
| in_sample | 2020-02-15 → 2024-12-31 | +60.20% | +10.13% | 0.65 | 0.96 | -27.73% | 0.37 | 0.69 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +4.46% | +2.51% | 0.26 | 0.38 | -19.14% | 0.13 | 0.27 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +11.96% | +11.96% | 0.82 | 1.21 | -19.14% | 0.62 | 0.92 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.30% | 42% | -7.48% | -7.54% | -2.47 | 14 | 94% |
| out_of_sample | 628 | -0.42% | 36% | -5.16% | -5.83% | -4.35 | 14 | 100% |
| in_sample | 1768 | -0.23% | 45% | -7.48% | -7.54% | -1.58 | 14 | 92% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.446% | 56% | 5.01 | +113.47% |
| bull | 687 | 28% | +0.036% | 46% | 0.87 | +25.71% |
| bear | 400 | 17% | +0.001% | 45% | 0.04 | -0.40% |
| chop | 1160 | 48% | -0.037% | 38% | -0.92 | -37.20% |

## Turnover, fees, activity

- trades: 6228 (2.57/day); active days 99%
- turnover 88.8x equity/year; fees 8.88% of equity/year ($42,016 total)
- average gross exposure 0.18; brake active 17.2% of hours
- correlation of daily returns with s3v2 baseline: 0.63
