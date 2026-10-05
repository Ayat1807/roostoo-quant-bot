# Run: b_r2_bo

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R2', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +135.32% | +14.36% | 0.59 | 0.83 | -49.66% | 0.29 | 0.60 |
| in_sample | 2020-02-15 → 2024-12-31 | +102.35% | +15.53% | 0.63 | 0.86 | -49.66% | 0.31 | 0.63 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +16.30% | +10.62% | 0.49 | 0.70 | -29.73% | 0.36 | 0.53 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +2.60% | +3.49% | 0.26 | 0.37 | -24.16% | 0.14 | 0.27 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.42% | 38% | -12.04% | -13.86% | -1.96 | 6 | 0% |
| out_of_sample | 532 | -1.04% | 39% | -9.82% | -9.82% | -2.70 | 5 | 0% |
| in_sample | 1768 | -0.37% | 38% | -12.04% | -13.86% | -1.83 | 6 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.231% | 25% | 1.87 | +41.38% |
| bull | 659 | 28% | +0.197% | 29% | 1.95 | +224.29% |
| bear | 399 | 17% | -0.143% | 14% | -2.53 | -44.73% |
| chop | 1099 | 47% | +0.003% | 25% | 0.04 | -7.14% |

## Turnover, fees, activity

- trades: 2123 (0.91/day); active days 40%
- turnover 59.0x equity/year; fees 5.90% of equity/year ($5,059 total)
- average gross exposure 0.19; brake active 28.2% of hours
- correlation of daily returns with s3v2 baseline: 0.20
