# Run: b3s_xsmom_r1_r12h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +168.65% | +16.05% | 0.59 | 0.81 | -80.63% | 0.20 | 0.56 |
| in_sample | 2020-02-15 → 2024-12-31 | +266.63% | +30.49% | 0.87 | 1.20 | -71.77% | 0.42 | 0.87 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -27.24% | -16.55% | -0.50 | -0.70 | -46.93% | -0.35 | -0.54 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -8.09% | -8.09% | -0.20 | -0.28 | -28.02% | -0.29 | -0.26 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.22% | 40% | -18.50% | -19.40% | -2.54 | 13 | 33% |
| out_of_sample | 628 | -2.10% | 36% | -11.82% | -14.29% | -4.56 | 12 | 23% |
| in_sample | 1768 | -0.92% | 41% | -18.50% | -19.40% | -2.01 | 13 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.673% | 45% | 3.97 | +197.87% |
| bull | 687 | 28% | +0.246% | 46% | 2.09 | +356.12% |
| bear | 400 | 17% | -0.262% | 28% | -3.69 | -66.24% |
| chop | 1160 | 48% | -0.037% | 34% | -0.50 | -41.43% |

## Turnover, fees, activity

- trades: 21596 (8.91/day); active days 83%
- turnover 218.2x equity/year; fees 21.82% of equity/year ($289,267 total)
- average gross exposure 0.30; brake active 48.4% of hours
- correlation of daily returns with s3v2 baseline: 0.34
