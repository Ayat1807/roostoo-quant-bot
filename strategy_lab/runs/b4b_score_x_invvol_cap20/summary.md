# Run: b4b_score_x_invvol_cap20

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'score_x_invvol', 'coin_cap': 0.2}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +232.15% | +19.82% | 0.69 | 0.94 | -66.51% | 0.30 | 0.67 |
| in_sample | 2020-02-15 → 2024-12-31 | +481.16% | +43.40% | 1.13 | 1.55 | -61.39% | 0.71 | 1.17 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -43.04% | -27.40% | -1.13 | -1.54 | -49.22% | -0.56 | -1.12 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -8.52% | -8.52% | -0.26 | -0.37 | -25.74% | -0.33 | -0.33 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.31% | 39% | -17.54% | -18.39% | -2.81 | 12 | 32% |
| out_of_sample | 628 | -2.37% | 31% | -11.08% | -12.51% | -5.56 | 12 | 20% |
| in_sample | 1768 | -0.85% | 42% | -17.54% | -18.39% | -2.00 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.630% | 47% | 3.63 | +175.21% |
| bull | 687 | 28% | +0.270% | 49% | 2.42 | +446.21% |
| bear | 400 | 17% | -0.254% | 31% | -4.00 | -64.86% |
| chop | 1160 | 48% | -0.031% | 33% | -0.44 | -37.13% |

## Turnover, fees, activity

- trades: 14452 (5.96/day); active days 82%
- turnover 181.8x equity/year; fees 18.18% of equity/year ($268,052 total)
- average gross exposure 0.30; brake active 47.0% of hours
- correlation of daily returns with s3v2 baseline: 0.38
