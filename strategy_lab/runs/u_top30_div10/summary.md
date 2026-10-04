# Run: u_top30_div10

Strategy `s3v2x`; universe `{'type': 'top_volume', 'n': 30, 'reselect': 'monthly', 'min_history_days': 60, 'min_quote_volume_usd': 5000000.0}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +104.57% | +11.38% | 0.86 | 1.19 | -16.34% | 0.70 | 0.94 |
| in_sample | 2020-02-15 → 2024-12-31 | +83.16% | +13.20% | 0.93 | 1.27 | -16.34% | 0.81 | 1.03 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +11.79% | +6.55% | 0.66 | 0.94 | -9.75% | 0.67 | 0.78 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +8.92% | +8.92% | 0.87 | 1.25 | -9.75% | 0.91 | 1.04 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.19% | 44% | -7.78% | -11.21% | -1.50 | 14 | 100% |
| out_of_sample | 628 | -0.24% | 43% | -3.71% | -4.23% | -1.28 | 14 | 100% |
| in_sample | 1768 | -0.17% | 45% | -7.78% | -11.21% | -1.50 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.235% | 53% | 3.48 | +49.01% |
| bull | 687 | 28% | +0.087% | 52% | 2.10 | +77.94% |
| bear | 400 | 17% | +0.020% | 47% | 0.76 | +7.65% |
| chop | 1160 | 48% | -0.027% | 44% | -1.00 | -28.04% |

## Turnover, fees, activity

- trades: 5487 (2.26/day); active days 100%
- turnover 52.1x equity/year; fees 5.21% of equity/year ($26,147 total)
- average gross exposure 0.21; brake active 3.7% of hours
- correlation of daily returns with s3v2 baseline: 0.72
