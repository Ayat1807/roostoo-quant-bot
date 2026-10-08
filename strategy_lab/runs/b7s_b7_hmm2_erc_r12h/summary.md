# Run: b7s_b7_hmm2_erc_r12h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'inner': 's3v2x_alloc', 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +264.58% | +21.51% | 1.26 | 1.89 | -17.73% | 1.21 | 1.50 |
| in_sample | 2020-02-15 → 2024-12-31 | +182.05% | +23.66% | 1.35 | 2.03 | -12.66% | 1.87 | 1.78 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +29.40% | +15.79% | 1.01 | 1.48 | -17.73% | 0.89 | 1.16 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +18.89% | +18.89% | 1.04 | 1.54 | -17.73% | 1.07 | 1.25 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.07% | 48% | -7.05% | -8.50% | -0.54 | 14 | 100% |
| out_of_sample | 628 | -0.11% | 47% | -5.59% | -6.04% | -0.79 | 14 | 100% |
| in_sample | 1768 | -0.03% | 49% | -7.05% | -8.50% | -0.22 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.327% | 57% | 4.02 | +73.93% |
| bull | 687 | 28% | +0.083% | 48% | 2.08 | +73.75% |
| bear | 400 | 17% | +0.072% | 46% | 1.78 | +31.91% |
| chop | 1160 | 48% | -0.002% | 43% | -0.04 | -6.14% |

## Turnover, fees, activity

- trades: 6342 (2.62/day); active days 100%
- turnover 60.4x equity/year; fees 6.04% of equity/year ($43,919 total)
- average gross exposure 0.17; brake active 12.7% of hours
- correlation of daily returns with s3v2 baseline: 0.77
