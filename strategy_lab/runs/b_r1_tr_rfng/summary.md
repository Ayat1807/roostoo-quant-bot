# Run: b_r1_tr_rfng

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'riskoff': 'fng'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +60.54% | +7.70% | 0.39 | 0.53 | -56.44% | 0.14 | 0.37 |
| in_sample | 2020-02-15 → 2024-12-31 | +73.51% | +11.95% | 0.51 | 0.68 | -56.44% | 0.21 | 0.49 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -7.47% | -5.06% | -0.02 | -0.03 | -34.14% | -0.15 | -0.06 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -16.01% | -20.81% | -0.82 | -1.17 | -24.60% | -0.85 | -0.97 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.51% | 35% | -9.22% | -11.45% | -2.22 | 6 | 6% |
| out_of_sample | 532 | -1.37% | 33% | -8.75% | -9.36% | -4.29 | 6 | 4% |
| in_sample | 1768 | -0.32% | 36% | -9.22% | -11.45% | -1.52 | 6 | 6% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.285% | 27% | 3.41 | +58.90% |
| bull | 659 | 28% | +0.182% | 27% | 1.78 | +193.04% |
| bear | 399 | 17% | -0.170% | 22% | -3.00 | -50.37% |
| chop | 1099 | 47% | -0.022% | 30% | -0.29 | -30.54% |

## Turnover, fees, activity

- trades: 5943 (2.55/day); active days 45%
- turnover 81.4x equity/year; fees 8.14% of equity/year ($6,372 total)
- average gross exposure 0.23; brake active 35.2% of hours
- correlation of daily returns with s3v2 baseline: 0.31
