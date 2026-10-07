# Run: b6s_b6e_trend_top10_r1h

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'TREND', 'n_liquid': 10, 'min_history_days': 180, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -5.32% | -0.82% | 0.03 | 0.04 | -42.83% | -0.02 | 0.02 |
| in_sample | 2020-02-15 → 2024-12-31 | +1.50% | +0.31% | 0.10 | 0.15 | -42.83% | 0.01 | 0.09 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -6.66% | -3.85% | -0.23 | -0.34 | -22.55% | -0.17 | -0.25 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +5.69% | +5.69% | 0.43 | 0.64 | -22.55% | 0.25 | 0.46 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.42% | 42% | -7.57% | -8.47% | -3.08 | 14 | 99% |
| out_of_sample | 628 | -0.55% | 35% | -5.53% | -6.33% | -5.14 | 14 | 100% |
| in_sample | 1768 | -0.38% | 45% | -7.57% | -8.47% | -2.15 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.473% | 53% | 5.17 | +123.68% |
| bull | 687 | 28% | +0.004% | 41% | 0.10 | +0.60% |
| bear | 400 | 17% | -0.013% | 43% | -0.36 | -6.06% |
| chop | 1160 | 48% | -0.065% | 34% | -1.61 | -54.53% |

## Turnover, fees, activity

- trades: 11839 (4.88/day); active days 100%
- turnover 180.6x equity/year; fees 18.06% of equity/year ($62,662 total)
- average gross exposure 0.18; brake active 22.9% of hours
- correlation of daily returns with s3v2 baseline: 0.62
