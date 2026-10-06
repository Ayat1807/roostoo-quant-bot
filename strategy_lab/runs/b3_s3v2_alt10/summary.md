# Run: b3_s3v2_alt10

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT', 'BTCUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'no_trade': ['BTCUSDT'], 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +48.21% | +6.11% | 0.66 | 0.96 | -12.86% | 0.47 | 0.73 |
| in_sample | 2020-02-15 → 2024-12-31 | +28.71% | +5.31% | 0.61 | 0.90 | -12.86% | 0.41 | 0.67 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +15.18% | +8.37% | 0.79 | 1.12 | -9.33% | 0.90 | 0.96 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +13.78% | +13.78% | 1.10 | 1.58 | -9.33% | 1.48 | 1.41 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.17% | 41% | -4.65% | -6.45% | -1.94 | 14 | 99% |
| out_of_sample | 628 | -0.16% | 43% | -4.65% | -6.45% | -1.32 | 14 | 100% |
| in_sample | 1768 | -0.17% | 41% | -4.61% | -5.21% | -2.14 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.134% | 52% | 2.22 | +25.10% |
| bull | 687 | 28% | +0.038% | 49% | 1.54 | +28.99% |
| bear | 400 | 17% | +0.010% | 46% | 0.52 | +3.74% |
| chop | 1160 | 48% | -0.010% | 46% | -0.45 | -11.46% |

## Turnover, fees, activity

- trades: 3832 (1.58/day); active days 100%
- turnover 28.4x equity/year; fees 2.84% of equity/year ($10,448 total)
- average gross exposure 0.12; brake active 2.2% of hours
- correlation of daily returns with s3v2 baseline: 0.61
