# Run: b3s_xsmom_r1_r6h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +211.33% | +18.65% | 0.65 | 0.89 | -73.46% | 0.25 | 0.63 |
| in_sample | 2020-02-15 → 2024-12-31 | +335.41% | +35.17% | 0.95 | 1.32 | -66.33% | 0.53 | 0.97 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -28.67% | -17.48% | -0.53 | -0.74 | -47.64% | -0.37 | -0.57 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -8.37% | -8.37% | -0.21 | -0.30 | -29.42% | -0.28 | -0.27 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.10% | 41% | -16.50% | -17.38% | -2.27 | 13 | 36% |
| out_of_sample | 628 | -2.16% | 33% | -12.29% | -13.53% | -4.55 | 12 | 30% |
| in_sample | 1768 | -0.64% | 43% | -16.50% | -17.38% | -1.28 | 13 | 38% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.684% | 48% | 4.03 | +203.55% |
| bull | 687 | 28% | +0.280% | 47% | 2.33 | +472.00% |
| bear | 400 | 17% | -0.244% | 32% | -3.50 | -63.76% |
| chop | 1160 | 48% | -0.051% | 34% | -0.70 | -50.53% |

## Turnover, fees, activity

- trades: 34560 (14.26/day); active days 84%
- turnover 271.9x equity/year; fees 27.19% of equity/year ($363,951 total)
- average gross exposure 0.30; brake active 48.1% of hours
- correlation of daily returns with s3v2 baseline: 0.35
