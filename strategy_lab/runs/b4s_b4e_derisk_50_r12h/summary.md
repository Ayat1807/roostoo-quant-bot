# Run: b4s_b4e_derisk_50_r12h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +227.32% | +19.55% | 0.67 | 0.93 | -74.79% | 0.26 | 0.65 |
| in_sample | 2020-02-15 → 2024-12-31 | +303.15% | +33.05% | 0.92 | 1.27 | -72.11% | 0.46 | 0.92 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -19.39% | -11.54% | -0.29 | -0.41 | -41.26% | -0.28 | -0.34 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -7.26% | -7.26% | -0.17 | -0.24 | -27.39% | -0.27 | -0.23 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.10% | 40% | -18.50% | -19.40% | -2.43 | 12 | 34% |
| out_of_sample | 628 | -1.80% | 38% | -11.82% | -14.32% | -4.13 | 12 | 24% |
| in_sample | 1768 | -0.89% | 41% | -18.50% | -19.40% | -1.96 | 13 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.665% | 52% | 4.02 | +195.06% |
| bull | 687 | 28% | +0.273% | 47% | 2.34 | +451.08% |
| bear | 400 | 17% | -0.258% | 30% | -3.65 | -65.65% |
| chop | 1160 | 48% | -0.037% | 36% | -0.51 | -41.39% |

## Turnover, fees, activity

- trades: 21774 (8.98/day); active days 83%
- turnover 215.0x equity/year; fees 21.50% of equity/year ($284,247 total)
- average gross exposure 0.30; brake active 47.1% of hours
- correlation of daily returns with s3v2 baseline: 0.37
