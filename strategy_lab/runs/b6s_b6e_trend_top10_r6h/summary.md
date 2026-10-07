# Run: b6s_b6e_trend_top10_r6h

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'TREND', 'n_liquid': 10, 'min_history_days': 180, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +64.74% | +7.81% | 0.55 | 0.81 | -27.73% | 0.28 | 0.57 |
| in_sample | 2020-02-15 → 2024-12-31 | +59.15% | +9.99% | 0.64 | 0.95 | -27.73% | 0.36 | 0.68 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +3.58% | +2.02% | 0.22 | 0.32 | -19.14% | 0.11 | 0.22 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +11.58% | +11.58% | 0.79 | 1.17 | -19.14% | 0.60 | 0.89 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.34% | 42% | -7.48% | -7.54% | -2.31 | 14 | 94% |
| out_of_sample | 628 | -0.51% | 35% | -5.16% | -5.83% | -4.26 | 14 | 100% |
| in_sample | 1768 | -0.25% | 45% | -7.48% | -7.54% | -1.36 | 14 | 92% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.439% | 55% | 4.90 | +110.83% |
| bull | 687 | 28% | +0.039% | 46% | 0.93 | +28.10% |
| bear | 400 | 17% | +0.005% | 45% | 0.13 | +0.87% |
| chop | 1160 | 48% | -0.040% | 38% | -0.99 | -39.34% |

## Turnover, fees, activity

- trades: 6289 (2.59/day); active days 99%
- turnover 90.3x equity/year; fees 9.03% of equity/year ($42,674 total)
- average gross exposure 0.19; brake active 17.2% of hours
- correlation of daily returns with s3v2 baseline: 0.63
