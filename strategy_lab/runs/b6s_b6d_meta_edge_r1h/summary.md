# Run: b6s_b6d_meta_edge_r1h

Strategy `s3v2x_meta`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'size_map': 'edge'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +16.07% | +2.27% | 0.37 | 0.56 | -16.90% | 0.13 | 0.38 |
| in_sample | 2020-02-15 → 2024-12-31 | +25.99% | +4.85% | 0.66 | 1.00 | -16.90% | 0.29 | 0.68 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -7.87% | -4.56% | -1.93 | -2.67 | -9.33% | -0.49 | -1.80 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -6.92% | -6.92% | -2.76 | -3.78 | -8.87% | -0.78 | -2.57 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.05% | 43% | -5.82% | -6.69% | -2.40 | 13 | 47% |
| out_of_sample | 628 | -0.14% | 29% | -1.87% | -2.12% | -5.27 | 12 | 23% |
| in_sample | 1768 | -0.01% | 49% | -5.82% | -6.69% | -0.44 | 14 | 55% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.070% | 50% | 3.64 | +12.97% |
| bull | 687 | 28% | +0.010% | 40% | 0.59 | +6.65% |
| bear | 400 | 17% | -0.001% | 34% | -0.13 | -0.29% |
| chop | 1160 | 48% | +0.001% | 34% | 0.02 | -0.78% |

## Turnover, fees, activity

- trades: 5212 (2.15/day); active days 91%
- turnover 43.8x equity/year; fees 4.38% of equity/year ($17,569 total)
- average gross exposure 0.03; brake active 2.0% of hours
- correlation of daily returns with s3v2 baseline: 0.37
