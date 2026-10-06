# Run: b3s_xsmom_tm10_r6h

Strategy `xsmom`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'PAXGUSDT', 'POLUSDT', 'ICPUSDT', 'TRXUSDT', 'LISTAUSDT', 'STOUSDT', 'CAKEUSDT', 'TUTUSDT', 'SOLUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +217.17% | +18.99% | 0.76 | 1.08 | -43.51% | 0.44 | 0.79 |
| in_sample | 2020-02-15 → 2024-12-31 | +54.55% | +9.33% | 0.48 | 0.65 | -43.51% | 0.21 | 0.47 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +105.23% | +50.53% | 1.37 | 2.09 | -21.35% | 2.37 | 1.96 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +114.35% | +114.35% | 2.25 | 3.52 | -21.35% | 5.36 | 3.69 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.68% | 42% | -12.36% | -14.78% | -1.97 | 12 | 30% |
| out_of_sample | 628 | -0.08% | 50% | -12.36% | -14.78% | -0.09 | 14 | 51% |
| in_sample | 1768 | -0.78% | 40% | -10.47% | -12.05% | -2.72 | 12 | 23% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.128% | 47% | 1.42 | +22.06% |
| bull | 687 | 28% | +0.210% | 44% | 2.54 | +288.87% |
| bear | 400 | 17% | -0.096% | 32% | -1.67 | -33.55% |
| chop | 1160 | 48% | +0.012% | 37% | 0.16 | +2.11% |

## Turnover, fees, activity

- trades: 21346 (8.81/day); active days 82%
- turnover 143.0x equity/year; fees 14.30% of equity/year ($65,080 total)
- average gross exposure 0.21; brake active 37.9% of hours
- correlation of daily returns with s3v2 baseline: 0.22
