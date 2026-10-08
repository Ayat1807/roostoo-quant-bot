# Run: b7s_b7_hmm2_erc_cusum_r2h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'inner': 's3v2x_alloc', 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +29.47% | +3.97% | 0.34 | 0.52 | -22.11% | 0.18 | 0.37 |
| in_sample | 2020-02-15 → 2024-12-31 | +30.11% | +5.54% | 0.44 | 0.69 | -15.55% | 0.36 | 0.51 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -0.42% | -0.24% | 0.05 | 0.08 | -22.11% | -0.01 | 0.04 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -1.35% | -1.35% | -0.01 | -0.01 | -22.11% | -0.06 | -0.02 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.32% | 41% | -8.29% | -8.40% | -2.75 | 14 | 99% |
| out_of_sample | 628 | -0.54% | 39% | -8.29% | -8.40% | -3.26 | 14 | 100% |
| in_sample | 1768 | -0.25% | 42% | -5.17% | -5.58% | -2.56 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.304% | 55% | 4.49 | +68.25% |
| bull | 687 | 28% | -0.001% | 43% | -0.04 | -2.17% |
| bear | 400 | 17% | +0.039% | 41% | 0.96 | +15.34% |
| chop | 1160 | 48% | -0.027% | 36% | -0.64 | -29.98% |

## Turnover, fees, activity

- trades: 12763 (5.27/day); active days 100%
- turnover 123.9x equity/year; fees 12.39% of equity/year ($51,262 total)
- average gross exposure 0.16; brake active 15.1% of hours
- correlation of daily returns with s3v2 baseline: 0.67
