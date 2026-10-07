# Run: b4c_B_c4_w05_m200

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 4, 'w': 0.5, 'swap_m': 2.0, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +221.36% | +19.22% | 0.68 | 0.95 | -47.26% | 0.41 | 0.71 |
| in_sample | 2020-02-15 → 2024-12-31 | +275.86% | +31.15% | 0.92 | 1.28 | -46.07% | 0.68 | 0.99 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -14.46% | -8.50% | -0.20 | -0.28 | -35.13% | -0.24 | -0.24 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -0.98% | -0.98% | 0.09 | 0.12 | -27.23% | -0.04 | 0.06 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.73% | 42% | -14.35% | -18.32% | -1.52 | 14 | 72% |
| out_of_sample | 628 | -1.60% | 36% | -11.54% | -13.76% | -3.95 | 14 | 80% |
| in_sample | 1768 | -0.40% | 45% | -14.35% | -18.32% | -0.75 | 14 | 69% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.569% | 57% | 3.72 | +152.19% |
| bull | 687 | 28% | +0.241% | 50% | 2.28 | +354.78% |
| bear | 400 | 17% | -0.099% | 42% | -1.49 | -34.94% |
| chop | 1160 | 48% | -0.064% | 37% | -0.95 | -56.93% |

## Turnover, fees, activity

- trades: 17864 (7.37/day); active days 96%
- turnover 226.9x equity/year; fees 22.69% of equity/year ($242,507 total)
- average gross exposure 0.29; brake active 51.3% of hours
- correlation of daily returns with s3v2 baseline: 0.49
