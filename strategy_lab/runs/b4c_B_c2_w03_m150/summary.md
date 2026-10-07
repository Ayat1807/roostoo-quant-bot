# Run: b4c_B_c2_w03_m150

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 2, 'w': 0.3, 'swap_m': 1.5, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +126.13% | +13.08% | 0.54 | 0.76 | -52.34% | 0.25 | 0.54 |
| in_sample | 2020-02-15 → 2024-12-31 | +150.21% | +20.67% | 0.72 | 1.00 | -52.34% | 0.39 | 0.73 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -9.51% | -5.53% | -0.10 | -0.15 | -31.24% | -0.18 | -0.14 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +5.22% | +5.22% | 0.33 | 0.48 | -28.01% | 0.19 | 0.35 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.81% | 41% | -14.85% | -18.72% | -1.91 | 14 | 66% |
| out_of_sample | 628 | -1.41% | 38% | -11.13% | -11.19% | -3.64 | 14 | 67% |
| in_sample | 1768 | -0.60% | 42% | -14.85% | -18.72% | -1.35 | 14 | 65% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.665% | 53% | 4.72 | +202.11% |
| bull | 687 | 28% | +0.186% | 48% | 1.87 | +216.86% |
| bear | 400 | 17% | -0.069% | 43% | -1.08 | -26.39% |
| chop | 1160 | 48% | -0.091% | 37% | -1.44 | -67.91% |

## Turnover, fees, activity

- trades: 16917 (6.98/day); active days 95%
- turnover 220.6x equity/year; fees 22.06% of equity/year ($170,079 total)
- average gross exposure 0.26; brake active 53.1% of hours
- correlation of daily returns with s3v2 baseline: 0.49
