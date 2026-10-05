# Run: b2_core

Strategy `s3v2`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +141.93% | +14.86% | 0.97 | 1.41 | -20.10% | 0.74 | 1.07 |
| in_sample | 2020-02-15 → 2024-12-31 | +75.71% | +12.24% | 0.84 | 1.22 | -20.10% | 0.61 | 0.92 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +37.83% | +23.92% | 1.36 | 1.97 | -14.60% | 1.64 | 1.69 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +16.72% | +22.97% | 1.21 | 1.78 | -14.60% | 1.57 | 1.55 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.19% | 45% | -7.88% | -8.53% | -1.42 | 14 | 100% |
| out_of_sample | 532 | -0.11% | 48% | -7.88% | -8.53% | -0.55 | 14 | 100% |
| in_sample | 1768 | -0.19% | 45% | -7.22% | -7.66% | -1.59 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.178% | 58% | 2.58 | +33.38% |
| bull | 659 | 28% | +0.093% | 54% | 2.69 | +81.97% |
| bear | 399 | 17% | +0.017% | 47% | 0.44 | +5.84% |
| chop | 1099 | 47% | +0.001% | 44% | 0.01 | -3.04% |

## Turnover, fees, activity

- trades: 4965 (2.13/day); active days 100%
- turnover 42.0x equity/year; fees 4.20% of equity/year ($21,740 total)
- average gross exposure 0.19; brake active 10.8% of hours
