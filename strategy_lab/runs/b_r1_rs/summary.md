# Run: b_r1_rs

Strategy `sat_rs`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +87.05% | +10.32% | 0.46 | 0.62 | -60.68% | 0.17 | 0.44 |
| in_sample | 2020-02-15 → 2024-12-31 | +136.18% | +19.25% | 0.68 | 0.92 | -60.68% | 0.32 | 0.66 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -20.80% | -14.44% | -0.34 | -0.47 | -32.44% | -0.45 | -0.43 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -21.67% | -27.86% | -0.95 | -1.33 | -27.91% | -1.00 | -1.12 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.63% | 41% | -11.92% | -13.25% | -1.89 | 4 | 0% |
| out_of_sample | 532 | -1.01% | 42% | -9.16% | -9.84% | -3.28 | 5 | 0% |
| in_sample | 1768 | -0.41% | 40% | -11.92% | -13.25% | -1.63 | 4 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.283% | 27% | 2.85 | +56.85% |
| bull | 659 | 28% | +0.231% | 32% | 2.16 | +299.18% |
| bear | 399 | 17% | -0.272% | 17% | -4.01 | -67.40% |
| chop | 1099 | 47% | +0.005% | 29% | 0.06 | -8.36% |

## Turnover, fees, activity

- trades: 1796 (0.77/day); active days 33%
- turnover 44.5x equity/year; fees 4.45% of equity/year ($4,849 total)
- average gross exposure 0.28; brake active 43.6% of hours
- correlation of daily returns with s3v2 baseline: 0.25
