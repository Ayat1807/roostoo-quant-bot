# Run: b6a_A4_tstat_cusum4_c50

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'signal': 'tstat', 'tstat_cap': 2.0}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +116.03% | +12.30% | 1.34 | 1.93 | -9.01% | 1.36 | 1.58 |
| in_sample | 2020-02-15 → 2024-12-31 | +98.09% | +15.03% | 1.57 | 2.27 | -9.01% | 1.67 | 1.88 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +9.18% | +5.13% | 0.65 | 0.91 | -6.72% | 0.76 | 0.79 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +11.61% | +11.61% | 1.31 | 1.91 | -5.35% | 2.17 | 1.81 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.11% | 45% | -3.07% | -5.57% | -1.46 | 14 | 100% |
| out_of_sample | 628 | -0.20% | 38% | -2.59% | -3.50% | -2.55 | 14 | 100% |
| in_sample | 1768 | -0.06% | 48% | -3.07% | -5.57% | -0.71 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.137% | 57% | 2.88 | +26.25% |
| bull | 687 | 28% | +0.077% | 55% | 3.70 | +68.70% |
| bear | 400 | 17% | +0.022% | 50% | 1.08 | +8.87% |
| chop | 1160 | 48% | -0.005% | 46% | -0.23 | -6.37% |

## Turnover, fees, activity

- trades: 5465 (2.25/day); active days 100%
- turnover 10.8x equity/year; fees 1.08% of equity/year ($5,906 total)
- average gross exposure 0.11; brake active 0.7% of hours
- correlation of daily returns with s3v2 baseline: 0.78
