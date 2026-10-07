# Run: b4s_b4b_top7_g90_r6h

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'top_n': 7, 'gross': 0.9}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +110.41% | +11.86% | 0.48 | 0.66 | -81.22% | 0.15 | 0.45 |
| in_sample | 2020-02-15 → 2024-12-31 | +243.80% | +28.78% | 0.82 | 1.12 | -65.36% | 0.44 | 0.83 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -39.04% | -24.54% | -0.78 | -1.06 | -55.01% | -0.45 | -0.79 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -17.20% | -17.20% | -0.57 | -0.77 | -36.09% | -0.48 | -0.62 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.24% | 40% | -16.53% | -18.61% | -2.44 | 13 | 36% |
| out_of_sample | 628 | -2.78% | 32% | -14.13% | -16.81% | -5.90 | 12 | 31% |
| in_sample | 1768 | -0.74% | 43% | -16.53% | -18.61% | -1.50 | 13 | 38% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.741% | 53% | 4.33 | +234.61% |
| bull | 687 | 28% | +0.255% | 48% | 2.07 | +376.95% |
| bear | 400 | 17% | -0.247% | 38% | -3.33 | -64.31% |
| chop | 1160 | 48% | -0.075% | 38% | -0.98 | -63.06% |

## Turnover, fees, activity

- trades: 42076 (17.36/day); active days 84%
- turnover 272.0x equity/year; fees 27.20% of equity/year ($333,924 total)
- average gross exposure 0.31; brake active 49.1% of hours
- correlation of daily returns with s3v2 baseline: 0.38
