# Run: b8_h_U2

Strategy `s3v2x_regime`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 20, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +111.69% | +11.96% | 1.00 | 1.50 | -13.91% | 0.86 | 1.16 |
| in_sample | 2020-02-15 → 2024-12-31 | +93.36% | +14.46% | 1.16 | 1.76 | -13.91% | 1.04 | 1.36 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +9.59% | +5.35% | 0.52 | 0.75 | -10.65% | 0.50 | 0.61 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +4.83% | +4.83% | 0.45 | 0.66 | -10.65% | 0.45 | 0.53 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.13% | 45% | -5.29% | -6.19% | -1.41 | 14 | 99% |
| out_of_sample | 628 | -0.15% | 45% | -5.02% | -5.18% | -1.36 | 14 | 100% |
| in_sample | 1768 | -0.11% | 45% | -5.29% | -6.19% | -1.34 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.224% | 52% | 3.98 | +46.84% |
| bull | 687 | 28% | +0.059% | 50% | 2.17 | +49.08% |
| bear | 400 | 17% | +0.043% | 47% | 1.54 | +18.15% |
| chop | 1160 | 48% | -0.015% | 45% | -0.51 | -17.85% |

## Turnover, fees, activity

- trades: 6194 (2.56/day); active days 100%
- turnover 49.5x equity/year; fees 4.95% of equity/year ($24,968 total)
- average gross exposure 0.19; brake active 5.0% of hours
- correlation of daily returns with s3v2 baseline: 0.72
