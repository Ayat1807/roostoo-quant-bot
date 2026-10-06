# Run: b3s_regime_coreplusalt_r4h

Strategy `regime_switch`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10, 'base_tv': 0.6}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +199.63% | +17.97% | 0.69 | 0.99 | -35.82% | 0.50 | 0.75 |
| in_sample | 2020-02-15 → 2024-12-31 | +169.40% | +22.51% | 0.79 | 1.14 | -35.82% | 0.63 | 0.88 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +11.24% | +6.25% | 0.36 | 0.52 | -20.42% | 0.31 | 0.41 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +21.13% | +21.13% | 0.84 | 1.25 | -16.09% | 1.31 | 1.14 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.52% | 43% | -16.03% | -18.36% | -1.55 | 14 | 98% |
| out_of_sample | 628 | -0.81% | 42% | -12.26% | -13.78% | -1.89 | 14 | 95% |
| in_sample | 1768 | -0.41% | 44% | -16.03% | -18.36% | -1.46 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.540% | 52% | 3.94 | +143.71% |
| bull | 687 | 28% | +0.096% | 46% | 0.95 | +70.91% |
| bear | 400 | 17% | +0.079% | 40% | 1.16 | +32.52% |
| chop | 1160 | 48% | -0.040% | 41% | -0.55 | -43.75% |

## Turnover, fees, activity

- trades: 14809 (6.11/day); active days 100%
- turnover 187.6x equity/year; fees 18.76% of equity/year ($144,339 total)
- average gross exposure 0.32; brake active 44.1% of hours
- correlation of daily returns with s3v2 baseline: 0.60
