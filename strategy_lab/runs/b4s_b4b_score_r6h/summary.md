# Run: b4s_b4b_score_r6h

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'score'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +449.34% | +29.25% | 0.85 | 1.19 | -73.25% | 0.40 | 0.85 |
| in_sample | 2020-02-15 → 2024-12-31 | +553.32% | +46.88% | 1.11 | 1.57 | -67.69% | 0.69 | 1.17 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -16.11% | -9.51% | -0.19 | -0.27 | -42.16% | -0.23 | -0.23 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +6.78% | +6.78% | 0.38 | 0.54 | -24.48% | 0.28 | 0.41 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.18% | 41% | -16.84% | -19.06% | -2.31 | 13 | 37% |
| out_of_sample | 628 | -1.97% | 36% | -12.15% | -13.66% | -4.20 | 12 | 31% |
| in_sample | 1768 | -0.74% | 43% | -16.84% | -19.06% | -1.35 | 13 | 39% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.743% | 51% | 3.84 | +228.74% |
| bull | 687 | 28% | +0.299% | 48% | 2.30 | +533.04% |
| bear | 400 | 17% | -0.249% | 37% | -3.59 | -64.34% |
| chop | 1160 | 48% | -0.014% | 38% | -0.18 | -25.97% |

## Turnover, fees, activity

- trades: 34345 (14.17/day); active days 84%
- turnover 285.4x equity/year; fees 28.54% of equity/year ($585,980 total)
- average gross exposure 0.30; brake active 49.5% of hours
- correlation of daily returns with s3v2 baseline: 0.35
