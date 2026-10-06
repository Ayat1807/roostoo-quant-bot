# Run: b3s_xsmom_r1_r1h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -66.94% | -15.36% | -0.28 | -0.38 | -94.08% | -0.16 | -0.29 |
| in_sample | 2020-02-15 → 2024-12-31 | -5.21% | -1.09% | 0.17 | 0.23 | -82.27% | -0.01 | 0.14 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -65.21% | -45.16% | -2.02 | -2.77 | -72.26% | -0.62 | -1.90 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -37.49% | -37.49% | -1.67 | -2.34 | -47.92% | -0.78 | -1.67 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -2.33% | 33% | -21.10% | -22.29% | -4.17 | 13 | 38% |
| out_of_sample | 628 | -3.30% | 23% | -13.01% | -13.78% | -6.11 | 13 | 33% |
| in_sample | 1768 | -1.85% | 37% | -21.10% | -22.29% | -3.21 | 13 | 40% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.793% | 49% | 4.62 | +266.26% |
| bull | 687 | 28% | +0.123% | 42% | 1.07 | +97.74% |
| bear | 400 | 17% | -0.286% | 28% | -4.41 | -69.12% |
| chop | 1160 | 48% | -0.155% | 31% | -2.18 | -85.22% |

## Turnover, fees, activity

- trades: 151702 (62.58/day); active days 86%
- turnover 544.3x equity/year; fees 54.43% of equity/year ($251,737 total)
- average gross exposure 0.29; brake active 54.0% of hours
- correlation of daily returns with s3v2 baseline: 0.34
