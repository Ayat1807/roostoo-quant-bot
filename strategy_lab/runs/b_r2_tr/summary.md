# Run: b_r2_tr

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R2', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +63.42% | +8.01% | 0.41 | 0.56 | -52.35% | 0.15 | 0.39 |
| in_sample | 2020-02-15 → 2024-12-31 | +80.29% | +12.83% | 0.55 | 0.75 | -52.35% | 0.25 | 0.54 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -9.35% | -6.35% | -0.08 | -0.11 | -28.83% | -0.22 | -0.14 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -2.60% | -3.46% | 0.02 | 0.03 | -17.86% | -0.19 | -0.04 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.61% | 36% | -10.38% | -10.76% | -2.94 | 7 | 7% |
| out_of_sample | 532 | -1.00% | 34% | -10.38% | -10.73% | -3.26 | 6 | 5% |
| in_sample | 1768 | -0.55% | 36% | -9.84% | -10.76% | -2.83 | 8 | 8% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.183% | 31% | 1.73 | +31.99% |
| bull | 659 | 28% | +0.204% | 33% | 1.94 | +236.05% |
| bear | 399 | 17% | -0.150% | 28% | -2.63 | -46.46% |
| chop | 1099 | 47% | -0.025% | 29% | -0.34 | -31.18% |

## Turnover, fees, activity

- trades: 4437 (1.91/day); active days 51%
- turnover 70.2x equity/year; fees 7.02% of equity/year ($5,476 total)
- average gross exposure 0.19; brake active 30.1% of hours
- correlation of daily returns with s3v2 baseline: 0.28
