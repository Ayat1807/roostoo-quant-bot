# Run: d_30m_r12h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [48, 144, 336, 672], 'vol_win': 672, 'regime_win': 672, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'bars_per_year': 17520}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +295.34% | +24.05% | 1.45 | 2.14 | -12.85% | 1.87 | 1.85 |
| in_sample | 2020-02-15 → 2024-12-31 | +190.68% | +24.43% | 1.49 | 2.21 | -12.85% | 1.90 | 1.90 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +36.08% | +22.87% | 1.31 | 1.93 | -11.16% | 2.05 | 1.78 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +22.12% | +30.63% | 1.51 | 2.25 | -11.16% | 2.74 | 2.17 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.03% | 49% | -4.37% | -7.35% | -0.13 | 14 | 100% |
| out_of_sample | 532 | -0.29% | 45% | -4.17% | -4.98% | -1.36 | 14 | 100% |
| in_sample | 1768 | +0.03% | 51% | -4.37% | -7.35% | 0.32 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.242% | 58% | 3.48 | +48.68% |
| bull | 659 | 28% | +0.099% | 51% | 2.76 | +89.35% |
| bear | 399 | 17% | +0.060% | 46% | 1.48 | +25.52% |
| chop | 1099 | 47% | +0.016% | 43% | 0.36 | +14.51% |

## Turnover, fees, activity

- trades: 5572 (2.39/day); active days 100%
- turnover 51.0x equity/year; fees 5.10% of equity/year ($35,865 total)
- average gross exposure 0.18; brake active 12.3% of hours
- correlation of daily returns with s3v2 baseline: 0.87
