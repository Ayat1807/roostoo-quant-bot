# Run: b_r4_bo_gated

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R4', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +8.58% | +1.30% | 0.17 | 0.23 | -22.57% | 0.06 | 0.16 |
| in_sample | 2020-02-15 → 2024-12-31 | +2.79% | +0.56% | 0.11 | 0.15 | -22.57% | 0.03 | 0.10 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +5.63% | +3.73% | 0.38 | 0.54 | -10.11% | 0.37 | 0.44 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +1.12% | +1.49% | 0.24 | 0.35 | -4.85% | 0.31 | 0.30 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 22% | -8.33% | -8.51% | 0.00 | 0 | 0% |
| out_of_sample | 532 | -0.00% | 33% | -4.94% | -6.80% | -3.55 | 0 | 0% |
| in_sample | 1768 | +0.00% | 19% | -8.33% | -8.51% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.041% | 22% | 1.71 | +6.95% |
| bull | 659 | 28% | +0.042% | 25% | 0.82 | +28.12% |
| bear | 399 | 17% | -0.003% | 13% | -0.70 | -1.37% |
| chop | 1099 | 47% | -0.019% | 24% | -0.90 | -19.66% |

## Turnover, fees, activity

- trades: 519 (0.22/day); active days 9%
- turnover 13.6x equity/year; fees 1.36% of equity/year ($869 total)
- average gross exposure 0.03; brake active 3.6% of hours
- correlation of daily returns with s3v2 baseline: 0.11
