# Run: b5_slowshort_15

Strategy `slow_short`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'wa': 0.15}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -35.93% | -6.49% | -0.18 | -0.26 | -45.93% | -0.14 | -0.20 |
| in_sample | 2020-02-15 → 2024-12-31 | -18.28% | -4.05% | -0.07 | -0.11 | -32.77% | -0.12 | -0.10 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -20.77% | -12.40% | -0.43 | -0.59 | -33.67% | -0.37 | -0.48 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +0.99% | +0.99% | 0.16 | 0.23 | -19.34% | 0.05 | 0.15 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | +0.00% | 28% | -15.28% | -17.71% | 0.00 | 5 | 12% |
| out_of_sample | 628 | -0.23% | 32% | -11.27% | -12.80% | -3.42 | 7 | 13% |
| in_sample | 1768 | +0.00% | 27% | -15.28% | -17.71% | 0.00 | 3 | 12% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.045% | 26% | 0.36 | +3.15% |
| bull | 687 | 28% | -0.005% | 14% | -0.83 | -3.51% |
| bear | 400 | 17% | +0.188% | 50% | 2.03 | +99.40% |
| chop | 1160 | 48% | -0.093% | 31% | -1.85 | -67.72% |

## Turnover, fees, activity

- trades: 3453 (1.42/day); active days 41%
- turnover 38.3x equity/year; fees 3.83% of equity/year ($10,794 total)
- average gross exposure 0.12; brake active 20.8% of hours
- correlation of daily returns with s3v2 baseline: 0.41
