# Run: b8_h_U1

Strategy `s3v2x_regime`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +107.66% | +11.63% | 1.00 | 1.49 | -12.78% | 0.91 | 1.17 |
| in_sample | 2020-02-15 → 2024-12-31 | +85.28% | +13.46% | 1.15 | 1.71 | -12.78% | 1.05 | 1.35 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +12.19% | +6.76% | 0.62 | 0.90 | -12.27% | 0.55 | 0.71 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +11.97% | +11.97% | 0.92 | 1.35 | -9.19% | 1.30 | 1.21 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.14% | 45% | -5.04% | -5.86% | -1.66 | 14 | 99% |
| out_of_sample | 628 | -0.38% | 42% | -5.04% | -5.86% | -2.35 | 14 | 100% |
| in_sample | 1768 | -0.09% | 47% | -4.91% | -5.62% | -1.24 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.204% | 51% | 3.83 | +41.80% |
| bull | 687 | 28% | +0.063% | 49% | 2.37 | +52.59% |
| bear | 400 | 17% | +0.046% | 46% | 1.68 | +19.51% |
| chop | 1160 | 48% | -0.017% | 45% | -0.57 | -19.41% |

## Turnover, fees, activity

- trades: 5917 (2.44/day); active days 100%
- turnover 47.0x equity/year; fees 4.70% of equity/year ($23,279 total)
- average gross exposure 0.18; brake active 5.2% of hours
- correlation of daily returns with s3v2 baseline: 0.74
