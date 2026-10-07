# Run: b4c_A_g_S2_G75

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d'}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +64.41% | +7.78% | 0.39 | 0.54 | -81.49% | 0.10 | 0.36 |
| in_sample | 2020-02-15 → 2024-12-31 | +244.93% | +28.87% | 0.85 | 1.17 | -64.42% | 0.45 | 0.86 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -52.37% | -34.43% | -1.35 | -1.88 | -58.62% | -0.59 | -1.33 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -23.60% | -23.60% | -0.92 | -1.29 | -38.71% | -0.61 | -0.98 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.52% | 39% | -19.94% | -22.83% | -2.79 | 14 | 76% |
| out_of_sample | 628 | -2.72% | 30% | -11.84% | -14.96% | -5.40 | 14 | 68% |
| in_sample | 1768 | -0.97% | 42% | -19.94% | -22.83% | -1.75 | 14 | 79% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.648% | 55% | 3.80 | +184.98% |
| bull | 687 | 28% | +0.257% | 48% | 2.25 | +396.14% |
| bear | 400 | 17% | -0.153% | 43% | -2.40 | -47.49% |
| chop | 1160 | 48% | -0.121% | 37% | -1.68 | -77.86% |

## Turnover, fees, activity

- trades: 18534 (7.65/day); active days 95%
- turnover 224.9x equity/year; fees 22.49% of equity/year ($257,664 total)
- average gross exposure 0.35; brake active 52.9% of hours
- correlation of daily returns with s3v2 baseline: 0.51
