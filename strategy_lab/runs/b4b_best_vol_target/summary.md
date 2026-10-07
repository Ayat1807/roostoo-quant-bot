# Run: b4b_best_vol_target

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'score', 'exposure': 'vol_target'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +614.77% | +34.47% | 1.09 | 1.56 | -53.50% | 0.64 | 1.15 |
| in_sample | 2020-02-15 → 2024-12-31 | +609.73% | +49.39% | 1.40 | 1.98 | -53.50% | 0.92 | 1.49 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +0.16% | +0.09% | 0.15 | 0.22 | -36.17% | 0.00 | 0.13 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +31.51% | +31.51% | 1.07 | 1.62 | -27.82% | 1.13 | 1.31 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.46% | 46% | -12.74% | -12.75% | -0.86 | 12 | 32% |
| out_of_sample | 628 | -1.68% | 39% | -11.37% | -12.52% | -3.87 | 12 | 21% |
| in_sample | 1768 | +0.00% | 48% | -12.74% | -12.75% | 0.00 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.527% | 51% | 4.15 | +139.86% |
| bull | 687 | 28% | +0.321% | 51% | 3.32 | +704.52% |
| bear | 400 | 17% | -0.210% | 35% | -3.29 | -58.08% |
| chop | 1160 | 48% | +0.002% | 37% | 0.02 | -11.65% |

## Turnover, fees, activity

- trades: 13688 (5.65/day); active days 82%
- turnover 160.0x equity/year; fees 16.00% of equity/year ($257,052 total)
- average gross exposure 0.30; brake active 49.8% of hours
- correlation of daily returns with s3v2 baseline: 0.35
