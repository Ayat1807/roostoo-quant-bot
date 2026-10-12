# Run: b12_aggr_15

Strategy `s3v2x_regime`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.6, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +167.27% | +15.96% | 0.80 | 1.16 | -21.35% | 0.75 | 0.93 |
| in_sample | 2020-02-15 → 2024-12-31 | +125.88% | +18.16% | 0.89 | 1.29 | -21.35% | 0.85 | 1.04 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +18.51% | +10.14% | 0.56 | 0.81 | -19.68% | 0.52 | 0.65 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +12.09% | +12.09% | 0.65 | 0.94 | -15.03% | 0.80 | 0.81 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.13% | 48% | -8.01% | -8.81% | -0.67 | 14 | 99% |
| out_of_sample | 628 | -0.36% | 47% | -8.01% | -8.81% | -1.30 | 14 | 100% |
| in_sample | 1768 | -0.07% | 49% | -6.73% | -8.67% | -0.30 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.313% | 53% | 3.53 | +69.26% |
| bull | 687 | 28% | +0.117% | 52% | 2.17 | +115.33% |
| bear | 400 | 17% | +0.047% | 47% | 0.84 | +18.01% |
| chop | 1160 | 48% | -0.036% | 44% | -0.75 | -37.53% |

## Turnover, fees, activity

- trades: 8978 (3.70/day); active days 100%
- turnover 82.9x equity/year; fees 8.29% of equity/year ($52,796 total)
- average gross exposure 0.28; brake active 34.6% of hours
- correlation of daily returns with s3v2 baseline: 0.74
