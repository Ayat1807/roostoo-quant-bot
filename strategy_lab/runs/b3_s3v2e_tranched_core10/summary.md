# Run: b3_s3v2e_tranched_core10

Strategy `s3v2_tranched`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'tranches': 4, 'spacing_bars': 6}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +287.34% | +22.62% | 1.40 | 2.03 | -13.44% | 1.68 | 1.73 |
| in_sample | 2020-02-15 → 2024-12-31 | +199.98% | +25.23% | 1.52 | 2.22 | -12.95% | 1.95 | 1.93 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +29.26% | +15.72% | 1.04 | 1.49 | -11.49% | 1.37 | 1.32 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +19.25% | +19.25% | 1.15 | 1.67 | -11.49% | 1.68 | 1.52 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.14% | 46% | -7.00% | -7.67% | -0.89 | 14 | 100% |
| out_of_sample | 628 | -0.22% | 45% | -4.64% | -5.79% | -1.29 | 14 | 100% |
| in_sample | 1768 | -0.10% | 47% | -7.00% | -7.67% | -0.71 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.236% | 59% | 2.96 | +48.36% |
| bull | 687 | 28% | +0.124% | 55% | 3.41 | +130.74% |
| bear | 400 | 17% | +0.039% | 49% | 1.15 | +15.80% |
| chop | 1160 | 48% | +0.003% | 44% | 0.07 | +0.09% |

## Turnover, fees, activity

- trades: 4815 (1.99/day); active days 100%
- turnover 27.4x equity/year; fees 2.74% of equity/year ($22,194 total)
- average gross exposure 0.20; brake active 6.1% of hours
- correlation of daily returns with s3v2 baseline: 0.90
