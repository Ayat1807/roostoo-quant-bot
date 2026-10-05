# Run: b_r1_tr_near

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'near_high': 0.15}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +124.97% | +13.56% | 0.68 | 0.91 | -38.05% | 0.36 | 0.68 |
| in_sample | 2020-02-15 → 2024-12-31 | +182.63% | +23.72% | 1.00 | 1.36 | -38.05% | 0.62 | 1.03 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -20.40% | -14.15% | -0.85 | -1.14 | -27.61% | -0.51 | -0.86 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +0.16% | +0.21% | 0.08 | 0.11 | -11.60% | 0.02 | 0.08 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.06% | 36% | -9.34% | -11.45% | -0.68 | 8 | 8% |
| out_of_sample | 532 | -0.77% | 28% | -7.83% | -8.70% | -5.82 | 9 | 8% |
| in_sample | 1768 | +0.00% | 39% | -9.34% | -11.45% | 0.00 | 8 | 8% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.176% | 26% | 1.63 | +30.27% |
| bull | 659 | 28% | +0.182% | 34% | 2.12 | +204.56% |
| bear | 399 | 17% | -0.017% | 18% | -0.68 | -7.15% |
| chop | 1099 | 47% | -0.043% | 25% | -1.20 | -38.93% |

## Turnover, fees, activity

- trades: 2993 (1.29/day); active days 53%
- turnover 47.6x equity/year; fees 4.76% of equity/year ($5,687 total)
- average gross exposure 0.14; brake active 10.2% of hours
- correlation of daily returns with s3v2 baseline: 0.18
