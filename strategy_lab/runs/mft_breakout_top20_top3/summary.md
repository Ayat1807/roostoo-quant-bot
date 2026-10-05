# Run: mft_breakout_top20_top3

Strategy `breakout`; universe `{'type': 'top_volume', 'n': 20, 'reselect': 'monthly', 'min_history_days': 60, 'min_quote_volume_usd': 5000000.0}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'top_k': 3}`; band 0.06; brake True; shorts False; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-05 | -100.00% | -77.69% | -1.91 | -2.71 | -100.00% | -0.78 | -1.89 |
| in_sample | 2020-02-15 → 2024-12-31 | -99.96% | -80.39% | -1.90 | -2.70 | -99.98% | -0.80 | -1.89 |
| out_of_sample | 2025-01-01 → 2026-10-05 | -86.86% | -68.45% | -2.09 | -2.94 | -91.66% | -0.75 | -2.03 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -41.88% | -41.88% | -1.05 | -1.46 | -58.73% | -0.71 | -1.11 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2411 | -6.68% | 27% | -34.43% | -35.91% | -4.39 | 13 | 42% |
| out_of_sample | 629 | -3.80% | 29% | -23.29% | -26.80% | -4.01 | 9 | 8% |
| in_sample | 1768 | -7.98% | 27% | -34.43% | -35.91% | -4.47 | 14 | 54% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.626% | 41% | 2.22 | +135.50% |
| bull | 687 | 28% | -0.105% | 38% | -0.52 | -70.22% |
| bear | 400 | 17% | -0.926% | 28% | -6.50 | -97.92% |
| chop | 1160 | 48% | -0.459% | 32% | -3.38 | -99.67% |

## Turnover, fees, activity

- trades: 33083 (13.64/day); active days 82%
- turnover 1395.6x equity/year; fees 139.56% of equity/year ($106,668 total)
- average gross exposure 0.46; brake active 55.9% of hours
- correlation of daily returns with s3v2 baseline: 0.13
