# Run: b6d_meta_edge

Strategy `s3v2x_meta`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'size_map': 'edge'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +24.03% | +3.30% | 0.53 | 0.79 | -12.47% | 0.26 | 0.55 |
| in_sample | 2020-02-15 → 2024-12-31 | +23.71% | +4.45% | 0.61 | 0.91 | -12.47% | 0.36 | 0.65 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +0.26% | +0.15% | 0.27 | 0.36 | -0.93% | 0.16 | 0.27 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -0.00% | -0.00% | -0.05 | -0.07 | -0.07% | -0.05 | -0.06 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | +0.00% | 42% | -5.29% | -6.87% | 0.00 | 9 | 29% |
| out_of_sample | 628 | +0.00% | 41% | -0.17% | -0.93% | 0.00 | 4 | 7% |
| in_sample | 1768 | +0.00% | 42% | -5.29% | -6.87% | 0.00 | 12 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.062% | 34% | 2.24 | +11.18% |
| bull | 687 | 28% | +0.007% | 33% | 0.57 | +5.04% |
| bear | 400 | 17% | -0.002% | 27% | -1.12 | -0.61% |
| chop | 1160 | 48% | +0.009% | 25% | 0.34 | +9.93% |

## Turnover, fees, activity

- trades: 1854 (0.76/day); active days 58%
- turnover 5.5x equity/year; fees 0.55% of equity/year ($2,248 total)
- average gross exposure 0.02; brake active 1.8% of hours
- correlation of daily returns with s3v2 baseline: 0.39
