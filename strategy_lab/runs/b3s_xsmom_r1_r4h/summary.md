# Run: b3s_xsmom_r1_r4h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +174.28% | +16.41% | 0.60 | 0.83 | -71.60% | 0.23 | 0.58 |
| in_sample | 2020-02-15 → 2024-12-31 | +362.85% | +36.87% | 0.99 | 1.37 | -64.49% | 0.57 | 1.02 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -40.88% | -25.85% | -0.89 | -1.24 | -54.79% | -0.47 | -0.90 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -21.32% | -21.32% | -0.81 | -1.13 | -37.85% | -0.56 | -0.86 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.14% | 41% | -16.34% | -17.93% | -2.49 | 13 | 35% |
| out_of_sample | 628 | -2.21% | 34% | -12.20% | -13.39% | -4.87 | 12 | 27% |
| in_sample | 1768 | -0.62% | 44% | -16.34% | -17.93% | -1.16 | 13 | 39% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.726% | 49% | 4.25 | +226.10% |
| bull | 687 | 28% | +0.291% | 49% | 2.39 | +513.04% |
| bear | 400 | 17% | -0.277% | 28% | -4.13 | -68.07% |
| chop | 1160 | 48% | -0.063% | 34% | -0.87 | -57.03% |

## Turnover, fees, activity

- trades: 47295 (19.51/day); active days 85%
- turnover 311.2x equity/year; fees 31.12% of equity/year ($386,557 total)
- average gross exposure 0.30; brake active 49.6% of hours
- correlation of daily returns with s3v2 baseline: 0.34
