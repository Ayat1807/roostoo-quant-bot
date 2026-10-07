# Run: b4x_stop4

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +251.65% | +20.85% | 0.72 | 1.01 | -66.19% | 0.31 | 0.71 |
| in_sample | 2020-02-15 → 2024-12-31 | +322.77% | +34.35% | 0.99 | 1.37 | -66.19% | 0.52 | 1.00 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -17.11% | -10.13% | -0.26 | -0.36 | -37.81% | -0.27 | -0.30 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +0.53% | +0.53% | 0.14 | 0.21 | -24.83% | 0.02 | 0.13 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.21% | 40% | -15.47% | -16.06% | -2.62 | 12 | 30% |
| out_of_sample | 628 | -1.78% | 39% | -11.97% | -14.97% | -3.78 | 12 | 18% |
| in_sample | 1768 | -1.01% | 41% | -15.47% | -16.06% | -2.21 | 12 | 35% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.619% | 45% | 3.97 | +174.83% |
| bull | 687 | 28% | +0.247% | 48% | 2.27 | +370.81% |
| bear | 400 | 17% | -0.261% | 28% | -4.53 | -65.75% |
| chop | 1160 | 48% | -0.011% | 33% | -0.15 | -20.64% |

## Turnover, fees, activity

- trades: 13565 (5.60/day); active days 81%
- turnover 164.9x equity/year; fees 16.49% of equity/year ($205,996 total)
- average gross exposure 0.28; brake active 49.7% of hours
- correlation of daily returns with s3v2 baseline: 0.38
