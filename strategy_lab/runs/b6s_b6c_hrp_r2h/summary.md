# Run: b6s_b6c_hrp_r2h

Strategy `s3v2x_alloc`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'alloc': 'hrp'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +47.86% | +6.07% | 0.44 | 0.66 | -37.34% | 0.16 | 0.45 |
| in_sample | 2020-02-15 → 2024-12-31 | +67.64% | +11.16% | 0.72 | 1.09 | -26.73% | 0.42 | 0.78 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -11.70% | -6.83% | -0.36 | -0.54 | -23.94% | -0.29 | -0.41 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +2.35% | +2.35% | 0.22 | 0.33 | -18.26% | 0.13 | 0.23 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.51% | 40% | -5.52% | -6.58% | -3.01 | 14 | 100% |
| out_of_sample | 628 | -1.23% | 34% | -4.73% | -5.69% | -5.54 | 14 | 100% |
| in_sample | 1768 | -0.34% | 43% | -5.52% | -6.58% | -1.91 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.382% | 56% | 4.68 | +91.56% |
| bull | 687 | 28% | +0.043% | 45% | 1.04 | +31.84% |
| bear | 400 | 17% | +0.017% | 40% | 0.41 | +5.78% |
| chop | 1160 | 48% | -0.045% | 35% | -0.95 | -42.96% |

## Turnover, fees, activity

- trades: 15116 (6.24/day); active days 100%
- turnover 167.2x equity/year; fees 16.72% of equity/year ($91,124 total)
- average gross exposure 0.19; brake active 17.7% of hours
- correlation of daily returns with s3v2 baseline: 0.76
