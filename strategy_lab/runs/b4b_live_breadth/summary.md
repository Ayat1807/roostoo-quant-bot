# Run: b4b_live_breadth

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'exposure': 'breadth'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +416.55% | +28.06% | 0.92 | 1.27 | -50.07% | 0.56 | 0.95 |
| in_sample | 2020-02-15 → 2024-12-31 | +528.20% | +45.71% | 1.25 | 1.73 | -50.07% | 0.91 | 1.34 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -17.85% | -10.58% | -0.32 | -0.45 | -31.61% | -0.33 | -0.37 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -8.65% | -8.65% | -0.31 | -0.44 | -24.88% | -0.35 | -0.38 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.87% | 41% | -14.77% | -17.78% | -2.64 | 12 | 32% |
| out_of_sample | 628 | -1.60% | 37% | -11.39% | -13.36% | -5.42 | 12 | 21% |
| in_sample | 1768 | -0.64% | 43% | -14.77% | -17.78% | -1.80 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.623% | 44% | 4.17 | +178.69% |
| bull | 687 | 28% | +0.269% | 49% | 2.57 | +452.93% |
| bear | 400 | 17% | -0.223% | 31% | -3.97 | -60.04% |
| chop | 1160 | 48% | -0.008% | 34% | -0.12 | -16.12% |

## Turnover, fees, activity

- trades: 13228 (5.46/day); active days 83%
- turnover 134.6x equity/year; fees 13.46% of equity/year ($211,863 total)
- average gross exposure 0.24; brake active 43.7% of hours
- correlation of daily returns with s3v2 baseline: 0.40
