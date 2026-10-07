# Run: b4s_b4d_not_ext10_r6h

Strategy `xsmom_entry`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'entry_filter': 'not_extended', 'ext': 0.1}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +167.10% | +15.95% | 0.65 | 0.89 | -63.28% | 0.25 | 0.63 |
| in_sample | 2020-02-15 → 2024-12-31 | +222.15% | +27.08% | 0.92 | 1.26 | -54.61% | 0.50 | 0.93 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -17.09% | -10.11% | -0.33 | -0.47 | -38.64% | -0.26 | -0.37 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -3.31% | -3.31% | -0.05 | -0.07 | -26.39% | -0.13 | -0.08 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.19% | 40% | -10.77% | -12.41% | -2.94 | 12 | 25% |
| out_of_sample | 628 | -2.00% | 35% | -9.70% | -10.22% | -5.21 | 12 | 25% |
| in_sample | 1768 | -0.90% | 42% | -10.77% | -12.41% | -2.33 | 12 | 26% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.467% | 43% | 3.75 | +116.43% |
| bull | 687 | 28% | +0.247% | 50% | 2.52 | +384.68% |
| bear | 400 | 17% | -0.198% | 28% | -3.76 | -55.58% |
| chop | 1160 | 48% | -0.040% | 32% | -0.59 | -42.67% |

## Turnover, fees, activity

- trades: 29618 (12.22/day); active days 79%
- turnover 224.5x equity/year; fees 22.45% of equity/year ($241,436 total)
- average gross exposure 0.27; brake active 49.1% of hours
- correlation of daily returns with s3v2 baseline: 0.39
