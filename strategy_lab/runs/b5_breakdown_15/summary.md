# Run: b5_breakdown_15

Strategy `breakdown_short`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'wa': 0.15}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -3.75% | -0.57% | -0.05 | -0.07 | -15.75% | -0.04 | -0.05 |
| in_sample | 2020-02-15 → 2024-12-31 | +0.27% | +0.05% | 0.04 | 0.06 | -9.80% | 0.01 | 0.04 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -4.01% | -2.30% | -0.36 | -0.50 | -8.94% | -0.26 | -0.39 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +5.23% | +5.23% | 0.74 | 1.09 | -5.41% | 0.97 | 0.95 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | +0.00% | 5% | -4.70% | -7.19% | 0.00 | 0 | 0% |
| out_of_sample | 628 | +0.00% | 5% | -4.56% | -4.56% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 5% | -4.70% | -7.19% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.053% | 8% | 1.26 | +9.10% |
| bull | 687 | 28% | -0.001% | 0% | -0.98 | -0.74% |
| bear | 400 | 17% | -0.011% | 9% | -0.41 | -4.78% |
| chop | 1160 | 48% | -0.006% | 1% | -0.82 | -6.66% |

## Turnover, fees, activity

- trades: 82 (0.03/day); active days 2%
- turnover 1.9x equity/year; fees 0.19% of equity/year ($607 total)
- average gross exposure 0.01; brake active 1.4% of hours
- correlation of daily returns with s3v2 baseline: 0.31
