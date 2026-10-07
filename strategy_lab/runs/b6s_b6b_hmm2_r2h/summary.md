# Run: b6s_b6b_hmm2_r2h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +184.40% | +17.05% | 1.15 | 1.75 | -15.53% | 1.10 | 1.38 |
| in_sample | 2020-02-15 → 2024-12-31 | +124.33% | +18.00% | 1.23 | 1.89 | -13.36% | 1.35 | 1.53 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +26.86% | +14.49% | 0.95 | 1.43 | -15.53% | 0.93 | 1.14 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +16.53% | +16.53% | 0.96 | 1.44 | -15.53% | 1.06 | 1.18 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.18% | 45% | -4.81% | -6.85% | -1.78 | 14 | 99% |
| out_of_sample | 628 | -0.42% | 40% | -4.81% | -5.43% | -2.91 | 14 | 100% |
| in_sample | 1768 | -0.12% | 47% | -4.73% | -6.85% | -1.08 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.335% | 51% | 4.74 | +77.36% |
| bull | 687 | 28% | +0.062% | 45% | 1.82 | +50.81% |
| bear | 400 | 17% | +0.067% | 40% | 1.76 | +29.35% |
| chop | 1160 | 48% | -0.011% | 38% | -0.27 | -15.59% |

## Turnover, fees, activity

- trades: 8626 (3.56/day); active days 100%
- turnover 85.3x equity/year; fees 8.53% of equity/year ($53,245 total)
- average gross exposure 0.16; brake active 9.2% of hours
- correlation of daily returns with s3v2 baseline: 0.76
