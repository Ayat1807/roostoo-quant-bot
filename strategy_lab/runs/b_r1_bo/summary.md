# Run: b_r1_bo

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +109.23% | +12.27% | 0.52 | 0.72 | -69.66% | 0.18 | 0.50 |
| in_sample | 2020-02-15 → 2024-12-31 | +169.03% | +22.47% | 0.77 | 1.06 | -69.66% | 0.32 | 0.75 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -22.71% | -15.82% | -0.46 | -0.66 | -38.44% | -0.41 | -0.53 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +1.48% | +1.98% | 0.21 | 0.31 | -18.85% | 0.11 | 0.22 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -1.02% | 38% | -13.10% | -13.10% | -3.16 | 6 | 1% |
| out_of_sample | 532 | -1.81% | 31% | -8.96% | -10.67% | -5.50 | 5 | 0% |
| in_sample | 1768 | -0.77% | 40% | -13.10% | -13.10% | -2.35 | 6 | 1% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.434% | 34% | 3.30 | +98.31% |
| bull | 659 | 28% | +0.223% | 31% | 2.05 | +278.58% |
| bear | 399 | 17% | -0.186% | 19% | -3.17 | -53.57% |
| chop | 1099 | 47% | -0.037% | 23% | -0.52 | -39.98% |

## Turnover, fees, activity

- trades: 2717 (1.17/day); active days 45%
- turnover 71.0x equity/year; fees 7.10% of equity/year ($7,080 total)
- average gross exposure 0.23; brake active 33.0% of hours
- correlation of daily returns with s3v2 baseline: 0.21
