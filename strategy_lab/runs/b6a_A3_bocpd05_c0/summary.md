# Run: b6a_A3_bocpd05_c0

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +85.16% | +9.72% | 0.84 | 1.26 | -20.31% | 0.48 | 0.90 |
| in_sample | 2020-02-15 → 2024-12-31 | +44.97% | +7.90% | 0.71 | 1.07 | -20.31% | 0.39 | 0.76 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +27.85% | +15.00% | 1.20 | 1.79 | -11.02% | 1.36 | 1.48 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +15.92% | +15.92% | 1.13 | 1.70 | -11.02% | 1.44 | 1.45 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.20% | 43% | -7.22% | -8.09% | -2.25 | 14 | 99% |
| out_of_sample | 628 | -0.12% | 47% | -5.28% | -5.63% | -0.79 | 14 | 100% |
| in_sample | 1768 | -0.22% | 42% | -7.22% | -8.09% | -2.67 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.183% | 53% | 3.15 | +36.59% |
| bull | 687 | 28% | +0.061% | 50% | 2.19 | +50.18% |
| bear | 400 | 17% | +0.048% | 46% | 1.59 | +20.17% |
| chop | 1160 | 48% | -0.020% | 40% | -0.62 | -22.88% |

## Turnover, fees, activity

- trades: 5285 (2.18/day); active days 100%
- turnover 46.0x equity/year; fees 4.60% of equity/year ($19,336 total)
- average gross exposure 0.15; brake active 6.0% of hours
- correlation of daily returns with s3v2 baseline: 0.73
