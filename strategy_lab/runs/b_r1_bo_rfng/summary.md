# Run: b_r1_bo_rfng

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'riskoff': 'fng'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +17.87% | +2.61% | 0.24 | 0.33 | -70.58% | 0.04 | 0.21 |
| in_sample | 2020-02-15 → 2024-12-31 | +66.29% | +10.98% | 0.49 | 0.68 | -70.58% | 0.16 | 0.47 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -29.56% | -20.89% | -0.75 | -1.06 | -38.21% | -0.55 | -0.81 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -5.68% | -7.52% | -0.20 | -0.29 | -16.91% | -0.44 | -0.31 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.76% | 35% | -13.10% | -13.10% | -2.66 | 5 | 0% |
| out_of_sample | 532 | -1.58% | 27% | -9.21% | -10.67% | -5.95 | 4 | 0% |
| in_sample | 1768 | -0.45% | 37% | -13.10% | -13.10% | -2.02 | 6 | 1% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.264% | 25% | 2.56 | +51.60% |
| bull | 659 | 28% | +0.178% | 28% | 1.75 | +185.54% |
| bear | 399 | 17% | -0.178% | 14% | -3.66 | -51.72% |
| chop | 1099 | 47% | -0.043% | 23% | -0.61 | -43.60% |

## Turnover, fees, activity

- trades: 2477 (1.06/day); active days 40%
- turnover 64.5x equity/year; fees 6.45% of equity/year ($4,173 total)
- average gross exposure 0.20; brake active 30.0% of hours
- correlation of daily returns with s3v2 baseline: 0.20
