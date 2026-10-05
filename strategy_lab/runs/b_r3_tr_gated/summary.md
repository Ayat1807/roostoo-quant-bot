# Run: b_r3_tr_gated

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R3', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +22.37% | +3.22% | 0.32 | 0.44 | -22.25% | 0.14 | 0.31 |
| in_sample | 2020-02-15 → 2024-12-31 | +22.90% | +4.31% | 0.39 | 0.53 | -22.25% | 0.19 | 0.39 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -0.43% | -0.29% | 0.02 | 0.02 | -8.79% | -0.03 | 0.00 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -1.93% | -2.57% | -1.05 | -1.33 | -2.85% | -0.90 | -1.12 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 21% | -9.98% | -10.00% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 12% | -3.49% | -4.96% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 24% | -9.98% | -10.00% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.020% | 16% | 0.52 | +3.03% |
| bull | 659 | 28% | +0.069% | 22% | 1.51 | +53.54% |
| bear | 399 | 17% | -0.004% | 6% | -1.02 | -1.79% |
| chop | 1099 | 47% | -0.021% | 8% | -1.25 | -21.24% |

## Turnover, fees, activity

- trades: 794 (0.34/day); active days 12%
- turnover 14.1x equity/year; fees 1.41% of equity/year ($1,067 total)
- average gross exposure 0.04; brake active 3.6% of hours
- correlation of daily returns with s3v2 baseline: 0.13
