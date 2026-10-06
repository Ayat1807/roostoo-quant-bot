# Run: b3s_s3v2e_tv08_w04_core10_r1h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.4, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -8.92% | -1.40% | 0.11 | 0.16 | -70.17% | -0.02 | 0.09 |
| in_sample | 2020-02-15 → 2024-12-31 | +18.34% | +3.51% | 0.27 | 0.38 | -63.63% | 0.06 | 0.25 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -22.99% | -13.81% | -0.32 | -0.47 | -43.73% | -0.32 | -0.38 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -16.79% | -16.79% | -0.43 | -0.65 | -43.73% | -0.38 | -0.50 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.50% | 38% | -15.29% | -17.59% | -3.60 | 14 | 95% |
| out_of_sample | 628 | -1.75% | 38% | -11.76% | -15.16% | -3.95 | 14 | 88% |
| in_sample | 1768 | -1.45% | 38% | -15.29% | -17.59% | -3.49 | 14 | 97% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.812% | 52% | 4.93 | +282.04% |
| bull | 687 | 28% | +0.054% | 42% | 0.71 | +34.79% |
| bear | 400 | 17% | -0.031% | 38% | -0.40 | -15.40% |
| chop | 1160 | 48% | -0.119% | 34% | -1.46 | -77.91% |

## Turnover, fees, activity

- trades: 23651 (9.76/day); active days 99%
- turnover 249.6x equity/year; fees 24.96% of equity/year ($115,271 total)
- average gross exposure 0.31; brake active 59.0% of hours
- correlation of daily returns with s3v2 baseline: 0.75
