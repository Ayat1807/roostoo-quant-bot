# Run: b4b_best_conviction

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'score', 'exposure': 'conviction'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +126.83% | +13.13% | 0.51 | 0.71 | -77.37% | 0.17 | 0.49 |
| in_sample | 2020-02-15 → 2024-12-31 | +220.85% | +26.97% | 0.77 | 1.06 | -70.00% | 0.39 | 0.77 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -29.70% | -18.17% | -0.53 | -0.76 | -47.39% | -0.38 | -0.58 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -6.72% | -6.72% | -0.12 | -0.17 | -29.72% | -0.23 | -0.17 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.35% | 39% | -19.15% | -21.76% | -2.73 | 12 | 33% |
| out_of_sample | 628 | -2.64% | 35% | -13.45% | -14.55% | -5.91 | 12 | 21% |
| in_sample | 1768 | -1.13% | 40% | -19.15% | -21.76% | -2.24 | 12 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.861% | 46% | 4.33 | +302.47% |
| bull | 687 | 28% | +0.173% | 47% | 1.40 | +171.20% |
| bear | 400 | 17% | -0.244% | 29% | -3.88 | -63.51% |
| chop | 1160 | 48% | -0.037% | 34% | -0.47 | -43.04% |

## Turnover, fees, activity

- trades: 14986 (6.18/day); active days 83%
- turnover 192.2x equity/year; fees 19.22% of equity/year ($206,217 total)
- average gross exposure 0.28; brake active 48.8% of hours
- correlation of daily returns with s3v2 baseline: 0.35
