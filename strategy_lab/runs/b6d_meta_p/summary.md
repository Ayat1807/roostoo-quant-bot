# Run: b6d_meta_p

Strategy `s3v2x_meta`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'size_map': 'p'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +72.71% | +8.58% | 1.10 | 1.62 | -12.47% | 0.69 | 1.19 |
| in_sample | 2020-02-15 → 2024-12-31 | +62.47% | +10.45% | 1.18 | 1.74 | -12.47% | 0.84 | 1.30 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +6.35% | +3.57% | 0.97 | 1.42 | -3.71% | 0.96 | 1.15 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +5.38% | +5.38% | 1.34 | 2.04 | -3.02% | 1.78 | 1.75 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.10% | 41% | -5.29% | -6.87% | -2.37 | 14 | 100% |
| out_of_sample | 628 | -0.14% | 36% | -1.24% | -1.62% | -3.53 | 14 | 100% |
| in_sample | 1768 | -0.08% | 44% | -5.29% | -6.87% | -1.56 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.139% | 56% | 3.60 | +27.09% |
| bull | 687 | 28% | +0.045% | 56% | 2.64 | +36.13% |
| bear | 400 | 17% | +0.006% | 46% | 0.64 | +2.44% |
| chop | 1160 | 48% | +0.002% | 42% | 0.06 | +0.26% |

## Turnover, fees, activity

- trades: 3352 (1.38/day); active days 100%
- turnover 12.2x equity/year; fees 1.22% of equity/year ($6,066 total)
- average gross exposure 0.06; brake active 1.8% of hours
- correlation of daily returns with s3v2 baseline: 0.66
