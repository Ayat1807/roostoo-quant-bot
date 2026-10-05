# Run: mft_breakout_10

Strategy `breakout`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-05 | +8.41% | +1.22% | 0.62 | 0.87 | -4.32% | 0.28 | 0.62 |
| in_sample | 2020-02-15 → 2024-12-31 | +9.85% | +1.94% | 0.89 | 1.26 | -4.32% | 0.45 | 0.90 |
| out_of_sample | 2025-01-01 → 2026-10-05 | -1.32% | -0.75% | -0.54 | -0.74 | -2.10% | -0.36 | -0.57 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -0.68% | -0.68% | -0.50 | -0.70 | -1.99% | -0.34 | -0.53 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2411 | -0.06% | 40% | -0.70% | -1.98% | -3.06 | 12 | 16% |
| out_of_sample | 629 | -0.08% | 31% | -0.56% | -1.06% | -6.02 | 11 | 4% |
| in_sample | 1768 | -0.04% | 44% | -0.70% | -1.98% | -2.07 | 12 | 21% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.051% | 45% | 4.46 | +9.37% |
| bull | 687 | 28% | +0.010% | 39% | 1.42 | +6.71% |
| bear | 400 | 17% | -0.009% | 21% | -3.11 | -3.69% |
| chop | 1160 | 48% | -0.003% | 30% | -0.83 | -3.50% |

## Turnover, fees, activity

- trades: 2441 (1.01/day); active days 81%
- turnover 7.3x equity/year; fees 0.73% of equity/year ($2,578 total)
- average gross exposure 0.01; brake active 0.0% of hours
- correlation of daily returns with s3v2 baseline: 0.27
