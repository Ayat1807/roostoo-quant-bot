# Run: b5_slowshort_10

Strategy `slow_short`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'wa': 0.1}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -36.55% | -6.62% | -0.32 | -0.45 | -44.56% | -0.15 | -0.32 |
| in_sample | 2020-02-15 → 2024-12-31 | -27.75% | -6.44% | -0.31 | -0.44 | -34.01% | -0.19 | -0.32 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -11.88% | -6.94% | -0.33 | -0.45 | -22.95% | -0.30 | -0.37 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +2.39% | +2.39% | 0.22 | 0.32 | -14.01% | 0.17 | 0.25 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | +0.00% | 26% | -12.63% | -14.80% | 0.00 | 5 | 16% |
| out_of_sample | 628 | -0.00% | 30% | -10.22% | -11.23% | -0.51 | 7 | 21% |
| in_sample | 1768 | +0.00% | 25% | -12.63% | -14.80% | 0.00 | 3 | 14% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | -0.035% | 24% | -0.36 | -8.80% |
| bull | 687 | 28% | -0.005% | 5% | -1.05 | -3.17% |
| bear | 400 | 17% | +0.142% | 49% | 2.13 | +70.56% |
| chop | 1160 | 48% | -0.072% | 23% | -1.93 | -57.87% |

## Turnover, fees, activity

- trades: 3402 (1.40/day); active days 42%
- turnover 23.9x equity/year; fees 2.39% of equity/year ($6,379 total)
- average gross exposure 0.09; brake active 17.7% of hours
- correlation of daily returns with s3v2 baseline: 0.41
