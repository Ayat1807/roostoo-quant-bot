# Run: b6s_b6a_A3_bocpd05_c50_r4h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +161.56% | +15.58% | 1.17 | 1.78 | -14.24% | 1.09 | 1.39 |
| in_sample | 2020-02-15 → 2024-12-31 | +121.43% | +17.68% | 1.32 | 2.02 | -11.24% | 1.57 | 1.68 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +18.20% | +9.98% | 0.78 | 1.16 | -14.24% | 0.70 | 0.91 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +7.17% | +7.17% | 0.54 | 0.81 | -14.24% | 0.50 | 0.64 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.14% | 45% | -4.80% | -5.20% | -1.18 | 14 | 100% |
| out_of_sample | 628 | -0.35% | 41% | -4.75% | -5.20% | -2.42 | 14 | 100% |
| in_sample | 1768 | -0.09% | 47% | -4.80% | -4.86% | -0.68 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.299% | 53% | 4.81 | +67.02% |
| bull | 687 | 28% | +0.065% | 47% | 2.18 | +54.59% |
| bear | 400 | 17% | +0.056% | 42% | 1.68 | +24.08% |
| chop | 1160 | 48% | -0.012% | 39% | -0.31 | -16.19% |

## Turnover, fees, activity

- trades: 8000 (3.30/day); active days 100%
- turnover 70.5x equity/year; fees 7.05% of equity/year ($41,899 total)
- average gross exposure 0.16; brake active 6.4% of hours
- correlation of daily returns with s3v2 baseline: 0.74
