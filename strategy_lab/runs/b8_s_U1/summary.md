# Run: b8_s_U1

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +124.42% | +12.95% | 0.94 | 1.35 | -19.03% | 0.68 | 1.03 |
| in_sample | 2020-02-15 → 2024-12-31 | +80.10% | +12.81% | 0.96 | 1.37 | -19.03% | 0.67 | 1.04 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +24.74% | +13.40% | 0.90 | 1.32 | -12.68% | 1.06 | 1.11 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +26.91% | +26.91% | 1.43 | 2.10 | -12.68% | 2.12 | 1.91 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.23% | 43% | -5.29% | -6.30% | -2.18 | 14 | 99% |
| out_of_sample | 628 | -0.43% | 41% | -4.87% | -6.30% | -2.62 | 14 | 100% |
| in_sample | 1768 | -0.16% | 44% | -5.29% | -6.29% | -1.76 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.212% | 54% | 2.69 | +42.31% |
| bull | 687 | 28% | +0.089% | 51% | 2.75 | +81.82% |
| bear | 400 | 17% | +0.052% | 48% | 1.57 | +22.17% |
| chop | 1160 | 48% | -0.027% | 44% | -0.85 | -28.73% |

## Turnover, fees, activity

- trades: 5251 (2.17/day); active days 100%
- turnover 47.4x equity/year; fees 4.74% of equity/year ($23,512 total)
- average gross exposure 0.20; brake active 8.7% of hours
- correlation of daily returns with s3v2 baseline: 0.78
