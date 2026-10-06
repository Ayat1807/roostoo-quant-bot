# Run: b3s_s3v2e_tv08_w04_core10_r12h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.4, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +185.00% | +17.09% | 0.66 | 0.94 | -42.05% | 0.41 | 0.70 |
| in_sample | 2020-02-15 → 2024-12-31 | +208.25% | +25.93% | 0.89 | 1.26 | -42.05% | 0.62 | 0.96 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -7.52% | -4.35% | 0.01 | 0.02 | -26.84% | -0.16 | -0.04 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +10.09% | +10.09% | 0.46 | 0.69 | -26.29% | 0.38 | 0.53 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.82% | 43% | -18.25% | -19.35% | -1.86 | 14 | 92% |
| out_of_sample | 628 | -1.29% | 36% | -12.25% | -14.07% | -2.74 | 14 | 81% |
| in_sample | 1768 | -0.54% | 45% | -18.25% | -19.35% | -1.36 | 14 | 96% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.583% | 53% | 3.76 | +158.19% |
| bull | 687 | 28% | +0.163% | 50% | 2.13 | +184.03% |
| bear | 400 | 17% | -0.016% | 44% | -0.20 | -10.55% |
| chop | 1160 | 48% | -0.056% | 42% | -0.72 | -53.95% |

## Turnover, fees, activity

- trades: 12021 (4.96/day); active days 99%
- turnover 133.8x equity/year; fees 13.38% of equity/year ($104,445 total)
- average gross exposure 0.35; brake active 49.2% of hours
- correlation of daily returns with s3v2 baseline: 0.79
