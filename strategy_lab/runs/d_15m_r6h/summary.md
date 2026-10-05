# Run: d_15m_r6h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [96, 288, 672, 1344], 'vol_win': 1344, 'regime_win': 1344, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'bars_per_year': 35040}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +261.28% | +22.31% | 1.38 | 2.07 | -12.65% | 1.76 | 1.77 |
| in_sample | 2020-02-15 → 2024-12-31 | +159.06% | +21.53% | 1.36 | 2.05 | -12.65% | 1.70 | 1.74 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +39.54% | +24.95% | 1.44 | 2.15 | -12.59% | 1.98 | 1.89 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +20.82% | +28.78% | 1.43 | 2.16 | -12.59% | 2.29 | 1.98 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.13% | 47% | -4.94% | -6.09% | -1.34 | 14 | 99% |
| out_of_sample | 532 | -0.21% | 45% | -4.75% | -5.58% | -1.74 | 14 | 100% |
| in_sample | 1768 | -0.10% | 47% | -4.94% | -6.09% | -1.07 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.297% | 56% | 4.23 | +63.12% |
| bull | 659 | 28% | +0.077% | 47% | 2.08 | +62.92% |
| bear | 399 | 17% | +0.068% | 43% | 1.74 | +29.86% |
| chop | 1099 | 47% | +0.010% | 39% | 0.22 | +7.29% |

## Turnover, fees, activity

- trades: 6274 (2.70/day); active days 100%
- turnover 58.8x equity/year; fees 5.88% of equity/year ($38,655 total)
- average gross exposure 0.17; brake active 14.0% of hours
- correlation of daily returns with s3v2 baseline: 0.84
