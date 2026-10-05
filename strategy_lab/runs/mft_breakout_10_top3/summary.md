# Run: mft_breakout_10_top3

Strategy `breakout`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'top_k': 3}`; band 0.06; brake True; shorts False; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-05 | -98.95% | -49.63% | -1.04 | -1.50 | -99.73% | -0.50 | -1.06 |
| in_sample | 2020-02-15 → 2024-12-31 | -93.19% | -42.33% | -0.70 | -1.01 | -98.32% | -0.43 | -0.74 |
| out_of_sample | 2025-01-01 → 2026-10-05 | -84.72% | -65.62% | -2.34 | -3.51 | -88.03% | -0.75 | -2.33 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -70.12% | -70.12% | -3.14 | -4.42 | -75.45% | -0.93 | -2.99 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2411 | -4.62% | 29% | -24.19% | -25.51% | -4.59 | 12 | 26% |
| out_of_sample | 629 | -4.92% | 20% | -16.97% | -17.97% | -5.92 | 12 | 11% |
| in_sample | 1768 | -4.52% | 32% | -24.19% | -25.51% | -4.26 | 13 | 32% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.683% | 41% | 2.45 | +165.27% |
| bull | 687 | 28% | +0.007% | 37% | 0.04 | -24.02% |
| bear | 400 | 17% | -0.485% | 24% | -4.21 | -86.98% |
| chop | 1160 | 48% | -0.253% | 30% | -2.40 | -95.80% |

## Turnover, fees, activity

- trades: 28237 (11.64/day); active days 87%
- turnover 1003.7x equity/year; fees 100.37% of equity/year ($193,642 total)
- average gross exposure 0.40; brake active 61.8% of hours
- correlation of daily returns with s3v2 baseline: 0.23
