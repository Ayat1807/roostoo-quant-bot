# Run: mft_breakout_10_b01

Strategy `breakout`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.01; brake True; shorts False; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-05 | +65.05% | +7.84% | 0.79 | 1.10 | -22.48% | 0.35 | 0.78 |
| in_sample | 2020-02-15 → 2024-12-31 | +72.77% | +11.85% | 1.12 | 1.54 | -22.48% | 0.53 | 1.11 |
| out_of_sample | 2025-01-01 → 2026-10-05 | -4.67% | -2.68% | -0.25 | -0.35 | -15.93% | -0.17 | -0.27 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -7.23% | -7.23% | -0.86 | -1.22 | -14.93% | -0.48 | -0.89 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2411 | -0.15% | 46% | -4.30% | -4.73% | -1.04 | 13 | 31% |
| out_of_sample | 629 | -0.38% | 37% | -4.30% | -4.73% | -2.91 | 12 | 14% |
| in_sample | 1768 | -0.05% | 49% | -3.76% | -4.43% | -0.31 | 13 | 38% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.284% | 48% | 5.39 | +63.36% |
| bull | 687 | 28% | +0.072% | 44% | 2.30 | +61.79% |
| bear | 400 | 17% | -0.083% | 22% | -3.74 | -28.55% |
| chop | 1160 | 48% | -0.010% | 33% | -0.46 | -11.92% |

## Turnover, fees, activity

- trades: 10829 (4.47/day); active days 88%
- turnover 46.3x equity/year; fees 4.63% of equity/year ($23,207 total)
- average gross exposure 0.10; brake active 1.1% of hours
- correlation of daily returns with s3v2 baseline: 0.30
