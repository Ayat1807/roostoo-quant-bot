# Run: b12_aggr_mid

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.6, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2}`; band 0.05; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +136.88% | +13.87% | 0.67 | 0.97 | -22.29% | 0.62 | 0.78 |
| in_sample | 2020-02-15 → 2024-12-31 | +96.12% | +14.79% | 0.72 | 1.04 | -22.29% | 0.66 | 0.83 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +21.37% | +11.65% | 0.57 | 0.82 | -19.96% | 0.58 | 0.67 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +13.41% | +13.41% | 0.63 | 0.92 | -19.96% | 0.67 | 0.76 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.44% | 43% | -11.24% | -11.56% | -1.73 | 14 | 99% |
| out_of_sample | 628 | -0.51% | 44% | -11.24% | -11.56% | -1.47 | 14 | 96% |
| in_sample | 1768 | -0.40% | 43% | -7.06% | -9.73% | -1.73 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.325% | 51% | 3.39 | +72.07% |
| bull | 687 | 28% | +0.121% | 53% | 2.09 | +120.66% |
| bear | 400 | 17% | +0.026% | 45% | 0.40 | +7.58% |
| chop | 1160 | 48% | -0.036% | 42% | -0.59 | -38.86% |

## Turnover, fees, activity

- trades: 10280 (4.24/day); active days 100%
- turnover 87.1x equity/year; fees 8.71% of equity/year ($48,570 total)
- average gross exposure 0.28; brake active 39.6% of hours
- correlation of daily returns with s3v2 baseline: 0.83
