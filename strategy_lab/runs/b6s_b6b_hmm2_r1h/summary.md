# Run: b6s_b6b_hmm2_r1h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +155.36% | +15.16% | 1.03 | 1.57 | -16.90% | 0.90 | 1.21 |
| in_sample | 2020-02-15 → 2024-12-31 | +94.31% | +14.58% | 1.01 | 1.55 | -16.90% | 0.86 | 1.18 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +31.50% | +16.86% | 1.08 | 1.64 | -14.58% | 1.16 | 1.33 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +24.73% | +24.73% | 1.33 | 2.03 | -14.58% | 1.70 | 1.72 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.18% | 45% | -5.82% | -6.69% | -1.64 | 14 | 98% |
| out_of_sample | 628 | -0.42% | 39% | -4.63% | -4.99% | -3.04 | 14 | 100% |
| in_sample | 1768 | -0.10% | 47% | -5.82% | -6.69% | -0.89 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.340% | 53% | 4.57 | +78.54% |
| bull | 687 | 28% | +0.051% | 44% | 1.49 | +39.49% |
| bear | 400 | 17% | +0.061% | 41% | 1.65 | +26.46% |
| chop | 1160 | 48% | -0.013% | 36% | -0.29 | -16.73% |

## Turnover, fees, activity

- trades: 9938 (4.10/day); active days 100%
- turnover 98.8x equity/year; fees 9.88% of equity/year ($54,436 total)
- average gross exposure 0.16; brake active 10.2% of hours
- correlation of daily returns with s3v2 baseline: 0.76
