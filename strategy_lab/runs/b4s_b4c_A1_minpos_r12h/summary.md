# Run: b4s_b4c_A1_minpos_r12h

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +112.73% | +12.04% | 0.49 | 0.68 | -82.17% | 0.15 | 0.46 |
| in_sample | 2020-02-15 → 2024-12-31 | +259.93% | +30.00% | 0.86 | 1.19 | -65.93% | 0.45 | 0.87 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -40.90% | -25.86% | -0.89 | -1.24 | -52.86% | -0.49 | -0.91 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -14.60% | -14.60% | -0.47 | -0.66 | -32.42% | -0.45 | -0.54 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.03% | 41% | -18.43% | -19.01% | -2.02 | 14 | 91% |
| out_of_sample | 628 | -1.99% | 32% | -14.55% | -15.31% | -3.84 | 14 | 98% |
| in_sample | 1768 | -0.53% | 44% | -18.43% | -19.01% | -0.96 | 14 | 89% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.770% | 56% | 4.39 | +250.96% |
| bull | 687 | 28% | +0.219% | 49% | 1.89 | +280.95% |
| bear | 400 | 17% | -0.183% | 43% | -2.42 | -53.80% |
| chop | 1160 | 48% | -0.082% | 39% | -1.13 | -65.56% |

## Turnover, fees, activity

- trades: 27246 (11.24/day); active days 97%
- turnover 279.9x equity/year; fees 27.99% of equity/year ($362,842 total)
- average gross exposure 0.37; brake active 49.8% of hours
- correlation of daily returns with s3v2 baseline: 0.50
