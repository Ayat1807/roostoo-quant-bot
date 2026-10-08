# Run: b8_h_U5

Strategy `s3v2x_regime`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 20, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'n_divisor': 10, 'max_gross': 0.8}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +69.51% | +8.27% | 0.88 | 1.29 | -12.24% | 0.68 | 0.98 |
| in_sample | 2020-02-15 → 2024-12-31 | +66.56% | +11.02% | 1.09 | 1.61 | -12.24% | 0.90 | 1.24 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +1.88% | +1.06% | 0.17 | 0.25 | -11.19% | 0.09 | 0.18 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +0.29% | +0.29% | 0.08 | 0.11 | -11.19% | 0.03 | 0.08 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.10% | 46% | -4.73% | -4.94% | -1.22 | 14 | 99% |
| out_of_sample | 628 | -0.14% | 46% | -4.70% | -4.73% | -1.44 | 14 | 100% |
| in_sample | 1768 | -0.08% | 46% | -4.73% | -4.94% | -1.06 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.193% | 52% | 4.10 | +39.44% |
| bull | 687 | 28% | +0.049% | 50% | 2.07 | +39.18% |
| bear | 400 | 17% | +0.028% | 48% | 1.32 | +11.52% |
| chop | 1160 | 48% | -0.020% | 44% | -0.85 | -21.40% |

## Turnover, fees, activity

- trades: 5722 (2.36/day); active days 100%
- turnover 42.5x equity/year; fees 4.25% of equity/year ($19,676 total)
- average gross exposure 0.17; brake active 1.8% of hours
- correlation of daily returns with s3v2 baseline: 0.73
