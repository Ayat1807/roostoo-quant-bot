# Run: b3s_s3v2e_tv08_w04_core10_r2h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.4, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +139.36% | +14.05% | 0.58 | 0.85 | -44.69% | 0.31 | 0.61 |
| in_sample | 2020-02-15 → 2024-12-31 | +152.39% | +20.88% | 0.77 | 1.12 | -44.69% | 0.47 | 0.82 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -5.10% | -2.93% | 0.06 | 0.09 | -39.55% | -0.07 | 0.03 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -7.77% | -7.77% | -0.10 | -0.15 | -39.55% | -0.20 | -0.15 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.06% | 41% | -14.41% | -17.53% | -2.53 | 14 | 90% |
| out_of_sample | 628 | -1.35% | 42% | -11.72% | -12.48% | -2.84 | 14 | 81% |
| in_sample | 1768 | -1.00% | 41% | -14.41% | -17.53% | -2.44 | 14 | 94% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.670% | 53% | 4.27 | +200.35% |
| bull | 687 | 28% | +0.133% | 44% | 1.74 | +132.18% |
| bear | 400 | 17% | -0.023% | 36% | -0.28 | -12.89% |
| chop | 1160 | 48% | -0.063% | 36% | -0.76 | -58.20% |

## Turnover, fees, activity

- trades: 19371 (7.99/day); active days 99%
- turnover 210.4x equity/year; fees 21.04% of equity/year ($164,442 total)
- average gross exposure 0.32; brake active 57.2% of hours
- correlation of daily returns with s3v2 baseline: 0.76
