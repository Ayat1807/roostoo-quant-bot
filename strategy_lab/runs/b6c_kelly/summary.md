# Run: b6c_kelly

Strategy `s3v2x_alloc`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'alloc': 'kelly'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +119.45% | +12.57% | 0.80 | 1.15 | -17.49% | 0.72 | 0.92 |
| in_sample | 2020-02-15 → 2024-12-31 | +105.45% | +15.89% | 0.97 | 1.40 | -17.49% | 0.91 | 1.12 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +6.84% | +3.83% | 0.31 | 0.45 | -17.49% | 0.22 | 0.34 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +9.80% | +9.80% | 0.62 | 0.90 | -15.01% | 0.65 | 0.74 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.19% | 46% | -7.03% | -7.75% | -1.21 | 14 | 100% |
| out_of_sample | 628 | -0.34% | 42% | -5.64% | -7.15% | -2.47 | 14 | 100% |
| in_sample | 1768 | -0.11% | 48% | -7.03% | -7.75% | -0.73 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.174% | 53% | 2.16 | +33.02% |
| bull | 687 | 28% | +0.102% | 55% | 2.52 | +97.33% |
| bear | 400 | 17% | +0.034% | 45% | 0.96 | +13.56% |
| chop | 1160 | 48% | -0.020% | 44% | -0.46 | -24.28% |

## Turnover, fees, activity

- trades: 5192 (2.14/day); active days 100%
- turnover 42.8x equity/year; fees 4.28% of equity/year ($24,141 total)
- average gross exposure 0.18; brake active 14.7% of hours
- correlation of daily returns with s3v2 baseline: 0.78
