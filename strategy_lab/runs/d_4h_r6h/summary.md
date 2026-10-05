# Run: d_4h_r6h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +260.82% | +22.29% | 1.33 | 1.97 | -15.47% | 1.44 | 1.62 |
| in_sample | 2020-02-15 → 2024-12-31 | +190.87% | +24.45% | 1.44 | 2.15 | -14.15% | 1.73 | 1.81 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +24.13% | +15.55% | 0.97 | 1.42 | -15.47% | 1.00 | 1.16 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +9.13% | +12.39% | 0.73 | 1.09 | -15.47% | 0.80 | 0.89 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.08% | 48% | -5.19% | -6.90% | -0.63 | 14 | 99% |
| out_of_sample | 532 | -0.34% | 43% | -5.19% | -5.37% | -2.59 | 14 | 100% |
| in_sample | 1768 | -0.01% | 49% | -4.60% | -6.90% | -0.06 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.305% | 57% | 4.10 | +65.05% |
| bull | 659 | 28% | +0.090% | 50% | 2.59 | +78.36% |
| bear | 399 | 17% | +0.065% | 45% | 1.63 | +28.29% |
| chop | 1099 | 47% | +0.002% | 41% | 0.04 | -2.12% |

## Turnover, fees, activity

- trades: 6481 (2.78/day); active days 100%
- turnover 64.1x equity/year; fees 6.41% of equity/year ($45,354 total)
- average gross exposure 0.18; brake active 10.9% of hours
- correlation of daily returns with s3v2 baseline: 0.87
