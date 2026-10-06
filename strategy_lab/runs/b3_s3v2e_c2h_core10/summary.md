# Run: b3_s3v2e_c2h_core10

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +166.00% | +15.87% | 1.05 | 1.54 | -19.15% | 0.83 | 1.18 |
| in_sample | 2020-02-15 → 2024-12-31 | +86.46% | +13.61% | 0.93 | 1.37 | -19.15% | 0.71 | 1.04 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +42.80% | +22.47% | 1.37 | 2.00 | -13.10% | 1.72 | 1.73 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +25.19% | +25.19% | 1.37 | 2.02 | -13.10% | 1.92 | 1.79 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.18% | 45% | -6.92% | -7.22% | -1.50 | 14 | 100% |
| out_of_sample | 628 | -0.13% | 48% | -6.20% | -6.65% | -0.68 | 14 | 100% |
| in_sample | 1768 | -0.18% | 45% | -6.92% | -7.22% | -1.65 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.254% | 59% | 3.28 | +53.39% |
| bull | 687 | 28% | +0.096% | 53% | 2.89 | +90.53% |
| bear | 400 | 17% | +0.042% | 47% | 1.21 | +17.32% |
| chop | 1160 | 48% | -0.016% | 43% | -0.40 | -20.19% |

## Turnover, fees, activity

- trades: 5067 (2.09/day); active days 100%
- turnover 40.5x equity/year; fees 4.05% of equity/year ($22,003 total)
- average gross exposure 0.18; brake active 9.4% of hours
- correlation of daily returns with s3v2 baseline: 0.98
