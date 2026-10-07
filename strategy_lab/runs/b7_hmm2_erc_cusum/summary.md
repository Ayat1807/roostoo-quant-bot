# Run: b7_hmm2_erc_cusum

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'inner': 's3v2x_alloc', 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +104.46% | +11.37% | 0.84 | 1.27 | -19.45% | 0.58 | 0.94 |
| in_sample | 2020-02-15 → 2024-12-31 | +66.44% | +11.00% | 0.80 | 1.21 | -19.45% | 0.57 | 0.90 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +23.01% | +12.51% | 0.99 | 1.45 | -10.31% | 1.21 | 1.24 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +12.93% | +12.93% | 0.93 | 1.37 | -10.31% | 1.25 | 1.20 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.14% | 45% | -6.74% | -7.04% | -1.33 | 14 | 100% |
| out_of_sample | 628 | -0.03% | 50% | -5.23% | -6.25% | -0.12 | 14 | 100% |
| in_sample | 1768 | -0.17% | 43% | -6.74% | -7.04% | -1.56 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.227% | 54% | 3.50 | +47.06% |
| bull | 687 | 28% | +0.052% | 50% | 1.67 | +41.59% |
| bear | 400 | 17% | +0.028% | 46% | 0.87 | +10.94% |
| chop | 1160 | 48% | -0.005% | 44% | -0.13 | -8.80% |

## Turnover, fees, activity

- trades: 6082 (2.51/day); active days 100%
- turnover 46.8x equity/year; fees 4.68% of equity/year ($21,947 total)
- average gross exposure 0.17; brake active 7.8% of hours
- correlation of daily returns with s3v2 baseline: 0.78
