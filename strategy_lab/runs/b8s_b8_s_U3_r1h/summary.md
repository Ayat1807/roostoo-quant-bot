# Run: b8s_b8_s_U3_r1h

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 30, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +74.88% | +8.78% | 0.67 | 0.99 | -24.54% | 0.36 | 0.71 |
| in_sample | 2020-02-15 → 2024-12-31 | +98.38% | +15.06% | 1.04 | 1.55 | -16.24% | 0.93 | 1.21 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -11.79% | -6.89% | -0.50 | -0.73 | -22.03% | -0.31 | -0.54 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -4.21% | -4.21% | -0.23 | -0.34 | -17.00% | -0.25 | -0.28 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.25% | 43% | -4.74% | -6.00% | -2.12 | 14 | 99% |
| out_of_sample | 628 | -0.81% | 34% | -4.74% | -5.38% | -4.74 | 14 | 100% |
| in_sample | 1768 | -0.14% | 46% | -4.62% | -6.00% | -1.14 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.324% | 53% | 4.61 | +73.94% |
| bull | 687 | 28% | +0.052% | 43% | 1.40 | +40.11% |
| bear | 400 | 17% | +0.049% | 42% | 1.49 | +20.60% |
| chop | 1160 | 48% | -0.043% | 38% | -1.27 | -40.41% |

## Turnover, fees, activity

- trades: 12911 (5.33/day); active days 100%
- turnover 140.1x equity/year; fees 14.01% of equity/year ($70,954 total)
- average gross exposure 0.20; brake active 10.3% of hours
- correlation of daily returns with s3v2 baseline: 0.66
