# Run: b8_s_U6

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'floor_breadth': 7, 'floor_gross': 0.5}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +169.91% | +16.13% | 0.83 | 1.18 | -23.98% | 0.67 | 0.92 |
| in_sample | 2020-02-15 → 2024-12-31 | +112.06% | +16.65% | 0.83 | 1.19 | -23.98% | 0.69 | 0.93 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +27.43% | +14.79% | 0.82 | 1.18 | -16.10% | 0.92 | 0.99 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +22.73% | +22.73% | 1.11 | 1.63 | -16.10% | 1.41 | 1.41 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.37% | 44% | -7.79% | -11.24% | -1.38 | 14 | 99% |
| out_of_sample | 628 | -0.34% | 45% | -5.98% | -6.49% | -1.39 | 14 | 100% |
| in_sample | 1768 | -0.36% | 44% | -7.79% | -11.24% | -1.26 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.413% | 52% | 3.67 | +98.67% |
| bull | 687 | 28% | +0.092% | 52% | 1.81 | +82.05% |
| bear | 400 | 17% | -0.008% | 44% | -0.17 | -4.44% |
| chop | 1160 | 48% | -0.014% | 45% | -0.28 | -19.66% |

## Turnover, fees, activity

- trades: 6771 (2.79/day); active days 100%
- turnover 60.4x equity/year; fees 6.04% of equity/year ($37,292 total)
- average gross exposure 0.25; brake active 24.4% of hours
- correlation of daily returns with s3v2 baseline: 0.83
