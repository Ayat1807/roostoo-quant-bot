# Run: b_r1_rs_rfng

Strategy `sat_rs`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'riskoff': 'fng'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +48.08% | +6.35% | 0.35 | 0.48 | -62.38% | 0.10 | 0.33 |
| in_sample | 2020-02-15 → 2024-12-31 | +80.36% | +12.84% | 0.53 | 0.72 | -62.38% | 0.21 | 0.51 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -17.90% | -12.35% | -0.30 | -0.42 | -28.84% | -0.43 | -0.39 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -19.88% | -25.65% | -1.02 | -1.40 | -24.07% | -1.07 | -1.19 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.23% | 38% | -11.92% | -13.25% | -1.04 | 4 | 0% |
| out_of_sample | 532 | -0.32% | 41% | -9.29% | -9.84% | -1.55 | 4 | 0% |
| in_sample | 1768 | -0.16% | 37% | -11.92% | -13.25% | -0.67 | 4 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.233% | 22% | 2.82 | +45.53% |
| bull | 659 | 28% | +0.186% | 30% | 1.93 | +204.18% |
| bear | 399 | 17% | -0.207% | 14% | -3.29 | -57.54% |
| chop | 1099 | 47% | -0.010% | 28% | -0.12 | -21.23% |

## Turnover, fees, activity

- trades: 1702 (0.73/day); active days 31%
- turnover 42.4x equity/year; fees 4.24% of equity/year ($3,759 total)
- average gross exposure 0.25; brake active 37.8% of hours
- correlation of daily returns with s3v2 baseline: 0.24
