# Run: b8_h_U4

Strategy `s3v2x_regime`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 20, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'n_divisor': None}`; band 0.04; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +44.92% | +5.75% | 0.68 | 0.99 | -23.83% | 0.24 | 0.67 |
| in_sample | 2020-02-15 → 2024-12-31 | +33.95% | +6.17% | 0.66 | 0.96 | -23.83% | 0.26 | 0.66 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +8.25% | +4.61% | 0.97 | 1.43 | -5.65% | 0.82 | 1.11 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +7.23% | +7.23% | 1.26 | 1.88 | -5.65% | 1.28 | 1.52 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.10% | 44% | -5.29% | -7.45% | -1.81 | 14 | 99% |
| out_of_sample | 628 | -0.07% | 46% | -3.69% | -3.79% | -1.49 | 14 | 100% |
| in_sample | 1768 | -0.10% | 44% | -5.29% | -7.45% | -1.81 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.152% | 52% | 3.91 | +29.95% |
| bull | 687 | 28% | +0.031% | 51% | 1.39 | +23.33% |
| bear | 400 | 17% | +0.016% | 48% | 1.36 | +6.50% |
| chop | 1160 | 48% | -0.012% | 43% | -0.41 | -14.10% |

## Turnover, fees, activity

- trades: 5501 (2.27/day); active days 100%
- turnover 26.6x equity/year; fees 2.66% of equity/year ($10,511 total)
- average gross exposure 0.10; brake active 3.2% of hours
- correlation of daily returns with s3v2 baseline: 0.68
