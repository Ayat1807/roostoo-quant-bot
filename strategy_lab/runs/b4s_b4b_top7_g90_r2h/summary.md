# Run: b4s_b4b_top7_g90_r2h

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'top_n': 7, 'gross': 0.9}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -29.81% | -5.19% | 0.05 | 0.07 | -90.30% | -0.06 | 0.03 |
| in_sample | 2020-02-15 → 2024-12-31 | +52.74% | +9.06% | 0.42 | 0.57 | -78.53% | 0.12 | 0.39 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -54.14% | -35.82% | -1.32 | -1.79 | -65.34% | -0.55 | -1.28 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -33.03% | -33.03% | -1.35 | -1.86 | -45.87% | -0.72 | -1.36 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.87% | 37% | -19.80% | -21.48% | -3.58 | 13 | 37% |
| out_of_sample | 628 | -3.33% | 28% | -13.65% | -14.49% | -6.03 | 13 | 30% |
| in_sample | 1768 | -1.25% | 40% | -19.80% | -21.48% | -2.42 | 13 | 40% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.750% | 49% | 4.41 | +240.26% |
| bull | 687 | 28% | +0.202% | 44% | 1.64 | +232.65% |
| bear | 400 | 17% | -0.266% | 28% | -3.68 | -66.80% |
| chop | 1160 | 48% | -0.134% | 33% | -1.76 | -81.32% |

## Turnover, fees, activity

- trades: 101030 (41.68/day); active days 85%
- turnover 412.2x equity/year; fees 41.22% of equity/year ($252,945 total)
- average gross exposure 0.31; brake active 51.2% of hours
- correlation of daily returns with s3v2 baseline: 0.38
