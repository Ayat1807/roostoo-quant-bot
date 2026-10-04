# Run: s3v2_base

Strategy `s3v2`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard full

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +154.50% | +15.11% | 0.81 | 1.15 | -24.22% | 0.62 | 0.89 |
| in_sample | 2020-02-15 → 2024-12-31 | +149.33% | +20.58% | 1.04 | 1.49 | -24.22% | 0.85 | 1.16 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +2.43% | +1.38% | 0.17 | 0.24 | -20.46% | 0.07 | 0.16 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +4.27% | +4.27% | 0.31 | 0.43 | -20.46% | 0.21 | 0.33 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.47% | 42% | -8.73% | -9.47% | -2.13 | 14 | 93% |
| out_of_sample | 628 | -0.99% | 36% | -8.73% | -9.47% | -3.83 | 14 | 91% |
| in_sample | 1768 | -0.32% | 45% | -7.07% | -8.75% | -1.40 | 14 | 93% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.309% | 54% | 2.91 | +66.23% |
| bull | 687 | 28% | +0.117% | 54% | 2.63 | +118.22% |
| bear | 400 | 17% | +0.002% | 45% | 0.03 | -1.32% |
| chop | 1160 | 48% | -0.023% | 45% | -0.50 | -26.81% |

## Turnover, fees, activity

- trades: 9603 (3.96/day); active days 99%
- turnover 60.9x equity/year; fees 6.09% of equity/year ($37,910 total)
- average gross exposure 0.24; brake active 20.9% of hours
