# Run: b4s_b4c_A1_minpos_r4h

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +23.10% | +3.18% | 0.27 | 0.38 | -83.10% | 0.04 | 0.24 |
| in_sample | 2020-02-15 → 2024-12-31 | +209.16% | +26.01% | 0.77 | 1.08 | -70.74% | 0.37 | 0.77 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -60.11% | -40.72% | -1.67 | -2.30 | -68.21% | -0.60 | -1.60 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -31.81% | -31.81% | -1.33 | -1.87 | -43.30% | -0.73 | -1.37 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.50% | 39% | -18.84% | -19.96% | -2.71 | 14 | 92% |
| out_of_sample | 628 | -3.16% | 28% | -13.39% | -13.88% | -6.03 | 14 | 96% |
| in_sample | 1768 | -0.72% | 43% | -18.84% | -19.96% | -1.33 | 14 | 91% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.844% | 57% | 4.75 | +297.75% |
| bull | 687 | 28% | +0.264% | 48% | 2.20 | +413.77% |
| bear | 400 | 17% | -0.261% | 39% | -3.69 | -66.05% |
| chop | 1160 | 48% | -0.139% | 37% | -1.91 | -82.26% |

## Turnover, fees, activity

- trades: 60988 (25.16/day); active days 98%
- turnover 429.8x equity/year; fees 42.98% of equity/year ($376,562 total)
- average gross exposure 0.37; brake active 49.6% of hours
- correlation of daily returns with s3v2 baseline: 0.50
