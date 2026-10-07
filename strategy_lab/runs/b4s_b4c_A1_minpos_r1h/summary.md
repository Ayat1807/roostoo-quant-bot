# Run: b4s_b4c_A1_minpos_r1h

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -94.68% | -35.72% | -1.00 | -1.38 | -98.78% | -0.36 | -0.96 |
| in_sample | 2020-02-15 → 2024-12-31 | -68.48% | -21.06% | -0.40 | -0.55 | -91.96% | -0.23 | -0.41 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -83.09% | -63.62% | -3.36 | -4.58 | -85.66% | -0.74 | -3.06 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -56.69% | -56.69% | -3.00 | -4.14 | -61.93% | -0.92 | -2.83 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -3.24% | 30% | -17.18% | -22.10% | -4.55 | 14 | 93% |
| out_of_sample | 628 | -5.04% | 21% | -14.54% | -15.21% | -7.65 | 14 | 100% |
| in_sample | 1768 | -2.47% | 34% | -17.18% | -22.10% | -3.49 | 14 | 90% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.838% | 55% | 4.61 | +292.10% |
| bull | 687 | 28% | +0.116% | 43% | 1.00 | +87.81% |
| bear | 400 | 17% | -0.390% | 32% | -5.67 | -79.79% |
| chop | 1160 | 48% | -0.277% | 32% | -3.78 | -96.43% |

## Turnover, fees, activity

- trades: 183869 (75.85/day); active days 98%
- turnover 779.6x equity/year; fees 77.96% of equity/year ($224,316 total)
- average gross exposure 0.35; brake active 54.1% of hours
- correlation of daily returns with s3v2 baseline: 0.49
