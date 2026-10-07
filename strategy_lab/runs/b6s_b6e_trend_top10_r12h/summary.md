# Run: b6s_b6e_trend_top10_r12h

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'TREND', 'n_liquid': 10, 'min_history_days': 180, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +63.13% | +7.65% | 0.53 | 0.78 | -33.33% | 0.23 | 0.54 |
| in_sample | 2020-02-15 → 2024-12-31 | +48.96% | +8.50% | 0.56 | 0.82 | -33.33% | 0.26 | 0.57 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +9.54% | +5.32% | 0.46 | 0.67 | -12.81% | 0.42 | 0.53 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +20.98% | +20.98% | 1.32 | 1.97 | -12.25% | 1.71 | 1.70 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.36% | 44% | -9.10% | -9.16% | -2.22 | 14 | 89% |
| out_of_sample | 628 | -0.38% | 40% | -5.16% | -5.94% | -3.19 | 14 | 98% |
| in_sample | 1768 | -0.32% | 45% | -9.10% | -9.16% | -1.68 | 14 | 86% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.403% | 53% | 4.30 | +97.55% |
| bull | 687 | 28% | +0.055% | 49% | 1.33 | +42.91% |
| bear | 400 | 17% | +0.013% | 46% | 0.35 | +4.33% |
| chop | 1160 | 48% | -0.048% | 39% | -1.20 | -44.44% |

## Turnover, fees, activity

- trades: 5147 (2.12/day); active days 99%
- turnover 70.9x equity/year; fees 7.09% of equity/year ($32,010 total)
- average gross exposure 0.19; brake active 15.9% of hours
- correlation of daily returns with s3v2 baseline: 0.66
