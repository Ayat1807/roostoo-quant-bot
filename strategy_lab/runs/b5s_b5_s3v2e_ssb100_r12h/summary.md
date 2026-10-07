# Run: b5s_b5_s3v2e_ssb100_r12h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 1.0, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +306.40% | +23.51% | 1.45 | 2.18 | -14.31% | 1.64 | 1.80 |
| in_sample | 2020-02-15 → 2024-12-31 | +170.63% | +22.62% | 1.42 | 2.14 | -14.31% | 1.58 | 1.75 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +50.21% | +26.04% | 1.53 | 2.29 | -13.58% | 1.92 | 1.95 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +33.88% | +33.88% | 1.72 | 2.58 | -13.58% | 2.49 | 2.30 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.12% | 47% | -5.02% | -6.99% | -1.15 | 14 | 100% |
| out_of_sample | 628 | -0.13% | 46% | -4.90% | -5.94% | -0.84 | 14 | 100% |
| in_sample | 1768 | -0.09% | 47% | -5.02% | -6.99% | -1.03 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.308% | 55% | 3.88 | +68.59% |
| bull | 687 | 28% | +0.098% | 52% | 2.71 | +92.34% |
| bear | 400 | 17% | +0.068% | 48% | 1.90 | +30.22% |
| chop | 1160 | 48% | +0.002% | 42% | 0.05 | -1.41% |

## Turnover, fees, activity

- trades: 6057 (2.50/day); active days 100%
- turnover 55.5x equity/year; fees 5.55% of equity/year ($40,093 total)
- average gross exposure 0.18; brake active 11.6% of hours
- correlation of daily returns with s3v2 baseline: 0.82
