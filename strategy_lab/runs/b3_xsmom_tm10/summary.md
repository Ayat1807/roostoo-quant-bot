# Run: b3_xsmom_tm10

Strategy `xsmom`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'PAXGUSDT', 'POLUSDT', 'ICPUSDT', 'TRXUSDT', 'LISTAUSDT', 'STOUSDT', 'CAKEUSDT', 'TUTUSDT', 'SOLUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +188.76% | +17.32% | 0.69 | 0.96 | -34.85% | 0.50 | 0.74 |
| in_sample | 2020-02-15 → 2024-12-31 | +43.27% | +7.64% | 0.41 | 0.56 | -34.85% | 0.22 | 0.41 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +101.30% | +48.89% | 1.26 | 1.82 | -24.40% | 2.00 | 1.71 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +129.43% | +129.43% | 2.18 | 3.17 | -22.44% | 5.77 | 3.65 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.51% | 44% | -14.42% | -20.54% | -1.60 | 12 | 26% |
| out_of_sample | 628 | -1.08% | 45% | -14.42% | -20.54% | -2.30 | 13 | 44% |
| in_sample | 1768 | -0.39% | 43% | -11.26% | -13.16% | -1.34 | 11 | 20% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.089% | 39% | 0.83 | +12.67% |
| bull | 687 | 28% | +0.178% | 45% | 2.18 | +212.05% |
| bear | 400 | 17% | -0.085% | 27% | -1.48 | -30.41% |
| chop | 1160 | 48% | +0.026% | 35% | 0.34 | +20.25% |

## Turnover, fees, activity

- trades: 8618 (3.56/day); active days 79%
- turnover 97.1x equity/year; fees 9.71% of equity/year ($41,461 total)
- average gross exposure 0.21; brake active 37.6% of hours
- correlation of daily returns with s3v2 baseline: 0.22
