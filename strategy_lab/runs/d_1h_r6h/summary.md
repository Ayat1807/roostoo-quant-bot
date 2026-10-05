# Run: d_1h_r6h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +214.23% | +19.66% | 1.22 | 1.81 | -16.45% | 1.20 | 1.45 |
| in_sample | 2020-02-15 → 2024-12-31 | +146.46% | +20.29% | 1.26 | 1.88 | -16.45% | 1.23 | 1.50 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +27.58% | +17.68% | 1.08 | 1.59 | -15.53% | 1.14 | 1.30 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +9.66% | +13.12% | 0.77 | 1.14 | -15.53% | 0.84 | 0.94 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.12% | 47% | -5.69% | -6.90% | -0.91 | 14 | 99% |
| out_of_sample | 532 | -0.32% | 44% | -5.21% | -5.71% | -2.04 | 14 | 100% |
| in_sample | 1768 | -0.08% | 48% | -5.69% | -6.90% | -0.53 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.305% | 58% | 4.22 | +65.10% |
| bull | 659 | 28% | +0.065% | 49% | 1.90 | +51.13% |
| bear | 399 | 17% | +0.065% | 44% | 1.63 | +28.20% |
| chop | 1099 | 47% | +0.004% | 40% | 0.09 | +0.58% |

## Turnover, fees, activity

- trades: 6421 (2.76/day); active days 100%
- turnover 62.8x equity/year; fees 6.28% of equity/year ($41,444 total)
- average gross exposure 0.18; brake active 12.4% of hours
- correlation of daily returns with s3v2 baseline: 0.88
