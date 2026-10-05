# Run: d_15m_r12h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [96, 288, 672, 1344], 'vol_win': 1344, 'regime_win': 1344, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'bars_per_year': 35040}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +229.84% | +20.58% | 1.28 | 1.90 | -12.24% | 1.68 | 1.65 |
| in_sample | 2020-02-15 → 2024-12-31 | +154.90% | +21.13% | 1.33 | 1.97 | -12.24% | 1.73 | 1.71 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +29.43% | +18.83% | 1.15 | 1.69 | -10.94% | 1.72 | 1.54 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +18.38% | +25.31% | 1.33 | 1.98 | -10.71% | 2.36 | 1.90 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.11% | 47% | -5.37% | -6.68% | -0.83 | 14 | 100% |
| out_of_sample | 532 | -0.40% | 41% | -4.41% | -5.13% | -2.25 | 14 | 100% |
| in_sample | 1768 | -0.05% | 49% | -5.37% | -6.68% | -0.36 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.230% | 56% | 3.27 | +45.49% |
| bull | 659 | 28% | +0.088% | 52% | 2.43 | +75.85% |
| bear | 399 | 17% | +0.060% | 44% | 1.53 | +25.77% |
| chop | 1099 | 47% | +0.008% | 43% | 0.18 | +4.90% |

## Turnover, fees, activity

- trades: 5526 (2.37/day); active days 100%
- turnover 49.6x equity/year; fees 4.96% of equity/year ($32,361 total)
- average gross exposure 0.17; brake active 13.3% of hours
- correlation of daily returns with s3v2 baseline: 0.87
