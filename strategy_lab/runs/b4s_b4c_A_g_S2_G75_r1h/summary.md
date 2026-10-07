# Run: b4s_b4c_A_g_S2_G75_r1h

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d'}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -94.38% | -35.18% | -0.98 | -1.36 | -98.75% | -0.36 | -0.94 |
| in_sample | 2020-02-15 → 2024-12-31 | -67.32% | -20.47% | -0.38 | -0.52 | -91.93% | -0.22 | -0.39 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -82.76% | -63.22% | -3.34 | -4.56 | -85.40% | -0.74 | -3.05 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -56.70% | -56.70% | -3.01 | -4.15 | -61.90% | -0.92 | -2.84 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -3.22% | 31% | -17.18% | -22.19% | -4.57 | 14 | 85% |
| out_of_sample | 628 | -5.02% | 21% | -14.56% | -15.25% | -7.63 | 14 | 82% |
| in_sample | 1768 | -2.45% | 34% | -17.18% | -22.19% | -3.44 | 14 | 86% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.841% | 55% | 4.63 | +294.30% |
| bull | 687 | 28% | +0.115% | 43% | 0.99 | +86.67% |
| bear | 400 | 17% | -0.387% | 32% | -5.72 | -79.52% |
| chop | 1160 | 48% | -0.273% | 32% | -3.73 | -96.27% |

## Turnover, fees, activity

- trades: 182200 (75.17/day); active days 97%
- turnover 777.4x equity/year; fees 77.74% of equity/year ($230,458 total)
- average gross exposure 0.35; brake active 54.0% of hours
- correlation of daily returns with s3v2 baseline: 0.49
