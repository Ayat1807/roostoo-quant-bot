# Run: b_r1_rs_near

Strategy `sat_rs`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'near_high': 0.15}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +31.25% | +4.36% | 0.30 | 0.40 | -45.52% | 0.10 | 0.28 |
| in_sample | 2020-02-15 → 2024-12-31 | +77.11% | +12.42% | 0.60 | 0.80 | -45.52% | 0.27 | 0.58 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -25.89% | -18.15% | -0.94 | -1.29 | -29.28% | -0.62 | -0.98 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -13.72% | -17.91% | -1.12 | -1.50 | -18.90% | -0.95 | -1.22 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 36% | -11.89% | -13.49% | 0.00 | 4 | 0% |
| out_of_sample | 532 | -0.57% | 31% | -8.16% | -8.32% | -3.74 | 4 | 0% |
| in_sample | 1768 | +0.00% | 38% | -11.89% | -13.49% | 0.00 | 3 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.039% | 22% | 0.44 | +4.31% |
| bull | 659 | 28% | +0.161% | 33% | 1.88 | +163.99% |
| bear | 399 | 17% | -0.050% | 23% | -1.57 | -18.79% |
| chop | 1099 | 47% | -0.045% | 25% | -1.00 | -41.31% |

## Turnover, fees, activity

- trades: 1107 (0.48/day); active days 29%
- turnover 27.1x equity/year; fees 2.71% of equity/year ($2,514 total)
- average gross exposure 0.17; brake active 15.6% of hours
- correlation of daily returns with s3v2 baseline: 0.16
