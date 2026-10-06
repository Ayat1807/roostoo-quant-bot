# Run: b3_regime_cons_coreplusalt

Strategy `regime_switch`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10, 'base_tv': 0.4}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +84.67% | +9.68% | 0.48 | 0.70 | -42.82% | 0.23 | 0.49 |
| in_sample | 2020-02-15 → 2024-12-31 | +120.25% | +17.56% | 0.72 | 1.04 | -42.82% | 0.41 | 0.75 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -16.01% | -9.45% | -0.36 | -0.52 | -26.88% | -0.35 | -0.42 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +0.46% | +0.46% | 0.13 | 0.19 | -16.51% | 0.03 | 0.12 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.70% | 38% | -15.52% | -16.73% | -3.77 | 14 | 99% |
| out_of_sample | 628 | -0.93% | 30% | -11.46% | -12.70% | -4.32 | 14 | 100% |
| in_sample | 1768 | -0.58% | 40% | -15.52% | -16.73% | -3.39 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.347% | 52% | 2.79 | +75.40% |
| bull | 687 | 28% | +0.115% | 46% | 1.26 | +99.17% |
| bear | 400 | 17% | +0.037% | 47% | 0.69 | +13.70% |
| chop | 1160 | 48% | -0.059% | 42% | -1.01 | -53.33% |

## Turnover, fees, activity

- trades: 7215 (2.98/day); active days 100%
- turnover 86.9x equity/year; fees 8.69% of equity/year ($48,559 total)
- average gross exposure 0.26; brake active 23.6% of hours
- correlation of daily returns with s3v2 baseline: 0.53
