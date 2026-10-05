# Run: b_r1_rs_noR5

Strategy `sat_rs`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': False, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +218.17% | +19.90% | 0.69 | 0.95 | -50.85% | 0.39 | 0.70 |
| in_sample | 2020-02-15 → 2024-12-31 | +288.12% | +32.02% | 0.94 | 1.29 | -50.85% | 0.63 | 0.99 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -18.02% | -12.44% | -0.26 | -0.36 | -30.93% | -0.40 | -0.34 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -21.34% | -27.46% | -0.88 | -1.24 | -26.30% | -1.04 | -1.08 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.46% | 42% | -10.84% | -12.46% | -1.41 | 4 | 0% |
| out_of_sample | 532 | -0.93% | 43% | -9.16% | -9.84% | -2.15 | 4 | 0% |
| in_sample | 1768 | -0.33% | 42% | -10.84% | -12.46% | -1.06 | 4 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.379% | 30% | 3.06 | +81.51% |
| bull | 659 | 28% | +0.269% | 39% | 2.37 | +403.45% |
| bear | 399 | 17% | -0.247% | 28% | -3.26 | -64.26% |
| chop | 1099 | 47% | +0.010% | 35% | 0.12 | -2.57% |

## Turnover, fees, activity

- trades: 1709 (0.73/day); active days 33%
- turnover 40.1x equity/year; fees 4.01% of equity/year ($5,830 total)
- average gross exposure 0.28; brake active 43.6% of hours
- correlation of daily returns with s3v2 baseline: 0.27
