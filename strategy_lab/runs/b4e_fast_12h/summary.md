# Run: b4e_fast_12h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +302.70% | +23.34% | 0.76 | 1.05 | -67.09% | 0.35 | 0.75 |
| in_sample | 2020-02-15 → 2024-12-31 | +498.81% | +44.28% | 1.13 | 1.56 | -64.57% | 0.69 | 1.17 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -32.99% | -20.37% | -0.67 | -0.93 | -42.84% | -0.48 | -0.72 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -10.27% | -10.27% | -0.31 | -0.44 | -27.73% | -0.37 | -0.38 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.18% | 40% | -18.30% | -20.40% | -2.40 | 12 | 31% |
| out_of_sample | 628 | -2.24% | 32% | -11.76% | -13.38% | -4.88 | 12 | 22% |
| in_sample | 1768 | -0.78% | 43% | -18.30% | -20.40% | -1.56 | 12 | 35% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.697% | 47% | 4.19 | +211.74% |
| bull | 687 | 28% | +0.258% | 50% | 2.26 | +401.29% |
| bear | 400 | 17% | -0.243% | 30% | -3.59 | -63.46% |
| chop | 1160 | 48% | -0.021% | 35% | -0.28 | -29.47% |

## Turnover, fees, activity

- trades: 15965 (6.59/day); active days 82%
- turnover 180.6x equity/year; fees 18.06% of equity/year ($305,059 total)
- average gross exposure 0.30; brake active 46.7% of hours
- correlation of daily returns with s3v2 baseline: 0.38
