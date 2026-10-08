# Run: b8s_b8_s_U3_r6h

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 30, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +210.60% | +18.61% | 1.29 | 1.90 | -13.87% | 1.34 | 1.55 |
| in_sample | 2020-02-15 → 2024-12-31 | +197.51% | +25.02% | 1.58 | 2.33 | -12.86% | 1.95 | 1.99 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +4.47% | +2.52% | 0.28 | 0.40 | -13.87% | 0.18 | 0.30 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +6.96% | +6.96% | 0.59 | 0.86 | -13.87% | 0.50 | 0.67 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.12% | 47% | -7.22% | -7.59% | -1.09 | 14 | 99% |
| out_of_sample | 628 | -0.53% | 39% | -4.63% | -4.93% | -3.88 | 14 | 100% |
| in_sample | 1768 | -0.01% | 50% | -7.22% | -7.59% | 0.03 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.352% | 53% | 5.17 | +83.07% |
| bull | 687 | 28% | +0.094% | 46% | 2.47 | +86.90% |
| bear | 400 | 17% | +0.059% | 46% | 1.92 | +25.63% |
| chop | 1160 | 48% | -0.026% | 41% | -0.83 | -27.67% |

## Turnover, fees, activity

- trades: 8006 (3.30/day); active days 100%
- turnover 86.3x equity/year; fees 8.63% of equity/year ($57,497 total)
- average gross exposure 0.21; brake active 7.7% of hours
- correlation of daily returns with s3v2 baseline: 0.68
