# Run: b4c_A_ng_S2_G90

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.9, 'short_gate': 'none'}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +24.00% | +3.29% | 0.27 | 0.37 | -82.19% | 0.04 | 0.24 |
| in_sample | 2020-02-15 → 2024-12-31 | +201.87% | +25.40% | 0.79 | 1.10 | -59.24% | 0.43 | 0.80 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -58.98% | -39.77% | -1.58 | -2.21 | -63.93% | -0.62 | -1.54 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -23.98% | -23.98% | -0.91 | -1.29 | -38.82% | -0.62 | -0.97 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.32% | 40% | -19.92% | -23.11% | -2.49 | 14 | 98% |
| out_of_sample | 628 | -2.72% | 32% | -14.90% | -18.74% | -4.99 | 14 | 100% |
| in_sample | 1768 | -0.71% | 43% | -19.92% | -23.11% | -1.53 | 14 | 97% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.562% | 53% | 3.39 | +146.23% |
| bull | 687 | 28% | +0.164% | 49% | 1.48 | +165.38% |
| bear | 400 | 17% | -0.148% | 44% | -2.30 | -46.41% |
| chop | 1160 | 48% | -0.080% | 40% | -1.11 | -64.59% |

## Turnover, fees, activity

- trades: 20794 (8.58/day); active days 98%
- turnover 250.9x equity/year; fees 25.09% of equity/year ($235,844 total)
- average gross exposure 0.41; brake active 51.1% of hours
- correlation of daily returns with s3v2 baseline: 0.48
