# Run: b3_xsmom_r1

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +270.83% | +21.82% | 0.73 | 1.00 | -61.87% | 0.35 | 0.72 |
| in_sample | 2020-02-15 → 2024-12-31 | +414.43% | +39.86% | 1.06 | 1.46 | -60.24% | 0.66 | 1.10 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -28.17% | -17.16% | -0.52 | -0.73 | -40.17% | -0.43 | -0.58 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -6.76% | -6.76% | -0.15 | -0.22 | -26.42% | -0.26 | -0.21 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.16% | 40% | -19.13% | -19.84% | -2.27 | 12 | 31% |
| out_of_sample | 628 | -1.95% | 36% | -11.96% | -14.96% | -4.43 | 12 | 19% |
| in_sample | 1768 | -0.90% | 42% | -19.13% | -19.84% | -1.77 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.614% | 47% | 3.65 | +168.78% |
| bull | 687 | 28% | +0.272% | 49% | 2.39 | +450.24% |
| bear | 400 | 17% | -0.222% | 31% | -3.38 | -60.16% |
| chop | 1160 | 48% | -0.030% | 34% | -0.41 | -37.07% |

## Turnover, fees, activity

- trades: 14004 (5.78/day); active days 82%
- turnover 167.4x equity/year; fees 16.74% of equity/year ($242,266 total)
- average gross exposure 0.30; brake active 47.4% of hours
- correlation of daily returns with s3v2 baseline: 0.34
