# Run: b7_hmm2_erc

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'inner': 's3v2x_alloc', 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +207.35% | +18.42% | 1.12 | 1.67 | -18.63% | 0.99 | 1.30 |
| in_sample | 2020-02-15 → 2024-12-31 | +117.71% | +17.28% | 1.05 | 1.57 | -18.63% | 0.93 | 1.22 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +41.37% | +21.77% | 1.33 | 1.98 | -11.96% | 1.82 | 1.74 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +26.60% | +26.60% | 1.42 | 2.14 | -11.96% | 2.22 | 1.95 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.16% | 45% | -7.41% | -7.57% | -1.30 | 14 | 99% |
| out_of_sample | 628 | -0.03% | 50% | -5.47% | -6.48% | -0.16 | 14 | 100% |
| in_sample | 1768 | -0.18% | 44% | -7.41% | -7.57% | -1.64 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.295% | 55% | 3.57 | +64.47% |
| bull | 687 | 28% | +0.091% | 52% | 2.39 | +83.60% |
| bear | 400 | 17% | +0.044% | 46% | 1.15 | +17.98% |
| chop | 1160 | 48% | -0.007% | 44% | -0.17 | -11.14% |

## Turnover, fees, activity

- trades: 5352 (2.21/day); active days 100%
- turnover 46.2x equity/year; fees 4.62% of equity/year ($27,082 total)
- average gross exposure 0.18; brake active 11.5% of hours
- correlation of daily returns with s3v2 baseline: 0.82
