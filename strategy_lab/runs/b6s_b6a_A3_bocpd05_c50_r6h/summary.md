# Run: b6s_b6a_A3_bocpd05_c50_r6h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +177.03% | +16.59% | 1.25 | 1.89 | -13.86% | 1.20 | 1.49 |
| in_sample | 2020-02-15 → 2024-12-31 | +129.36% | +18.53% | 1.40 | 2.12 | -11.59% | 1.60 | 1.74 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +20.87% | +11.38% | 0.87 | 1.31 | -13.86% | 0.82 | 1.03 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +9.45% | +9.45% | 0.68 | 1.01 | -13.86% | 0.68 | 0.81 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.07% | 48% | -5.04% | -6.47% | -0.65 | 14 | 99% |
| out_of_sample | 628 | -0.27% | 42% | -5.04% | -5.39% | -1.88 | 14 | 100% |
| in_sample | 1768 | -0.00% | 50% | -5.01% | -6.47% | -0.02 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.318% | 56% | 4.95 | +72.66% |
| bull | 687 | 28% | +0.068% | 47% | 2.27 | +58.01% |
| bear | 400 | 17% | +0.051% | 44% | 1.57 | +21.52% |
| chop | 1160 | 48% | -0.011% | 39% | -0.30 | -14.49% |

## Turnover, fees, activity

- trades: 7398 (3.05/day); active days 100%
- turnover 63.4x equity/year; fees 6.34% of equity/year ($38,963 total)
- average gross exposure 0.16; brake active 6.2% of hours
- correlation of daily returns with s3v2 baseline: 0.76
