# Run: b4s_b4b_top7_g90_r1h

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'top_n': 7, 'gross': 0.9}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -75.98% | -19.33% | -0.37 | -0.50 | -95.22% | -0.20 | -0.37 |
| in_sample | 2020-02-15 → 2024-12-31 | -36.98% | -9.02% | -0.03 | -0.04 | -84.84% | -0.11 | -0.06 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -61.95% | -42.29% | -1.68 | -2.28 | -72.31% | -0.58 | -1.59 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -39.29% | -39.29% | -1.74 | -2.40 | -51.26% | -0.77 | -1.71 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -2.36% | 34% | -19.62% | -21.06% | -4.08 | 13 | 36% |
| out_of_sample | 628 | -3.66% | 26% | -13.37% | -14.31% | -6.34 | 13 | 30% |
| in_sample | 1768 | -1.79% | 37% | -19.62% | -21.06% | -3.03 | 13 | 38% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.750% | 53% | 4.49 | +241.33% |
| bull | 687 | 28% | +0.113% | 45% | 0.95 | +82.98% |
| bear | 400 | 17% | -0.299% | 31% | -4.16 | -70.98% |
| chop | 1160 | 48% | -0.163% | 31% | -2.12 | -86.74% |

## Turnover, fees, activity

- trades: 180695 (74.54/day); active days 86%
- turnover 546.1x equity/year; fees 54.61% of equity/year ($194,802 total)
- average gross exposure 0.31; brake active 52.5% of hours
- correlation of daily returns with s3v2 baseline: 0.38
