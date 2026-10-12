# Run: b12_hmm_cusum_aggr

Strategy `s3v2x_regime`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 1.0, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'n_divisor': 10, 'floor_share': 0.7, 'floor_gross': 0.6}`; band 0.04; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +79.38% | +9.20% | 0.43 | 0.61 | -41.97% | 0.22 | 0.44 |
| in_sample | 2020-02-15 → 2024-12-31 | +106.98% | +16.07% | 0.59 | 0.84 | -41.97% | 0.38 | 0.63 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -13.26% | -7.77% | -0.10 | -0.15 | -34.38% | -0.23 | -0.16 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -1.67% | -1.67% | 0.09 | 0.13 | -24.18% | -0.07 | 0.06 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.07% | 44% | -12.30% | -16.65% | -2.05 | 14 | 95% |
| out_of_sample | 628 | -1.89% | 40% | -10.38% | -12.43% | -3.52 | 14 | 93% |
| in_sample | 1768 | -0.75% | 45% | -12.30% | -16.22% | -1.36 | 14 | 96% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.702% | 50% | 4.17 | +214.15% |
| bull | 687 | 28% | +0.086% | 49% | 1.02 | +65.56% |
| bear | 400 | 17% | +0.006% | 45% | 0.07 | -3.27% |
| chop | 1160 | 48% | -0.077% | 41% | -0.94 | -64.24% |

## Turnover, fees, activity

- trades: 25053 (10.34/day); active days 100%
- turnover 212.5x equity/year; fees 21.25% of equity/year ($114,698 total)
- average gross exposure 0.48; brake active 43.5% of hours
- correlation of daily returns with s3v2 baseline: 0.73
