# Run: b_r1_bo_gated

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +17.30% | +2.53% | 0.24 | 0.33 | -45.56% | 0.06 | 0.22 |
| in_sample | 2020-02-15 → 2024-12-31 | +28.80% | +5.32% | 0.39 | 0.54 | -45.56% | 0.12 | 0.37 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -8.93% | -6.06% | -0.47 | -0.66 | -16.95% | -0.36 | -0.51 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -3.76% | -5.00% | -0.75 | -1.00 | -5.37% | -0.93 | -0.90 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 16% | -9.81% | -9.81% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 17% | -8.42% | -8.42% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 15% | -9.81% | -9.81% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.136% | 11% | 2.43 | +24.88% |
| bull | 659 | 28% | +0.065% | 16% | 0.95 | +45.50% |
| bear | 399 | 17% | -0.005% | 3% | -0.93 | -2.00% |
| chop | 1099 | 47% | -0.037% | 11% | -1.45 | -34.12% |

## Turnover, fees, activity

- trades: 745 (0.32/day); active days 10%
- turnover 19.9x equity/year; fees 1.99% of equity/year ($1,409 total)
- average gross exposure 0.04; brake active 6.0% of hours
- correlation of daily returns with s3v2 baseline: 0.12
