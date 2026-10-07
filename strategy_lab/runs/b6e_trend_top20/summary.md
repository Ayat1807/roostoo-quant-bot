# Run: b6e_trend_top20

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'TREND', 'n_liquid': 20, 'min_history_days': 180, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +79.76% | +9.23% | 0.63 | 0.93 | -22.44% | 0.41 | 0.68 |
| in_sample | 2020-02-15 → 2024-12-31 | +67.36% | +11.12% | 0.70 | 1.04 | -22.44% | 0.50 | 0.78 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +7.46% | +4.18% | 0.38 | 0.56 | -12.76% | 0.33 | 0.44 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +18.59% | +18.59% | 1.21 | 1.79 | -12.76% | 1.46 | 1.52 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.32% | 42% | -7.22% | -8.74% | -2.55 | 14 | 91% |
| out_of_sample | 628 | -0.32% | 37% | -5.00% | -6.28% | -3.95 | 14 | 100% |
| in_sample | 1768 | -0.32% | 45% | -7.22% | -8.74% | -1.82 | 14 | 88% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.328% | 53% | 3.54 | +73.21% |
| bull | 687 | 28% | +0.060% | 50% | 1.49 | +47.56% |
| bear | 400 | 17% | +0.018% | 45% | 0.49 | +6.43% |
| chop | 1160 | 48% | -0.032% | 39% | -0.81 | -33.08% |

## Turnover, fees, activity

- trades: 4377 (1.81/day); active days 99%
- turnover 55.2x equity/year; fees 5.52% of equity/year ($24,663 total)
- average gross exposure 0.19; brake active 14.6% of hours
- correlation of daily returns with s3v2 baseline: 0.69
