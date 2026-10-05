# Run: b_r1_tr

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +115.05% | +12.76% | 0.52 | 0.70 | -57.51% | 0.22 | 0.50 |
| in_sample | 2020-02-15 → 2024-12-31 | +136.23% | +19.25% | 0.67 | 0.90 | -57.51% | 0.33 | 0.66 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -8.96% | -6.08% | -0.05 | -0.07 | -34.48% | -0.18 | -0.09 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -16.44% | -21.36% | -0.76 | -1.07 | -24.99% | -0.85 | -0.91 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.87% | 39% | -10.50% | -11.45% | -2.95 | 7 | 9% |
| out_of_sample | 532 | -1.67% | 34% | -8.38% | -9.36% | -5.32 | 7 | 6% |
| in_sample | 1768 | -0.66% | 40% | -10.50% | -11.45% | -2.07 | 7 | 10% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.407% | 33% | 3.25 | +90.27% |
| bull | 659 | 28% | +0.193% | 30% | 1.75 | +209.06% |
| bear | 399 | 17% | -0.197% | 21% | -3.02 | -55.92% |
| chop | 1099 | 47% | -0.005% | 25% | -0.07 | -17.04% |

## Turnover, fees, activity

- trades: 6609 (2.84/day); active days 51%
- turnover 91.6x equity/year; fees 9.16% of equity/year ($9,267 total)
- average gross exposure 0.25; brake active 40.3% of hours
- correlation of daily returns with s3v2 baseline: 0.32
