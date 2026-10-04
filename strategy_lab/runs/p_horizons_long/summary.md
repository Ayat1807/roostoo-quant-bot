# Run: p_horizons_long

Strategy `s3v2`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [72, 168, 336, 720], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +332.52% | +24.68% | 1.28 | 1.84 | -19.84% | 1.24 | 1.49 |
| in_sample | 2020-02-15 → 2024-12-31 | +221.70% | +27.04% | 1.36 | 1.96 | -19.84% | 1.36 | 1.60 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +34.58% | +18.40% | 1.03 | 1.47 | -11.99% | 1.53 | 1.36 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +22.32% | +22.32% | 1.12 | 1.61 | -11.99% | 1.86 | 1.54 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.18% | 46% | -7.70% | -8.43% | -1.12 | 14 | 98% |
| out_of_sample | 628 | -0.30% | 43% | -5.81% | -7.22% | -1.71 | 14 | 98% |
| in_sample | 1768 | -0.13% | 47% | -7.70% | -8.43% | -0.76 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.281% | 50% | 2.86 | +59.02% |
| bull | 687 | 28% | +0.161% | 57% | 3.54 | +193.57% |
| bear | 400 | 17% | +0.100% | 50% | 2.15 | +47.05% |
| chop | 1160 | 48% | -0.034% | 44% | -0.74 | -35.13% |

## Turnover, fees, activity

- trades: 4219 (1.74/day); active days 100%
- turnover 31.2x equity/year; fees 3.12% of equity/year ($25,744 total)
- average gross exposure 0.22; brake active 12.1% of hours
- correlation of daily returns with s3v2 baseline: 0.82
