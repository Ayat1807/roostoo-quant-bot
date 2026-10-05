# Run: b_r3_rs_gated

Strategy `sat_rs`; universe `{'type': 'satellite', 'rule': 'R3', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | -5.28% | -0.85% | 0.03 | 0.04 | -31.91% | -0.03 | 0.02 |
| in_sample | 2020-02-15 → 2024-12-31 | +17.02% | +3.27% | 0.27 | 0.36 | -29.14% | 0.11 | 0.26 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -19.06% | -13.18% | -1.13 | -1.48 | -26.86% | -0.49 | -1.08 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -10.23% | -13.43% | -2.46 | -2.91 | -11.17% | -1.20 | -2.26 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 26% | -8.48% | -9.10% | 0.00 | 0 | 0% |
| out_of_sample | 532 | -0.00% | 27% | -6.89% | -8.73% | -5.58 | 0 | 0% |
| in_sample | 1768 | +0.00% | 25% | -8.48% | -9.10% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.034% | 24% | 0.80 | +5.42% |
| bull | 659 | 28% | +0.069% | 29% | 1.17 | +51.08% |
| bear | 399 | 17% | -0.004% | 13% | -0.89 | -1.59% |
| chop | 1099 | 47% | -0.044% | 25% | -1.42 | -39.57% |

## Turnover, fees, activity

- trades: 619 (0.27/day); active days 10%
- turnover 14.7x equity/year; fees 1.47% of equity/year ($1,050 total)
- average gross exposure 0.06; brake active 7.8% of hours
- correlation of daily returns with s3v2 baseline: 0.16
