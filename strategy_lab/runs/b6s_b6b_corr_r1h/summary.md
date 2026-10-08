# Run: b6s_b6b_corr_r1h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'corr_filter': True}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +140.49% | +14.13% | 1.01 | 1.53 | -16.90% | 0.84 | 1.16 |
| in_sample | 2020-02-15 → 2024-12-31 | +99.03% | +15.14% | 1.05 | 1.61 | -16.90% | 0.90 | 1.23 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +20.91% | +11.41% | 0.88 | 1.31 | -13.55% | 0.84 | 1.04 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +26.72% | +26.72% | 1.53 | 2.32 | -13.55% | 1.97 | 1.98 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.16% | 45% | -5.82% | -6.69% | -1.54 | 14 | 98% |
| out_of_sample | 628 | -0.26% | 38% | -5.16% | -6.60% | -3.04 | 14 | 100% |
| in_sample | 1768 | -0.09% | 47% | -5.82% | -6.69% | -0.88 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.327% | 52% | 4.43 | +74.68% |
| bull | 687 | 28% | +0.041% | 44% | 1.25 | +30.38% |
| bear | 400 | 17% | +0.063% | 41% | 1.88 | +27.79% |
| chop | 1160 | 48% | -0.011% | 37% | -0.28 | -15.14% |

## Turnover, fees, activity

- trades: 9314 (3.84/day); active days 100%
- turnover 89.2x equity/year; fees 8.92% of equity/year ($48,135 total)
- average gross exposure 0.15; brake active 7.7% of hours
- correlation of daily returns with s3v2 baseline: 0.72
