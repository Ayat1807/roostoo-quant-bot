# Run: b_r1_tr_jump

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'jump_filter': True}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +115.06% | +12.76% | 0.61 | 0.85 | -38.95% | 0.33 | 0.62 |
| in_sample | 2020-02-15 → 2024-12-31 | +122.69% | +17.82% | 0.78 | 1.07 | -38.95% | 0.46 | 0.80 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -3.43% | -2.30% | 0.01 | 0.01 | -22.33% | -0.10 | -0.02 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -6.66% | -8.81% | -0.43 | -0.61 | -16.66% | -0.53 | -0.53 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.57% | 40% | -9.31% | -9.31% | -2.47 | 10 | 16% |
| out_of_sample | 532 | -1.11% | 33% | -8.25% | -8.46% | -4.00 | 11 | 17% |
| in_sample | 1768 | -0.46% | 42% | -9.31% | -9.31% | -1.97 | 10 | 15% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.247% | 31% | 3.33 | +49.51% |
| bull | 659 | 28% | +0.113% | 40% | 1.43 | +95.75% |
| bear | 399 | 17% | -0.128% | 25% | -2.53 | -41.10% |
| chop | 1099 | 47% | +0.026% | 33% | 0.45 | +24.75% |

## Turnover, fees, activity

- trades: 5675 (2.44/day); active days 66%
- turnover 85.0x equity/year; fees 8.50% of equity/year ($9,419 total)
- average gross exposure 0.22; brake active 14.4% of hours
- correlation of daily returns with s3v2 baseline: 0.28
