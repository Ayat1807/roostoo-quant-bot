# Run: b_r2_bo_gated

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R2', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +18.17% | +2.65% | 0.25 | 0.34 | -29.29% | 0.09 | 0.24 |
| in_sample | 2020-02-15 → 2024-12-31 | +32.44% | +5.92% | 0.43 | 0.60 | -29.29% | 0.20 | 0.43 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -10.78% | -7.34% | -0.53 | -0.73 | -18.29% | -0.40 | -0.57 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -6.39% | -8.45% | -1.16 | -1.40 | -6.82% | -1.24 | -1.28 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 14% | -9.57% | -9.98% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 7% | -8.21% | -8.98% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 17% | -9.57% | -9.98% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.014% | 5% | 0.34 | +1.83% |
| bull | 659 | 28% | +0.080% | 16% | 1.11 | +59.83% |
| bear | 399 | 17% | -0.004% | 1% | -0.96 | -1.63% |
| chop | 1099 | 47% | -0.026% | 6% | -1.01 | -26.19% |

## Turnover, fees, activity

- trades: 605 (0.26/day); active days 9%
- turnover 16.9x equity/year; fees 1.69% of equity/year ($1,175 total)
- average gross exposure 0.04; brake active 4.8% of hours
- correlation of daily returns with s3v2 baseline: 0.11
