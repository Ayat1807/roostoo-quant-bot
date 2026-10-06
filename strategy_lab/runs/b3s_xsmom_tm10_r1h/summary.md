# Run: b3s_xsmom_tm10_r1h

Strategy `xsmom`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'PAXGUSDT', 'POLUSDT', 'ICPUSDT', 'TRXUSDT', 'LISTAUSDT', 'STOUSDT', 'CAKEUSDT', 'TUTUSDT', 'SOLUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -31.09% | -5.45% | -0.06 | -0.09 | -70.19% | -0.08 | -0.08 |
| in_sample | 2020-02-15 → 2024-12-31 | -46.24% | -11.94% | -0.38 | -0.51 | -67.17% | -0.18 | -0.37 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +28.17% | +15.16% | 0.59 | 0.87 | -34.08% | 0.44 | 0.66 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +70.58% | +70.58% | 1.67 | 2.52 | -33.38% | 2.11 | 2.14 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.43% | 35% | -11.27% | -14.34% | -3.78 | 12 | 33% |
| out_of_sample | 628 | -1.53% | 41% | -11.27% | -13.51% | -3.04 | 14 | 55% |
| in_sample | 1768 | -1.43% | 32% | -11.14% | -14.34% | -4.40 | 12 | 26% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.124% | 42% | 1.36 | +21.12% |
| bull | 687 | 28% | +0.106% | 40% | 1.30 | +91.09% |
| bear | 400 | 17% | -0.122% | 26% | -2.19 | -40.09% |
| chop | 1160 | 48% | -0.050% | 31% | -0.69 | -49.66% |

## Turnover, fees, activity

- trades: 100517 (41.47/day); active days 84%
- turnover 245.6x equity/year; fees 24.56% of equity/year ($57,046 total)
- average gross exposure 0.21; brake active 42.1% of hours
- correlation of daily returns with s3v2 baseline: 0.21
