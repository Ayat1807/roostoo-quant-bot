# Run: b3_donchian_core10

Strategy `donchian_long`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +121.02% | +12.69% | 1.31 | 1.76 | -10.66% | 1.19 | 1.45 |
| in_sample | 2020-02-15 → 2024-12-31 | +125.84% | +18.16% | 1.63 | 2.20 | -10.66% | 1.70 | 1.88 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -2.27% | -1.30% | -0.22 | -0.30 | -6.57% | -0.20 | -0.25 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -2.17% | -2.17% | -0.60 | -0.80 | -5.71% | -0.38 | -0.61 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.04% | 45% | -7.87% | -8.56% | -1.73 | 14 | 80% |
| out_of_sample | 628 | -0.11% | 33% | -2.87% | -3.70% | -4.51 | 14 | 73% |
| in_sample | 1768 | -0.01% | 49% | -7.87% | -8.56% | -0.60 | 14 | 82% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.103% | 47% | 1.72 | +18.56% |
| bull | 687 | 28% | +0.115% | 61% | 4.09 | +118.79% |
| bear | 400 | 17% | -0.020% | 35% | -1.84 | -7.58% |
| chop | 1160 | 48% | -0.007% | 47% | -0.45 | -7.80% |

## Turnover, fees, activity

- trades: 2492 (1.03/day); active days 94%
- turnover 2.5x equity/year; fees 0.25% of equity/year ($1,557 total)
- average gross exposure 0.08; brake active 0.6% of hours
- correlation of daily returns with s3v2 baseline: 0.25
