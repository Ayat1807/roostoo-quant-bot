# Run: b3_s3v2e_tranched_coreplusalt

Strategy `s3v2_tranched`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10, 'vol_method': 'ewma', 'ewma_halflife': 168, 'tranches': 4, 'spacing_bars': 6}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +156.22% | +15.22% | 1.00 | 1.40 | -15.90% | 0.96 | 1.15 |
| in_sample | 2020-02-15 → 2024-12-31 | +123.18% | +17.87% | 1.11 | 1.55 | -15.90% | 1.12 | 1.29 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +14.90% | +8.22% | 0.65 | 0.92 | -12.33% | 0.67 | 0.77 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +11.86% | +11.86% | 0.83 | 1.19 | -12.33% | 0.96 | 1.02 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.25% | 44% | -7.71% | -8.06% | -1.53 | 14 | 100% |
| out_of_sample | 628 | -0.42% | 41% | -4.86% | -5.51% | -2.45 | 14 | 100% |
| in_sample | 1768 | -0.18% | 45% | -7.71% | -8.06% | -1.12 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.174% | 57% | 2.29 | +33.31% |
| bull | 687 | 28% | +0.125% | 54% | 3.14 | +131.79% |
| bear | 400 | 17% | +0.034% | 49% | 1.03 | +13.87% |
| chop | 1160 | 48% | -0.025% | 44% | -0.82 | -26.93% |

## Turnover, fees, activity

- trades: 5423 (2.24/day); active days 100%
- turnover 34.4x equity/year; fees 3.44% of equity/year ($21,179 total)
- average gross exposure 0.23; brake active 9.7% of hours
- correlation of daily returns with s3v2 baseline: 0.79
