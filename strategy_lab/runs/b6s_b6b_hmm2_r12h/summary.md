# Run: b6s_b6b_hmm2_r12h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +254.71% | +21.01% | 1.35 | 2.02 | -14.73% | 1.43 | 1.64 |
| in_sample | 2020-02-15 → 2024-12-31 | +142.40% | +19.88% | 1.30 | 1.95 | -14.73% | 1.35 | 1.58 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +46.38% | +24.20% | 1.47 | 2.19 | -12.64% | 1.91 | 1.89 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +30.44% | +30.44% | 1.62 | 2.43 | -12.64% | 2.41 | 2.18 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.17% | 45% | -6.53% | -8.27% | -1.58 | 14 | 100% |
| out_of_sample | 628 | -0.26% | 44% | -5.60% | -6.06% | -1.66 | 14 | 100% |
| in_sample | 1768 | -0.15% | 46% | -6.53% | -8.27% | -1.38 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.293% | 56% | 3.75 | +64.17% |
| bull | 687 | 28% | +0.090% | 52% | 2.63 | +82.83% |
| bear | 400 | 17% | +0.064% | 48% | 1.80 | +27.91% |
| chop | 1160 | 48% | -0.002% | 42% | -0.04 | -5.36% |

## Turnover, fees, activity

- trades: 5623 (2.32/day); active days 100%
- turnover 48.6x equity/year; fees 4.86% of equity/year ($33,391 total)
- average gross exposure 0.17; brake active 10.6% of hours
- correlation of daily returns with s3v2 baseline: 0.82
