# Run: b4c_B_c2_w00_m125

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 2, 'w': 0.0, 'swap_m': 1.25, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +71.90% | +8.50% | 0.41 | 0.57 | -48.29% | 0.18 | 0.41 |
| in_sample | 2020-02-15 → 2024-12-31 | +122.21% | +17.77% | 0.64 | 0.89 | -41.64% | 0.43 | 0.68 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -22.54% | -13.52% | -0.46 | -0.65 | -35.76% | -0.38 | -0.51 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +4.56% | +4.56% | 0.31 | 0.44 | -26.00% | 0.18 | 0.32 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.81% | 41% | -13.67% | -15.85% | -1.77 | 14 | 64% |
| out_of_sample | 628 | -1.83% | 34% | -11.38% | -11.53% | -4.64 | 14 | 63% |
| in_sample | 1768 | -0.46% | 44% | -13.67% | -15.85% | -1.03 | 14 | 64% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.560% | 53% | 3.60 | +147.87% |
| bull | 687 | 28% | +0.189% | 47% | 1.89 | +223.17% |
| bear | 400 | 17% | -0.065% | 44% | -0.99 | -25.43% |
| chop | 1160 | 48% | -0.101% | 38% | -1.65 | -71.22% |

## Turnover, fees, activity

- trades: 16595 (6.85/day); active days 94%
- turnover 216.2x equity/year; fees 21.62% of equity/year ($129,020 total)
- average gross exposure 0.26; brake active 51.3% of hours
- correlation of daily returns with s3v2 baseline: 0.50
