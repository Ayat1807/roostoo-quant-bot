# Run: b3_s3v2e_coreplusalt

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10, 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +103.93% | +11.33% | 0.79 | 1.14 | -20.40% | 0.56 | 0.86 |
| in_sample | 2020-02-15 → 2024-12-31 | +76.03% | +12.28% | 0.85 | 1.22 | -20.40% | 0.60 | 0.92 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +15.98% | +8.80% | 0.65 | 0.94 | -13.77% | 0.64 | 0.76 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +15.72% | +15.72% | 0.96 | 1.39 | -13.77% | 1.14 | 1.19 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.30% | 42% | -6.51% | -9.03% | -2.52 | 14 | 100% |
| out_of_sample | 628 | -0.36% | 41% | -5.59% | -9.03% | -2.33 | 14 | 100% |
| in_sample | 1768 | -0.27% | 42% | -6.51% | -8.14% | -2.62 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.234% | 54% | 3.03 | +48.03% |
| bull | 687 | 28% | +0.090% | 48% | 2.35 | +81.69% |
| bear | 400 | 17% | +0.049% | 48% | 1.39 | +20.50% |
| chop | 1160 | 48% | -0.038% | 45% | -1.12 | -36.83% |

## Turnover, fees, activity

- trades: 5732 (2.36/day); active days 100%
- turnover 50.1x equity/year; fees 5.01% of equity/year ($24,477 total)
- average gross exposure 0.22; brake active 9.9% of hours
- correlation of daily returns with s3v2 baseline: 0.83
