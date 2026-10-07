# Run: b5_betahedge_btc7d

Strategy `beta_hedge`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'btc_7d'}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +272.94% | +21.92% | 0.74 | 1.02 | -65.08% | 0.34 | 0.73 |
| in_sample | 2020-02-15 → 2024-12-31 | +462.68% | +42.45% | 1.13 | 1.55 | -58.51% | 0.73 | 1.18 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -33.95% | -21.02% | -0.74 | -1.03 | -43.29% | -0.49 | -0.78 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -7.69% | -7.69% | -0.21 | -0.30 | -25.66% | -0.30 | -0.27 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.24% | 39% | -17.50% | -19.99% | -2.61 | 12 | 30% |
| out_of_sample | 628 | -2.32% | 33% | -11.84% | -14.96% | -5.20 | 12 | 20% |
| in_sample | 1768 | -0.87% | 42% | -17.50% | -19.99% | -1.86 | 12 | 33% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.681% | 44% | 4.39 | +206.62% |
| bull | 687 | 28% | +0.266% | 48% | 2.34 | +428.73% |
| bear | 400 | 17% | -0.228% | 30% | -3.56 | -60.99% |
| chop | 1160 | 48% | -0.036% | 34% | -0.50 | -41.03% |

## Turnover, fees, activity

- trades: 14434 (5.95/day); active days 82%
- turnover 173.0x equity/year; fees 17.30% of equity/year ($269,427 total)
- average gross exposure 0.30; brake active 47.6% of hours
- correlation of daily returns with s3v2 baseline: 0.40
