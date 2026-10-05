# Run: d_1h_r12h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +244.57% | +21.41% | 1.29 | 1.92 | -15.78% | 1.36 | 1.56 |
| in_sample | 2020-02-15 → 2024-12-31 | +143.52% | +20.00% | 1.24 | 1.84 | -15.78% | 1.27 | 1.49 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +41.53% | +26.14% | 1.47 | 2.17 | -13.11% | 1.99 | 1.91 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +22.75% | +31.53% | 1.58 | 2.36 | -13.11% | 2.41 | 2.14 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.14% | 46% | -5.45% | -6.95% | -1.08 | 14 | 100% |
| out_of_sample | 532 | -0.18% | 47% | -4.83% | -5.31% | -1.08 | 14 | 100% |
| in_sample | 1768 | -0.12% | 47% | -5.45% | -6.95% | -0.88 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.250% | 56% | 3.32 | +50.33% |
| bull | 659 | 28% | +0.089% | 52% | 2.51 | +77.46% |
| bear | 399 | 17% | +0.066% | 49% | 1.65 | +28.46% |
| chop | 1099 | 47% | +0.006% | 43% | 0.14 | +3.05% |

## Turnover, fees, activity

- trades: 5571 (2.39/day); active days 100%
- turnover 50.8x equity/year; fees 5.08% of equity/year ($32,636 total)
- average gross exposure 0.18; brake active 13.1% of hours
- correlation of daily returns with s3v2 baseline: 0.90
