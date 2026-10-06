# Run: b3s_s3v2e_tv08_w04_core10_r4h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.4, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +273.50% | +21.95% | 0.78 | 1.15 | -36.40% | 0.60 | 0.88 |
| in_sample | 2020-02-15 → 2024-12-31 | +235.94% | +28.17% | 0.94 | 1.37 | -36.40% | 0.77 | 1.06 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +11.25% | +6.26% | 0.35 | 0.52 | -29.29% | 0.21 | 0.38 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +0.63% | +0.63% | 0.18 | 0.27 | -28.65% | 0.02 | 0.17 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.77% | 44% | -13.40% | -16.78% | -1.99 | 14 | 96% |
| out_of_sample | 628 | -1.44% | 41% | -9.96% | -14.56% | -3.37 | 14 | 85% |
| in_sample | 1768 | -0.57% | 45% | -13.40% | -16.78% | -1.42 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.747% | 53% | 4.75 | +243.51% |
| bull | 687 | 28% | +0.139% | 46% | 1.79 | +140.38% |
| bear | 400 | 17% | +0.006% | 38% | 0.07 | -2.46% |
| chop | 1160 | 48% | -0.049% | 38% | -0.57 | -50.74% |

## Turnover, fees, activity

- trades: 16029 (6.61/day); active days 100%
- turnover 180.4x equity/year; fees 18.04% of equity/year ($164,059 total)
- average gross exposure 0.33; brake active 54.9% of hours
- correlation of daily returns with s3v2 baseline: 0.78
