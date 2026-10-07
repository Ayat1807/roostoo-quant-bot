# Run: b4s_b4e_combined_50_r1h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -56.73% | -11.85% | -0.17 | -0.23 | -91.82% | -0.13 | -0.18 |
| in_sample | 2020-02-15 → 2024-12-31 | +15.93% | +3.07% | 0.27 | 0.37 | -79.91% | 0.04 | 0.24 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -62.77% | -43.00% | -1.89 | -2.60 | -70.33% | -0.61 | -1.79 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -36.83% | -36.83% | -1.65 | -2.30 | -47.37% | -0.78 | -1.65 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -2.21% | 34% | -20.05% | -21.26% | -3.91 | 13 | 37% |
| out_of_sample | 628 | -3.18% | 24% | -13.01% | -13.78% | -5.87 | 13 | 30% |
| in_sample | 1768 | -1.74% | 38% | -20.05% | -21.26% | -3.05 | 13 | 40% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.785% | 51% | 4.65 | +262.38% |
| bull | 687 | 28% | +0.153% | 44% | 1.32 | +142.68% |
| bear | 400 | 17% | -0.285% | 30% | -4.43 | -69.04% |
| chop | 1160 | 48% | -0.149% | 31% | -2.09 | -84.11% |

## Turnover, fees, activity

- trades: 152948 (63.10/day); active days 86%
- turnover 543.9x equity/year; fees 54.39% of equity/year ($270,760 total)
- average gross exposure 0.29; brake active 53.0% of hours
- correlation of daily returns with s3v2 baseline: 0.36
