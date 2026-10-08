# Run: b7s_b7_hmm2_erc_r6h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'inner': 's3v2x_alloc', 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +171.47% | +16.23% | 1.00 | 1.51 | -18.51% | 0.88 | 1.17 |
| in_sample | 2020-02-15 → 2024-12-31 | +139.10% | +19.55% | 1.16 | 1.76 | -12.07% | 1.62 | 1.54 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +13.68% | +7.57% | 0.54 | 0.80 | -18.51% | 0.41 | 0.61 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +9.47% | +9.47% | 0.59 | 0.88 | -18.51% | 0.51 | 0.68 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.17% | 46% | -5.37% | -7.28% | -1.43 | 14 | 99% |
| out_of_sample | 628 | -0.42% | 42% | -5.29% | -5.44% | -2.51 | 14 | 100% |
| in_sample | 1768 | -0.10% | 48% | -5.37% | -7.28% | -0.65 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.372% | 57% | 4.65 | +88.52% |
| bull | 687 | 28% | +0.058% | 46% | 1.56 | +46.67% |
| bear | 400 | 17% | +0.057% | 45% | 1.31 | +23.79% |
| chop | 1160 | 48% | -0.014% | 38% | -0.31 | -18.56% |

## Turnover, fees, activity

- trades: 7972 (3.29/day); active days 100%
- turnover 80.6x equity/year; fees 8.06% of equity/year ($51,381 total)
- average gross exposure 0.17; brake active 14.3% of hours
- correlation of daily returns with s3v2 baseline: 0.76
