# Run: b11_news_rules

Strategy `s3v2x_fng`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'fng_high': 85, 'fng_low': 10, 'fng_mult': 0.8}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +170.17% | +16.15% | 1.08 | 1.59 | -16.32% | 0.99 | 1.26 |
| in_sample | 2020-02-15 → 2024-12-31 | +83.29% | +13.21% | 0.93 | 1.37 | -16.32% | 0.81 | 1.07 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +47.55% | +24.77% | 1.47 | 2.15 | -11.79% | 2.10 | 1.93 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +29.44% | +29.44% | 1.53 | 2.26 | -11.79% | 2.50 | 2.11 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.19% | 45% | -5.36% | -6.71% | -1.66 | 14 | 100% |
| out_of_sample | 628 | -0.16% | 46% | -4.96% | -6.71% | -1.21 | 14 | 100% |
| in_sample | 1768 | -0.18% | 45% | -5.36% | -6.69% | -1.81 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.245% | 59% | 3.13 | +51.05% |
| bull | 687 | 28% | +0.095% | 53% | 2.90 | +89.06% |
| bear | 400 | 17% | +0.037% | 46% | 1.23 | +15.37% |
| chop | 1160 | 48% | -0.012% | 44% | -0.28 | -15.63% |

## Turnover, fees, activity

- trades: 5112 (2.11/day); active days 100%
- turnover 40.9x equity/year; fees 4.09% of equity/year ($21,834 total)
- average gross exposure 0.18; brake active 9.1% of hours
- correlation of daily returns with s3v2 baseline: 0.84
