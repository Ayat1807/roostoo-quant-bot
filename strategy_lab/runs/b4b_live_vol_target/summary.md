# Run: b4b_live_vol_target

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'exposure': 'vol_target'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +529.05% | +31.91% | 1.05 | 1.49 | -52.77% | 0.60 | 1.09 |
| in_sample | 2020-02-15 → 2024-12-31 | +531.85% | +45.88% | 1.35 | 1.90 | -52.77% | 0.87 | 1.43 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -0.99% | -0.57% | 0.12 | 0.18 | -34.79% | -0.02 | 0.10 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +28.15% | +28.15% | 0.99 | 1.52 | -27.86% | 1.01 | 1.21 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.79% | 44% | -12.41% | -13.39% | -1.54 | 12 | 32% |
| out_of_sample | 628 | -1.68% | 40% | -12.41% | -13.39% | -3.12 | 12 | 21% |
| in_sample | 1768 | -0.39% | 46% | -11.59% | -12.47% | -0.77 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.471% | 50% | 3.92 | +118.50% |
| bull | 687 | 28% | +0.301% | 50% | 3.23 | +608.74% |
| bear | 400 | 17% | -0.201% | 33% | -3.08 | -56.65% |
| chop | 1160 | 48% | +0.006% | 35% | 0.08 | -6.29% |

## Turnover, fees, activity

- trades: 13370 (5.52/day); active days 82%
- turnover 160.3x equity/year; fees 16.03% of equity/year ($229,932 total)
- average gross exposure 0.30; brake active 48.5% of hours
- correlation of daily returns with s3v2 baseline: 0.35
