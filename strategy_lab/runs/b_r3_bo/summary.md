# Run: b_r3_bo

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R3', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +68.52% | +8.53% | 0.44 | 0.61 | -46.94% | 0.18 | 0.43 |
| in_sample | 2020-02-15 → 2024-12-31 | +165.11% | +22.10% | 0.86 | 1.18 | -31.47% | 0.70 | 0.94 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -36.44% | -26.14% | -1.25 | -1.75 | -46.94% | -0.56 | -1.24 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -14.59% | -19.01% | -0.87 | -1.24 | -28.18% | -0.67 | -0.96 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.53% | 40% | -10.43% | -11.46% | -2.09 | 7 | 0% |
| out_of_sample | 532 | -1.42% | 30% | -8.12% | -8.91% | -4.59 | 6 | 0% |
| in_sample | 1768 | -0.25% | 44% | -10.43% | -11.46% | -0.71 | 7 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.348% | 37% | 3.63 | +75.63% |
| bull | 659 | 28% | +0.189% | 36% | 2.17 | +216.48% |
| bear | 399 | 17% | -0.129% | 22% | -3.04 | -40.93% |
| chop | 1099 | 47% | -0.055% | 25% | -0.95 | -48.68% |

## Turnover, fees, activity

- trades: 2053 (0.88/day); active days 45%
- turnover 52.1x equity/year; fees 5.21% of equity/year ($5,791 total)
- average gross exposure 0.18; brake active 15.6% of hours
- correlation of daily returns with s3v2 baseline: 0.22
