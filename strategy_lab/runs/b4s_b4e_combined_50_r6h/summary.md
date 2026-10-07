# Run: b4s_b4e_combined_50_r6h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +188.07% | +17.27% | 0.62 | 0.85 | -74.70% | 0.23 | 0.59 |
| in_sample | 2020-02-15 → 2024-12-31 | +297.03% | +32.64% | 0.91 | 1.25 | -69.71% | 0.47 | 0.92 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -27.62% | -16.79% | -0.51 | -0.71 | -47.32% | -0.35 | -0.54 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -7.99% | -7.99% | -0.20 | -0.28 | -28.76% | -0.28 | -0.25 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.01% | 40% | -14.14% | -16.37% | -2.16 | 13 | 36% |
| out_of_sample | 628 | -1.91% | 33% | -12.60% | -13.53% | -4.42 | 12 | 31% |
| in_sample | 1768 | -0.69% | 43% | -14.14% | -16.37% | -1.33 | 13 | 38% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.681% | 47% | 4.16 | +203.84% |
| bull | 687 | 28% | +0.270% | 47% | 2.26 | +436.44% |
| bear | 400 | 17% | -0.245% | 32% | -3.52 | -63.87% |
| chop | 1160 | 48% | -0.052% | 33% | -0.72 | -51.08% |

## Turnover, fees, activity

- trades: 34984 (14.43/day); active days 84%
- turnover 272.5x equity/year; fees 27.25% of equity/year ($339,452 total)
- average gross exposure 0.30; brake active 48.2% of hours
- correlation of daily returns with s3v2 baseline: 0.38
