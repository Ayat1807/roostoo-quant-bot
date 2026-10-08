# Run: b6s_b6b_corr_r2h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'corr_filter': True}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +155.71% | +15.19% | 1.09 | 1.65 | -13.55% | 1.12 | 1.32 |
| in_sample | 2020-02-15 → 2024-12-31 | +115.96% | +17.08% | 1.18 | 1.81 | -12.99% | 1.32 | 1.47 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +18.49% | +10.13% | 0.81 | 1.19 | -13.40% | 0.76 | 0.94 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +21.13% | +21.13% | 1.29 | 1.92 | -13.40% | 1.58 | 1.63 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.16% | 44% | -5.18% | -6.85% | -1.75 | 14 | 99% |
| out_of_sample | 628 | -0.28% | 38% | -5.18% | -6.46% | -3.21 | 14 | 100% |
| in_sample | 1768 | -0.11% | 46% | -4.72% | -6.85% | -1.08 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.317% | 51% | 4.55 | +72.08% |
| bull | 687 | 28% | +0.053% | 46% | 1.64 | +41.84% |
| bear | 400 | 17% | +0.058% | 41% | 1.78 | +25.37% |
| chop | 1160 | 48% | -0.010% | 38% | -0.26 | -14.18% |

## Turnover, fees, activity

- trades: 7906 (3.26/day); active days 100%
- turnover 73.7x equity/year; fees 7.37% of equity/year ($43,325 total)
- average gross exposure 0.15; brake active 7.9% of hours
- correlation of daily returns with s3v2 baseline: 0.72
