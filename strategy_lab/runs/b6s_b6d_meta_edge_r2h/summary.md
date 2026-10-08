# Run: b6s_b6d_meta_edge_r2h

Strategy `s3v2x_meta`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'size_map': 'edge'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +35.89% | +4.73% | 0.72 | 1.14 | -12.99% | 0.36 | 0.78 |
| in_sample | 2020-02-15 → 2024-12-31 | +45.32% | +7.96% | 1.03 | 1.63 | -12.99% | 0.61 | 1.15 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -6.49% | -3.74% | -1.66 | -2.28 | -8.34% | -0.45 | -1.55 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -6.25% | -6.25% | -2.67 | -3.60 | -8.24% | -0.76 | -2.47 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.03% | 46% | -4.59% | -6.85% | -1.24 | 13 | 46% |
| out_of_sample | 628 | -0.10% | 31% | -1.46% | -1.69% | -5.01 | 12 | 22% |
| in_sample | 1768 | +0.02% | 52% | -4.59% | -6.85% | 1.06 | 14 | 54% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.073% | 49% | 4.04 | +13.50% |
| bull | 687 | 28% | +0.014% | 42% | 0.86 | +9.81% |
| bear | 400 | 17% | +0.000% | 35% | 0.01 | -0.01% |
| chop | 1160 | 48% | +0.011% | 36% | 0.39 | +11.98% |

## Turnover, fees, activity

- trades: 4377 (1.81/day); active days 91%
- turnover 34.8x equity/year; fees 3.48% of equity/year ($15,768 total)
- average gross exposure 0.03; brake active 1.6% of hours
- correlation of daily returns with s3v2 baseline: 0.36
