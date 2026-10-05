# Run: d_2h_r12h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +238.38% | +21.06% | 1.28 | 1.89 | -16.73% | 1.26 | 1.52 |
| in_sample | 2020-02-15 → 2024-12-31 | +139.56% | +19.60% | 1.21 | 1.80 | -16.73% | 1.17 | 1.44 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +41.29% | +25.99% | 1.46 | 2.16 | -12.93% | 2.01 | 1.91 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +22.61% | +31.34% | 1.57 | 2.34 | -12.93% | 2.42 | 2.14 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.15% | 46% | -5.52% | -6.95% | -1.19 | 14 | 100% |
| out_of_sample | 532 | -0.18% | 47% | -4.82% | -5.31% | -1.50 | 14 | 100% |
| in_sample | 1768 | -0.13% | 46% | -5.52% | -6.95% | -0.89 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.251% | 56% | 3.33 | +50.62% |
| bull | 659 | 28% | +0.090% | 52% | 2.52 | +77.95% |
| bear | 399 | 17% | +0.065% | 49% | 1.63 | +28.14% |
| chop | 1099 | 47% | +0.004% | 43% | 0.10 | +0.97% |

## Turnover, fees, activity

- trades: 5557 (2.39/day); active days 100%
- turnover 50.6x equity/year; fees 5.06% of equity/year ($32,155 total)
- average gross exposure 0.18; brake active 13.0% of hours
- correlation of daily returns with s3v2 baseline: 0.90
