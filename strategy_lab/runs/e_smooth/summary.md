# Run: e_smooth

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'signal': 'tstat', 'tstat_cap': 2.0}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +173.01% | +17.05% | 1.48 | 2.12 | -10.97% | 1.55 | 1.76 |
| in_sample | 2020-02-15 → 2024-12-31 | +152.33% | +20.87% | 1.69 | 2.45 | -10.97% | 1.90 | 2.06 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +8.25% | +5.44% | 0.62 | 0.86 | -7.23% | 0.75 | 0.76 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +5.99% | +8.09% | 0.80 | 1.13 | -5.14% | 1.58 | 1.16 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.05% | 48% | -6.65% | -7.23% | -0.51 | 14 | 100% |
| out_of_sample | 532 | -0.14% | 39% | -3.53% | -4.94% | -1.91 | 14 | 100% |
| in_sample | 1768 | +0.02% | 51% | -6.65% | -7.23% | 0.29 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.151% | 55% | 2.63 | +27.91% |
| bull | 659 | 28% | +0.098% | 58% | 3.70 | +89.59% |
| bear | 399 | 17% | +0.032% | 53% | 1.49 | +13.29% |
| chop | 1099 | 47% | +0.001% | 45% | 0.04 | -0.10% |

## Turnover, fees, activity

- trades: 3534 (1.52/day); active days 100%
- turnover 10.8x equity/year; fees 1.08% of equity/year ($6,811 total)
- average gross exposure 0.14; brake active 1.0% of hours
- correlation of daily returns with s3v2 baseline: 0.71
