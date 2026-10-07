# Run: b4e_fast_6h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +297.23% | +23.09% | 0.75 | 1.04 | -67.93% | 0.34 | 0.74 |
| in_sample | 2020-02-15 → 2024-12-31 | +447.68% | +41.67% | 1.08 | 1.50 | -63.71% | 0.65 | 1.12 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -27.73% | -16.87% | -0.51 | -0.71 | -46.48% | -0.36 | -0.55 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -6.65% | -6.65% | -0.15 | -0.21 | -31.67% | -0.21 | -0.19 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.38% | 40% | -18.65% | -19.65% | -2.80 | 12 | 32% |
| out_of_sample | 628 | -2.50% | 36% | -12.02% | -14.24% | -5.18 | 12 | 21% |
| in_sample | 1768 | -0.92% | 42% | -18.65% | -19.65% | -1.90 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.695% | 44% | 4.22 | +211.08% |
| bull | 687 | 28% | +0.289% | 49% | 2.47 | +515.29% |
| bear | 400 | 17% | -0.257% | 30% | -3.89 | -65.40% |
| chop | 1160 | 48% | -0.035% | 33% | -0.48 | -40.01% |

## Turnover, fees, activity

- trades: 18884 (7.79/day); active days 82%
- turnover 194.6x equity/year; fees 19.46% of equity/year ($304,867 total)
- average gross exposure 0.30; brake active 47.8% of hours
- correlation of daily returns with s3v2 baseline: 0.37
