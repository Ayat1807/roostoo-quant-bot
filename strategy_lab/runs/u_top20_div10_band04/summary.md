# Run: u_top20_div10_band04

Strategy `s3v2x`; universe `{'type': 'top_volume', 'n': 20, 'reselect': 'monthly', 'min_history_days': 60, 'min_quote_volume_usd': 5000000.0}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10}`; band 0.04; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +112.19% | +12.00% | 0.59 | 0.84 | -29.70% | 0.40 | 0.63 |
| in_sample | 2020-02-15 → 2024-12-31 | +110.15% | +16.43% | 0.75 | 1.06 | -29.70% | 0.55 | 0.82 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +1.08% | +0.61% | 0.14 | 0.20 | -24.10% | 0.03 | 0.13 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +15.26% | +15.26% | 0.71 | 1.03 | -22.37% | 0.68 | 0.83 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.42% | 43% | -13.00% | -15.08% | -1.76 | 14 | 99% |
| out_of_sample | 628 | -0.92% | 40% | -10.38% | -12.74% | -2.77 | 14 | 98% |
| in_sample | 1768 | -0.32% | 44% | -13.00% | -15.08% | -1.41 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.317% | 51% | 2.71 | +67.28% |
| bull | 687 | 28% | +0.082% | 50% | 1.45 | +69.06% |
| bear | 400 | 17% | +0.052% | 48% | 0.81 | +19.63% |
| chop | 1160 | 48% | -0.034% | 44% | -0.56 | -37.02% |

## Turnover, fees, activity

- trades: 10911 (4.50/day); active days 100%
- turnover 81.6x equity/year; fees 8.16% of equity/year ($45,511 total)
- average gross exposure 0.30; brake active 32.2% of hours
- correlation of daily returns with s3v2 baseline: 0.81
