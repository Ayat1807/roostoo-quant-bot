# Run: mft_breakout_top20_b01

Strategy `breakout`; universe `{'type': 'top_volume', 'n': 20, 'reselect': 'monthly', 'min_history_days': 60, 'min_quote_volume_usd': 5000000.0}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.01; brake True; shorts False; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-05 | -11.37% | -1.80% | -0.00 | -0.00 | -42.70% | -0.04 | -0.02 |
| in_sample | 2020-02-15 → 2024-12-31 | +0.89% | +0.18% | 0.11 | 0.14 | -40.24% | 0.00 | 0.09 |
| out_of_sample | 2025-01-01 → 2026-10-05 | -12.60% | -7.37% | -0.38 | -0.54 | -29.32% | -0.25 | -0.41 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -9.45% | -9.45% | -0.61 | -0.86 | -22.57% | -0.42 | -0.65 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2411 | -0.80% | 41% | -6.19% | -7.08% | -2.59 | 14 | 79% |
| out_of_sample | 629 | -1.31% | 35% | -6.04% | -6.74% | -5.34 | 14 | 97% |
| in_sample | 1768 | -0.64% | 43% | -6.19% | -7.08% | -2.01 | 14 | 72% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.446% | 51% | 4.75 | +112.97% |
| bull | 687 | 28% | +0.032% | 44% | 0.61 | +20.51% |
| bear | 400 | 17% | -0.155% | 28% | -3.98 | -46.75% |
| chop | 1160 | 48% | -0.034% | 36% | -0.81 | -34.97% |

## Turnover, fees, activity

- trades: 31915 (13.16/day); active days 97%
- turnover 100.3x equity/year; fees 10.03% of equity/year ($33,699 total)
- average gross exposure 0.17; brake active 32.3% of hours
- correlation of daily returns with s3v2 baseline: 0.26
