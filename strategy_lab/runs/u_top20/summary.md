# Run: u_top20

Strategy `s3v2`; universe `{'type': 'top_volume', 'n': 20, 'reselect': 'monthly', 'min_history_days': 60, 'min_quote_volume_usd': 5000000.0}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +28.27% | +3.82% | 0.76 | 1.11 | -8.15% | 0.47 | 0.81 |
| in_sample | 2020-02-15 → 2024-12-31 | +26.88% | +5.00% | 0.93 | 1.33 | -6.02% | 0.83 | 1.06 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +1.15% | +0.65% | 0.18 | 0.27 | -8.04% | 0.08 | 0.19 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +1.62% | +1.62% | 0.38 | 0.61 | -8.04% | 0.20 | 0.42 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.10% | 42% | -3.89% | -4.79% | -2.20 | 14 | 100% |
| out_of_sample | 628 | -0.15% | 35% | -2.17% | -2.19% | -3.57 | 14 | 100% |
| in_sample | 1768 | -0.08% | 44% | -3.89% | -4.79% | -1.61 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.126% | 55% | 3.83 | +24.30% |
| bull | 687 | 28% | +0.027% | 53% | 2.34 | +20.58% |
| bear | 400 | 17% | +0.000% | 46% | 0.04 | +0.11% |
| chop | 1160 | 48% | -0.012% | 42% | -1.11 | -13.43% |

## Turnover, fees, activity

- trades: 3279 (1.35/day); active days 100%
- turnover 17.6x equity/year; fees 1.76% of equity/year ($6,893 total)
- average gross exposure 0.08; brake active 0.2% of hours
- correlation of daily returns with s3v2 baseline: 0.71
