# Run: e_tranched

Strategy `s3v2_tranched`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'tranches': 4, 'spacing_bars': 6}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +256.91% | +22.08% | 1.31 | 1.87 | -17.29% | 1.28 | 1.53 |
| in_sample | 2020-02-15 → 2024-12-31 | +187.60% | +24.16% | 1.41 | 2.02 | -17.29% | 1.40 | 1.65 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +24.21% | +15.60% | 0.98 | 1.40 | -11.97% | 1.30 | 1.24 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +12.74% | +17.39% | 1.02 | 1.47 | -11.97% | 1.45 | 1.33 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.16% | 46% | -7.72% | -8.35% | -0.91 | 14 | 99% |
| out_of_sample | 532 | -0.19% | 45% | -4.69% | -5.70% | -0.94 | 14 | 100% |
| in_sample | 1768 | -0.14% | 46% | -7.72% | -8.35% | -0.72 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.183% | 60% | 2.39 | +34.06% |
| bull | 659 | 28% | +0.138% | 56% | 3.52 | +144.12% |
| bear | 399 | 17% | +0.038% | 49% | 1.06 | +15.15% |
| chop | 1099 | 47% | +0.000% | 45% | 0.01 | -2.92% |

## Turnover, fees, activity

- trades: 4716 (2.03/day); active days 100%
- turnover 28.1x equity/year; fees 2.81% of equity/year ($20,997 total)
- average gross exposure 0.21; brake active 8.7% of hours
- correlation of daily returns with s3v2 baseline: 0.88
