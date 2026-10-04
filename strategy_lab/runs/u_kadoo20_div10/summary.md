# Run: u_kadoo20_div10

Strategy `s3v2x`; universe `{'type': 'top_volume', 'n': 20, 'reselect': 'monthly', 'min_history_days': 60, 'min_quote_volume_usd': 5000000.0, 'rank_pool': 'all', 'trade': 'roostoo'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +127.71% | +13.19% | 0.90 | 1.30 | -19.04% | 0.69 | 1.00 |
| in_sample | 2020-02-15 → 2024-12-31 | +69.37% | +11.40% | 0.82 | 1.19 | -19.04% | 0.60 | 0.90 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +34.58% | +18.41% | 1.10 | 1.59 | -14.78% | 1.25 | 1.34 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +25.36% | +25.36% | 1.34 | 1.97 | -14.78% | 1.72 | 1.71 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.23% | 44% | -5.49% | -6.50% | -1.84 | 14 | 100% |
| out_of_sample | 628 | -0.31% | 46% | -5.37% | -6.32% | -1.62 | 14 | 100% |
| in_sample | 1768 | -0.19% | 44% | -5.49% | -6.50% | -1.81 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.223% | 55% | 2.74 | +44.92% |
| bull | 687 | 28% | +0.084% | 51% | 2.43 | +75.35% |
| bear | 400 | 17% | +0.038% | 48% | 1.00 | +15.02% |
| chop | 1160 | 48% | -0.019% | 45% | -0.56 | -21.78% |

## Turnover, fees, activity

- trades: 5588 (2.31/day); active days 100%
- turnover 52.2x equity/year; fees 5.22% of equity/year ($24,950 total)
- average gross exposure 0.21; brake active 11.6% of hours
- correlation of daily returns with s3v2 baseline: 0.81
