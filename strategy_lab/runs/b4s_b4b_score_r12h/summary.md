# Run: b4s_b4b_score_r12h

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'score'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +500.50% | +30.99% | 0.88 | 1.24 | -73.63% | 0.42 | 0.89 |
| in_sample | 2020-02-15 → 2024-12-31 | +664.61% | +51.69% | 1.19 | 1.68 | -69.34% | 0.75 | 1.25 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -22.06% | -13.22% | -0.34 | -0.48 | -38.63% | -0.34 | -0.40 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -4.26% | -4.26% | -0.04 | -0.06 | -23.63% | -0.18 | -0.09 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.09% | 40% | -18.36% | -20.67% | -2.19 | 12 | 33% |
| out_of_sample | 628 | -1.92% | 37% | -11.19% | -15.12% | -3.94 | 12 | 24% |
| in_sample | 1768 | -0.87% | 42% | -18.36% | -20.67% | -1.69 | 13 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.868% | 47% | 4.41 | +308.01% |
| bull | 687 | 28% | +0.281% | 50% | 2.16 | +458.00% |
| bear | 400 | 17% | -0.258% | 30% | -3.74 | -65.59% |
| chop | 1160 | 48% | -0.012% | 36% | -0.15 | -23.35% |

## Turnover, fees, activity

- trades: 21516 (8.88/day); active days 83%
- turnover 225.6x equity/year; fees 22.56% of equity/year ($551,382 total)
- average gross exposure 0.30; brake active 47.1% of hours
- correlation of daily returns with s3v2 baseline: 0.35
