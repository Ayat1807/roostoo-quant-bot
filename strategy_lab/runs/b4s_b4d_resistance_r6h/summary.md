# Run: b4s_b4d_resistance_r6h

Strategy `xsmom_entry`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'entry_filter': 'resistance'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +204.38% | +18.25% | 0.64 | 0.88 | -74.43% | 0.25 | 0.62 |
| in_sample | 2020-02-15 → 2024-12-31 | +281.41% | +31.55% | 0.89 | 1.23 | -69.98% | 0.45 | 0.89 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -20.57% | -12.28% | -0.31 | -0.43 | -44.32% | -0.28 | -0.35 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -6.08% | -6.08% | -0.11 | -0.16 | -29.86% | -0.20 | -0.16 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.03% | 41% | -15.32% | -16.37% | -2.27 | 12 | 36% |
| out_of_sample | 628 | -1.82% | 35% | -12.29% | -13.53% | -3.88 | 12 | 30% |
| in_sample | 1768 | -0.74% | 43% | -15.32% | -16.37% | -1.40 | 13 | 38% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.684% | 49% | 4.10 | +204.34% |
| bull | 687 | 28% | +0.272% | 49% | 2.27 | +442.34% |
| bear | 400 | 17% | -0.236% | 32% | -3.40 | -62.46% |
| chop | 1160 | 48% | -0.052% | 35% | -0.71 | -50.87% |

## Turnover, fees, activity

- trades: 34373 (14.18/day); active days 84%
- turnover 268.4x equity/year; fees 26.84% of equity/year ($336,231 total)
- average gross exposure 0.30; brake active 48.3% of hours
- correlation of daily returns with s3v2 baseline: 0.38
