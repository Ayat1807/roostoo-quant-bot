# Run: b_r4_rs

Strategy `sat_rs`; universe `{'type': 'satellite', 'rule': 'R4', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +19.43% | +2.82% | 0.24 | 0.33 | -50.29% | 0.06 | 0.22 |
| in_sample | 2020-02-15 → 2024-12-31 | +28.42% | +5.26% | 0.32 | 0.43 | -48.63% | 0.11 | 0.30 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -7.00% | -4.74% | -0.04 | -0.05 | -32.43% | -0.15 | -0.08 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -8.92% | -11.74% | -0.37 | -0.53 | -20.24% | -0.58 | -0.50 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.50% | 37% | -12.70% | -13.95% | -1.80 | 4 | 0% |
| out_of_sample | 532 | -1.07% | 34% | -8.42% | -9.47% | -3.93 | 5 | 0% |
| in_sample | 1768 | -0.30% | 38% | -12.70% | -13.95% | -1.04 | 4 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.019% | 16% | 0.20 | +0.44% |
| bull | 659 | 28% | +0.268% | 33% | 2.73 | +419.34% |
| bear | 399 | 17% | -0.208% | 21% | -3.45 | -57.60% |
| chop | 1099 | 47% | -0.046% | 23% | -0.62 | -46.01% |

## Turnover, fees, activity

- trades: 1402 (0.60/day); active days 34%
- turnover 34.4x equity/year; fees 3.44% of equity/year ($3,075 total)
- average gross exposure 0.23; brake active 34.5% of hours
- correlation of daily returns with s3v2 baseline: 0.30
