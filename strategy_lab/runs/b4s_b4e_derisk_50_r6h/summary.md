# Run: b4s_b4e_derisk_50_r6h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +187.56% | +17.24% | 0.62 | 0.85 | -75.18% | 0.23 | 0.59 |
| in_sample | 2020-02-15 → 2024-12-31 | +306.40% | +33.27% | 0.92 | 1.27 | -69.73% | 0.48 | 0.93 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -29.41% | -17.97% | -0.56 | -0.78 | -48.87% | -0.37 | -0.59 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -7.39% | -7.39% | -0.17 | -0.24 | -28.76% | -0.26 | -0.23 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.03% | 40% | -14.14% | -16.37% | -2.14 | 13 | 36% |
| out_of_sample | 628 | -1.91% | 34% | -12.60% | -13.53% | -4.51 | 12 | 31% |
| in_sample | 1768 | -0.69% | 43% | -14.14% | -16.37% | -1.33 | 13 | 38% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.674% | 47% | 4.11 | +199.89% |
| bull | 687 | 28% | +0.274% | 48% | 2.29 | +449.98% |
| bear | 400 | 17% | -0.242% | 32% | -3.47 | -63.41% |
| chop | 1160 | 48% | -0.054% | 36% | -0.75 | -52.35% |

## Turnover, fees, activity

- trades: 34932 (14.41/day); active days 84%
- turnover 271.5x equity/year; fees 27.15% of equity/year ($341,119 total)
- average gross exposure 0.30; brake active 47.9% of hours
- correlation of daily returns with s3v2 baseline: 0.38
