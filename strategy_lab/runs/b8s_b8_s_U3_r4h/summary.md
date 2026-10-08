# Run: b8s_b8_s_U3_r4h

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 30, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +136.34% | +13.83% | 1.01 | 1.49 | -20.96% | 0.66 | 1.10 |
| in_sample | 2020-02-15 → 2024-12-31 | +154.60% | +21.10% | 1.38 | 2.05 | -15.87% | 1.33 | 1.64 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -7.11% | -4.11% | -0.32 | -0.46 | -20.25% | -0.20 | -0.34 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -1.90% | -1.90% | -0.09 | -0.13 | -17.64% | -0.11 | -0.11 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.15% | 46% | -5.30% | -6.20% | -1.44 | 14 | 99% |
| out_of_sample | 628 | -0.58% | 39% | -4.80% | -5.16% | -4.13 | 14 | 100% |
| in_sample | 1768 | -0.06% | 49% | -5.30% | -6.20% | -0.60 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.319% | 53% | 4.71 | +72.82% |
| bull | 687 | 28% | +0.089% | 46% | 2.45 | +80.87% |
| bear | 400 | 17% | +0.036% | 42% | 1.25 | +14.72% |
| chop | 1160 | 48% | -0.034% | 39% | -1.07 | -34.03% |

## Turnover, fees, activity

- trades: 8791 (3.63/day); active days 100%
- turnover 94.1x equity/year; fees 9.41% of equity/year ($54,871 total)
- average gross exposure 0.20; brake active 8.7% of hours
- correlation of daily returns with s3v2 baseline: 0.68
