# Run: u_kadoo30

Strategy `s3v2`; universe `{'type': 'top_volume', 'n': 30, 'reselect': 'monthly', 'min_history_days': 60, 'min_quote_volume_usd': 5000000.0, 'rank_pool': 'all', 'trade': 'roostoo'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +63.38% | +7.67% | 0.96 | 1.37 | -9.30% | 0.83 | 1.08 |
| in_sample | 2020-02-15 → 2024-12-31 | +54.00% | +9.25% | 1.01 | 1.44 | -9.30% | 0.99 | 1.18 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +6.14% | +3.45% | 0.99 | 1.54 | -2.81% | 1.23 | 1.28 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +5.94% | +5.94% | 1.41 | 2.25 | -2.81% | 2.12 | 1.96 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.12% | 40% | -4.02% | -6.14% | -2.81 | 14 | 100% |
| out_of_sample | 628 | -0.11% | 34% | -1.32% | -2.13% | -3.98 | 14 | 100% |
| in_sample | 1768 | -0.13% | 42% | -4.02% | -6.14% | -2.19 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.185% | 56% | 4.02 | +37.49% |
| bull | 687 | 28% | +0.047% | 51% | 2.22 | +37.32% |
| bear | 400 | 17% | +0.002% | 48% | 0.19 | +0.84% |
| chop | 1160 | 48% | -0.012% | 41% | -0.72 | -13.10% |

## Turnover, fees, activity

- trades: 3509 (1.45/day); active days 100%
- turnover 17.0x equity/year; fees 1.70% of equity/year ($7,625 total)
- average gross exposure 0.08; brake active 0.6% of hours
- correlation of daily returns with s3v2 baseline: 0.67
