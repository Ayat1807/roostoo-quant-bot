# Run: b5_breakdown_10

Strategy `breakdown_short`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'wa': 0.1}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -3.36% | -0.51% | -0.08 | -0.11 | -11.74% | -0.04 | -0.08 |
| in_sample | 2020-02-15 → 2024-12-31 | -0.75% | -0.15% | -0.00 | -0.01 | -7.68% | -0.02 | -0.01 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -2.62% | -1.50% | -0.35 | -0.49 | -6.03% | -0.25 | -0.38 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +3.50% | +3.50% | 0.72 | 1.07 | -3.72% | 0.94 | 0.93 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | +0.00% | 5% | -3.15% | -6.71% | 0.00 | 0 | 0% |
| out_of_sample | 628 | +0.00% | 5% | -3.15% | -3.15% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 5% | -3.15% | -6.71% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.035% | 8% | 1.25 | +6.08% |
| bull | 687 | 28% | -0.001% | 0% | -0.98 | -0.50% |
| bear | 400 | 17% | -0.010% | 10% | -0.49 | -4.16% |
| chop | 1160 | 48% | -0.004% | 1% | -0.82 | -4.47% |

## Turnover, fees, activity

- trades: 82 (0.03/day); active days 2%
- turnover 1.2x equity/year; fees 0.12% of equity/year ($404 total)
- average gross exposure 0.01; brake active 0.9% of hours
- correlation of daily returns with s3v2 baseline: 0.29
