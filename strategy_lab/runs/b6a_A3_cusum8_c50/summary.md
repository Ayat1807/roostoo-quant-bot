# Run: b6a_A3_cusum8_c50

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +166.56% | +15.91% | 1.07 | 1.59 | -16.46% | 0.97 | 1.25 |
| in_sample | 2020-02-15 → 2024-12-31 | +93.74% | +14.51% | 1.01 | 1.50 | -16.46% | 0.88 | 1.16 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +37.73% | +19.98% | 1.25 | 1.83 | -12.85% | 1.55 | 1.57 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +20.96% | +20.96% | 1.19 | 1.75 | -12.85% | 1.63 | 1.55 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.18% | 45% | -7.21% | -7.82% | -1.53 | 14 | 100% |
| out_of_sample | 628 | -0.17% | 47% | -6.02% | -6.42% | -1.10 | 14 | 100% |
| in_sample | 1768 | -0.18% | 45% | -7.21% | -7.82% | -1.57 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.225% | 56% | 2.95 | +45.95% |
| bull | 687 | 28% | +0.099% | 53% | 2.98 | +94.48% |
| bear | 400 | 17% | +0.043% | 48% | 1.29 | +17.98% |
| chop | 1160 | 48% | -0.014% | 43% | -0.35 | -18.01% |

## Turnover, fees, activity

- trades: 5195 (2.14/day); active days 100%
- turnover 40.5x equity/year; fees 4.05% of equity/year ($22,222 total)
- average gross exposure 0.18; brake active 9.0% of hours
- correlation of daily returns with s3v2 baseline: 0.85
