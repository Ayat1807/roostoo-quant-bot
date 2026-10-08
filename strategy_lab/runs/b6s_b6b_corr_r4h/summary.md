# Run: b6s_b6b_corr_r4h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'corr_filter': True}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +208.68% | +18.50% | 1.26 | 1.90 | -16.29% | 1.14 | 1.48 |
| in_sample | 2020-02-15 → 2024-12-31 | +141.25% | +19.77% | 1.31 | 1.98 | -16.29% | 1.21 | 1.55 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +28.04% | +15.10% | 1.12 | 1.67 | -12.44% | 1.21 | 1.37 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +30.04% | +30.04% | 1.70 | 2.57 | -12.44% | 2.42 | 2.26 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.16% | 44% | -6.98% | -7.50% | -1.56 | 14 | 99% |
| out_of_sample | 628 | -0.35% | 37% | -4.31% | -6.55% | -3.56 | 14 | 100% |
| in_sample | 1768 | -0.10% | 46% | -6.98% | -7.50% | -1.00 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.302% | 51% | 4.09 | +67.19% |
| bull | 687 | 28% | +0.074% | 46% | 2.32 | +64.43% |
| bear | 400 | 17% | +0.063% | 42% | 1.89 | +27.63% |
| chop | 1160 | 48% | -0.006% | 39% | -0.14 | -9.92% |

## Turnover, fees, activity

- trades: 6612 (2.73/day); active days 100%
- turnover 59.3x equity/year; fees 5.93% of equity/year ($36,067 total)
- average gross exposure 0.15; brake active 9.0% of hours
- correlation of daily returns with s3v2 baseline: 0.74
