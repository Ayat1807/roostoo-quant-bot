# Run: b_r4_tr_gated_jump

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R4', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally', 'jump_filter': True}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | -7.74% | -1.26% | -0.11 | -0.15 | -17.90% | -0.07 | -0.11 |
| in_sample | 2020-02-15 → 2024-12-31 | -5.21% | -1.09% | -0.08 | -0.11 | -17.90% | -0.06 | -0.09 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -2.67% | -1.79% | -0.21 | -0.28 | -9.93% | -0.18 | -0.23 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -3.12% | -4.16% | -2.01 | -2.39 | -3.45% | -1.20 | -1.92 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 14% | -6.25% | -8.40% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 9% | -4.72% | -6.81% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 15% | -6.25% | -8.40% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.026% | 5% | 1.45 | +4.37% |
| bull | 659 | 28% | +0.012% | 12% | 0.34 | +6.49% |
| bear | 399 | 17% | -0.001% | 0% | -0.65 | -0.60% |
| chop | 1099 | 47% | -0.016% | 3% | -1.11 | -16.50% |

## Turnover, fees, activity

- trades: 534 (0.23/day); active days 11%
- turnover 11.0x equity/year; fees 1.10% of equity/year ($689 total)
- average gross exposure 0.02; brake active 0.6% of hours
- correlation of daily returns with s3v2 baseline: 0.15
