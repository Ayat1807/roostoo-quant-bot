# Run: guard_band_edge

Strategy `s3v2`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard band_edge

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +147.41% | +14.62% | 0.88 | 1.28 | -22.08% | 0.66 | 0.97 |
| in_sample | 2020-02-15 → 2024-12-31 | +83.07% | +13.19% | 0.82 | 1.19 | -22.08% | 0.60 | 0.90 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +35.34% | +18.79% | 1.04 | 1.52 | -17.48% | 1.07 | 1.24 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +16.27% | +16.27% | 0.87 | 1.27 | -17.48% | 0.93 | 1.05 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.33% | 43% | -7.96% | -8.63% | -1.89 | 14 | 99% |
| out_of_sample | 628 | -0.48% | 42% | -7.96% | -8.63% | -2.26 | 14 | 100% |
| in_sample | 1768 | -0.29% | 43% | -7.73% | -8.56% | -1.63 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.234% | 55% | 2.69 | +47.27% |
| bull | 687 | 28% | +0.101% | 53% | 2.62 | +96.99% |
| bear | 400 | 17% | +0.028% | 48% | 0.69 | +10.53% |
| chop | 1160 | 48% | -0.016% | 44% | -0.36 | -20.56% |

## Turnover, fees, activity

- trades: 5440 (2.24/day); active days 100%
- turnover 48.5x equity/year; fees 4.85% of equity/year ($25,455 total)
- average gross exposure 0.21; brake active 12.9% of hours
- correlation of daily returns with s3v2 baseline: 0.91
