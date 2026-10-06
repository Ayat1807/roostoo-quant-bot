# Run: b3s_xsmom_tm10_r12h

Strategy `xsmom`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'PAXGUSDT', 'POLUSDT', 'ICPUSDT', 'TRXUSDT', 'LISTAUSDT', 'STOUSDT', 'CAKEUSDT', 'TUTUSDT', 'SOLUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +158.97% | +15.41% | 0.65 | 0.91 | -34.86% | 0.44 | 0.69 |
| in_sample | 2020-02-15 → 2024-12-31 | +45.70% | +8.01% | 0.43 | 0.59 | -34.86% | 0.23 | 0.43 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +77.53% | +38.62% | 1.11 | 1.63 | -26.41% | 1.46 | 1.42 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +104.43% | +104.43% | 2.05 | 3.06 | -26.41% | 3.95 | 3.02 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.60% | 43% | -14.74% | -16.99% | -1.86 | 12 | 27% |
| out_of_sample | 628 | -0.46% | 47% | -14.74% | -16.99% | -0.84 | 13 | 48% |
| in_sample | 1768 | -0.65% | 41% | -13.38% | -14.47% | -2.06 | 11 | 20% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.069% | 41% | 0.69 | +9.26% |
| bull | 687 | 28% | +0.185% | 44% | 2.25 | +228.01% |
| bear | 400 | 17% | -0.104% | 26% | -1.74 | -35.60% |
| chop | 1160 | 48% | +0.021% | 36% | 0.28 | +13.93% |

## Turnover, fees, activity

- trades: 12816 (5.29/day); active days 80%
- turnover 112.1x equity/year; fees 11.21% of equity/year ($45,013 total)
- average gross exposure 0.21; brake active 38.9% of hours
- correlation of daily returns with s3v2 baseline: 0.21
