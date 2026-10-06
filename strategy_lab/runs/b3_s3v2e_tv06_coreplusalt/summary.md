# Run: b3_s3v2e_tv06_coreplusalt

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.6, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10, 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +110.92% | +11.90% | 0.59 | 0.83 | -30.69% | 0.39 | 0.62 |
| in_sample | 2020-02-15 → 2024-12-31 | +75.26% | +12.18% | 0.59 | 0.83 | -30.69% | 0.40 | 0.63 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +20.41% | +11.14% | 0.57 | 0.82 | -19.55% | 0.57 | 0.67 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +17.47% | +17.47% | 0.80 | 1.15 | -19.55% | 0.89 | 0.97 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.52% | 43% | -10.25% | -12.39% | -1.96 | 14 | 97% |
| out_of_sample | 628 | -0.33% | 46% | -8.98% | -10.00% | -1.17 | 14 | 96% |
| in_sample | 1768 | -0.57% | 42% | -10.25% | -12.39% | -2.24 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.255% | 51% | 2.23 | +50.23% |
| bull | 687 | 28% | +0.124% | 51% | 1.98 | +123.53% |
| bear | 400 | 17% | +0.044% | 48% | 0.81 | +16.83% |
| chop | 1160 | 48% | -0.043% | 44% | -0.71 | -43.97% |

## Turnover, fees, activity

- trades: 8542 (3.52/day); active days 100%
- turnover 83.0x equity/year; fees 8.30% of equity/year ($42,809 total)
- average gross exposure 0.34; brake active 36.6% of hours
- correlation of daily returns with s3v2 baseline: 0.75
