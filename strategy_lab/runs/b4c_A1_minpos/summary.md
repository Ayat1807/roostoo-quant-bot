# Run: b4c_A1_minpos

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +85.55% | +9.76% | 0.44 | 0.61 | -78.70% | 0.12 | 0.41 |
| in_sample | 2020-02-15 → 2024-12-31 | +260.89% | +30.07% | 0.87 | 1.20 | -64.89% | 0.46 | 0.88 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -48.59% | -31.51% | -1.20 | -1.67 | -54.37% | -0.58 | -1.20 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -17.94% | -17.94% | -0.64 | -0.91 | -36.59% | -0.49 | -0.70 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.41% | 39% | -19.94% | -22.83% | -2.72 | 14 | 89% |
| out_of_sample | 628 | -2.54% | 31% | -11.72% | -14.85% | -5.23 | 14 | 95% |
| in_sample | 1768 | -0.85% | 43% | -19.94% | -22.83% | -1.54 | 14 | 87% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.635% | 53% | 3.71 | +178.53% |
| bull | 687 | 28% | +0.255% | 50% | 2.24 | +390.84% |
| bear | 400 | 17% | -0.141% | 44% | -2.19 | -44.77% |
| chop | 1160 | 48% | -0.112% | 38% | -1.56 | -75.43% |

## Turnover, fees, activity

- trades: 18422 (7.60/day); active days 97%
- turnover 223.4x equity/year; fees 22.34% of equity/year ($259,756 total)
- average gross exposure 0.36; brake active 52.2% of hours
- correlation of daily returns with s3v2 baseline: 0.51
