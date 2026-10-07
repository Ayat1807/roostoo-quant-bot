# Run: b6c_erc

Strategy `s3v2x_alloc`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +209.06% | +18.52% | 1.11 | 1.64 | -18.63% | 0.99 | 1.29 |
| in_sample | 2020-02-15 → 2024-12-31 | +124.57% | +18.02% | 1.07 | 1.60 | -18.63% | 0.97 | 1.25 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +37.81% | +20.02% | 1.21 | 1.78 | -13.12% | 1.53 | 1.53 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +24.86% | +24.86% | 1.30 | 1.93 | -13.12% | 1.89 | 1.73 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.22% | 44% | -7.41% | -7.57% | -1.66 | 14 | 99% |
| out_of_sample | 628 | -0.13% | 48% | -5.52% | -6.35% | -0.65 | 14 | 100% |
| in_sample | 1768 | -0.23% | 44% | -7.41% | -7.57% | -1.96 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.316% | 53% | 3.70 | +70.37% |
| bull | 687 | 28% | +0.081% | 51% | 2.12 | +71.71% |
| bear | 400 | 17% | +0.040% | 46% | 1.01 | +15.83% |
| chop | 1160 | 48% | -0.002% | 44% | -0.05 | -6.05% |

## Turnover, fees, activity

- trades: 5364 (2.21/day); active days 100%
- turnover 46.8x equity/year; fees 4.68% of equity/year ($27,821 total)
- average gross exposure 0.18; brake active 12.8% of hours
- correlation of daily returns with s3v2 baseline: 0.83
