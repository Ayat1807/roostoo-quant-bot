# Run: b3s_xsmom_tm10_r4h

Strategy `xsmom`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'PAXGUSDT', 'POLUSDT', 'ICPUSDT', 'TRXUSDT', 'LISTAUSDT', 'STOUSDT', 'CAKEUSDT', 'TUTUSDT', 'SOLUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +104.12% | +11.34% | 0.52 | 0.74 | -43.79% | 0.26 | 0.53 |
| in_sample | 2020-02-15 → 2024-12-31 | +17.61% | +3.38% | 0.26 | 0.35 | -43.79% | 0.08 | 0.24 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +73.55% | +36.84% | 1.09 | 1.62 | -29.67% | 1.24 | 1.35 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +82.11% | +82.11% | 1.79 | 2.70 | -29.67% | 2.77 | 2.45 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.77% | 41% | -16.34% | -18.73% | -2.35 | 12 | 31% |
| out_of_sample | 628 | -0.61% | 46% | -16.34% | -18.73% | -1.24 | 14 | 51% |
| in_sample | 1768 | -0.78% | 40% | -10.80% | -14.43% | -2.81 | 12 | 24% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.106% | 47% | 1.13 | +17.13% |
| bull | 687 | 28% | +0.151% | 42% | 1.82 | +159.68% |
| bear | 400 | 17% | -0.104% | 28% | -1.81 | -35.50% |
| chop | 1160 | 48% | +0.015% | 35% | 0.20 | +5.58% |

## Turnover, fees, activity

- trades: 29878 (12.33/day); active days 83%
- turnover 158.8x equity/year; fees 15.88% of equity/year ($58,622 total)
- average gross exposure 0.21; brake active 38.0% of hours
- correlation of daily returns with s3v2 baseline: 0.21
