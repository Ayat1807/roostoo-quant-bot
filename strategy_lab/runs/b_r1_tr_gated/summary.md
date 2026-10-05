# Run: b_r1_tr_gated

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +34.87% | +4.80% | 0.34 | 0.46 | -32.26% | 0.15 | 0.33 |
| in_sample | 2020-02-15 → 2024-12-31 | +48.54% | +8.44% | 0.51 | 0.68 | -32.26% | 0.26 | 0.50 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -9.21% | -6.25% | -0.34 | -0.47 | -22.91% | -0.27 | -0.37 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -10.26% | -13.48% | -2.02 | -2.52 | -10.26% | -1.31 | -2.01 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 22% | -12.55% | -13.73% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 12% | -8.61% | -9.38% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 25% | -12.55% | -13.73% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.183% | 23% | 2.62 | +34.47% |
| bull | 659 | 28% | +0.085% | 22% | 1.12 | +63.40% |
| bear | 399 | 17% | -0.007% | 5% | -1.03 | -2.89% |
| chop | 1099 | 47% | -0.040% | 10% | -1.49 | -36.79% |

## Turnover, fees, activity

- trades: 1679 (0.72/day); active days 10%
- turnover 23.2x equity/year; fees 2.32% of equity/year ($1,880 total)
- average gross exposure 0.06; brake active 8.4% of hours
- correlation of daily returns with s3v2 baseline: 0.16
