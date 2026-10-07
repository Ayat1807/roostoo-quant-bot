# Run: b4b_top7

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'top_n': 7}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +207.24% | +18.42% | 0.68 | 0.93 | -54.36% | 0.34 | 0.68 |
| in_sample | 2020-02-15 → 2024-12-31 | +331.22% | +34.90% | 1.03 | 1.41 | -52.42% | 0.67 | 1.07 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -28.93% | -17.66% | -0.63 | -0.86 | -43.71% | -0.40 | -0.65 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -7.13% | -7.13% | -0.22 | -0.31 | -28.23% | -0.25 | -0.26 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.96% | 39% | -20.39% | -22.19% | -2.23 | 12 | 33% |
| out_of_sample | 628 | -1.97% | 30% | -12.57% | -12.90% | -4.62 | 12 | 21% |
| in_sample | 1768 | -0.64% | 43% | -20.39% | -22.19% | -1.40 | 12 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.659% | 47% | 4.58 | +198.01% |
| bull | 687 | 28% | +0.214% | 50% | 2.15 | +284.58% |
| bear | 400 | 17% | -0.224% | 30% | -3.86 | -60.17% |
| chop | 1160 | 48% | -0.027% | 35% | -0.41 | -32.69% |

## Turnover, fees, activity

- trades: 16811 (6.94/day); active days 83%
- turnover 137.2x equity/year; fees 13.72% of equity/year ($152,116 total)
- average gross exposure 0.27; brake active 47.4% of hours
- correlation of daily returns with s3v2 baseline: 0.40
