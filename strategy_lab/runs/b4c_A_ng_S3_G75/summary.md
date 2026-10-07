# Run: b4c_A_ng_S3_G75

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 3, 'gross_cap': 0.75, 'short_gate': 'none'}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +18.50% | +2.59% | 0.25 | 0.35 | -74.05% | 0.03 | 0.23 |
| in_sample | 2020-02-15 → 2024-12-31 | +183.93% | +23.83% | 0.74 | 1.04 | -54.83% | 0.43 | 0.77 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -58.30% | -39.20% | -1.50 | -2.09 | -61.44% | -0.64 | -1.48 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -27.31% | -27.31% | -1.06 | -1.48 | -41.83% | -0.65 | -1.11 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.01% | 43% | -21.46% | -23.19% | -1.82 | 14 | 98% |
| out_of_sample | 628 | -2.39% | 32% | -14.71% | -18.94% | -4.32 | 14 | 100% |
| in_sample | 1768 | -0.25% | 46% | -21.46% | -23.19% | -0.38 | 14 | 97% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.621% | 52% | 3.49 | +169.37% |
| bull | 687 | 28% | +0.129% | 48% | 1.18 | +109.84% |
| bear | 400 | 17% | -0.132% | 44% | -1.70 | -43.67% |
| chop | 1160 | 48% | -0.075% | 40% | -1.02 | -62.78% |

## Turnover, fees, activity

- trades: 23049 (9.51/day); active days 98%
- turnover 260.0x equity/year; fees 26.00% of equity/year ($194,400 total)
- average gross exposure 0.43; brake active 53.3% of hours
- correlation of daily returns with s3v2 baseline: 0.50
