# Run: b6s_b6a_A3_cusum4_c50_r1h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +165.96% | +15.87% | 1.05 | 1.60 | -16.90% | 0.94 | 1.24 |
| in_sample | 2020-02-15 → 2024-12-31 | +103.45% | +15.66% | 1.06 | 1.62 | -16.90% | 0.93 | 1.25 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +30.81% | +16.51% | 1.03 | 1.55 | -15.09% | 1.09 | 1.26 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +24.45% | +24.45% | 1.27 | 1.91 | -15.09% | 1.62 | 1.63 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.18% | 45% | -5.82% | -6.69% | -1.60 | 14 | 98% |
| out_of_sample | 628 | -0.45% | 40% | -4.64% | -6.60% | -2.75 | 14 | 100% |
| in_sample | 1768 | -0.12% | 47% | -5.82% | -6.69% | -1.02 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.348% | 53% | 4.54 | +81.01% |
| bull | 687 | 28% | +0.054% | 44% | 1.57 | +42.37% |
| bear | 400 | 17% | +0.067% | 41% | 1.72 | +29.07% |
| chop | 1160 | 48% | -0.014% | 36% | -0.32 | -17.88% |

## Turnover, fees, activity

- trades: 10108 (4.17/day); active days 100%
- turnover 101.6x equity/year; fees 10.16% of equity/year ($57,403 total)
- average gross exposure 0.16; brake active 10.4% of hours
- correlation of daily returns with s3v2 baseline: 0.76
