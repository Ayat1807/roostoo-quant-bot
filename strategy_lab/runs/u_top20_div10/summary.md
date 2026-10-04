# Run: u_top20_div10

Strategy `s3v2x`; universe `{'type': 'top_volume', 'n': 20, 'reselect': 'monthly', 'min_history_days': 60, 'min_quote_volume_usd': 5000000.0}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +120.29% | +12.63% | 0.85 | 1.19 | -18.02% | 0.70 | 0.94 |
| in_sample | 2020-02-15 → 2024-12-31 | +83.66% | +13.26% | 0.87 | 1.22 | -18.02% | 0.74 | 0.97 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +20.07% | +10.96% | 0.78 | 1.11 | -13.11% | 0.84 | 0.93 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +12.33% | +12.33% | 0.85 | 1.23 | -13.11% | 0.94 | 1.03 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.24% | 44% | -7.03% | -10.37% | -1.76 | 14 | 100% |
| out_of_sample | 628 | -0.30% | 45% | -5.42% | -6.14% | -1.69 | 14 | 100% |
| in_sample | 1768 | -0.20% | 44% | -7.03% | -10.37% | -1.71 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.232% | 53% | 3.08 | +47.78% |
| bull | 687 | 28% | +0.090% | 51% | 2.24 | +81.45% |
| bear | 400 | 17% | +0.018% | 46% | 0.51 | +6.48% |
| chop | 1160 | 48% | -0.020% | 45% | -0.59 | -22.53% |

## Turnover, fees, activity

- trades: 5701 (2.35/day); active days 100%
- turnover 55.2x equity/year; fees 5.52% of equity/year ($27,718 total)
- average gross exposure 0.22; brake active 10.9% of hours
- correlation of daily returns with s3v2 baseline: 0.78
