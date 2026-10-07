# Run: b4s_b4e_derisk_50_r1h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -56.06% | -11.65% | -0.16 | -0.22 | -91.68% | -0.13 | -0.17 |
| in_sample | 2020-02-15 → 2024-12-31 | +15.46% | +2.99% | 0.27 | 0.37 | -80.15% | 0.04 | 0.24 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -62.03% | -42.36% | -1.85 | -2.54 | -69.74% | -0.61 | -1.75 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -35.94% | -35.94% | -1.59 | -2.23 | -46.63% | -0.77 | -1.60 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -2.22% | 34% | -20.05% | -21.26% | -3.92 | 13 | 37% |
| out_of_sample | 628 | -3.17% | 24% | -13.01% | -13.78% | -5.79 | 13 | 30% |
| in_sample | 1768 | -1.77% | 38% | -20.05% | -21.26% | -3.10 | 13 | 40% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.784% | 51% | 4.65 | +261.97% |
| bull | 687 | 28% | +0.153% | 44% | 1.33 | +142.97% |
| bear | 400 | 17% | -0.284% | 31% | -4.43 | -68.88% |
| chop | 1160 | 48% | -0.148% | 31% | -2.08 | -83.94% |

## Turnover, fees, activity

- trades: 152926 (63.09/day); active days 86%
- turnover 540.8x equity/year; fees 54.08% of equity/year ($268,058 total)
- average gross exposure 0.29; brake active 53.5% of hours
- correlation of daily returns with s3v2 baseline: 0.36
