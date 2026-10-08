# Run: b6s_b6c_hrp_r6h

Strategy `s3v2x_alloc`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'alloc': 'hrp'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +120.91% | +12.68% | 0.83 | 1.22 | -24.09% | 0.53 | 0.89 |
| in_sample | 2020-02-15 → 2024-12-31 | +102.01% | +15.49% | 0.99 | 1.45 | -24.09% | 0.64 | 1.07 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +9.67% | +5.39% | 0.40 | 0.60 | -19.50% | 0.28 | 0.44 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +15.56% | +15.56% | 0.86 | 1.28 | -19.50% | 0.80 | 1.01 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.35% | 43% | -5.22% | -6.06% | -2.07 | 14 | 100% |
| out_of_sample | 628 | -0.67% | 39% | -4.88% | -5.71% | -3.21 | 14 | 100% |
| in_sample | 1768 | -0.24% | 45% | -5.22% | -6.06% | -1.48 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.413% | 54% | 4.97 | +102.13% |
| bull | 687 | 28% | +0.049% | 48% | 1.36 | +37.38% |
| bear | 400 | 17% | +0.021% | 43% | 0.51 | +7.45% |
| chop | 1160 | 48% | -0.021% | 38% | -0.51 | -24.06% |

## Turnover, fees, activity

- trades: 9654 (3.98/day); active days 100%
- turnover 106.4x equity/year; fees 10.64% of equity/year ($62,650 total)
- average gross exposure 0.20; brake active 13.0% of hours
- correlation of daily returns with s3v2 baseline: 0.78
