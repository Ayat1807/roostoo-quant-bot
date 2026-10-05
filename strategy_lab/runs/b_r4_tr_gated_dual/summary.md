# Run: b_r4_tr_gated_dual

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R4', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally', 'dual': True}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +15.80% | +2.33% | 0.25 | 0.34 | -15.27% | 0.15 | 0.26 |
| in_sample | 2020-02-15 → 2024-12-31 | +15.91% | +3.07% | 0.30 | 0.41 | -15.27% | 0.20 | 0.32 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -0.09% | -0.06% | 0.05 | 0.07 | -10.79% | -0.01 | 0.04 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -5.83% | -7.72% | -1.54 | -2.09 | -6.02% | -1.28 | -1.68 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 15% | -7.88% | -8.62% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 14% | -4.45% | -7.71% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 15% | -7.88% | -8.62% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.034% | 5% | 1.33 | +5.73% |
| bull | 659 | 28% | +0.055% | 14% | 1.08 | +39.20% |
| bear | 399 | 17% | -0.000% | 0% | -0.08 | -0.10% |
| chop | 1099 | 47% | -0.021% | 4% | -1.09 | -21.24% |

## Turnover, fees, activity

- trades: 754 (0.32/day); active days 12%
- turnover 14.8x equity/year; fees 1.48% of equity/year ($1,069 total)
- average gross exposure 0.04; brake active 3.0% of hours
- correlation of daily returns with s3v2 baseline: 0.16
