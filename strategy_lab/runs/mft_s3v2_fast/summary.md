# Run: mft_s3v2_fast

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'bars_per_year': 17520}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-05 | +4.62% | +0.68% | 0.12 | 0.18 | -36.59% | 0.02 | 0.12 |
| in_sample | 2020-02-15 → 2024-12-31 | +32.48% | +5.93% | 0.46 | 0.72 | -27.91% | 0.21 | 0.49 |
| out_of_sample | 2025-01-01 → 2026-10-05 | -20.91% | -12.48% | -0.80 | -1.17 | -35.23% | -0.35 | -0.81 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -17.02% | -17.02% | -1.06 | -1.54 | -33.14% | -0.51 | -1.09 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2411 | -0.23% | 44% | -6.10% | -6.37% | -1.85 | 14 | 100% |
| out_of_sample | 629 | -1.03% | 33% | -5.29% | -6.07% | -4.69 | 14 | 100% |
| in_sample | 1768 | -0.07% | 48% | -6.10% | -6.37% | -0.68 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.425% | 50% | 5.80 | +107.57% |
| bull | 687 | 28% | -0.003% | 37% | -0.08 | -3.88% |
| bear | 400 | 17% | +0.009% | 38% | 0.26 | +2.68% |
| chop | 1160 | 48% | -0.054% | 32% | -1.27 | -48.20% |

## Turnover, fees, activity

- trades: 19001 (7.84/day); active days 100%
- turnover 196.3x equity/year; fees 19.63% of equity/year ($81,476 total)
- average gross exposure 0.16; brake active 21.7% of hours
- correlation of daily returns with s3v2 baseline: 0.57
