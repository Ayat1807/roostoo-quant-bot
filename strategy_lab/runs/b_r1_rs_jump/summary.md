# Run: b_r1_rs_jump

Strategy `sat_rs`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'jump_filter': True}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | -7.48% | -1.21% | 0.07 | 0.09 | -53.13% | -0.02 | 0.05 |
| in_sample | 2020-02-15 → 2024-12-31 | +12.61% | +2.46% | 0.22 | 0.30 | -47.11% | 0.05 | 0.20 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -17.84% | -12.31% | -0.44 | -0.62 | -25.61% | -0.48 | -0.52 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -19.80% | -25.54% | -1.38 | -1.91 | -21.53% | -1.19 | -1.53 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.25% | 42% | -10.92% | -11.10% | -1.33 | 6 | 0% |
| out_of_sample | 532 | -0.86% | 40% | -9.74% | -10.13% | -3.00 | 7 | 0% |
| in_sample | 1768 | -0.07% | 43% | -10.92% | -11.10% | -0.72 | 6 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.264% | 38% | 3.25 | +53.53% |
| bull | 659 | 28% | +0.136% | 41% | 1.73 | +127.48% |
| bear | 399 | 17% | -0.226% | 23% | -4.66 | -60.16% |
| chop | 1099 | 47% | -0.031% | 32% | -0.53 | -33.51% |

## Turnover, fees, activity

- trades: 1760 (0.76/day); active days 44%
- turnover 46.7x equity/year; fees 4.67% of equity/year ($3,531 total)
- average gross exposure 0.23; brake active 21.0% of hours
- correlation of daily returns with s3v2 baseline: 0.19
