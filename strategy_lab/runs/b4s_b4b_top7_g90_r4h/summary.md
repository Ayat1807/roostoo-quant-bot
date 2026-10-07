# Run: b4s_b4b_top7_g90_r4h

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'top_n': 7, 'gross': 0.9}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +125.77% | +13.05% | 0.51 | 0.70 | -74.59% | 0.17 | 0.49 |
| in_sample | 2020-02-15 → 2024-12-31 | +285.84% | +31.86% | 0.88 | 1.20 | -63.44% | 0.50 | 0.90 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -41.61% | -26.36% | -0.85 | -1.17 | -57.94% | -0.46 | -0.86 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -24.32% | -24.32% | -0.91 | -1.25 | -40.70% | -0.60 | -0.95 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.27% | 41% | -16.26% | -17.77% | -2.62 | 13 | 35% |
| out_of_sample | 628 | -2.92% | 31% | -13.65% | -13.89% | -5.83 | 12 | 25% |
| in_sample | 1768 | -0.73% | 44% | -16.26% | -17.77% | -1.18 | 13 | 38% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.714% | 45% | 4.28 | +220.68% |
| bull | 687 | 28% | +0.279% | 48% | 2.26 | +461.29% |
| bear | 400 | 17% | -0.255% | 30% | -3.44 | -65.41% |
| chop | 1160 | 48% | -0.076% | 35% | -0.98 | -63.74% |

## Turnover, fees, activity

- trades: 57663 (23.79/day); active days 85%
- turnover 317.4x equity/year; fees 31.74% of equity/year ($355,040 total)
- average gross exposure 0.32; brake active 49.4% of hours
- correlation of daily returns with s3v2 baseline: 0.38
