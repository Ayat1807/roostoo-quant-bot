# Run: mft_breakout_top20

Strategy `breakout`; universe `{'type': 'top_volume', 'n': 20, 'reselect': 'monthly', 'min_history_days': 60, 'min_quote_volume_usd': 5000000.0}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-05 | -8.37% | -1.31% | -0.62 | -0.85 | -11.06% | -0.12 | -0.56 |
| in_sample | 2020-02-15 → 2024-12-31 | -5.59% | -1.17% | -0.52 | -0.71 | -9.28% | -0.13 | -0.48 |
| out_of_sample | 2025-01-01 → 2026-10-05 | -2.95% | -1.68% | -1.03 | -1.39 | -5.05% | -0.33 | -0.96 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -1.52% | -1.52% | -0.90 | -1.20 | -3.22% | -0.47 | -0.89 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2411 | -0.13% | 33% | -0.99% | -1.30% | -5.07 | 13 | 37% |
| out_of_sample | 629 | -0.10% | 32% | -0.99% | -1.04% | -5.80 | 13 | 34% |
| in_sample | 1768 | -0.14% | 34% | -0.99% | -1.30% | -4.86 | 13 | 38% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.030% | 44% | 2.89 | +5.32% |
| bull | 687 | 28% | -0.001% | 41% | -0.19 | -0.91% |
| bear | 400 | 17% | -0.015% | 32% | -3.65 | -5.77% |
| chop | 1160 | 48% | -0.006% | 33% | -1.42 | -6.80% |

## Turnover, fees, activity

- trades: 2682 (1.11/day); active days 90%
- turnover 8.0x equity/year; fees 0.80% of equity/year ($2,534 total)
- average gross exposure 0.01; brake active 0.0% of hours
- correlation of daily returns with s3v2 baseline: 0.19
