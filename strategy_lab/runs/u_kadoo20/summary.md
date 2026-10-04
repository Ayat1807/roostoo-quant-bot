# Run: u_kadoo20

Strategy `s3v2`; universe `{'type': 'top_volume', 'n': 20, 'reselect': 'monthly', 'min_history_days': 60, 'min_quote_volume_usd': 5000000.0, 'rank_pool': 'all', 'trade': 'roostoo'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +78.97% | +9.16% | 0.94 | 1.35 | -13.40% | 0.68 | 1.03 |
| in_sample | 2020-02-15 → 2024-12-31 | +62.07% | +10.40% | 0.98 | 1.39 | -13.40% | 0.78 | 1.08 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +10.49% | +5.84% | 0.90 | 1.30 | -6.51% | 0.90 | 1.06 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +8.45% | +8.45% | 1.08 | 1.56 | -6.51% | 1.30 | 1.34 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.14% | 42% | -5.35% | -6.08% | -2.14 | 14 | 100% |
| out_of_sample | 628 | -0.14% | 40% | -3.15% | -4.72% | -2.80 | 14 | 100% |
| in_sample | 1768 | -0.13% | 43% | -5.35% | -6.08% | -1.72 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.177% | 54% | 3.31 | +35.38% |
| bull | 687 | 28% | +0.064% | 51% | 2.80 | +54.40% |
| bear | 400 | 17% | +0.006% | 47% | 0.34 | +2.18% |
| chop | 1160 | 48% | -0.013% | 42% | -0.63 | -15.15% |

## Turnover, fees, activity

- trades: 3990 (1.65/day); active days 100%
- turnover 25.5x equity/year; fees 2.55% of equity/year ($11,743 total)
- average gross exposure 0.12; brake active 1.7% of hours
- correlation of daily returns with s3v2 baseline: 0.75
