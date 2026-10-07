# Run: b4s_b4d_not_ext10_r1h

Strategy `xsmom_entry`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'entry_filter': 'not_extended', 'ext': 0.1}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -50.07% | -9.93% | -0.21 | -0.28 | -90.75% | -0.11 | -0.21 |
| in_sample | 2020-02-15 → 2024-12-31 | -4.73% | -0.99% | 0.13 | 0.17 | -80.61% | -0.01 | 0.10 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -47.59% | -30.76% | -1.47 | -2.05 | -59.73% | -0.52 | -1.41 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -30.61% | -30.61% | -1.62 | -2.30 | -43.53% | -0.70 | -1.62 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.94% | 34% | -11.73% | -13.58% | -4.48 | 12 | 30% |
| out_of_sample | 628 | -2.47% | 28% | -11.73% | -12.39% | -6.63 | 12 | 28% |
| in_sample | 1768 | -1.73% | 37% | -11.52% | -13.58% | -4.02 | 12 | 31% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.430% | 52% | 3.21 | +101.03% |
| bull | 687 | 28% | +0.172% | 46% | 1.74 | +188.67% |
| bear | 400 | 17% | -0.228% | 31% | -4.26 | -60.78% |
| chop | 1160 | 48% | -0.122% | 32% | -1.81 | -78.06% |

## Turnover, fees, activity

- trades: 136830 (56.45/day); active days 82%
- turnover 441.8x equity/year; fees 44.18% of equity/year ($252,917 total)
- average gross exposure 0.26; brake active 51.6% of hours
- correlation of daily returns with s3v2 baseline: 0.39
