# Run: b8s_b8_h_U6_r4h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'floor_breadth': 7, 'floor_gross': 0.5}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +146.42% | +14.55% | 0.80 | 1.17 | -28.84% | 0.50 | 0.86 |
| in_sample | 2020-02-15 → 2024-12-31 | +110.90% | +16.52% | 0.87 | 1.27 | -28.84% | 0.57 | 0.94 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +17.46% | +9.59% | 0.59 | 0.88 | -14.32% | 0.67 | 0.73 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +11.79% | +11.79% | 0.70 | 1.06 | -14.32% | 0.82 | 0.88 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.58% | 42% | -9.53% | -12.07% | -2.37 | 14 | 99% |
| out_of_sample | 628 | -0.56% | 44% | -5.25% | -5.75% | -2.00 | 14 | 100% |
| in_sample | 1768 | -0.56% | 42% | -9.53% | -12.07% | -2.35 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.541% | 54% | 5.52 | +151.09% |
| bull | 687 | 28% | +0.079% | 48% | 1.69 | +67.26% |
| bear | 400 | 17% | +0.002% | 40% | 0.05 | -0.63% |
| chop | 1160 | 48% | -0.037% | 39% | -0.70 | -38.91% |

## Turnover, fees, activity

- trades: 12444 (5.13/day); active days 100%
- turnover 111.1x equity/year; fees 11.11% of equity/year ($65,007 total)
- average gross exposure 0.23; brake active 28.7% of hours
- correlation of daily returns with s3v2 baseline: 0.78
