# Run: b_r1_tr_noR5

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': False, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +60.40% | +7.69% | 0.39 | 0.52 | -54.07% | 0.14 | 0.37 |
| in_sample | 2020-02-15 → 2024-12-31 | +82.80% | +13.15% | 0.52 | 0.70 | -54.07% | 0.24 | 0.51 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -12.25% | -8.36% | -0.12 | -0.16 | -35.45% | -0.24 | -0.17 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -17.67% | -22.90% | -0.75 | -1.05 | -25.13% | -0.91 | -0.92 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.86% | 38% | -9.22% | -11.45% | -2.94 | 7 | 8% |
| out_of_sample | 532 | -1.60% | 35% | -8.24% | -9.42% | -5.11 | 7 | 8% |
| in_sample | 1768 | -0.69% | 39% | -9.22% | -11.45% | -2.17 | 7 | 8% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.280% | 29% | 2.40 | +54.43% |
| bull | 659 | 28% | +0.185% | 33% | 1.72 | +195.40% |
| bear | 399 | 17% | -0.200% | 25% | -2.87 | -56.66% |
| chop | 1099 | 47% | -0.008% | 26% | -0.10 | -18.87% |

## Turnover, fees, activity

- trades: 6734 (2.89/day); active days 50%
- turnover 90.2x equity/year; fees 9.02% of equity/year ($7,941 total)
- average gross exposure 0.25; brake active 42.1% of hours
- correlation of daily returns with s3v2 baseline: 0.30
