# Run: b4s_b4e_combined_50_r4h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +198.15% | +17.88% | 0.63 | 0.88 | -67.43% | 0.27 | 0.62 |
| in_sample | 2020-02-15 → 2024-12-31 | +382.31% | +38.03% | 1.02 | 1.41 | -65.00% | 0.59 | 1.04 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -38.33% | -24.04% | -0.82 | -1.14 | -52.01% | -0.46 | -0.84 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -19.39% | -19.39% | -0.72 | -1.02 | -34.55% | -0.56 | -0.79 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.15% | 41% | -16.09% | -17.92% | -2.46 | 13 | 36% |
| out_of_sample | 628 | -2.19% | 34% | -12.20% | -13.39% | -4.56 | 12 | 27% |
| in_sample | 1768 | -0.74% | 43% | -16.09% | -17.92% | -1.40 | 13 | 39% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.726% | 49% | 4.28 | +226.45% |
| bull | 687 | 28% | +0.293% | 50% | 2.40 | +520.88% |
| bear | 400 | 17% | -0.287% | 30% | -4.36 | -69.34% |
| chop | 1160 | 48% | -0.054% | 35% | -0.74 | -52.02% |

## Turnover, fees, activity

- trades: 47501 (19.60/day); active days 85%
- turnover 310.4x equity/year; fees 31.04% of equity/year ($394,933 total)
- average gross exposure 0.30; brake active 48.9% of hours
- correlation of daily returns with s3v2 baseline: 0.37
