# Run: b4s_b4b_score_r4h

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'score'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +333.04% | +24.70% | 0.76 | 1.07 | -73.02% | 0.34 | 0.76 |
| in_sample | 2020-02-15 → 2024-12-31 | +613.66% | +49.56% | 1.16 | 1.64 | -67.48% | 0.73 | 1.22 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -39.47% | -24.84% | -0.83 | -1.17 | -52.19% | -0.48 | -0.86 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -15.52% | -15.52% | -0.52 | -0.73 | -30.97% | -0.50 | -0.60 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.16% | 41% | -16.14% | -17.36% | -2.39 | 13 | 36% |
| out_of_sample | 628 | -2.06% | 32% | -12.46% | -13.65% | -4.86 | 12 | 27% |
| in_sample | 1768 | -0.69% | 45% | -16.14% | -17.36% | -1.22 | 13 | 39% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.877% | 51% | 4.48 | +314.15% |
| bull | 687 | 28% | +0.263% | 47% | 2.03 | +394.31% |
| bear | 400 | 17% | -0.267% | 30% | -3.93 | -66.78% |
| chop | 1160 | 48% | -0.027% | 34% | -0.34 | -36.33% |

## Turnover, fees, activity

- trades: 47138 (19.45/day); active days 85%
- turnover 329.5x equity/year; fees 32.95% of equity/year ($627,551 total)
- average gross exposure 0.29; brake active 51.2% of hours
- correlation of daily returns with s3v2 baseline: 0.35
