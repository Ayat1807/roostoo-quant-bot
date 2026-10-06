# Run: b3_s3v2e_r12_core10

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +236.91% | +20.07% | 1.27 | 1.90 | -14.73% | 1.36 | 1.55 |
| in_sample | 2020-02-15 → 2024-12-31 | +129.12% | +18.51% | 1.21 | 1.80 | -14.73% | 1.26 | 1.46 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +47.09% | +24.55% | 1.45 | 2.16 | -13.09% | 1.87 | 1.86 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +31.23% | +31.23% | 1.60 | 2.41 | -13.09% | 2.38 | 2.16 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.20% | 45% | -6.53% | -8.27% | -1.60 | 14 | 100% |
| out_of_sample | 628 | -0.26% | 44% | -5.60% | -6.06% | -1.52 | 14 | 100% |
| in_sample | 1768 | -0.18% | 45% | -6.53% | -8.27% | -1.58 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.300% | 55% | 3.75 | +66.03% |
| bull | 687 | 28% | +0.089% | 52% | 2.56 | +81.36% |
| bear | 400 | 17% | +0.063% | 47% | 1.75 | +27.50% |
| chop | 1160 | 48% | -0.006% | 42% | -0.14 | -10.11% |

## Turnover, fees, activity

- trades: 5679 (2.34/day); active days 100%
- turnover 49.6x equity/year; fees 4.96% of equity/year ($32,656 total)
- average gross exposure 0.17; brake active 11.8% of hours
- correlation of daily returns with s3v2 baseline: 0.93
