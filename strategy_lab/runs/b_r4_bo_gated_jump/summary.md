# Run: b_r4_bo_gated_jump

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R4', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally', 'jump_filter': True}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +10.71% | +1.61% | 0.24 | 0.34 | -12.58% | 0.13 | 0.25 |
| in_sample | 2020-02-15 → 2024-12-31 | +5.43% | +1.09% | 0.17 | 0.24 | -12.58% | 0.09 | 0.17 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +5.01% | +3.32% | 0.54 | 0.80 | -4.05% | 0.82 | 0.73 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +0.19% | +0.25% | 0.10 | 0.13 | -1.62% | 0.15 | 0.13 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 15% | -5.53% | -6.70% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 14% | -1.94% | -4.05% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 16% | -5.53% | -6.70% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.028% | 5% | 1.56 | +4.84% |
| bull | 659 | 28% | +0.034% | 11% | 0.93 | +23.30% |
| bear | 399 | 17% | -0.005% | 0% | -0.99 | -1.85% |
| chop | 1099 | 47% | -0.012% | 3% | -0.90 | -12.74% |

## Turnover, fees, activity

- trades: 361 (0.16/day); active days 8%
- turnover 10.2x equity/year; fees 1.02% of equity/year ($678 total)
- average gross exposure 0.02; brake active 0.0% of hours
- correlation of daily returns with s3v2 baseline: 0.09
