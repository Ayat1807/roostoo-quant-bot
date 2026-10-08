# Run: b6s_b6d_meta_p_r1h

Strategy `s3v2x_meta`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'size_map': 'p'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +43.56% | +5.60% | 0.71 | 1.08 | -16.90% | 0.33 | 0.75 |
| in_sample | 2020-02-15 → 2024-12-31 | +52.87% | +9.08% | 1.02 | 1.56 | -16.90% | 0.54 | 1.09 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -6.09% | -3.51% | -0.67 | -0.96 | -13.33% | -0.26 | -0.66 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -5.58% | -5.58% | -0.99 | -1.40 | -13.16% | -0.42 | -0.98 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.09% | 45% | -5.82% | -6.69% | -1.81 | 14 | 99% |
| out_of_sample | 628 | -0.23% | 34% | -2.85% | -3.42% | -4.16 | 14 | 100% |
| in_sample | 1768 | -0.04% | 48% | -5.82% | -6.69% | -0.76 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.155% | 56% | 5.01 | +31.01% |
| bull | 687 | 28% | +0.021% | 43% | 1.06 | +15.26% |
| bear | 400 | 17% | -0.002% | 38% | -0.19 | -0.94% |
| chop | 1160 | 48% | +0.000% | 36% | 0.01 | -1.44% |

## Turnover, fees, activity

- trades: 6062 (2.50/day); active days 100%
- turnover 47.4x equity/year; fees 4.74% of equity/year ($21,294 total)
- average gross exposure 0.07; brake active 2.0% of hours
- correlation of daily returns with s3v2 baseline: 0.60
