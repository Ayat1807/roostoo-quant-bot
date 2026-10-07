# Run: b4s_b4d_resistance_r1h

Strategy `xsmom_entry`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'entry_filter': 'resistance'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -64.66% | -14.50% | -0.25 | -0.35 | -93.62% | -0.15 | -0.26 |
| in_sample | 2020-02-15 → 2024-12-31 | -4.68% | -0.98% | 0.17 | 0.23 | -81.91% | -0.01 | 0.14 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -63.02% | -43.22% | -1.89 | -2.59 | -70.71% | -0.61 | -1.78 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -36.59% | -36.59% | -1.62 | -2.26 | -47.53% | -0.77 | -1.62 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -2.23% | 33% | -21.10% | -22.29% | -4.07 | 13 | 37% |
| out_of_sample | 628 | -3.28% | 24% | -13.01% | -13.78% | -5.94 | 13 | 30% |
| in_sample | 1768 | -1.79% | 37% | -21.10% | -22.29% | -3.15 | 13 | 40% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.796% | 49% | 4.65 | +268.74% |
| bull | 687 | 28% | +0.129% | 43% | 1.12 | +105.53% |
| bear | 400 | 17% | -0.289% | 30% | -4.41 | -69.56% |
| chop | 1160 | 48% | -0.152% | 30% | -2.14 | -84.68% |

## Turnover, fees, activity

- trades: 151378 (62.45/day); active days 86%
- turnover 542.8x equity/year; fees 54.28% of equity/year ($247,739 total)
- average gross exposure 0.29; brake active 53.3% of hours
- correlation of daily returns with s3v2 baseline: 0.36
