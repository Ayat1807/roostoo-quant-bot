# Run: b4c_B_c6_w00_m150

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 6, 'w': 0.0, 'swap_m': 1.5, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +104.62% | +11.39% | 0.48 | 0.67 | -71.30% | 0.16 | 0.46 |
| in_sample | 2020-02-15 → 2024-12-31 | +263.61% | +30.27% | 0.89 | 1.23 | -60.55% | 0.50 | 0.91 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -43.70% | -27.88% | -1.10 | -1.53 | -50.49% | -0.55 | -1.11 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -4.62% | -4.62% | -0.07 | -0.10 | -25.84% | -0.18 | -0.12 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.95% | 42% | -14.75% | -18.08% | -2.09 | 14 | 76% |
| out_of_sample | 628 | -2.39% | 33% | -13.65% | -14.19% | -5.41 | 14 | 82% |
| in_sample | 1768 | -0.30% | 46% | -14.75% | -18.08% | -0.45 | 14 | 73% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.659% | 56% | 4.16 | +193.86% |
| bull | 687 | 28% | +0.209% | 49% | 1.98 | +266.15% |
| bear | 400 | 17% | -0.143% | 42% | -2.24 | -45.33% |
| chop | 1160 | 48% | -0.082% | 36% | -1.16 | -65.21% |

## Turnover, fees, activity

- trades: 17852 (7.36/day); active days 95%
- turnover 224.5x equity/year; fees 22.45% of equity/year ($235,258 total)
- average gross exposure 0.30; brake active 50.6% of hours
- correlation of daily returns with s3v2 baseline: 0.51
