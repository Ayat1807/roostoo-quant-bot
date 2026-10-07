# Run: b4s_b4c_A1_minpos_r6h

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +6.94% | +1.02% | 0.21 | 0.30 | -87.08% | 0.01 | 0.19 |
| in_sample | 2020-02-15 → 2024-12-31 | +90.92% | +14.16% | 0.53 | 0.73 | -75.46% | 0.19 | 0.51 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -43.77% | -27.93% | -0.95 | -1.34 | -56.56% | -0.49 | -0.97 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -20.14% | -20.14% | -0.71 | -0.99 | -36.74% | -0.55 | -0.77 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.45% | 38% | -17.01% | -19.77% | -2.74 | 14 | 90% |
| out_of_sample | 628 | -2.38% | 30% | -13.89% | -14.76% | -4.94 | 14 | 96% |
| in_sample | 1768 | -1.02% | 41% | -17.01% | -19.77% | -1.74 | 14 | 89% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.778% | 56% | 4.51 | +256.40% |
| bull | 687 | 28% | +0.242% | 48% | 2.03 | +342.21% |
| bear | 400 | 17% | -0.253% | 40% | -3.44 | -65.06% |
| chop | 1160 | 48% | -0.132% | 37% | -1.81 | -80.58% |

## Turnover, fees, activity

- trades: 44456 (18.34/day); active days 97%
- turnover 360.7x equity/year; fees 36.07% of equity/year ($284,591 total)
- average gross exposure 0.36; brake active 52.3% of hours
- correlation of daily returns with s3v2 baseline: 0.51
