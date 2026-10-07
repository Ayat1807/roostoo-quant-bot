# Run: b6s_b6e_trend_top10_r4h

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'TREND', 'n_liquid': 10, 'min_history_days': 180, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +42.18% | +5.44% | 0.41 | 0.60 | -36.55% | 0.15 | 0.41 |
| in_sample | 2020-02-15 → 2024-12-31 | +35.36% | +6.40% | 0.45 | 0.66 | -36.55% | 0.18 | 0.45 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +5.11% | +2.88% | 0.28 | 0.41 | -15.86% | 0.18 | 0.30 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +16.03% | +16.03% | 1.02 | 1.52 | -15.86% | 1.01 | 1.22 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.38% | 43% | -9.97% | -10.44% | -2.70 | 14 | 97% |
| out_of_sample | 628 | -0.55% | 36% | -4.89% | -6.43% | -4.35 | 14 | 100% |
| in_sample | 1768 | -0.27% | 46% | -9.97% | -10.44% | -1.72 | 14 | 96% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.459% | 55% | 5.06 | +118.12% |
| bull | 687 | 28% | +0.033% | 45% | 0.79 | +22.88% |
| bear | 400 | 17% | -0.004% | 44% | -0.09 | -2.50% |
| chop | 1160 | 48% | -0.049% | 35% | -1.21 | -45.43% |

## Turnover, fees, activity

- trades: 7321 (3.02/day); active days 100%
- turnover 107.6x equity/year; fees 10.76% of equity/year ($45,918 total)
- average gross exposure 0.18; brake active 19.9% of hours
- correlation of daily returns with s3v2 baseline: 0.64
