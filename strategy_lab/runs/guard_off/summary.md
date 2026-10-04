# Run: guard_off

Strategy `s3v2`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +111.24% | +11.92% | 0.82 | 1.19 | -19.57% | 0.61 | 0.90 |
| in_sample | 2020-02-15 → 2024-12-31 | +50.68% | +8.76% | 0.65 | 0.95 | -19.57% | 0.45 | 0.71 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +40.28% | +21.23% | 1.21 | 1.77 | -16.81% | 1.26 | 1.45 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +18.86% | +18.86% | 1.02 | 1.50 | -16.81% | 1.12 | 1.24 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.07% | 43% | -8.05% | -8.76% | -1.00 | 9 | 5% |
| out_of_sample | 628 | -0.22% | 45% | -8.05% | -8.76% | -1.42 | 9 | 5% |
| in_sample | 1768 | -0.03% | 42% | -7.01% | -7.46% | -0.82 | 8 | 6% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.206% | 34% | 2.87 | +41.36% |
| bull | 687 | 28% | +0.071% | 44% | 2.08 | +60.50% |
| bear | 400 | 17% | +0.019% | 33% | 0.49 | +6.72% |
| chop | 1160 | 48% | -0.006% | 40% | -0.15 | -10.18% |

## Turnover, fees, activity

- trades: 3863 (1.59/day); active days 57%
- turnover 40.8x equity/year; fees 4.08% of equity/year ($19,789 total)
- average gross exposure 0.18; brake active 11.0% of hours
- correlation of daily returns with s3v2 baseline: 0.83
