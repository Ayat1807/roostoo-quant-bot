# Run: b3_s3v2e_tv06_alt10

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT', 'BTCUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.6, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'no_trade': ['BTCUSDT'], 'n_divisor': 10, 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +60.44% | +7.38% | 0.51 | 0.73 | -23.78% | 0.31 | 0.54 |
| in_sample | 2020-02-15 → 2024-12-31 | +27.49% | +5.10% | 0.40 | 0.58 | -19.86% | 0.26 | 0.43 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +25.88% | +13.99% | 0.76 | 1.07 | -23.78% | 0.59 | 0.83 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +41.05% | +41.05% | 1.74 | 2.49 | -13.15% | 3.12 | 2.45 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.43% | 41% | -9.75% | -11.53% | -2.41 | 14 | 99% |
| out_of_sample | 628 | -0.63% | 43% | -9.75% | -11.53% | -2.27 | 14 | 98% |
| in_sample | 1768 | -0.38% | 40% | -5.65% | -7.57% | -2.47 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.181% | 49% | 2.21 | +34.62% |
| bull | 687 | 28% | +0.058% | 49% | 1.38 | +45.73% |
| bear | 400 | 17% | +0.033% | 48% | 0.82 | +12.77% |
| chop | 1160 | 48% | -0.024% | 44% | -0.58 | -27.08% |

## Turnover, fees, activity

- trades: 5385 (2.22/day); active days 100%
- turnover 53.2x equity/year; fees 5.32% of equity/year ($19,777 total)
- average gross exposure 0.21; brake active 15.5% of hours
- correlation of daily returns with s3v2 baseline: 0.66
