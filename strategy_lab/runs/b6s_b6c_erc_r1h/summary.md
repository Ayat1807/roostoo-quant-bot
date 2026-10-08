# Run: b6s_b6c_erc_r1h

Strategy `s3v2x_alloc`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +32.86% | +4.37% | 0.34 | 0.52 | -24.77% | 0.18 | 0.36 |
| in_sample | 2020-02-15 → 2024-12-31 | +33.88% | +6.16% | 0.44 | 0.68 | -19.68% | 0.31 | 0.50 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -0.69% | -0.39% | 0.06 | 0.09 | -17.63% | -0.02 | 0.05 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +8.94% | +8.94% | 0.55 | 0.81 | -17.63% | 0.51 | 0.64 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.45% | 40% | -5.93% | -6.72% | -2.77 | 14 | 99% |
| out_of_sample | 628 | -0.69% | 35% | -5.93% | -6.72% | -3.39 | 14 | 100% |
| in_sample | 1768 | -0.35% | 42% | -4.91% | -6.50% | -2.54 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.358% | 51% | 4.21 | +83.47% |
| bull | 687 | 28% | -0.012% | 41% | -0.34 | -9.53% |
| bear | 400 | 17% | +0.060% | 42% | 1.31 | +25.01% |
| chop | 1160 | 48% | -0.033% | 35% | -0.72 | -34.61% |

## Turnover, fees, activity

- trades: 15082 (6.22/day); active days 100%
- turnover 163.7x equity/year; fees 16.37% of equity/year ($68,663 total)
- average gross exposure 0.17; brake active 19.6% of hours
- correlation of daily returns with s3v2 baseline: 0.71
