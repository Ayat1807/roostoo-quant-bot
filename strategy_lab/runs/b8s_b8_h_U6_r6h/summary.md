# Run: b8s_b8_h_U6_r6h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'floor_breadth': 7, 'floor_gross': 0.5}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +131.37% | +13.47% | 0.77 | 1.13 | -30.23% | 0.45 | 0.81 |
| in_sample | 2020-02-15 → 2024-12-31 | +102.96% | +15.60% | 0.85 | 1.25 | -30.23% | 0.52 | 0.91 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +14.72% | +8.12% | 0.53 | 0.79 | -12.98% | 0.63 | 0.66 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +7.96% | +7.96% | 0.51 | 0.78 | -12.98% | 0.61 | 0.65 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.49% | 43% | -8.63% | -9.16% | -1.99 | 14 | 100% |
| out_of_sample | 628 | -0.67% | 38% | -5.66% | -5.78% | -2.66 | 14 | 100% |
| in_sample | 1768 | -0.35% | 45% | -8.63% | -9.16% | -1.51 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.509% | 56% | 5.33 | +137.62% |
| bull | 687 | 28% | +0.072% | 48% | 1.49 | +58.88% |
| bear | 400 | 17% | +0.008% | 43% | 0.16 | +1.51% |
| chop | 1160 | 48% | -0.037% | 39% | -0.73 | -38.06% |

## Turnover, fees, activity

- trades: 11137 (4.59/day); active days 100%
- turnover 98.3x equity/year; fees 9.83% of equity/year ($58,216 total)
- average gross exposure 0.22; brake active 25.2% of hours
- correlation of daily returns with s3v2 baseline: 0.77
