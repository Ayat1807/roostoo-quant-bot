# Run: d_2h_r24h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +148.27% | +15.32% | 0.99 | 1.43 | -20.29% | 0.76 | 1.09 |
| in_sample | 2020-02-15 → 2024-12-31 | +80.80% | +12.90% | 0.87 | 1.26 | -20.29% | 0.64 | 0.95 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +37.46% | +23.70% | 1.34 | 1.96 | -14.72% | 1.61 | 1.67 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +16.44% | +22.57% | 1.20 | 1.75 | -14.72% | 1.53 | 1.52 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.18% | 45% | -7.98% | -8.62% | -1.31 | 14 | 100% |
| out_of_sample | 532 | -0.11% | 48% | -7.98% | -8.62% | -0.55 | 14 | 100% |
| in_sample | 1768 | -0.18% | 45% | -5.30% | -7.28% | -1.40 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.193% | 58% | 2.75 | +36.65% |
| bull | 659 | 28% | +0.096% | 54% | 2.78 | +85.89% |
| bear | 399 | 17% | +0.022% | 48% | 0.56 | +7.88% |
| chop | 1099 | 47% | -0.003% | 44% | -0.07 | -6.73% |

## Turnover, fees, activity

- trades: 4947 (2.12/day); active days 100%
- turnover 41.9x equity/year; fees 4.19% of equity/year ($22,160 total)
- average gross exposure 0.19; brake active 10.7% of hours
- correlation of daily returns with s3v2 baseline: 0.99
