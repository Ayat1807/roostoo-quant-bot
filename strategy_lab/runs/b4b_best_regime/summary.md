# Run: b4b_best_regime

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'score', 'exposure': 'regime'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +241.01% | +20.29% | 0.66 | 0.92 | -71.10% | 0.29 | 0.65 |
| in_sample | 2020-02-15 → 2024-12-31 | +303.67% | +33.09% | 0.88 | 1.22 | -59.79% | 0.55 | 0.92 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -15.74% | -9.28% | -0.17 | -0.25 | -38.25% | -0.24 | -0.22 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +12.44% | +12.44% | 0.57 | 0.84 | -22.91% | 0.54 | 0.67 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.31% | 39% | -22.16% | -23.41% | -3.03 | 12 | 33% |
| out_of_sample | 628 | -1.85% | 34% | -14.71% | -20.15% | -4.47 | 12 | 21% |
| in_sample | 1768 | -0.96% | 41% | -22.16% | -23.41% | -2.19 | 12 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.856% | 45% | 4.43 | +301.84% |
| bull | 687 | 28% | +0.209% | 46% | 1.53 | +235.13% |
| bear | 400 | 17% | -0.179% | 30% | -3.53 | -52.07% |
| chop | 1160 | 48% | -0.044% | 34% | -0.57 | -47.17% |

## Turnover, fees, activity

- trades: 14874 (6.14/day); active days 83%
- turnover 190.3x equity/year; fees 19.03% of equity/year ($266,100 total)
- average gross exposure 0.29; brake active 43.3% of hours
- correlation of daily returns with s3v2 baseline: 0.37
