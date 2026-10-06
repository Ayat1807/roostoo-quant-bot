# Run: b3_regime_coreplusalt

Strategy `regime_switch`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10, 'base_tv': 0.6}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +127.05% | +13.14% | 0.56 | 0.80 | -52.73% | 0.25 | 0.56 |
| in_sample | 2020-02-15 → 2024-12-31 | +130.15% | +18.62% | 0.70 | 1.00 | -52.73% | 0.35 | 0.72 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -1.16% | -0.66% | 0.10 | 0.15 | -23.76% | -0.03 | 0.08 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +10.72% | +10.72% | 0.53 | 0.75 | -19.26% | 0.56 | 0.62 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.71% | 41% | -15.87% | -17.48% | -2.49 | 14 | 99% |
| out_of_sample | 628 | -0.62% | 42% | -11.89% | -13.09% | -1.71 | 14 | 100% |
| in_sample | 1768 | -0.70% | 41% | -15.87% | -17.48% | -2.57 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.352% | 51% | 2.63 | +75.44% |
| bull | 687 | 28% | +0.146% | 50% | 1.42 | +140.04% |
| bear | 400 | 17% | +0.023% | 48% | 0.36 | +6.42% |
| chop | 1160 | 48% | -0.045% | 44% | -0.59 | -47.20% |

## Turnover, fees, activity

- trades: 9311 (3.84/day); active days 100%
- turnover 110.7x equity/year; fees 11.07% of equity/year ($70,610 total)
- average gross exposure 0.35; brake active 38.8% of hours
- correlation of daily returns with s3v2 baseline: 0.60
