# Run: b5_betahedge_btc30

Strategy `beta_hedge`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'btc_below_30d'}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +310.60% | +23.70% | 0.81 | 1.13 | -53.60% | 0.44 | 0.83 |
| in_sample | 2020-02-15 → 2024-12-31 | +384.27% | +38.14% | 1.09 | 1.51 | -47.35% | 0.81 | 1.17 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -15.39% | -9.07% | -0.25 | -0.36 | -31.60% | -0.29 | -0.31 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -3.78% | -3.78% | -0.07 | -0.11 | -22.96% | -0.16 | -0.11 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.12% | 38% | -18.00% | -19.84% | -3.03 | 11 | 26% |
| out_of_sample | 628 | -1.40% | 33% | -11.84% | -14.96% | -4.89 | 11 | 17% |
| in_sample | 1768 | -0.95% | 40% | -18.00% | -19.84% | -2.46 | 12 | 29% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.636% | 42% | 4.33 | +185.84% |
| bull | 687 | 28% | +0.249% | 48% | 2.22 | +373.31% |
| bear | 400 | 17% | -0.065% | 31% | -1.75 | -23.63% |
| chop | 1160 | 48% | -0.072% | 33% | -1.12 | -60.26% |

## Turnover, fees, activity

- trades: 13329 (5.50/day); active days 77%
- turnover 162.4x equity/year; fees 16.24% of equity/year ($252,576 total)
- average gross exposure 0.29; brake active 39.7% of hours
- correlation of daily returns with s3v2 baseline: 0.42
