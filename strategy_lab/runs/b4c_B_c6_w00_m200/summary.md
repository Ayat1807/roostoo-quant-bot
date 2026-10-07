# Run: b4c_B_c6_w00_m200

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 6, 'w': 0.0, 'swap_m': 2.0, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +168.67% | +16.05% | 0.60 | 0.83 | -59.41% | 0.27 | 0.59 |
| in_sample | 2020-02-15 → 2024-12-31 | +327.57% | +34.66% | 0.98 | 1.36 | -58.01% | 0.60 | 1.02 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -37.14% | -23.21% | -0.87 | -1.21 | -47.69% | -0.49 | -0.89 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -4.40% | -4.40% | -0.07 | -0.10 | -25.25% | -0.17 | -0.11 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.85% | 42% | -14.72% | -18.12% | -1.77 | 14 | 76% |
| out_of_sample | 628 | -2.36% | 32% | -10.40% | -12.53% | -4.97 | 14 | 82% |
| in_sample | 1768 | -0.30% | 46% | -14.72% | -18.12% | -0.54 | 14 | 74% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.674% | 56% | 4.24 | +201.38% |
| bull | 687 | 28% | +0.218% | 49% | 2.10 | +291.68% |
| bear | 400 | 17% | -0.123% | 43% | -1.88 | -40.76% |
| chop | 1160 | 48% | -0.073% | 37% | -1.02 | -61.58% |

## Turnover, fees, activity

- trades: 17150 (7.08/day); active days 95%
- turnover 214.3x equity/year; fees 21.43% of equity/year ($235,636 total)
- average gross exposure 0.30; brake active 51.5% of hours
- correlation of daily returns with s3v2 baseline: 0.50
