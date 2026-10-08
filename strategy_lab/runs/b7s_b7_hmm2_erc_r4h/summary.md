# Run: b7s_b7_hmm2_erc_r4h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'inner': 's3v2x_alloc', 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +146.53% | +14.56% | 0.91 | 1.38 | -17.43% | 0.84 | 1.08 |
| in_sample | 2020-02-15 → 2024-12-31 | +104.88% | +15.83% | 0.97 | 1.50 | -14.59% | 1.08 | 1.22 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +20.45% | +11.16% | 0.73 | 1.07 | -17.43% | 0.64 | 0.84 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +13.83% | +13.83% | 0.79 | 1.18 | -17.43% | 0.79 | 0.94 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.19% | 45% | -5.59% | -7.34% | -1.48 | 14 | 99% |
| out_of_sample | 628 | -0.34% | 42% | -5.11% | -5.67% | -2.13 | 14 | 100% |
| in_sample | 1768 | -0.13% | 46% | -5.59% | -7.34% | -1.02 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.289% | 49% | 3.74 | +63.20% |
| bull | 687 | 28% | +0.056% | 44% | 1.53 | +44.29% |
| bear | 400 | 17% | +0.053% | 45% | 1.23 | +22.11% |
| chop | 1160 | 48% | -0.007% | 37% | -0.15 | -11.97% |

## Turnover, fees, activity

- trades: 9216 (3.80/day); active days 100%
- turnover 94.2x equity/year; fees 9.42% of equity/year ($53,507 total)
- average gross exposure 0.17; brake active 14.4% of hours
- correlation of daily returns with s3v2 baseline: 0.73
