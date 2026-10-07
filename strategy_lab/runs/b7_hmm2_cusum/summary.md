# Run: b7_hmm2_cusum

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +148.73% | +14.71% | 1.13 | 1.69 | -17.53% | 0.84 | 1.27 |
| in_sample | 2020-02-15 → 2024-12-31 | +84.49% | +13.36% | 1.04 | 1.56 | -17.53% | 0.76 | 1.17 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +34.97% | +18.60% | 1.39 | 2.05 | -10.74% | 1.73 | 1.75 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +16.08% | +16.08% | 1.14 | 1.67 | -10.74% | 1.50 | 1.46 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.13% | 46% | -6.53% | -7.06% | -1.21 | 14 | 100% |
| out_of_sample | 628 | -0.05% | 49% | -5.52% | -5.92% | -0.38 | 14 | 100% |
| in_sample | 1768 | -0.14% | 45% | -6.53% | -7.06% | -1.33 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.232% | 54% | 3.81 | +48.62% |
| bull | 687 | 28% | +0.077% | 53% | 2.75 | +67.94% |
| bear | 400 | 17% | +0.043% | 47% | 1.52 | +17.91% |
| chop | 1160 | 48% | -0.009% | 43% | -0.24 | -13.14% |

## Turnover, fees, activity

- trades: 5786 (2.39/day); active days 100%
- turnover 41.0x equity/year; fees 4.10% of equity/year ($21,873 total)
- average gross exposure 0.16; brake active 4.9% of hours
- correlation of daily returns with s3v2 baseline: 0.81
