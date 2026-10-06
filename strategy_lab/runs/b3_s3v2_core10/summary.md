# Run: b3_s3v2_core10

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +148.54% | +14.70% | 0.95 | 1.38 | -20.10% | 0.73 | 1.06 |
| in_sample | 2020-02-15 → 2024-12-31 | +75.71% | +12.24% | 0.84 | 1.22 | -20.10% | 0.61 | 0.92 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +41.59% | +21.88% | 1.23 | 1.80 | -14.60% | 1.50 | 1.54 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +19.72% | +19.72% | 1.05 | 1.55 | -14.60% | 1.35 | 1.34 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.22% | 45% | -7.88% | -8.53% | -1.64 | 14 | 100% |
| out_of_sample | 628 | -0.26% | 45% | -7.88% | -8.53% | -1.44 | 14 | 100% |
| in_sample | 1768 | -0.19% | 45% | -7.22% | -7.66% | -1.59 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.240% | 57% | 3.11 | +49.61% |
| bull | 687 | 28% | +0.084% | 53% | 2.45 | +75.13% |
| bear | 400 | 17% | +0.016% | 47% | 0.41 | +5.32% |
| chop | 1160 | 48% | -0.003% | 44% | -0.07 | -7.27% |

## Turnover, fees, activity

- trades: 5265 (2.17/day); active days 100%
- turnover 44.0x equity/year; fees 4.40% of equity/year ($24,139 total)
- average gross exposure 0.19; brake active 11.8% of hours
- correlation of daily returns with s3v2 baseline: 0.93
