# Run: b6b_hmm2_corr

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'corr_filter': True}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +167.07% | +15.94% | 1.14 | 1.68 | -16.08% | 0.99 | 1.31 |
| in_sample | 2020-02-15 → 2024-12-31 | +104.83% | +15.82% | 1.09 | 1.61 | -16.08% | 0.98 | 1.27 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +30.52% | +16.36% | 1.33 | 1.96 | -9.62% | 1.70 | 1.70 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +29.39% | +29.39% | 1.89 | 2.83 | -9.62% | 3.06 | 2.62 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.16% | 45% | -5.29% | -6.87% | -1.57 | 14 | 100% |
| out_of_sample | 628 | -0.13% | 45% | -4.37% | -5.49% | -1.07 | 14 | 100% |
| in_sample | 1768 | -0.16% | 45% | -5.29% | -6.87% | -1.61 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.255% | 57% | 3.48 | +54.07% |
| bull | 687 | 28% | +0.085% | 53% | 2.82 | +77.08% |
| bear | 400 | 17% | +0.042% | 48% | 1.54 | +17.57% |
| chop | 1160 | 48% | -0.011% | 44% | -0.28 | -14.34% |

## Turnover, fees, activity

- trades: 4763 (1.96/day); active days 100%
- turnover 35.1x equity/year; fees 3.51% of equity/year ($19,748 total)
- average gross exposure 0.16; brake active 6.2% of hours
- correlation of daily returns with s3v2 baseline: 0.82
