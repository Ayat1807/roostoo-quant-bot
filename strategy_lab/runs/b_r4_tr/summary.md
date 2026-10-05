# Run: b_r4_tr

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R4', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | -7.64% | -1.24% | 0.08 | 0.11 | -47.55% | -0.03 | 0.06 |
| in_sample | 2020-02-15 → 2024-12-31 | -10.41% | -2.23% | 0.05 | 0.06 | -45.10% | -0.05 | 0.02 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +3.09% | +2.06% | 0.20 | 0.29 | -29.93% | 0.07 | 0.20 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -12.32% | -16.12% | -0.77 | -1.12 | -20.41% | -0.79 | -0.92 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.80% | 35% | -9.21% | -11.45% | -3.45 | 9 | 9% |
| out_of_sample | 532 | -0.90% | 35% | -8.39% | -9.12% | -3.65 | 9 | 7% |
| in_sample | 1768 | -0.80% | 34% | -9.21% | -11.45% | -3.40 | 9 | 10% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.027% | 29% | 0.38 | +3.06% |
| bull | 659 | 28% | +0.111% | 36% | 1.31 | +90.57% |
| bear | 399 | 17% | -0.106% | 27% | -2.32 | -35.50% |
| chop | 1099 | 47% | -0.022% | 31% | -0.38 | -27.10% |

## Turnover, fees, activity

- trades: 3325 (1.43/day); active days 59%
- turnover 58.4x equity/year; fees 5.84% of equity/year ($3,919 total)
- average gross exposure 0.18; brake active 18.0% of hours
- correlation of daily returns with s3v2 baseline: 0.31
