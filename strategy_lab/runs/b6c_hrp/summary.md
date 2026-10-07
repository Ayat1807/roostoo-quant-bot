# Run: b6c_hrp

Strategy `s3v2x_alloc`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'alloc': 'hrp'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +156.25% | +15.23% | 0.99 | 1.45 | -15.39% | 0.99 | 1.18 |
| in_sample | 2020-02-15 → 2024-12-31 | +114.88% | +16.96% | 1.09 | 1.60 | -15.39% | 1.10 | 1.30 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +19.31% | +10.57% | 0.72 | 1.06 | -13.29% | 0.79 | 0.88 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +19.39% | +19.39% | 1.06 | 1.56 | -13.29% | 1.46 | 1.38 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.24% | 44% | -5.22% | -7.53% | -1.41 | 14 | 99% |
| out_of_sample | 628 | -0.22% | 45% | -5.06% | -5.97% | -1.35 | 14 | 100% |
| in_sample | 1768 | -0.22% | 43% | -5.22% | -7.53% | -1.37 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.306% | 52% | 3.63 | +67.52% |
| bull | 687 | 28% | +0.077% | 52% | 2.14 | +67.48% |
| bear | 400 | 17% | +0.035% | 47% | 0.94 | +13.85% |
| chop | 1160 | 48% | -0.014% | 42% | -0.38 | -17.79% |

## Turnover, fees, activity

- trades: 5540 (2.29/day); active days 100%
- turnover 57.3x equity/year; fees 5.73% of equity/year ($34,233 total)
- average gross exposure 0.20; brake active 11.0% of hours
- correlation of daily returns with s3v2 baseline: 0.82
