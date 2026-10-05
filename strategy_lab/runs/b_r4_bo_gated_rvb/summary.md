# Run: b_r4_bo_gated_rvb

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R4', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally', 'riskoff': 'vol_breadth'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +1.95% | +0.30% | 0.09 | 0.12 | -25.94% | 0.01 | 0.08 |
| in_sample | 2020-02-15 → 2024-12-31 | -3.48% | -0.72% | 0.01 | 0.01 | -25.94% | -0.03 | -0.00 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +5.63% | +3.73% | 0.38 | 0.54 | -10.11% | 0.37 | 0.44 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +1.11% | +1.49% | 0.24 | 0.35 | -4.85% | 0.31 | 0.30 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 12% | -8.33% | -8.51% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 12% | -4.94% | -6.80% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 12% | -8.33% | -8.51% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.041% | 4% | 1.71 | +6.96% |
| bull | 659 | 28% | +0.039% | 10% | 0.76 | +25.32% |
| bear | 399 | 17% | -0.003% | 0% | -0.70 | -1.37% |
| chop | 1099 | 47% | -0.023% | 2% | -1.09 | -22.88% |

## Turnover, fees, activity

- trades: 514 (0.22/day); active days 9%
- turnover 13.5x equity/year; fees 1.35% of equity/year ($818 total)
- average gross exposure 0.03; brake active 3.6% of hours
- correlation of daily returns with s3v2 baseline: 0.11
