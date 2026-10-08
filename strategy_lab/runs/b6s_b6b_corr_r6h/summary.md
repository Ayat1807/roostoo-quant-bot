# Run: b6s_b6b_corr_r6h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'corr_filter': True}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +242.53% | +20.37% | 1.38 | 2.07 | -12.51% | 1.63 | 1.73 |
| in_sample | 2020-02-15 → 2024-12-31 | +166.77% | +22.26% | 1.45 | 2.20 | -12.51% | 1.78 | 1.85 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +28.49% | +15.33% | 1.15 | 1.71 | -11.47% | 1.34 | 1.43 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +30.53% | +30.53% | 1.73 | 2.61 | -11.47% | 2.66 | 2.36 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.10% | 46% | -4.59% | -6.91% | -0.99 | 14 | 100% |
| out_of_sample | 628 | -0.26% | 39% | -4.30% | -6.44% | -2.69 | 14 | 100% |
| in_sample | 1768 | -0.03% | 49% | -4.59% | -6.91% | -0.24 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.351% | 54% | 4.60 | +82.03% |
| bull | 687 | 28% | +0.069% | 48% | 2.19 | +58.45% |
| bear | 400 | 17% | +0.062% | 45% | 1.93 | +27.38% |
| chop | 1160 | 48% | -0.001% | 40% | -0.03 | -4.59% |

## Turnover, fees, activity

- trades: 6095 (2.51/day); active days 100%
- turnover 54.0x equity/year; fees 5.40% of equity/year ($37,042 total)
- average gross exposure 0.15; brake active 8.1% of hours
- correlation of daily returns with s3v2 baseline: 0.76
