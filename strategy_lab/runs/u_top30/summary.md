# Run: u_top30

Strategy `s3v2`; universe `{'type': 'top_volume', 'n': 30, 'reselect': 'monthly', 'min_history_days': 60, 'min_quote_volume_usd': 5000000.0}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +23.14% | +3.18% | 0.78 | 1.11 | -6.64% | 0.48 | 0.82 |
| in_sample | 2020-02-15 → 2024-12-31 | +29.82% | +5.49% | 1.17 | 1.67 | -4.79% | 1.15 | 1.36 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -5.11% | -2.94% | -1.47 | -2.05 | -5.87% | -0.50 | -1.41 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -4.20% | -4.20% | -2.26 | -3.17 | -5.30% | -0.79 | -2.18 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.10% | 40% | -2.93% | -4.79% | -3.14 | 14 | 100% |
| out_of_sample | 628 | -0.17% | 30% | -1.72% | -1.72% | -6.49 | 14 | 100% |
| in_sample | 1768 | -0.06% | 44% | -2.93% | -4.79% | -1.73 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.074% | 57% | 3.04 | +13.66% |
| bull | 687 | 28% | +0.030% | 51% | 2.41 | +22.99% |
| bear | 400 | 17% | -0.001% | 46% | -0.15 | -0.54% |
| chop | 1160 | 48% | -0.009% | 42% | -1.14 | -10.31% |

## Turnover, fees, activity

- trades: 3136 (1.29/day); active days 100%
- turnover 14.7x equity/year; fees 1.47% of equity/year ($5,835 total)
- average gross exposure 0.06; brake active 0.2% of hours
- correlation of daily returns with s3v2 baseline: 0.61
