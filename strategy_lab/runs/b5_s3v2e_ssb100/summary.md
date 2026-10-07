# Run: b5_s3v2e_ssb100

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 1.0, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +184.35% | +17.04% | 1.11 | 1.63 | -17.50% | 0.97 | 1.28 |
| in_sample | 2020-02-15 → 2024-12-31 | +105.92% | +15.95% | 1.06 | 1.57 | -17.50% | 0.91 | 1.22 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +38.23% | +20.23% | 1.24 | 1.81 | -15.57% | 1.30 | 1.49 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +22.36% | +22.36% | 1.23 | 1.80 | -15.57% | 1.44 | 1.52 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.18% | 46% | -7.13% | -7.80% | -1.37 | 14 | 99% |
| out_of_sample | 628 | -0.15% | 48% | -5.32% | -6.43% | -0.77 | 14 | 100% |
| in_sample | 1768 | -0.16% | 45% | -7.13% | -7.80% | -1.39 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.243% | 59% | 3.16 | +50.54% |
| bull | 687 | 28% | +0.090% | 52% | 2.63 | +82.82% |
| bear | 400 | 17% | +0.049% | 48% | 1.40 | +20.43% |
| chop | 1160 | 48% | -0.008% | 43% | -0.18 | -11.74% |

## Turnover, fees, activity

- trades: 5433 (2.24/day); active days 100%
- turnover 45.4x equity/year; fees 4.54% of equity/year ($25,879 total)
- average gross exposure 0.19; brake active 9.7% of hours
- correlation of daily returns with s3v2 baseline: 0.85
