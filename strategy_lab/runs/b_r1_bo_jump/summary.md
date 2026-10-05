# Run: b_r1_bo_jump

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'jump_filter': True}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | -31.14% | -5.68% | -0.17 | -0.25 | -57.89% | -0.10 | -0.18 |
| in_sample | 2020-02-15 → 2024-12-31 | +10.66% | +2.10% | 0.20 | 0.29 | -57.89% | 0.04 | 0.19 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -37.92% | -27.29% | -1.61 | -2.31 | -43.45% | -0.63 | -1.59 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -23.91% | -30.61% | -2.37 | -3.39 | -28.02% | -1.09 | -2.39 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.76% | 38% | -8.10% | -8.62% | -2.92 | 7 | 0% |
| out_of_sample | 532 | -1.90% | 27% | -8.06% | -8.39% | -6.76 | 8 | 0% |
| in_sample | 1768 | -0.45% | 42% | -8.10% | -8.62% | -1.54 | 7 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.209% | 32% | 2.74 | +40.16% |
| bull | 659 | 28% | +0.087% | 34% | 1.35 | +69.12% |
| bear | 399 | 17% | -0.150% | 20% | -3.41 | -45.89% |
| chop | 1099 | 47% | -0.052% | 26% | -1.05 | -46.31% |

## Turnover, fees, activity

- trades: 2310 (0.99/day); active days 50%
- turnover 65.1x equity/year; fees 6.51% of equity/year ($4,035 total)
- average gross exposure 0.16; brake active 7.8% of hours
- correlation of daily returns with s3v2 baseline: 0.17
