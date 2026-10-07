# Run: b4s_b4b_score_r1h

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'score'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -68.29% | -15.89% | -0.25 | -0.36 | -95.17% | -0.17 | -0.27 |
| in_sample | 2020-02-15 → 2024-12-31 | +1.08% | +0.22% | 0.21 | 0.30 | -85.18% | 0.00 | 0.18 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -68.71% | -48.36% | -2.13 | -2.93 | -73.73% | -0.66 | -2.01 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -42.04% | -42.04% | -1.87 | -2.60 | -50.05% | -0.84 | -1.85 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -2.60% | 33% | -18.62% | -21.87% | -4.52 | 13 | 37% |
| out_of_sample | 628 | -3.59% | 23% | -12.22% | -15.10% | -6.26 | 13 | 29% |
| in_sample | 1768 | -2.22% | 36% | -18.62% | -21.87% | -3.62 | 13 | 40% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.861% | 49% | 4.57 | +306.29% |
| bull | 687 | 28% | +0.068% | 41% | 0.57 | +33.71% |
| bear | 400 | 17% | -0.335% | 28% | -5.03 | -74.68% |
| chop | 1160 | 48% | -0.115% | 31% | -1.44 | -76.95% |

## Turnover, fees, activity

- trades: 154761 (63.85/day); active days 85%
- turnover 577.0x equity/year; fees 57.70% of equity/year ($284,827 total)
- average gross exposure 0.28; brake active 55.4% of hours
- correlation of daily returns with s3v2 baseline: 0.34
