# Run: b6b_hmm2

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +181.11% | +16.84% | 1.13 | 1.65 | -18.47% | 0.91 | 1.27 |
| in_sample | 2020-02-15 → 2024-12-31 | +96.86% | +14.88% | 1.02 | 1.50 | -18.47% | 0.81 | 1.15 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +42.94% | +22.54% | 1.41 | 2.08 | -12.19% | 1.85 | 1.81 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +25.48% | +25.48% | 1.43 | 2.13 | -12.19% | 2.09 | 1.91 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.16% | 46% | -6.01% | -6.87% | -1.24 | 14 | 100% |
| out_of_sample | 628 | -0.09% | 47% | -6.01% | -6.45% | -0.60 | 14 | 100% |
| in_sample | 1768 | -0.16% | 46% | -5.64% | -6.87% | -1.29 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.251% | 56% | 3.31 | +52.75% |
| bull | 687 | 28% | +0.104% | 53% | 3.18 | +101.05% |
| bear | 400 | 17% | +0.040% | 47% | 1.29 | +16.72% |
| chop | 1160 | 48% | -0.015% | 44% | -0.37 | -19.32% |

## Turnover, fees, activity

- trades: 5080 (2.10/day); active days 100%
- turnover 40.4x equity/year; fees 4.04% of equity/year ($23,165 total)
- average gross exposure 0.18; brake active 8.7% of hours
- correlation of daily returns with s3v2 baseline: 0.86
