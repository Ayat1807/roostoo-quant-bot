# Run: b4b_live_regime

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'exposure': 'regime'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +62.41% | +7.58% | 0.38 | 0.52 | -79.70% | 0.10 | 0.35 |
| in_sample | 2020-02-15 → 2024-12-31 | +141.15% | +19.76% | 0.64 | 0.88 | -65.71% | 0.30 | 0.63 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -32.80% | -20.24% | -0.62 | -0.86 | -47.52% | -0.43 | -0.66 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +0.90% | +0.90% | 0.17 | 0.24 | -25.39% | 0.04 | 0.16 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.52% | 36% | -21.97% | -22.29% | -3.52 | 12 | 33% |
| out_of_sample | 628 | -2.06% | 30% | -12.91% | -18.58% | -4.56 | 12 | 21% |
| in_sample | 1768 | -1.16% | 39% | -21.97% | -22.29% | -3.02 | 12 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.722% | 47% | 4.02 | +221.02% |
| bull | 687 | 28% | +0.147% | 46% | 1.17 | +126.31% |
| bear | 400 | 17% | -0.202% | 30% | -4.22 | -56.17% |
| chop | 1160 | 48% | -0.048% | 35% | -0.65 | -49.00% |

## Turnover, fees, activity

- trades: 15029 (6.20/day); active days 83%
- turnover 190.7x equity/year; fees 19.07% of equity/year ($171,695 total)
- average gross exposure 0.29; brake active 45.8% of hours
- correlation of daily returns with s3v2 baseline: 0.40
