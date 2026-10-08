# Run: b6s_b6d_meta_p_r12h

Strategy `s3v2x_meta`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'size_map': 'p'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +77.43% | +9.02% | 1.12 | 1.68 | -14.73% | 0.61 | 1.19 |
| in_sample | 2020-02-15 → 2024-12-31 | +68.70% | +11.31% | 1.25 | 1.87 | -14.73% | 0.77 | 1.35 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +5.18% | +2.91% | 0.69 | 1.01 | -6.86% | 0.42 | 0.74 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +4.52% | +4.52% | 0.98 | 1.48 | -6.86% | 0.66 | 1.09 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.06% | 46% | -6.53% | -8.27% | -1.19 | 14 | 100% |
| out_of_sample | 628 | -0.12% | 41% | -1.82% | -1.86% | -3.09 | 14 | 100% |
| in_sample | 1768 | -0.03% | 48% | -6.53% | -8.27% | -0.62 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.146% | 59% | 4.29 | +28.90% |
| bull | 687 | 28% | +0.031% | 49% | 1.76 | +23.54% |
| bear | 400 | 17% | +0.010% | 49% | 0.94 | +3.92% |
| chop | 1160 | 48% | +0.010% | 41% | 0.32 | +9.84% |

## Turnover, fees, activity

- trades: 3637 (1.50/day); active days 100%
- turnover 18.4x equity/year; fees 1.84% of equity/year ($9,468 total)
- average gross exposure 0.06; brake active 2.0% of hours
- correlation of daily returns with s3v2 baseline: 0.63
