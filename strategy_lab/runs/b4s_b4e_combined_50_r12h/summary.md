# Run: b4s_b4e_combined_50_r12h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +218.94% | +19.09% | 0.66 | 0.91 | -74.89% | 0.25 | 0.64 |
| in_sample | 2020-02-15 → 2024-12-31 | +311.70% | +33.62% | 0.93 | 1.29 | -71.56% | 0.47 | 0.94 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -23.08% | -13.87% | -0.39 | -0.55 | -42.25% | -0.33 | -0.43 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -10.59% | -10.59% | -0.32 | -0.45 | -27.39% | -0.39 | -0.39 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.15% | 40% | -18.50% | -19.40% | -2.45 | 12 | 34% |
| out_of_sample | 628 | -1.90% | 36% | -11.82% | -14.32% | -4.19 | 12 | 24% |
| in_sample | 1768 | -0.89% | 41% | -18.50% | -19.40% | -1.99 | 13 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.619% | 47% | 3.70 | +171.50% |
| bull | 687 | 28% | +0.277% | 47% | 2.37 | +465.36% |
| bear | 400 | 17% | -0.257% | 31% | -3.66 | -65.59% |
| chop | 1160 | 48% | -0.034% | 35% | -0.47 | -39.61% |

## Turnover, fees, activity

- trades: 21827 (9.00/day); active days 83%
- turnover 217.3x equity/year; fees 21.73% of equity/year ($293,068 total)
- average gross exposure 0.30; brake active 46.6% of hours
- correlation of daily returns with s3v2 baseline: 0.37
