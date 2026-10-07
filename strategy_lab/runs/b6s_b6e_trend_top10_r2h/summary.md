# Run: b6s_b6e_trend_top10_r2h

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'TREND', 'n_liquid': 10, 'min_history_days': 180, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +34.51% | +4.57% | 0.36 | 0.53 | -34.28% | 0.13 | 0.36 |
| in_sample | 2020-02-15 → 2024-12-31 | +35.67% | +6.45% | 0.45 | 0.67 | -34.28% | 0.19 | 0.46 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -0.79% | -0.45% | 0.03 | 0.05 | -19.68% | -0.02 | 0.02 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +7.91% | +7.91% | 0.56 | 0.83 | -19.68% | 0.40 | 0.62 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.42% | 42% | -7.45% | -7.45% | -2.94 | 14 | 98% |
| out_of_sample | 628 | -0.55% | 35% | -5.23% | -6.18% | -4.53 | 14 | 100% |
| in_sample | 1768 | -0.34% | 45% | -7.45% | -7.45% | -2.08 | 14 | 97% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.491% | 55% | 5.25 | +130.42% |
| bull | 687 | 28% | +0.024% | 43% | 0.56 | +15.22% |
| bear | 400 | 17% | -0.006% | 42% | -0.15 | -3.26% |
| chop | 1160 | 48% | -0.052% | 35% | -1.30 | -46.84% |

## Turnover, fees, activity

- trades: 9211 (3.80/day); active days 100%
- turnover 136.5x equity/year; fees 13.65% of equity/year ($58,264 total)
- average gross exposure 0.18; brake active 21.0% of hours
- correlation of daily returns with s3v2 baseline: 0.64
