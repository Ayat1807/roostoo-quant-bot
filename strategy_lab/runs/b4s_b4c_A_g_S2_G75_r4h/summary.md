# Run: b4s_b4c_A_g_S2_G75_r4h

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d'}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +13.79% | +1.97% | 0.24 | 0.33 | -82.47% | 0.02 | 0.21 |
| in_sample | 2020-02-15 → 2024-12-31 | +166.83% | +22.27% | 0.70 | 0.97 | -71.99% | 0.31 | 0.69 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -57.28% | -38.36% | -1.51 | -2.09 | -66.73% | -0.57 | -1.46 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -31.54% | -31.54% | -1.30 | -1.83 | -43.75% | -0.72 | -1.34 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.48% | 39% | -18.76% | -19.89% | -2.61 | 14 | 83% |
| out_of_sample | 628 | -3.05% | 30% | -12.98% | -13.87% | -5.92 | 14 | 80% |
| in_sample | 1768 | -0.78% | 43% | -18.76% | -19.89% | -1.44 | 14 | 84% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.815% | 56% | 4.62 | +278.50% |
| bull | 687 | 28% | +0.247% | 47% | 2.07 | +357.95% |
| bear | 400 | 17% | -0.266% | 39% | -3.74 | -66.75% |
| chop | 1160 | 48% | -0.130% | 37% | -1.77 | -80.26% |

## Turnover, fees, activity

- trades: 59921 (24.72/day); active days 96%
- turnover 426.1x equity/year; fees 42.61% of equity/year ($327,626 total)
- average gross exposure 0.36; brake active 49.5% of hours
- correlation of daily returns with s3v2 baseline: 0.50
