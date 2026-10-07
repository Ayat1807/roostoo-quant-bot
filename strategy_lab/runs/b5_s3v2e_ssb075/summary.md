# Run: b5_s3v2e_ssb075

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.75, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +185.99% | +17.15% | 1.12 | 1.66 | -15.80% | 1.09 | 1.33 |
| in_sample | 2020-02-15 → 2024-12-31 | +100.33% | +15.29% | 1.03 | 1.53 | -15.80% | 0.97 | 1.21 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +42.91% | +22.52% | 1.37 | 2.00 | -14.39% | 1.57 | 1.68 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +24.92% | +24.92% | 1.35 | 1.98 | -14.39% | 1.73 | 1.72 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.18% | 45% | -6.64% | -7.07% | -1.38 | 14 | 100% |
| out_of_sample | 628 | -0.12% | 48% | -5.15% | -6.43% | -0.67 | 14 | 100% |
| in_sample | 1768 | -0.18% | 44% | -6.64% | -7.07% | -1.54 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.224% | 59% | 2.94 | +45.71% |
| bull | 687 | 28% | +0.097% | 52% | 2.81 | +91.83% |
| bear | 400 | 17% | +0.046% | 48% | 1.36 | +19.29% |
| chop | 1160 | 48% | -0.008% | 43% | -0.19 | -11.75% |

## Turnover, fees, activity

- trades: 5180 (2.14/day); active days 100%
- turnover 42.4x equity/year; fees 4.24% of equity/year ($23,502 total)
- average gross exposure 0.19; brake active 8.8% of hours
- correlation of daily returns with s3v2 baseline: 0.86
