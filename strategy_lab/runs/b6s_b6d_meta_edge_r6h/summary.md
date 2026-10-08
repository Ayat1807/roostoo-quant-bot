# Run: b6s_b6d_meta_edge_r6h

Strategy `s3v2x_meta`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'size_map': 'edge'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +42.45% | +5.47% | 0.80 | 1.23 | -10.18% | 0.54 | 0.90 |
| in_sample | 2020-02-15 → 2024-12-31 | +51.27% | +8.85% | 1.10 | 1.69 | -10.18% | 0.87 | 1.27 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -5.83% | -3.36% | -1.68 | -2.27 | -7.15% | -0.47 | -1.55 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -5.11% | -5.11% | -2.49 | -3.29 | -6.98% | -0.73 | -2.28 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.03% | 45% | -4.59% | -6.91% | -1.35 | 13 | 43% |
| out_of_sample | 628 | -0.10% | 34% | -1.54% | -1.56% | -5.31 | 12 | 19% |
| in_sample | 1768 | -0.00% | 50% | -4.59% | -6.91% | -0.05 | 14 | 51% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.082% | 48% | 3.72 | +15.36% |
| bull | 687 | 28% | +0.012% | 40% | 0.81 | +8.00% |
| bear | 400 | 17% | -0.001% | 35% | -0.24 | -0.48% |
| chop | 1160 | 48% | +0.016% | 38% | 0.51 | +17.57% |

## Turnover, fees, activity

- trades: 3325 (1.37/day); active days 90%
- turnover 22.6x equity/year; fees 2.26% of equity/year ($10,864 total)
- average gross exposure 0.03; brake active 2.2% of hours
- correlation of daily returns with s3v2 baseline: 0.37
