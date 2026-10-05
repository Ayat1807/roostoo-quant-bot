# Run: b_r4_bo

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R4', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +59.94% | +7.64% | 0.41 | 0.56 | -37.04% | 0.21 | 0.41 |
| in_sample | 2020-02-15 → 2024-12-31 | +46.45% | +8.13% | 0.42 | 0.58 | -37.04% | 0.22 | 0.42 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +8.77% | +5.78% | 0.35 | 0.50 | -30.86% | 0.19 | 0.36 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -12.14% | -15.89% | -0.60 | -0.86 | -24.99% | -0.64 | -0.71 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.49% | 40% | -8.86% | -11.46% | -2.21 | 6 | 0% |
| out_of_sample | 532 | -1.06% | 37% | -8.70% | -8.70% | -3.77 | 6 | 0% |
| in_sample | 1768 | -0.39% | 40% | -8.86% | -11.46% | -1.66 | 7 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.237% | 31% | 2.70 | +45.98% |
| bull | 659 | 28% | +0.158% | 34% | 1.79 | +157.80% |
| bear | 399 | 17% | -0.132% | 20% | -2.88 | -41.77% |
| chop | 1099 | 47% | -0.021% | 24% | -0.34 | -27.02% |

## Turnover, fees, activity

- trades: 1930 (0.83/day); active days 44%
- turnover 51.6x equity/year; fees 5.16% of equity/year ($4,592 total)
- average gross exposure 0.18; brake active 16.8% of hours
- correlation of daily returns with s3v2 baseline: 0.24
