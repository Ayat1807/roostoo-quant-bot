# Run: b4b_score_x_invvol_cap25

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'score_x_invvol', 'coin_cap': 0.25}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +341.57% | +25.07% | 0.81 | 1.12 | -59.59% | 0.42 | 0.81 |
| in_sample | 2020-02-15 → 2024-12-31 | +581.41% | +48.15% | 1.21 | 1.68 | -59.59% | 0.81 | 1.28 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -35.42% | -22.02% | -0.84 | -1.16 | -44.77% | -0.49 | -0.86 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -8.51% | -8.51% | -0.27 | -0.38 | -26.11% | -0.33 | -0.33 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.11% | 40% | -17.56% | -18.30% | -2.35 | 12 | 31% |
| out_of_sample | 628 | -1.81% | 34% | -11.07% | -12.74% | -4.39 | 12 | 19% |
| in_sample | 1768 | -0.85% | 42% | -17.56% | -18.30% | -1.73 | 12 | 35% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.683% | 46% | 3.89 | +201.71% |
| bull | 687 | 28% | +0.286% | 50% | 2.51 | +507.98% |
| bear | 400 | 17% | -0.240% | 32% | -3.82 | -62.92% |
| chop | 1160 | 48% | -0.028% | 34% | -0.40 | -35.08% |

## Turnover, fees, activity

- trades: 14065 (5.80/day); active days 82%
- turnover 178.2x equity/year; fees 17.82% of equity/year ($302,850 total)
- average gross exposure 0.31; brake active 45.3% of hours
- correlation of daily returns with s3v2 baseline: 0.38
