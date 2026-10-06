# Run: b3_s3v2e_tv06_core10

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.6, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +153.65% | +15.05% | 0.69 | 0.99 | -31.93% | 0.47 | 0.75 |
| in_sample | 2020-02-15 → 2024-12-31 | +116.03% | +17.09% | 0.77 | 1.11 | -31.93% | 0.54 | 0.83 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +17.61% | +9.66% | 0.48 | 0.70 | -21.62% | 0.45 | 0.56 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +12.78% | +12.78% | 0.58 | 0.85 | -21.62% | 0.59 | 0.69 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.50% | 43% | -12.99% | -16.02% | -1.99 | 14 | 94% |
| out_of_sample | 628 | -0.88% | 40% | -12.99% | -16.02% | -2.53 | 14 | 86% |
| in_sample | 1768 | -0.39% | 44% | -8.95% | -11.61% | -1.47 | 14 | 96% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.372% | 53% | 3.19 | +84.16% |
| bull | 687 | 28% | +0.131% | 55% | 2.20 | +134.58% |
| bear | 400 | 17% | +0.045% | 46% | 0.70 | +16.38% |
| chop | 1160 | 48% | -0.047% | 43% | -0.74 | -46.83% |

## Turnover, fees, activity

- trades: 7853 (3.24/day); active days 99%
- turnover 79.2x equity/year; fees 7.92% of equity/year ($51,326 total)
- average gross exposure 0.29; brake active 35.3% of hours
- correlation of daily returns with s3v2 baseline: 0.84
