# Run: b_r4_tr_gated_rfng

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R4', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally', 'riskoff': 'fng'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +12.89% | +1.92% | 0.21 | 0.29 | -17.92% | 0.11 | 0.21 |
| in_sample | 2020-02-15 → 2024-12-31 | +16.96% | +3.26% | 0.31 | 0.42 | -17.92% | 0.18 | 0.32 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -3.48% | -2.34% | -0.18 | -0.24 | -14.67% | -0.16 | -0.20 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -5.51% | -7.30% | -1.39 | -1.89 | -5.70% | -1.28 | -1.56 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 19% | -7.58% | -8.64% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 10% | -5.13% | -8.32% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 21% | -7.58% | -8.64% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.037% | 8% | 1.46 | +6.36% |
| bull | 659 | 28% | +0.051% | 17% | 0.99 | +35.36% |
| bear | 399 | 17% | -0.000% | 6% | -0.08 | -0.10% |
| chop | 1099 | 47% | -0.021% | 11% | -0.97 | -21.51% |

## Turnover, fees, activity

- trades: 739 (0.32/day); active days 10%
- turnover 15.1x equity/year; fees 1.51% of equity/year ($1,092 total)
- average gross exposure 0.03; brake active 3.0% of hours
- correlation of daily returns with s3v2 baseline: 0.14
