# Run: mft_breakout_top30

Strategy `breakout`; universe `{'type': 'top_volume', 'n': 30, 'reselect': 'monthly', 'min_history_days': 60, 'min_quote_volume_usd': 5000000.0}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-05 | -8.81% | -1.38% | -0.62 | -0.86 | -12.24% | -0.11 | -0.56 |
| in_sample | 2020-02-15 → 2024-12-31 | -4.91% | -1.03% | -0.43 | -0.60 | -9.24% | -0.11 | -0.40 |
| out_of_sample | 2025-01-01 → 2026-10-05 | -4.10% | -2.35% | -1.29 | -1.76 | -6.91% | -0.34 | -1.19 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -1.82% | -1.82% | -0.95 | -1.29 | -4.39% | -0.41 | -0.93 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2411 | -0.14% | 32% | -1.06% | -1.30% | -4.76 | 14 | 82% |
| out_of_sample | 629 | -0.15% | 27% | -1.06% | -1.09% | -6.38 | 14 | 83% |
| in_sample | 1768 | -0.14% | 34% | -0.90% | -1.30% | -4.23 | 14 | 81% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.035% | 53% | 3.31 | +6.23% |
| bull | 687 | 28% | +0.002% | 42% | 0.24 | +1.09% |
| bear | 400 | 17% | -0.017% | 36% | -3.69 | -6.75% |
| chop | 1160 | 48% | -0.008% | 36% | -1.81 | -8.92% |

## Turnover, fees, activity

- trades: 2874 (1.19/day); active days 97%
- turnover 8.3x equity/year; fees 0.83% of equity/year ($2,621 total)
- average gross exposure 0.01; brake active 0.0% of hours
- correlation of daily returns with s3v2 baseline: 0.17
