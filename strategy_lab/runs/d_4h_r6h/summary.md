# Run: d_4h_r6h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +238.91% | +21.09% | 1.28 | 1.90 | -16.43% | 1.28 | 1.53 |
| in_sample | 2020-02-15 → 2024-12-31 | +140.39% | +19.68% | 1.22 | 1.82 | -16.43% | 1.20 | 1.45 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +41.02% | +25.84% | 1.45 | 2.14 | -12.80% | 2.02 | 1.90 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +22.40% | +31.03% | 1.56 | 2.32 | -12.80% | 2.42 | 2.12 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.15% | 46% | -5.64% | -6.95% | -1.26 | 14 | 100% |
| out_of_sample | 532 | -0.23% | 47% | -4.70% | -5.38% | -1.67 | 14 | 100% |
| in_sample | 1768 | -0.12% | 46% | -5.64% | -6.95% | -0.89 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.239% | 55% | 3.17 | +47.49% |
| bull | 659 | 28% | +0.090% | 52% | 2.51 | +77.96% |
| bear | 399 | 17% | +0.066% | 49% | 1.65 | +28.41% |
| chop | 1099 | 47% | +0.006% | 43% | 0.14 | +3.06% |

## Turnover, fees, activity

- trades: 5493 (2.36/day); active days 100%
- turnover 50.1x equity/year; fees 5.01% of equity/year ($31,792 total)
- average gross exposure 0.18; brake active 12.9% of hours
- correlation of daily returns with s3v2 baseline: 0.90
