# Run: mft_breakout_top30_top3

Strategy `breakout`; universe `{'type': 'top_volume', 'n': 30, 'reselect': 'monthly', 'min_history_days': 60, 'min_quote_volume_usd': 5000000.0}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'top_k': 3}`; band 0.06; brake True; shorts False; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-05 | -100.00% | -82.00% | -1.84 | -2.62 | -100.00% | -0.82 | -1.84 |
| in_sample | 2020-02-15 → 2024-12-31 | -99.99% | -86.22% | -2.14 | -3.05 | -99.99% | -0.86 | -2.12 |
| out_of_sample | 2025-01-01 → 2026-10-05 | -82.13% | -62.42% | -0.97 | -1.37 | -89.78% | -0.70 | -1.05 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -75.62% | -75.62% | -1.42 | -1.99 | -85.69% | -0.88 | -1.49 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2411 | -8.28% | 28% | -35.66% | -37.81% | -4.26 | 14 | 53% |
| out_of_sample | 629 | -5.47% | 32% | -35.66% | -37.81% | -3.26 | 0 | 4% |
| in_sample | 1768 | -9.79% | 26% | -30.97% | -33.27% | -4.56 | 14 | 70% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.702% | 43% | 2.08 | +142.47% |
| bull | 687 | 28% | +0.024% | 44% | 0.11 | -34.32% |
| bear | 400 | 17% | -1.093% | 29% | -7.20 | -98.96% |
| chop | 1160 | 48% | -0.578% | 35% | -3.52 | -99.93% |

## Turnover, fees, activity

- trades: 28526 (11.76/day); active days 76%
- turnover 1447.8x equity/year; fees 144.78% of equity/year ($55,793 total)
- average gross exposure 0.55; brake active 55.3% of hours
- correlation of daily returns with s3v2 baseline: 0.08
