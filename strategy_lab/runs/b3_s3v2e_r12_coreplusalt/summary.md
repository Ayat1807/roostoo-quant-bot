# Run: b3_s3v2e_r12_coreplusalt

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10, 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +230.73% | +19.74% | 1.23 | 1.80 | -19.79% | 1.00 | 1.39 |
| in_sample | 2020-02-15 → 2024-12-31 | +155.54% | +21.19% | 1.31 | 1.91 | -19.79% | 1.07 | 1.48 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +29.46% | +15.82% | 1.02 | 1.48 | -13.48% | 1.17 | 1.25 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +26.39% | +26.39% | 1.42 | 2.09 | -13.48% | 1.96 | 1.85 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.17% | 45% | -5.66% | -6.84% | -1.25 | 14 | 100% |
| out_of_sample | 628 | -0.34% | 44% | -5.65% | -5.82% | -1.78 | 14 | 100% |
| in_sample | 1768 | -0.12% | 46% | -5.66% | -6.84% | -1.02 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.337% | 54% | 4.33 | +77.51% |
| bull | 687 | 28% | +0.101% | 48% | 2.47 | +96.57% |
| bear | 400 | 17% | +0.073% | 46% | 1.98 | +32.51% |
| chop | 1160 | 48% | -0.027% | 44% | -0.76 | -28.40% |

## Turnover, fees, activity

- trades: 6737 (2.78/day); active days 100%
- turnover 67.0x equity/year; fees 6.70% of equity/year ($41,822 total)
- average gross exposure 0.22; brake active 11.8% of hours
- correlation of daily returns with s3v2 baseline: 0.81
