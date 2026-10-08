# Run: b8_h_U3

Strategy `s3v2x_regime`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 30, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +87.32% | +9.91% | 0.92 | 1.37 | -15.11% | 0.66 | 1.02 |
| in_sample | 2020-02-15 → 2024-12-31 | +67.07% | +11.09% | 0.96 | 1.45 | -15.11% | 0.73 | 1.09 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +12.25% | +6.79% | 0.78 | 1.13 | -11.06% | 0.61 | 0.87 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +7.05% | +7.05% | 0.72 | 1.04 | -11.06% | 0.64 | 0.82 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.13% | 46% | -5.29% | -6.19% | -1.56 | 14 | 99% |
| out_of_sample | 628 | -0.08% | 48% | -5.08% | -5.26% | -0.65 | 14 | 100% |
| in_sample | 1768 | -0.13% | 45% | -5.29% | -6.19% | -1.62 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.219% | 53% | 4.17 | +45.76% |
| bull | 687 | 28% | +0.060% | 51% | 2.19 | +49.52% |
| bear | 400 | 17% | +0.021% | 47% | 0.94 | +8.52% |
| chop | 1160 | 48% | -0.018% | 45% | -0.68 | -20.51% |

## Turnover, fees, activity

- trades: 6205 (2.56/day); active days 100%
- turnover 48.8x equity/year; fees 4.88% of equity/year ($22,678 total)
- average gross exposure 0.19; brake active 3.7% of hours
- correlation of daily returns with s3v2 baseline: 0.69
