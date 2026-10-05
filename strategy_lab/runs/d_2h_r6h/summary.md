# Run: d_2h_r6h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +251.22% | +21.77% | 1.31 | 1.96 | -16.01% | 1.36 | 1.59 |
| in_sample | 2020-02-15 → 2024-12-31 | +176.02% | +23.12% | 1.39 | 2.09 | -13.70% | 1.69 | 1.76 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +27.32% | +17.53% | 1.07 | 1.57 | -16.01% | 1.09 | 1.28 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +9.43% | +12.80% | 0.75 | 1.11 | -16.01% | 0.80 | 0.91 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.09% | 48% | -6.18% | -6.90% | -0.76 | 14 | 99% |
| out_of_sample | 532 | -0.32% | 44% | -5.21% | -5.71% | -2.01 | 14 | 100% |
| in_sample | 1768 | -0.03% | 49% | -6.18% | -6.90% | -0.33 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.316% | 57% | 4.35 | +68.36% |
| bull | 659 | 28% | +0.075% | 49% | 2.16 | +62.02% |
| bear | 399 | 17% | +0.069% | 44% | 1.72 | +30.32% |
| chop | 1099 | 47% | +0.005% | 40% | 0.10 | +1.15% |

## Turnover, fees, activity

- trades: 6440 (2.77/day); active days 100%
- turnover 63.3x equity/year; fees 6.33% of equity/year ($43,916 total)
- average gross exposure 0.18; brake active 12.0% of hours
- correlation of daily returns with s3v2 baseline: 0.87
