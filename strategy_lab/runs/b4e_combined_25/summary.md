# Run: b4e_combined_25

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +232.00% | +19.81% | 0.68 | 0.94 | -65.87% | 0.30 | 0.67 |
| in_sample | 2020-02-15 → 2024-12-31 | +307.38% | +33.34% | 0.94 | 1.29 | -65.87% | 0.51 | 0.95 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -18.78% | -11.16% | -0.28 | -0.40 | -32.32% | -0.35 | -0.35 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -0.97% | -0.97% | 0.08 | 0.12 | -24.77% | -0.04 | 0.06 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.22% | 40% | -20.63% | -20.63% | -2.67 | 12 | 32% |
| out_of_sample | 628 | -1.81% | 36% | -11.97% | -13.23% | -3.80 | 12 | 21% |
| in_sample | 1768 | -0.94% | 42% | -20.63% | -20.63% | -2.04 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.553% | 44% | 3.31 | +142.19% |
| bull | 687 | 28% | +0.262% | 49% | 2.32 | +415.89% |
| bear | 400 | 17% | -0.215% | 29% | -3.32 | -59.03% |
| chop | 1160 | 48% | -0.028% | 34% | -0.39 | -35.14% |

## Turnover, fees, activity

- trades: 14592 (6.02/day); active days 82%
- turnover 167.8x equity/year; fees 16.78% of equity/year ($202,472 total)
- average gross exposure 0.29; brake active 45.2% of hours
- correlation of daily returns with s3v2 baseline: 0.37
