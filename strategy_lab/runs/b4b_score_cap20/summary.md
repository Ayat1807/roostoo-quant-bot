# Run: b4b_score_cap20

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'score', 'coin_cap': 0.2}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +466.91% | +29.86% | 0.88 | 1.23 | -60.11% | 0.50 | 0.91 |
| in_sample | 2020-02-15 → 2024-12-31 | +642.12% | +50.76% | 1.22 | 1.70 | -60.11% | 0.84 | 1.30 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -23.90% | -14.39% | -0.40 | -0.56 | -43.42% | -0.33 | -0.45 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +1.97% | +1.97% | 0.20 | 0.29 | -28.08% | 0.07 | 0.20 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.09% | 41% | -18.57% | -18.57% | -2.39 | 12 | 32% |
| out_of_sample | 628 | -1.94% | 37% | -12.68% | -16.36% | -4.06 | 12 | 21% |
| in_sample | 1768 | -0.80% | 43% | -18.57% | -18.57% | -1.73 | 12 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.703% | 49% | 3.96 | +211.73% |
| bull | 687 | 28% | +0.291% | 49% | 2.47 | +520.61% |
| bear | 400 | 17% | -0.243% | 35% | -3.73 | -63.43% |
| chop | 1160 | 48% | -0.008% | 36% | -0.11 | -19.87% |

## Turnover, fees, activity

- trades: 14290 (5.90/day); active days 82%
- turnover 173.7x equity/year; fees 17.37% of equity/year ($312,850 total)
- average gross exposure 0.30; brake active 47.3% of hours
- correlation of daily returns with s3v2 baseline: 0.37
