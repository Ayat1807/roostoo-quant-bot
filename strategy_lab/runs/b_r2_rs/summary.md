# Run: b_r2_rs

Strategy `sat_rs`; universe `{'type': 'satellite', 'rule': 'R2', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | -23.60% | -4.13% | 0.03 | 0.04 | -76.76% | -0.05 | 0.01 |
| in_sample | 2020-02-15 → 2024-12-31 | -23.49% | -5.34% | -0.01 | -0.01 | -76.76% | -0.07 | -0.03 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -0.14% | -0.10% | 0.15 | 0.22 | -27.93% | -0.00 | 0.13 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -2.80% | -3.72% | 0.02 | 0.03 | -22.44% | -0.17 | -0.03 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.80% | 35% | -14.91% | -16.27% | -2.82 | 4 | 0% |
| out_of_sample | 532 | -1.02% | 38% | -8.87% | -9.38% | -3.64 | 4 | 0% |
| in_sample | 1768 | -0.71% | 34% | -14.91% | -16.27% | -2.68 | 4 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.282% | 21% | 2.66 | +55.98% |
| bull | 659 | 28% | +0.191% | 33% | 1.77 | +205.94% |
| bear | 399 | 17% | -0.272% | 14% | -4.17 | -67.36% |
| chop | 1099 | 47% | -0.053% | 22% | -0.67 | -50.95% |

## Turnover, fees, activity

- trades: 1455 (0.62/day); active days 30%
- turnover 37.1x equity/year; fees 3.71% of equity/year ($2,440 total)
- average gross exposure 0.22; brake active 41.2% of hours
- correlation of daily returns with s3v2 baseline: 0.27
