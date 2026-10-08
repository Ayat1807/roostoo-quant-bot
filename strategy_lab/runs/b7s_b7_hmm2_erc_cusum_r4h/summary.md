# Run: b7s_b7_hmm2_erc_cusum_r4h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'inner': 's3v2x_alloc', 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +78.37% | +9.11% | 0.66 | 1.02 | -22.30% | 0.41 | 0.73 |
| in_sample | 2020-02-15 → 2024-12-31 | +70.79% | +11.59% | 0.81 | 1.25 | -14.02% | 0.83 | 0.99 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +4.54% | +2.56% | 0.25 | 0.37 | -22.30% | 0.11 | 0.26 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -1.84% | -1.84% | -0.04 | -0.06 | -22.30% | -0.08 | -0.06 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.23% | 44% | -5.41% | -6.05% | -1.99 | 14 | 100% |
| out_of_sample | 628 | -0.47% | 40% | -5.41% | -6.05% | -3.30 | 14 | 100% |
| in_sample | 1768 | -0.15% | 46% | -4.83% | -5.70% | -1.53 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.303% | 51% | 4.40 | +67.71% |
| bull | 687 | 28% | +0.027% | 44% | 0.82 | +18.61% |
| bear | 400 | 17% | +0.032% | 45% | 0.83 | +12.30% |
| chop | 1160 | 48% | -0.013% | 37% | -0.31 | -17.59% |

## Turnover, fees, activity

- trades: 10205 (4.21/day); active days 100%
- turnover 95.5x equity/year; fees 9.55% of equity/year ($46,607 total)
- average gross exposure 0.16; brake active 11.8% of hours
- correlation of daily returns with s3v2 baseline: 0.70
