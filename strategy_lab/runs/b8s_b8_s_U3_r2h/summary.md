# Run: b8s_b8_s_U3_r2h

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 30, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +98.42% | +10.87% | 0.83 | 1.21 | -22.04% | 0.49 | 0.88 |
| in_sample | 2020-02-15 → 2024-12-31 | +100.24% | +15.28% | 1.08 | 1.59 | -22.04% | 0.69 | 1.17 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -0.84% | -0.48% | 0.02 | 0.03 | -15.63% | -0.03 | 0.01 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +4.39% | +4.39% | 0.38 | 0.55 | -13.80% | 0.32 | 0.43 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.21% | 43% | -5.38% | -5.81% | -1.94 | 14 | 98% |
| out_of_sample | 628 | -0.55% | 38% | -4.58% | -5.02% | -4.03 | 14 | 100% |
| in_sample | 1768 | -0.13% | 46% | -5.38% | -5.81% | -1.12 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.304% | 55% | 4.62 | +68.21% |
| bull | 687 | 28% | +0.073% | 44% | 1.99 | +62.52% |
| bear | 400 | 17% | +0.044% | 43% | 1.44 | +18.55% |
| chop | 1160 | 48% | -0.040% | 40% | -1.29 | -38.71% |

## Turnover, fees, activity

- trades: 10807 (4.46/day); active days 100%
- turnover 115.9x equity/year; fees 11.59% of equity/year ($60,476 total)
- average gross exposure 0.20; brake active 8.9% of hours
- correlation of daily returns with s3v2 baseline: 0.66
