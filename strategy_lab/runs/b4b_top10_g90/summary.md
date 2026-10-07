# Run: b4b_top10_g90

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'top_n': 10, 'gross': 0.9}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +110.02% | +11.82% | 0.51 | 0.68 | -60.90% | 0.19 | 0.48 |
| in_sample | 2020-02-15 → 2024-12-31 | +177.14% | +23.22% | 0.77 | 1.04 | -51.85% | 0.45 | 0.78 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -24.38% | -14.70% | -0.47 | -0.64 | -42.88% | -0.34 | -0.50 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -7.75% | -7.75% | -0.22 | -0.31 | -30.13% | -0.26 | -0.27 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.07% | 40% | -17.28% | -20.50% | -2.56 | 12 | 32% |
| out_of_sample | 628 | -1.96% | 32% | -12.01% | -12.74% | -4.95 | 12 | 21% |
| in_sample | 1768 | -0.68% | 42% | -17.28% | -20.50% | -1.46 | 12 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.520% | 44% | 3.39 | +131.28% |
| bull | 687 | 28% | +0.219% | 49% | 2.23 | +299.35% |
| bear | 400 | 17% | -0.198% | 28% | -3.21 | -55.96% |
| chop | 1160 | 48% | -0.049% | 34% | -0.74 | -48.37% |

## Turnover, fees, activity

- trades: 20156 (8.32/day); active days 83%
- turnover 135.5x equity/year; fees 13.55% of equity/year ($108,533 total)
- average gross exposure 0.27; brake active 45.1% of hours
- correlation of daily returns with s3v2 baseline: 0.41
