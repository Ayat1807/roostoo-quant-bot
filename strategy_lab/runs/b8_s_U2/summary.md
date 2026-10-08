# Run: b8_s_U2

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 20, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +154.30% | +15.09% | 1.05 | 1.54 | -17.07% | 0.88 | 1.20 |
| in_sample | 2020-02-15 → 2024-12-31 | +118.30% | +17.34% | 1.17 | 1.73 | -17.07% | 1.02 | 1.35 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +16.61% | +9.14% | 0.69 | 1.00 | -12.47% | 0.73 | 0.83 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +15.50% | +15.50% | 0.99 | 1.43 | -12.47% | 1.24 | 1.24 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.22% | 43% | -5.66% | -6.55% | -1.90 | 14 | 99% |
| out_of_sample | 628 | -0.37% | 42% | -4.57% | -6.55% | -1.92 | 14 | 100% |
| in_sample | 1768 | -0.19% | 44% | -5.66% | -6.49% | -1.76 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.257% | 55% | 3.36 | +54.23% |
| bull | 687 | 28% | +0.090% | 51% | 2.71 | +83.27% |
| bear | 400 | 17% | +0.053% | 50% | 1.57 | +22.60% |
| chop | 1160 | 48% | -0.024% | 45% | -0.77 | -26.33% |

## Turnover, fees, activity

- trades: 5582 (2.30/day); active days 100%
- turnover 51.4x equity/year; fees 5.14% of equity/year ($28,161 total)
- average gross exposure 0.21; brake active 8.1% of hours
- correlation of daily returns with s3v2 baseline: 0.77
