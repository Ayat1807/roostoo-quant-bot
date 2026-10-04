# Run: p_band04

Strategy `s3v2`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.04; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +159.66% | +15.45% | 0.82 | 1.19 | -21.43% | 0.72 | 0.94 |
| in_sample | 2020-02-15 → 2024-12-31 | +114.48% | +16.92% | 0.90 | 1.31 | -17.87% | 0.95 | 1.08 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +21.19% | +11.55% | 0.62 | 0.89 | -21.43% | 0.54 | 0.70 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +4.79% | +4.79% | 0.32 | 0.47 | -21.43% | 0.22 | 0.35 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.28% | 45% | -9.75% | -10.55% | -1.29 | 14 | 99% |
| out_of_sample | 628 | -0.44% | 42% | -9.75% | -10.55% | -1.67 | 14 | 98% |
| in_sample | 1768 | -0.20% | 46% | -6.28% | -8.83% | -0.96 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.291% | 54% | 3.19 | +62.51% |
| bull | 687 | 28% | +0.104% | 52% | 2.36 | +99.45% |
| bear | 400 | 17% | +0.034% | 46% | 0.62 | +11.97% |
| chop | 1160 | 48% | -0.021% | 44% | -0.42 | -25.85% |

## Turnover, fees, activity

- trades: 8700 (3.59/day); active days 100%
- turnover 64.9x equity/year; fees 6.49% of equity/year ($37,354 total)
- average gross exposure 0.24; brake active 24.7% of hours
- correlation of daily returns with s3v2 baseline: 0.90
