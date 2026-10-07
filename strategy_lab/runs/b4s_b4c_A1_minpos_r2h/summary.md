# Run: b4s_b4c_A1_minpos_r2h

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -74.99% | -18.84% | -0.37 | -0.52 | -96.08% | -0.20 | -0.38 |
| in_sample | 2020-02-15 → 2024-12-31 | -23.38% | -5.31% | 0.06 | 0.09 | -86.73% | -0.06 | 0.03 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -67.32% | -47.07% | -2.05 | -2.84 | -73.90% | -0.64 | -1.94 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -46.40% | -46.40% | -2.25 | -3.09 | -55.46% | -0.84 | -2.16 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -2.46% | 34% | -18.48% | -21.48% | -3.97 | 14 | 92% |
| out_of_sample | 628 | -3.62% | 26% | -15.01% | -15.45% | -6.06 | 14 | 96% |
| in_sample | 1768 | -1.88% | 38% | -18.48% | -21.48% | -2.95 | 14 | 90% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.916% | 59% | 5.10 | +350.67% |
| bull | 687 | 28% | +0.194% | 44% | 1.66 | +219.45% |
| bear | 400 | 17% | -0.354% | 33% | -4.94 | -76.67% |
| chop | 1160 | 48% | -0.214% | 34% | -2.90 | -92.55% |

## Turnover, fees, activity

- trades: 106773 (44.05/day); active days 98%
- turnover 573.0x equity/year; fees 57.30% of equity/year ($256,740 total)
- average gross exposure 0.36; brake active 52.6% of hours
- correlation of daily returns with s3v2 baseline: 0.50
