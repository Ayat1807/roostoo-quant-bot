# Run: d_30m_r24h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [48, 144, 336, 672], 'vol_win': 672, 'regime_win': 672, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'bars_per_year': 17520}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +200.32% | +18.82% | 1.16 | 1.67 | -20.27% | 0.93 | 1.29 |
| in_sample | 2020-02-15 → 2024-12-31 | +123.41% | +17.90% | 1.14 | 1.63 | -20.27% | 0.88 | 1.26 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +34.58% | +21.96% | 1.23 | 1.78 | -15.46% | 1.42 | 1.51 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +19.66% | +27.13% | 1.35 | 1.98 | -15.46% | 1.75 | 1.72 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.12% | 47% | -7.31% | -9.22% | -0.94 | 14 | 99% |
| out_of_sample | 532 | -0.10% | 47% | -5.57% | -6.39% | -0.77 | 14 | 100% |
| in_sample | 1768 | -0.11% | 47% | -7.31% | -9.22% | -0.76 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.156% | 54% | 1.93 | +27.71% |
| bull | 659 | 28% | +0.114% | 55% | 3.16 | +109.13% |
| bear | 399 | 17% | +0.049% | 46% | 1.32 | +20.39% |
| chop | 1099 | 47% | -0.001% | 45% | -0.02 | -3.96% |

## Turnover, fees, activity

- trades: 4931 (2.12/day); active days 100%
- turnover 42.0x equity/year; fees 4.20% of equity/year ($22,398 total)
- average gross exposure 0.19; brake active 11.7% of hours
- correlation of daily returns with s3v2 baseline: 0.90
