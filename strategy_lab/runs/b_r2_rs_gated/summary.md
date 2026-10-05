# Run: b_r2_rs_gated

Strategy `sat_rs`; universe `{'type': 'satellite', 'rule': 'R2', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | -15.06% | -2.53% | -0.06 | -0.08 | -37.92% | -0.07 | -0.07 |
| in_sample | 2020-02-15 → 2024-12-31 | +7.01% | +1.40% | 0.17 | 0.23 | -37.92% | 0.04 | 0.15 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -20.62% | -14.31% | -0.95 | -1.23 | -26.79% | -0.53 | -0.94 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -12.90% | -16.87% | -1.97 | -2.28 | -13.19% | -1.28 | -1.88 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 14% | -14.91% | -16.27% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 8% | -9.72% | -10.03% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 16% | -14.91% | -16.27% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.104% | 4% | 2.37 | +18.60% |
| bull | 659 | 28% | +0.039% | 11% | 0.50 | +20.47% |
| bear | 399 | 17% | -0.001% | 3% | -0.95 | -0.55% |
| chop | 1099 | 47% | -0.044% | 4% | -1.18 | -40.22% |

## Turnover, fees, activity

- trades: 515 (0.22/day); active days 8%
- turnover 14.8x equity/year; fees 1.48% of equity/year ($944 total)
- average gross exposure 0.05; brake active 9.6% of hours
- correlation of daily returns with s3v2 baseline: 0.15
