# Run: b6s_b6b_hmm2_r4h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +220.13% | +19.15% | 1.25 | 1.88 | -16.29% | 1.18 | 1.48 |
| in_sample | 2020-02-15 → 2024-12-31 | +146.83% | +20.33% | 1.34 | 2.03 | -16.29% | 1.25 | 1.59 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +29.78% | +15.99% | 1.02 | 1.52 | -14.38% | 1.11 | 1.25 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +16.05% | +16.05% | 0.94 | 1.40 | -14.38% | 1.12 | 1.18 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.17% | 44% | -6.98% | -7.50% | -1.68 | 14 | 99% |
| out_of_sample | 628 | -0.47% | 38% | -4.75% | -5.43% | -3.44 | 14 | 100% |
| in_sample | 1768 | -0.11% | 46% | -6.98% | -7.50% | -1.06 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.308% | 52% | 4.28 | +69.14% |
| bull | 687 | 28% | +0.085% | 46% | 2.46 | +76.59% |
| bear | 400 | 17% | +0.068% | 42% | 1.80 | +29.94% |
| chop | 1160 | 48% | -0.011% | 39% | -0.26 | -15.53% |

## Turnover, fees, activity

- trades: 7119 (2.94/day); active days 100%
- turnover 67.8x equity/year; fees 6.78% of equity/year ($43,228 total)
- average gross exposure 0.16; brake active 10.6% of hours
- correlation of daily returns with s3v2 baseline: 0.78
