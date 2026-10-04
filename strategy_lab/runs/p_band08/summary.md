# Run: p_band08

Strategy `s3v2`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.08; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +154.99% | +15.14% | 1.27 | 1.85 | -12.15% | 1.25 | 1.49 |
| in_sample | 2020-02-15 → 2024-12-31 | +99.92% | +15.25% | 1.27 | 1.84 | -12.15% | 1.25 | 1.49 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +27.61% | +14.88% | 1.26 | 1.87 | -10.13% | 1.47 | 1.57 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +22.44% | +22.44% | 1.54 | 2.29 | -10.13% | 2.22 | 2.04 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.10% | 46% | -5.64% | -5.92% | -1.09 | 14 | 100% |
| out_of_sample | 628 | -0.16% | 45% | -5.64% | -5.92% | -1.42 | 14 | 100% |
| in_sample | 1768 | -0.08% | 47% | -5.09% | -5.72% | -0.91 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.261% | 59% | 3.96 | +56.11% |
| bull | 687 | 28% | +0.079% | 54% | 3.05 | +70.55% |
| bear | 400 | 17% | +0.036% | 48% | 1.43 | +14.76% |
| chop | 1160 | 48% | -0.014% | 43% | -0.47 | -16.06% |

## Turnover, fees, activity

- trades: 3862 (1.59/day); active days 100%
- turnover 29.5x equity/year; fees 2.95% of equity/year ($16,368 total)
- average gross exposure 0.14; brake active 4.1% of hours
- correlation of daily returns with s3v2 baseline: 0.80
