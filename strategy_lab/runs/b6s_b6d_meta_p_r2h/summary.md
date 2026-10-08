# Run: b6s_b6d_meta_p_r2h

Strategy `s3v2x_meta`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'size_map': 'p'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +61.53% | +7.49% | 0.93 | 1.44 | -12.99% | 0.58 | 1.03 |
| in_sample | 2020-02-15 → 2024-12-31 | +71.27% | +11.65% | 1.27 | 1.99 | -12.99% | 0.90 | 1.45 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -5.69% | -3.28% | -0.65 | -0.92 | -12.47% | -0.26 | -0.64 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -4.87% | -4.87% | -0.89 | -1.26 | -12.47% | -0.39 | -0.89 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.07% | 46% | -4.59% | -6.85% | -1.52 | 14 | 100% |
| out_of_sample | 628 | -0.24% | 33% | -2.75% | -3.15% | -4.40 | 14 | 100% |
| in_sample | 1768 | +0.02% | 51% | -4.59% | -6.85% | 0.31 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.147% | 53% | 4.90 | +29.18% |
| bull | 687 | 28% | +0.025% | 44% | 1.26 | +17.91% |
| bear | 400 | 17% | +0.001% | 39% | 0.12 | +0.43% |
| chop | 1160 | 48% | +0.009% | 37% | 0.28 | +8.44% |

## Turnover, fees, activity

- trades: 5166 (2.13/day); active days 100%
- turnover 38.2x equity/year; fees 3.82% of equity/year ($18,940 total)
- average gross exposure 0.07; brake active 1.6% of hours
- correlation of daily returns with s3v2 baseline: 0.60
