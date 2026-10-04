# Run: u_top10

Strategy `s3v2`; universe `{'type': 'top_volume', 'n': 10, 'reselect': 'monthly', 'min_history_days': 60, 'min_quote_volume_usd': 5000000.0}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +94.89% | +10.57% | 0.84 | 1.22 | -14.18% | 0.75 | 0.96 |
| in_sample | 2020-02-15 → 2024-12-31 | +50.40% | +8.72% | 0.73 | 1.06 | -14.18% | 0.61 | 0.83 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +29.72% | +15.96% | 1.10 | 1.61 | -10.95% | 1.46 | 1.41 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +25.29% | +25.29% | 1.51 | 2.26 | -10.95% | 2.31 | 2.05 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.27% | 43% | -4.99% | -6.14% | -2.34 | 14 | 99% |
| out_of_sample | 628 | -0.35% | 44% | -4.99% | -5.55% | -2.24 | 14 | 100% |
| in_sample | 1768 | -0.25% | 43% | -4.41% | -6.14% | -2.27 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.216% | 52% | 2.90 | +43.59% |
| bull | 687 | 28% | +0.068% | 53% | 2.44 | +58.36% |
| bear | 400 | 17% | +0.036% | 46% | 1.21 | +14.91% |
| chop | 1160 | 48% | -0.022% | 43% | -0.73 | -24.47% |

## Turnover, fees, activity

- trades: 4887 (2.02/day); active days 100%
- turnover 43.3x equity/year; fees 4.33% of equity/year ($19,010 total)
- average gross exposure 0.18; brake active 6.2% of hours
- correlation of daily returns with s3v2 baseline: 0.81
