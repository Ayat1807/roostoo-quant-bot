# Run: b4c_C_m_c4_w05_m100_h6

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 4, 'w': 0.5, 'swap_m': 1.0, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +152.48% | +14.97% | 0.58 | 0.80 | -63.83% | 0.23 | 0.56 |
| in_sample | 2020-02-15 → 2024-12-31 | +215.85% | +26.56% | 0.82 | 1.14 | -61.18% | 0.43 | 0.83 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -20.03% | -11.94% | -0.34 | -0.47 | -39.87% | -0.30 | -0.38 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +5.15% | +5.15% | 0.33 | 0.47 | -24.38% | 0.21 | 0.35 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.90% | 41% | -14.21% | -18.23% | -2.01 | 14 | 73% |
| out_of_sample | 628 | -1.68% | 37% | -11.53% | -12.95% | -3.76 | 14 | 76% |
| in_sample | 1768 | -0.66% | 42% | -14.21% | -18.23% | -1.35 | 14 | 72% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.594% | 56% | 3.73 | +161.99% |
| bull | 687 | 28% | +0.255% | 51% | 2.38 | +400.88% |
| bear | 400 | 17% | -0.143% | 42% | -2.14 | -45.51% |
| chop | 1160 | 48% | -0.082% | 36% | -1.21 | -64.69% |

## Turnover, fees, activity

- trades: 19313 (7.97/day); active days 96%
- turnover 255.7x equity/year; fees 25.57% of equity/year ($235,560 total)
- average gross exposure 0.29; brake active 50.6% of hours
- correlation of daily returns with s3v2 baseline: 0.48
