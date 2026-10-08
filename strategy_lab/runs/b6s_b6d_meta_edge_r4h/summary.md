# Run: b6s_b6d_meta_edge_r4h

Strategy `s3v2x_meta`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'size_map': 'edge'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +31.33% | +4.19% | 0.63 | 0.96 | -16.29% | 0.26 | 0.65 |
| in_sample | 2020-02-15 → 2024-12-31 | +40.30% | +7.18% | 0.92 | 1.40 | -16.29% | 0.44 | 0.97 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -6.39% | -3.69% | -1.78 | -2.41 | -8.22% | -0.45 | -1.64 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -5.88% | -5.88% | -2.77 | -3.67 | -7.53% | -0.78 | -2.53 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.02% | 47% | -6.98% | -7.50% | -1.05 | 13 | 46% |
| out_of_sample | 628 | -0.11% | 32% | -1.55% | -1.66% | -5.53 | 12 | 22% |
| in_sample | 1768 | +0.01% | 52% | -6.98% | -7.50% | 0.78 | 14 | 54% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.069% | 49% | 3.75 | +12.78% |
| bull | 687 | 28% | +0.011% | 44% | 0.80 | +7.80% |
| bear | 400 | 17% | -0.000% | 34% | -0.05 | -0.12% |
| chop | 1160 | 48% | +0.010% | 37% | 0.34 | +10.75% |

## Turnover, fees, activity

- trades: 3645 (1.50/day); active days 91%
- turnover 26.9x equity/year; fees 2.69% of equity/year ($11,876 total)
- average gross exposure 0.03; brake active 2.4% of hours
- correlation of daily returns with s3v2 baseline: 0.35
