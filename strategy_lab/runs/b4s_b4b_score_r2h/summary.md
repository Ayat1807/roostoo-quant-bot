# Run: b4s_b4b_score_r2h

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'score'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +41.31% | +5.35% | 0.33 | 0.46 | -86.07% | 0.06 | 0.30 |
| in_sample | 2020-02-15 → 2024-12-31 | +195.55% | +24.85% | 0.74 | 1.04 | -75.69% | 0.33 | 0.74 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -52.30% | -34.37% | -1.29 | -1.80 | -62.65% | -0.55 | -1.27 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -26.14% | -26.14% | -0.98 | -1.39 | -41.11% | -0.64 | -1.04 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.79% | 37% | -15.08% | -18.38% | -3.41 | 13 | 37% |
| out_of_sample | 628 | -2.82% | 27% | -12.50% | -15.02% | -5.54 | 13 | 26% |
| in_sample | 1768 | -1.30% | 40% | -15.08% | -18.38% | -2.42 | 13 | 41% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.988% | 48% | 4.98 | +401.33% |
| bull | 687 | 28% | +0.186% | 45% | 1.50 | +196.66% |
| bear | 400 | 17% | -0.285% | 27% | -4.15 | -69.15% |
| chop | 1160 | 48% | -0.090% | 33% | -1.12 | -69.20% |

## Turnover, fees, activity

- trades: 83999 (34.65/day); active days 85%
- turnover 435.1x equity/year; fees 43.51% of equity/year ($423,364 total)
- average gross exposure 0.29; brake active 51.9% of hours
- correlation of daily returns with s3v2 baseline: 0.36
