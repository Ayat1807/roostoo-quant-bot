# Run: b_r3_rs

Strategy `sat_rs`; universe `{'type': 'satellite', 'rule': 'R3', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +70.21% | +8.70% | 0.43 | 0.58 | -51.35% | 0.17 | 0.41 |
| in_sample | 2020-02-15 → 2024-12-31 | +145.19% | +20.17% | 0.73 | 0.99 | -49.97% | 0.40 | 0.74 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -30.58% | -21.65% | -0.83 | -1.15 | -38.63% | -0.56 | -0.88 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -13.57% | -17.72% | -0.68 | -0.96 | -19.01% | -0.93 | -0.87 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.49% | 40% | -10.09% | -11.48% | -1.85 | 5 | 0% |
| out_of_sample | 532 | -1.40% | 33% | -8.94% | -10.02% | -4.11 | 5 | 0% |
| in_sample | 1768 | -0.20% | 42% | -10.09% | -11.48% | -1.06 | 4 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.175% | 29% | 1.87 | +31.07% |
| bull | 659 | 28% | +0.279% | 42% | 2.78 | +455.36% |
| bear | 399 | 17% | -0.234% | 24% | -3.79 | -61.89% |
| chop | 1099 | 47% | -0.036% | 29% | -0.52 | -38.65% |

## Turnover, fees, activity

- trades: 1553 (0.67/day); active days 36%
- turnover 35.7x equity/year; fees 3.57% of equity/year ($4,471 total)
- average gross exposure 0.26; brake active 34.3% of hours
- correlation of daily returns with s3v2 baseline: 0.27
