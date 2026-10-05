# Run: b_r4_rs_gated

Strategy `sat_rs`; universe `{'type': 'satellite', 'rule': 'R4', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | -16.28% | -2.75% | -0.09 | -0.12 | -31.06% | -0.09 | -0.10 |
| in_sample | 2020-02-15 → 2024-12-31 | -2.38% | -0.49% | 0.05 | 0.07 | -28.77% | -0.02 | 0.04 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -14.23% | -9.75% | -0.60 | -0.80 | -23.27% | -0.42 | -0.63 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -8.15% | -10.75% | -1.08 | -1.39 | -9.18% | -1.17 | -1.23 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 24% | -11.44% | -11.78% | 0.00 | 0 | 0% |
| out_of_sample | 532 | -0.00% | 31% | -8.23% | -9.43% | -3.92 | 0 | 0% |
| in_sample | 1768 | +0.00% | 21% | -11.44% | -11.78% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.007% | 22% | 0.13 | +0.19% |
| bull | 659 | 28% | +0.058% | 26% | 0.94 | +39.88% |
| bear | 399 | 17% | +0.001% | 13% | 0.45 | +0.57% |
| chop | 1099 | 47% | -0.046% | 24% | -1.48 | -40.60% |

## Turnover, fees, activity

- trades: 571 (0.25/day); active days 9%
- turnover 14.9x equity/year; fees 1.49% of equity/year ($924 total)
- average gross exposure 0.05; brake active 9.6% of hours
- correlation of daily returns with s3v2 baseline: 0.16
