# Run: d_15m_r24h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [96, 288, 672, 1344], 'vol_win': 1344, 'regime_win': 1344, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'bars_per_year': 35040}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +184.05% | +17.78% | 1.12 | 1.64 | -18.63% | 0.95 | 1.28 |
| in_sample | 2020-02-15 → 2024-12-31 | +125.71% | +18.15% | 1.16 | 1.70 | -18.63% | 0.97 | 1.32 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +25.96% | +16.68% | 1.02 | 1.47 | -14.18% | 1.18 | 1.25 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +17.43% | +23.97% | 1.27 | 1.86 | -14.18% | 1.69 | 1.63 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.17% | 45% | -6.91% | -7.41% | -1.30 | 14 | 99% |
| out_of_sample | 532 | -0.27% | 43% | -5.40% | -5.73% | -1.71 | 14 | 100% |
| in_sample | 1768 | -0.14% | 46% | -6.91% | -7.41% | -0.96 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.174% | 54% | 2.27 | +32.05% |
| bull | 659 | 28% | +0.114% | 54% | 3.20 | +108.57% |
| bear | 399 | 17% | +0.058% | 44% | 1.53 | +24.76% |
| chop | 1099 | 47% | -0.012% | 44% | -0.31 | -15.09% |

## Turnover, fees, activity

- trades: 5013 (2.15/day); active days 100%
- turnover 41.2x equity/year; fees 4.12% of equity/year ($23,335 total)
- average gross exposure 0.18; brake active 13.2% of hours
- correlation of daily returns with s3v2 baseline: 0.89
