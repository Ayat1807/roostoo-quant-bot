# Run: b3_s3v2e_tv08_w04_coreplusalt

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.4, 'btc_pair': 'BTCUSDT', 'n_divisor': 10, 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +93.16% | +10.42% | 0.48 | 0.67 | -46.13% | 0.23 | 0.48 |
| in_sample | 2020-02-15 → 2024-12-31 | +60.07% | +10.12% | 0.46 | 0.64 | -45.11% | 0.22 | 0.46 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +21.70% | +11.82% | 0.56 | 0.80 | -20.48% | 0.58 | 0.66 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +30.60% | +30.60% | 1.17 | 1.70 | -17.32% | 1.77 | 1.56 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.87% | 42% | -19.06% | -20.11% | -2.26 | 14 | 96% |
| out_of_sample | 628 | -0.37% | 46% | -8.70% | -13.85% | -0.83 | 14 | 93% |
| in_sample | 1768 | -1.00% | 41% | -19.06% | -20.11% | -2.59 | 14 | 97% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.401% | 53% | 2.45 | +86.00% |
| bull | 687 | 28% | +0.157% | 53% | 1.96 | +171.09% |
| bear | 400 | 17% | +0.063% | 48% | 0.77 | +22.48% |
| chop | 1160 | 48% | -0.084% | 44% | -1.18 | -66.09% |

## Turnover, fees, activity

- trades: 10801 (4.46/day); active days 100%
- turnover 110.3x equity/year; fees 11.03% of equity/year ($57,033 total)
- average gross exposure 0.41; brake active 44.3% of hours
- correlation of daily returns with s3v2 baseline: 0.68
