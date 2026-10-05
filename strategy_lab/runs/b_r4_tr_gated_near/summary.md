# Run: b_r4_tr_gated_near

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R4', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally', 'near_high': 0.15}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +1.85% | +0.29% | 0.08 | 0.10 | -18.54% | 0.02 | 0.07 |
| in_sample | 2020-02-15 → 2024-12-31 | +4.54% | +0.91% | 0.15 | 0.20 | -16.49% | 0.06 | 0.14 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -2.58% | -1.73% | -0.18 | -0.24 | -7.55% | -0.23 | -0.22 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +0.41% | +0.55% | 0.15 | 0.22 | -4.29% | 0.13 | 0.17 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 13% | -8.13% | -8.28% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 8% | -3.36% | -7.55% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 14% | -8.13% | -8.28% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | -0.002% | 3% | -0.10 | -0.35% |
| bull | 659 | 28% | +0.021% | 12% | 0.59 | +13.16% |
| bear | 399 | 17% | +0.001% | 0% | 0.96 | +0.50% |
| chop | 1099 | 47% | -0.009% | 3% | -0.73 | -10.13% |

## Turnover, fees, activity

- trades: 463 (0.20/day); active days 10%
- turnover 9.2x equity/year; fees 0.92% of equity/year ($633 total)
- average gross exposure 0.02; brake active 1.8% of hours
- correlation of daily returns with s3v2 baseline: 0.12
