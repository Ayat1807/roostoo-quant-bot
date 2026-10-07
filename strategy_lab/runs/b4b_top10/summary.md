# Run: b4b_top10

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'top_n': 10}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +152.59% | +14.98% | 0.63 | 0.85 | -47.31% | 0.32 | 0.63 |
| in_sample | 2020-02-15 → 2024-12-31 | +246.13% | +28.96% | 0.99 | 1.33 | -42.90% | 0.68 | 1.03 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -27.15% | -16.49% | -0.68 | -0.94 | -44.29% | -0.37 | -0.69 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -10.65% | -10.65% | -0.47 | -0.65 | -29.87% | -0.36 | -0.51 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.72% | 41% | -11.72% | -13.14% | -2.36 | 12 | 33% |
| out_of_sample | 628 | -1.68% | 35% | -11.72% | -11.96% | -5.37 | 12 | 21% |
| in_sample | 1768 | -0.45% | 44% | -11.31% | -13.14% | -1.52 | 12 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.497% | 46% | 3.83 | +127.10% |
| bull | 687 | 28% | +0.179% | 51% | 2.13 | +212.72% |
| bear | 400 | 17% | -0.172% | 32% | -3.47 | -50.63% |
| chop | 1160 | 48% | -0.022% | 35% | -0.39 | -27.96% |

## Turnover, fees, activity

- trades: 19550 (8.07/day); active days 83%
- turnover 106.9x equity/year; fees 10.69% of equity/year ($93,406 total)
- average gross exposure 0.23; brake active 41.9% of hours
- correlation of daily returns with s3v2 baseline: 0.42
