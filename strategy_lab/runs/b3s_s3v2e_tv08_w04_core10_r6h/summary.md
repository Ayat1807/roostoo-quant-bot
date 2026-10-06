# Run: b3s_s3v2e_tv08_w04_core10_r6h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.4, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +293.03% | +22.89% | 0.81 | 1.17 | -38.11% | 0.60 | 0.89 |
| in_sample | 2020-02-15 → 2024-12-31 | +315.45% | +33.87% | 1.07 | 1.54 | -34.16% | 0.99 | 1.23 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -5.33% | -3.07% | 0.05 | 0.08 | -38.11% | -0.08 | 0.02 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -15.63% | -15.63% | -0.42 | -0.60 | -37.06% | -0.42 | -0.49 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.83% | 43% | -14.24% | -17.94% | -1.92 | 14 | 93% |
| out_of_sample | 628 | -1.42% | 39% | -14.12% | -14.88% | -3.17 | 14 | 86% |
| in_sample | 1768 | -0.54% | 45% | -14.24% | -17.94% | -1.24 | 14 | 95% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.673% | 54% | 4.41 | +203.07% |
| bull | 687 | 28% | +0.178% | 48% | 2.30 | +215.55% |
| bear | 400 | 17% | +0.014% | 41% | 0.17 | +0.45% |
| chop | 1160 | 48% | -0.062% | 40% | -0.80 | -56.71% |

## Turnover, fees, activity

- trades: 14587 (6.02/day); active days 99%
- turnover 165.8x equity/year; fees 16.58% of equity/year ($173,602 total)
- average gross exposure 0.35; brake active 51.3% of hours
- correlation of daily returns with s3v2 baseline: 0.77
