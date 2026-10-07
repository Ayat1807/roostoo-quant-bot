# Run: b6s_b6a_A3_cusum4_c50_r2h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +149.08% | +14.73% | 1.09 | 1.66 | -16.63% | 0.89 | 1.26 |
| in_sample | 2020-02-15 → 2024-12-31 | +111.30% | +16.56% | 1.21 | 1.88 | -13.25% | 1.25 | 1.49 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +17.96% | +9.85% | 0.75 | 1.12 | -16.63% | 0.59 | 0.85 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +7.18% | +7.18% | 0.52 | 0.78 | -16.63% | 0.43 | 0.60 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.14% | 46% | -4.62% | -5.28% | -1.20 | 14 | 99% |
| out_of_sample | 628 | -0.37% | 41% | -4.46% | -5.28% | -2.29 | 14 | 100% |
| in_sample | 1768 | -0.07% | 48% | -4.62% | -5.28% | -0.61 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.362% | 56% | 5.53 | +86.33% |
| bull | 687 | 28% | +0.053% | 45% | 1.66 | +42.20% |
| bear | 400 | 17% | +0.050% | 40% | 1.49 | +21.12% |
| chop | 1160 | 48% | -0.017% | 37% | -0.41 | -20.12% |

## Turnover, fees, activity

- trades: 9790 (4.04/day); active days 100%
- turnover 87.7x equity/year; fees 8.77% of equity/year ($51,048 total)
- average gross exposure 0.16; brake active 7.0% of hours
- correlation of daily returns with s3v2 baseline: 0.74
