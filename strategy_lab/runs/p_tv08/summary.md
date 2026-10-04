# Run: p_tv08

Strategy `s3v2`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +113.19% | +12.08% | 0.52 | 0.74 | -44.49% | 0.27 | 0.53 |
| in_sample | 2020-02-15 → 2024-12-31 | +84.45% | +13.36% | 0.55 | 0.79 | -44.49% | 0.30 | 0.57 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +16.46% | +9.06% | 0.43 | 0.61 | -28.24% | 0.32 | 0.47 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +8.45% | +8.45% | 0.41 | 0.60 | -28.24% | 0.30 | 0.46 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.81% | 41% | -19.30% | -20.67% | -2.14 | 14 | 89% |
| out_of_sample | 628 | -0.59% | 44% | -15.38% | -16.73% | -1.13 | 14 | 80% |
| in_sample | 1768 | -0.85% | 40% | -19.30% | -20.67% | -2.36 | 14 | 93% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.325% | 55% | 2.03 | +63.41% |
| bull | 687 | 28% | +0.170% | 53% | 2.20 | +197.53% |
| bear | 400 | 17% | +0.045% | 44% | 0.55 | +14.16% |
| chop | 1160 | 48% | -0.064% | 44% | -0.76 | -58.41% |

## Turnover, fees, activity

- trades: 10297 (4.25/day); active days 99%
- turnover 115.0x equity/year; fees 11.50% of equity/year ($63,905 total)
- average gross exposure 0.38; brake active 45.3% of hours
- correlation of daily returns with s3v2 baseline: 0.83
