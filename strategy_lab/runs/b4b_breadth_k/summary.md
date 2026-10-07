# Run: b4b_breadth_k

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'select': 'breadth_k'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +118.91% | +12.52% | 0.50 | 0.68 | -75.37% | 0.17 | 0.47 |
| in_sample | 2020-02-15 → 2024-12-31 | +193.31% | +24.66% | 0.75 | 1.01 | -69.06% | 0.36 | 0.74 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -26.25% | -15.91% | -0.43 | -0.61 | -46.28% | -0.34 | -0.48 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -0.33% | -0.33% | 0.12 | 0.17 | -32.38% | -0.01 | 0.10 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.16% | 41% | -18.51% | -19.41% | -2.01 | 12 | 32% |
| out_of_sample | 628 | -2.29% | 36% | -12.21% | -14.03% | -4.31 | 12 | 21% |
| in_sample | 1768 | -0.78% | 43% | -18.51% | -19.41% | -1.18 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.549% | 49% | 3.10 | +137.18% |
| bull | 687 | 28% | +0.294% | 49% | 2.63 | +545.41% |
| bear | 400 | 17% | -0.240% | 32% | -3.17 | -63.29% |
| chop | 1160 | 48% | -0.070% | 35% | -0.91 | -61.04% |

## Turnover, fees, activity

- trades: 18290 (7.55/day); active days 82%
- turnover 196.5x equity/year; fees 19.65% of equity/year ($189,074 total)
- average gross exposure 0.33; brake active 46.4% of hours
- correlation of daily returns with s3v2 baseline: 0.35
