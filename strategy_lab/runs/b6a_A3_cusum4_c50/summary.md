# Run: b6a_A3_cusum4_c50

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +155.89% | +15.20% | 1.14 | 1.70 | -17.53% | 0.87 | 1.28 |
| in_sample | 2020-02-15 → 2024-12-31 | +91.76% | +14.27% | 1.09 | 1.63 | -17.53% | 0.81 | 1.22 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +33.59% | +17.91% | 1.30 | 1.91 | -11.33% | 1.58 | 1.63 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +15.07% | +15.07% | 1.03 | 1.51 | -11.33% | 1.33 | 1.31 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.16% | 45% | -6.53% | -7.06% | -1.51 | 14 | 100% |
| out_of_sample | 628 | -0.10% | 49% | -5.53% | -5.94% | -0.62 | 14 | 100% |
| in_sample | 1768 | -0.16% | 44% | -6.53% | -7.06% | -1.61 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.243% | 56% | 3.79 | +51.45% |
| bull | 687 | 28% | +0.084% | 53% | 2.86 | +76.17% |
| bear | 400 | 17% | +0.038% | 46% | 1.31 | +15.53% |
| chop | 1160 | 48% | -0.011% | 42% | -0.28 | -14.68% |

## Turnover, fees, activity

- trades: 5813 (2.40/day); active days 100%
- turnover 41.7x equity/year; fees 4.17% of equity/year ($22,426 total)
- average gross exposure 0.17; brake active 5.6% of hours
- correlation of daily returns with s3v2 baseline: 0.82
