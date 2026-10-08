# Run: b6s_b6d_meta_edge_r12h

Strategy `s3v2x_meta`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'size_map': 'edge'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +31.12% | +4.17% | 0.64 | 0.97 | -14.73% | 0.28 | 0.66 |
| in_sample | 2020-02-15 → 2024-12-31 | +33.97% | +6.17% | 0.81 | 1.22 | -14.73% | 0.42 | 0.86 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -2.13% | -1.22% | -0.77 | -1.07 | -3.63% | -0.33 | -0.76 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -1.91% | -1.91% | -1.18 | -1.66 | -3.60% | -0.53 | -1.18 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.00% | 49% | -6.53% | -8.27% | -0.22 | 13 | 38% |
| out_of_sample | 628 | -0.03% | 43% | -1.27% | -1.41% | -3.00 | 11 | 14% |
| in_sample | 1768 | +0.01% | 52% | -6.53% | -8.27% | 0.85 | 13 | 47% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.054% | 42% | 2.36 | +9.76% |
| bull | 687 | 28% | +0.005% | 42% | 0.35 | +3.14% |
| bear | 400 | 17% | -0.001% | 37% | -0.16 | -0.28% |
| chop | 1160 | 48% | +0.016% | 36% | 0.56 | +18.98% |

## Turnover, fees, activity

- trades: 2780 (1.15/day); active days 87%
- turnover 15.1x equity/year; fees 1.51% of equity/year ($6,514 total)
- average gross exposure 0.03; brake active 2.0% of hours
- correlation of daily returns with s3v2 baseline: 0.37
