# Run: b6b_hmm3

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 3}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +195.21% | +17.71% | 1.07 | 1.55 | -18.87% | 0.94 | 1.22 |
| in_sample | 2020-02-15 → 2024-12-31 | +115.01% | +16.98% | 1.05 | 1.52 | -18.87% | 0.90 | 1.19 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +37.43% | +19.83% | 1.12 | 1.64 | -15.39% | 1.29 | 1.38 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +22.90% | +22.90% | 1.12 | 1.65 | -15.39% | 1.49 | 1.44 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.23% | 44% | -5.98% | -7.48% | -1.66 | 14 | 99% |
| out_of_sample | 628 | -0.24% | 43% | -5.98% | -6.44% | -1.36 | 14 | 98% |
| in_sample | 1768 | -0.22% | 44% | -5.47% | -7.48% | -1.72 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.266% | 56% | 2.93 | +55.45% |
| bull | 687 | 28% | +0.116% | 53% | 3.04 | +117.22% |
| bear | 400 | 17% | +0.051% | 48% | 1.34 | +21.51% |
| chop | 1160 | 48% | -0.023% | 43% | -0.53 | -25.98% |

## Turnover, fees, activity

- trades: 5462 (2.25/day); active days 100%
- turnover 46.1x equity/year; fees 4.61% of equity/year ($27,198 total)
- average gross exposure 0.20; brake active 11.8% of hours
- correlation of daily returns with s3v2 baseline: 0.86
