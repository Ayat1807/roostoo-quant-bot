# Run: b4s_b4b_top7_g90_r12h

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'top_n': 7, 'gross': 0.9}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +77.03% | +8.98% | 0.42 | 0.57 | -80.19% | 0.11 | 0.39 |
| in_sample | 2020-02-15 → 2024-12-31 | +147.22% | +20.37% | 0.66 | 0.89 | -70.60% | 0.29 | 0.64 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -28.83% | -17.59% | -0.48 | -0.65 | -47.71% | -0.37 | -0.52 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -12.52% | -12.52% | -0.37 | -0.51 | -29.99% | -0.42 | -0.44 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.40% | 37% | -19.24% | -20.07% | -2.91 | 12 | 32% |
| out_of_sample | 628 | -2.55% | 30% | -12.44% | -14.90% | -5.36 | 12 | 24% |
| in_sample | 1768 | -1.12% | 39% | -19.24% | -20.07% | -2.16 | 13 | 35% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.704% | 48% | 4.17 | +214.75% |
| bull | 687 | 28% | +0.231% | 46% | 1.87 | +304.44% |
| bear | 400 | 17% | -0.273% | 32% | -3.84 | -67.77% |
| chop | 1160 | 48% | -0.062% | 35% | -0.81 | -56.85% |

## Turnover, fees, activity

- trades: 26787 (11.05/day); active days 83%
- turnover 224.3x equity/year; fees 22.43% of equity/year ($203,604 total)
- average gross exposure 0.31; brake active 48.2% of hours
- correlation of daily returns with s3v2 baseline: 0.39
