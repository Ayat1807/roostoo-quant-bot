# Run: b4b_score

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'score'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +520.11% | +31.63% | 0.90 | 1.26 | -61.06% | 0.52 | 0.93 |
| in_sample | 2020-02-15 → 2024-12-31 | +781.06% | +56.16% | 1.27 | 1.78 | -61.06% | 0.92 | 1.37 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -30.15% | -18.47% | -0.57 | -0.80 | -43.71% | -0.42 | -0.62 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -11.13% | -11.13% | -0.33 | -0.47 | -28.31% | -0.39 | -0.40 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.98% | 42% | -16.67% | -18.67% | -2.01 | 12 | 32% |
| out_of_sample | 628 | -2.02% | 38% | -11.10% | -15.20% | -4.49 | 12 | 20% |
| in_sample | 1768 | -0.60% | 44% | -16.67% | -18.67% | -1.16 | 12 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.761% | 45% | 3.97 | +240.01% |
| bull | 687 | 28% | +0.292% | 49% | 2.37 | +515.69% |
| bear | 400 | 17% | -0.260% | 30% | -3.96 | -65.78% |
| chop | 1160 | 48% | -0.002% | 34% | -0.03 | -13.44% |

## Turnover, fees, activity

- trades: 14145 (5.84/day); active days 82%
- turnover 175.3x equity/year; fees 17.53% of equity/year ($368,773 total)
- average gross exposure 0.30; brake active 45.8% of hours
- correlation of daily returns with s3v2 baseline: 0.36
