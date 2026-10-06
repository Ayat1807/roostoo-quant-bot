# Run: b3s_regime_coreplusalt_r6h

Strategy `regime_switch`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10, 'base_tv': 0.6}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +235.36% | +19.99% | 0.75 | 1.08 | -42.33% | 0.47 | 0.80 |
| in_sample | 2020-02-15 → 2024-12-31 | +194.28% | +24.74% | 0.85 | 1.23 | -42.33% | 0.58 | 0.92 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +13.99% | +7.74% | 0.41 | 0.60 | -21.54% | 0.36 | 0.47 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +14.54% | +14.54% | 0.64 | 0.95 | -19.71% | 0.74 | 0.79 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.80% | 43% | -15.69% | -16.78% | -2.60 | 14 | 97% |
| out_of_sample | 628 | -1.08% | 39% | -13.22% | -14.57% | -3.01 | 14 | 95% |
| in_sample | 1768 | -0.62% | 44% | -15.69% | -16.78% | -2.38 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.623% | 57% | 4.61 | +182.25% |
| bull | 687 | 28% | +0.136% | 48% | 1.33 | +124.19% |
| bear | 400 | 17% | +0.035% | 43% | 0.56 | +11.92% |
| chop | 1160 | 48% | -0.052% | 38% | -0.70 | -50.92% |

## Turnover, fees, activity

- trades: 13218 (5.45/day); active days 100%
- turnover 166.1x equity/year; fees 16.61% of equity/year ($138,265 total)
- average gross exposure 0.33; brake active 43.9% of hours
- correlation of daily returns with s3v2 baseline: 0.61
