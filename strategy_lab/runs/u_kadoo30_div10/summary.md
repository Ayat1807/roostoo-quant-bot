# Run: u_kadoo30_div10

Strategy `s3v2x`; universe `{'type': 'top_volume', 'n': 30, 'reselect': 'monthly', 'min_history_days': 60, 'min_quote_volume_usd': 5000000.0, 'rank_pool': 'all', 'trade': 'roostoo'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +140.31% | +14.12% | 0.94 | 1.35 | -22.97% | 0.61 | 1.01 |
| in_sample | 2020-02-15 → 2024-12-31 | +106.57% | +16.02% | 1.01 | 1.45 | -22.97% | 0.70 | 1.09 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +16.44% | +9.05% | 0.73 | 1.04 | -11.14% | 0.81 | 0.88 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +14.56% | +14.56% | 1.01 | 1.46 | -11.14% | 1.31 | 1.28 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.22% | 45% | -6.92% | -8.73% | -1.70 | 14 | 99% |
| out_of_sample | 628 | -0.19% | 47% | -4.92% | -6.13% | -1.18 | 14 | 100% |
| in_sample | 1768 | -0.22% | 44% | -6.92% | -8.73% | -1.92 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.228% | 53% | 3.07 | +46.65% |
| bull | 687 | 28% | +0.101% | 50% | 2.54 | +95.58% |
| bear | 400 | 17% | +0.026% | 48% | 0.76 | +10.13% |
| chop | 1160 | 48% | -0.021% | 44% | -0.61 | -23.61% |

## Turnover, fees, activity

- trades: 5675 (2.34/day); active days 100%
- turnover 52.0x equity/year; fees 5.20% of equity/year ($27,571 total)
- average gross exposure 0.22; brake active 10.5% of hours
- correlation of daily returns with s3v2 baseline: 0.77
