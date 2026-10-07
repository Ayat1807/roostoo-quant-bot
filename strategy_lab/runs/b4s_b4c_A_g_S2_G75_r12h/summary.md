# Run: b4s_b4c_A_g_S2_G75_r12h

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d'}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +104.55% | +11.38% | 0.48 | 0.66 | -82.07% | 0.14 | 0.45 |
| in_sample | 2020-02-15 → 2024-12-31 | +241.33% | +28.59% | 0.83 | 1.15 | -66.48% | 0.43 | 0.84 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -40.12% | -25.30% | -0.86 | -1.21 | -52.19% | -0.48 | -0.89 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -15.17% | -15.17% | -0.50 | -0.70 | -32.68% | -0.46 | -0.57 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.07% | 41% | -18.50% | -19.01% | -2.10 | 14 | 78% |
| out_of_sample | 628 | -1.96% | 32% | -14.55% | -15.31% | -3.91 | 14 | 71% |
| in_sample | 1768 | -0.57% | 44% | -18.50% | -19.01% | -1.03 | 14 | 81% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.781% | 56% | 4.46 | +257.79% |
| bull | 687 | 28% | +0.214% | 47% | 1.85 | +267.68% |
| bear | 400 | 17% | -0.186% | 43% | -2.48 | -54.37% |
| chop | 1160 | 48% | -0.083% | 39% | -1.14 | -65.92% |

## Turnover, fees, activity

- trades: 26973 (11.13/day); active days 96%
- turnover 279.4x equity/year; fees 27.94% of equity/year ($346,590 total)
- average gross exposure 0.36; brake active 49.5% of hours
- correlation of daily returns with s3v2 baseline: 0.50
