# Run: d_4h_r24h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +149.09% | +15.38% | 0.99 | 1.43 | -19.79% | 0.78 | 1.10 |
| in_sample | 2020-02-15 → 2024-12-31 | +83.40% | +13.23% | 0.89 | 1.28 | -19.79% | 0.67 | 0.98 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +35.95% | +22.79% | 1.30 | 1.89 | -15.22% | 1.50 | 1.60 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +15.00% | +20.55% | 1.11 | 1.62 | -15.22% | 1.35 | 1.38 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.18% | 45% | -7.98% | -8.62% | -1.32 | 14 | 100% |
| out_of_sample | 532 | -0.12% | 47% | -7.98% | -8.62% | -0.66 | 14 | 100% |
| in_sample | 1768 | -0.18% | 45% | -5.21% | -7.36% | -1.37 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.192% | 58% | 2.75 | +36.61% |
| bull | 659 | 28% | +0.097% | 53% | 2.80 | +86.68% |
| bear | 399 | 17% | +0.023% | 48% | 0.59 | +8.28% |
| chop | 1099 | 47% | -0.003% | 44% | -0.08 | -7.13% |

## Turnover, fees, activity

- trades: 4922 (2.11/day); active days 100%
- turnover 41.6x equity/year; fees 4.16% of equity/year ($22,211 total)
- average gross exposure 0.19; brake active 10.6% of hours
- correlation of daily returns with s3v2 baseline: 0.99
