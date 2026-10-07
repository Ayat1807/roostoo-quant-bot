# Run: b4e_breakout

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +209.30% | +18.54% | 0.65 | 0.90 | -65.54% | 0.28 | 0.64 |
| in_sample | 2020-02-15 → 2024-12-31 | +341.90% | +35.58% | 0.98 | 1.35 | -59.88% | 0.59 | 1.01 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -30.25% | -18.53% | -0.58 | -0.81 | -42.07% | -0.44 | -0.63 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -7.79% | -7.79% | -0.20 | -0.28 | -26.58% | -0.29 | -0.26 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.17% | 40% | -19.13% | -19.84% | -2.31 | 12 | 31% |
| out_of_sample | 628 | -2.00% | 35% | -11.96% | -14.96% | -4.67 | 12 | 19% |
| in_sample | 1768 | -0.89% | 42% | -19.13% | -19.84% | -1.82 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.531% | 45% | 3.18 | +133.10% |
| bull | 687 | 28% | +0.269% | 50% | 2.36 | +439.13% |
| bear | 400 | 17% | -0.225% | 32% | -3.41 | -60.59% |
| chop | 1160 | 48% | -0.031% | 36% | -0.42 | -37.55% |

## Turnover, fees, activity

- trades: 14127 (5.83/day); active days 82%
- turnover 168.8x equity/year; fees 16.88% of equity/year ($221,172 total)
- average gross exposure 0.30; brake active 47.0% of hours
- correlation of daily returns with s3v2 baseline: 0.37
