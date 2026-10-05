# Run: b_r2_tr_gated

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R2', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +25.94% | +3.68% | 0.30 | 0.41 | -28.10% | 0.13 | 0.29 |
| in_sample | 2020-02-15 → 2024-12-31 | +38.52% | +6.90% | 0.47 | 0.64 | -28.10% | 0.25 | 0.47 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -9.08% | -6.17% | -0.33 | -0.45 | -21.77% | -0.28 | -0.37 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -9.16% | -12.06% | -1.54 | -2.00 | -9.16% | -1.32 | -1.66 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 18% | -8.95% | -10.84% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 11% | -8.85% | -9.81% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 20% | -8.95% | -10.84% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.068% | 11% | 1.83 | +11.71% |
| bull | 659 | 28% | +0.085% | 16% | 1.06 | +62.31% |
| bear | 399 | 17% | +0.000% | 3% | 0.10 | +0.14% |
| chop | 1099 | 47% | -0.032% | 10% | -1.24 | -30.64% |

## Turnover, fees, activity

- trades: 1183 (0.51/day); active days 11%
- turnover 19.6x equity/year; fees 1.96% of equity/year ($1,463 total)
- average gross exposure 0.05; brake active 6.0% of hours
- correlation of daily returns with s3v2 baseline: 0.15
