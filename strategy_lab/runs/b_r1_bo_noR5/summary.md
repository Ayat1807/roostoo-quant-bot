# Run: b_r1_bo_noR5

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': False, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +85.83% | +10.20% | 0.46 | 0.64 | -67.20% | 0.15 | 0.44 |
| in_sample | 2020-02-15 → 2024-12-31 | +164.92% | +22.09% | 0.75 | 1.05 | -67.20% | 0.33 | 0.74 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -30.30% | -21.44% | -0.67 | -0.95 | -37.08% | -0.58 | -0.76 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -20.41% | -26.31% | -0.89 | -1.28 | -24.57% | -1.07 | -1.10 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -1.14% | 38% | -9.64% | -11.46% | -2.90 | 6 | 1% |
| out_of_sample | 532 | -1.92% | 29% | -8.95% | -10.66% | -4.29 | 6 | 0% |
| in_sample | 1768 | -0.70% | 41% | -9.64% | -11.46% | -2.23 | 6 | 1% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.530% | 38% | 4.13 | +133.69% |
| bull | 659 | 28% | +0.148% | 28% | 1.41 | +133.46% |
| bear | 399 | 17% | -0.159% | 21% | -2.20 | -49.00% |
| chop | 1099 | 47% | -0.027% | 24% | -0.35 | -33.21% |

## Turnover, fees, activity

- trades: 2618 (1.12/day); active days 45%
- turnover 66.2x equity/year; fees 6.62% of equity/year ($7,000 total)
- average gross exposure 0.23; brake active 33.1% of hours
- correlation of daily returns with s3v2 baseline: 0.20
