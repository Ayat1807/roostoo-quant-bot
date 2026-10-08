# Run: b6s_b6e_trend_top15_r12h

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'TREND', 'n_liquid': 15, 'min_history_days': 180, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +64.01% | +7.74% | 0.54 | 0.79 | -33.33% | 0.23 | 0.55 |
| in_sample | 2020-02-15 → 2024-12-31 | +47.65% | +8.31% | 0.55 | 0.80 | -33.33% | 0.25 | 0.56 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +11.08% | +6.16% | 0.53 | 0.77 | -12.25% | 0.50 | 0.62 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +20.85% | +20.85% | 1.32 | 1.97 | -12.25% | 1.70 | 1.70 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.36% | 42% | -9.10% | -9.16% | -2.48 | 14 | 89% |
| out_of_sample | 628 | -0.35% | 37% | -5.16% | -5.94% | -3.27 | 14 | 98% |
| in_sample | 1768 | -0.36% | 44% | -9.10% | -9.16% | -2.02 | 14 | 86% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.408% | 55% | 4.36 | +99.26% |
| bull | 687 | 28% | +0.052% | 48% | 1.25 | +39.78% |
| bear | 400 | 17% | +0.010% | 46% | 0.26 | +2.95% |
| chop | 1160 | 48% | -0.045% | 39% | -1.14 | -42.62% |

## Turnover, fees, activity

- trades: 5119 (2.11/day); active days 99%
- turnover 69.8x equity/year; fees 6.98% of equity/year ($31,416 total)
- average gross exposure 0.19; brake active 15.9% of hours
- correlation of daily returns with s3v2 baseline: 0.65
