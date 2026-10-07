# Run: b6b_corr

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'corr_filter': True}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +164.70% | +15.79% | 1.10 | 1.62 | -16.15% | 0.98 | 1.27 |
| in_sample | 2020-02-15 → 2024-12-31 | +101.70% | +15.45% | 1.05 | 1.54 | -16.15% | 0.96 | 1.22 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +31.37% | +16.79% | 1.30 | 1.90 | -9.93% | 1.69 | 1.65 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +30.32% | +30.32% | 1.82 | 2.70 | -9.93% | 3.06 | 2.54 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.17% | 45% | -5.29% | -6.87% | -1.61 | 14 | 100% |
| out_of_sample | 628 | -0.14% | 45% | -4.38% | -5.85% | -1.07 | 14 | 100% |
| in_sample | 1768 | -0.18% | 45% | -5.29% | -6.87% | -1.70 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.265% | 59% | 3.51 | +56.58% |
| bull | 687 | 28% | +0.084% | 53% | 2.77 | +76.55% |
| bear | 400 | 17% | +0.044% | 48% | 1.44 | +18.26% |
| chop | 1160 | 48% | -0.013% | 44% | -0.34 | -16.70% |

## Turnover, fees, activity

- trades: 4794 (1.98/day); active days 100%
- turnover 35.7x equity/year; fees 3.57% of equity/year ($19,741 total)
- average gross exposure 0.16; brake active 7.2% of hours
- correlation of daily returns with s3v2 baseline: 0.82
