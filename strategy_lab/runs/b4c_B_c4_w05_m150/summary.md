# Run: b4c_B_c4_w05_m150

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 4, 'w': 0.5, 'swap_m': 1.5, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +244.66% | +20.48% | 0.71 | 0.99 | -47.67% | 0.43 | 0.74 |
| in_sample | 2020-02-15 → 2024-12-31 | +325.77% | +34.55% | 0.98 | 1.37 | -44.90% | 0.77 | 1.07 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -19.01% | -11.31% | -0.31 | -0.44 | -35.46% | -0.32 | -0.37 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -4.76% | -4.76% | -0.07 | -0.11 | -26.40% | -0.18 | -0.12 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.77% | 42% | -14.85% | -18.32% | -1.68 | 14 | 73% |
| out_of_sample | 628 | -1.74% | 37% | -11.61% | -13.00% | -4.27 | 14 | 76% |
| in_sample | 1768 | -0.44% | 45% | -14.85% | -18.32% | -0.82 | 14 | 73% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.692% | 56% | 4.29 | +210.49% |
| bull | 687 | 28% | +0.243% | 50% | 2.27 | +359.74% |
| bear | 400 | 17% | -0.132% | 39% | -1.93 | -43.06% |
| chop | 1160 | 48% | -0.066% | 37% | -0.98 | -57.59% |

## Turnover, fees, activity

- trades: 18412 (7.60/day); active days 96%
- turnover 235.9x equity/year; fees 23.59% of equity/year ($266,208 total)
- average gross exposure 0.29; brake active 51.5% of hours
- correlation of daily returns with s3v2 baseline: 0.50
