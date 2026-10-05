# Run: b_r1_bo_dual

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'dual': True}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +21.47% | +3.10% | 0.25 | 0.35 | -44.50% | 0.07 | 0.24 |
| in_sample | 2020-02-15 → 2024-12-31 | +44.52% | +7.83% | 0.42 | 0.59 | -44.50% | 0.18 | 0.41 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -16.28% | -11.20% | -0.45 | -0.66 | -26.90% | -0.42 | -0.53 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -0.94% | -1.26% | 0.05 | 0.08 | -13.55% | -0.09 | 0.02 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.53% | 39% | -9.24% | -11.46% | -2.13 | 8 | 2% |
| out_of_sample | 532 | -0.81% | 40% | -7.84% | -8.63% | -2.39 | 9 | 0% |
| in_sample | 1768 | -0.45% | 39% | -9.24% | -11.46% | -1.85 | 8 | 2% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.287% | 35% | 3.45 | +59.31% |
| bull | 659 | 28% | +0.077% | 32% | 0.91 | +52.70% |
| bear | 399 | 17% | -0.131% | 22% | -2.89 | -41.71% |
| chop | 1099 | 47% | -0.008% | 26% | -0.15 | -14.34% |

## Turnover, fees, activity

- trades: 3460 (1.49/day); active days 56%
- turnover 95.1x equity/year; fees 9.51% of equity/year ($7,506 total)
- average gross exposure 0.16; brake active 14.4% of hours
- correlation of daily returns with s3v2 baseline: 0.19
