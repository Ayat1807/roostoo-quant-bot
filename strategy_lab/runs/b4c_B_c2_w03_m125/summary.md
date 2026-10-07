# Run: b4c_B_c2_w03_m125

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 2, 'w': 0.3, 'swap_m': 1.25, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +80.89% | +9.34% | 0.44 | 0.61 | -53.40% | 0.17 | 0.43 |
| in_sample | 2020-02-15 → 2024-12-31 | +133.42% | +18.96% | 0.68 | 0.94 | -48.74% | 0.39 | 0.70 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -22.41% | -13.44% | -0.47 | -0.67 | -39.62% | -0.34 | -0.51 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +3.90% | +3.90% | 0.28 | 0.40 | -30.94% | 0.13 | 0.28 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.85% | 41% | -15.23% | -19.08% | -1.88 | 14 | 64% |
| out_of_sample | 628 | -1.76% | 37% | -11.16% | -11.22% | -4.53 | 14 | 72% |
| in_sample | 1768 | -0.60% | 43% | -15.23% | -19.08% | -1.32 | 14 | 62% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.638% | 53% | 4.38 | +186.82% |
| bull | 687 | 28% | +0.180% | 47% | 1.85 | +206.17% |
| bear | 400 | 17% | -0.066% | 42% | -0.96 | -25.78% |
| chop | 1160 | 48% | -0.104% | 36% | -1.70 | -72.25% |

## Turnover, fees, activity

- trades: 17370 (7.17/day); active days 94%
- turnover 225.9x equity/year; fees 22.59% of equity/year ($149,821 total)
- average gross exposure 0.26; brake active 54.3% of hours
- correlation of daily returns with s3v2 baseline: 0.50
