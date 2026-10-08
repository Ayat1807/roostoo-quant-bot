# Run: b7s_b7_hmm2_erc_cusum_r12h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'inner': 's3v2x_alloc', 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +128.82% | +13.28% | 0.95 | 1.42 | -16.52% | 0.80 | 1.09 |
| in_sample | 2020-02-15 → 2024-12-31 | +89.24% | +13.96% | 0.97 | 1.46 | -15.16% | 0.92 | 1.15 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +21.05% | +11.48% | 0.88 | 1.30 | -16.52% | 0.69 | 0.99 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +12.93% | +12.93% | 0.88 | 1.30 | -16.52% | 0.78 | 1.02 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.05% | 49% | -6.48% | -8.52% | -0.36 | 14 | 100% |
| out_of_sample | 628 | -0.04% | 49% | -5.36% | -5.82% | -0.28 | 14 | 100% |
| in_sample | 1768 | -0.04% | 49% | -6.48% | -8.52% | -0.30 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.269% | 56% | 4.02 | +58.24% |
| bull | 687 | 28% | +0.061% | 49% | 1.80 | +49.42% |
| bear | 400 | 17% | +0.043% | 46% | 1.31 | +17.86% |
| chop | 1160 | 48% | -0.012% | 42% | -0.28 | -15.65% |

## Turnover, fees, activity

- trades: 7154 (2.95/day); active days 100%
- turnover 61.2x equity/year; fees 6.12% of equity/year ($32,580 total)
- average gross exposure 0.16; brake active 9.9% of hours
- correlation of daily returns with s3v2 baseline: 0.74
