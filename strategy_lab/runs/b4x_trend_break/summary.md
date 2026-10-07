# Run: b4x_trend_break

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +325.67% | +24.38% | 0.78 | 1.08 | -61.25% | 0.40 | 0.79 |
| in_sample | 2020-02-15 → 2024-12-31 | +479.70% | +43.33% | 1.12 | 1.54 | -58.69% | 0.74 | 1.18 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -26.83% | -16.28% | -0.51 | -0.71 | -44.50% | -0.37 | -0.55 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -1.92% | -1.92% | 0.05 | 0.07 | -27.99% | -0.07 | 0.02 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.24% | 41% | -20.09% | -20.93% | -2.64 | 12 | 31% |
| out_of_sample | 628 | -2.04% | 36% | -12.02% | -15.07% | -5.03 | 12 | 20% |
| in_sample | 1768 | -0.94% | 43% | -20.09% | -20.93% | -1.94 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.634% | 44% | 3.78 | +178.71% |
| bull | 687 | 28% | +0.282% | 49% | 2.48 | +491.09% |
| bear | 400 | 17% | -0.230% | 31% | -3.53 | -61.36% |
| chop | 1160 | 48% | -0.025% | 35% | -0.35 | -33.14% |

## Turnover, fees, activity

- trades: 14011 (5.78/day); active days 82%
- turnover 168.8x equity/year; fees 16.88% of equity/year ($272,162 total)
- average gross exposure 0.29; brake active 46.4% of hours
- correlation of daily returns with s3v2 baseline: 0.38
