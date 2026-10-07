# Run: b6a_A2_ema_ens

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'signal': 'ema_ensemble'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +193.18% | +17.58% | 1.06 | 1.53 | -17.08% | 1.03 | 1.24 |
| in_sample | 2020-02-15 → 2024-12-31 | +116.11% | +17.10% | 1.04 | 1.51 | -17.08% | 1.00 | 1.22 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +35.85% | +19.04% | 1.12 | 1.61 | -10.86% | 1.75 | 1.51 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +25.56% | +25.56% | 1.29 | 1.89 | -10.86% | 2.35 | 1.85 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.31% | 42% | -7.58% | -8.74% | -2.04 | 14 | 100% |
| out_of_sample | 628 | -0.22% | 42% | -4.52% | -5.60% | -1.03 | 14 | 100% |
| in_sample | 1768 | -0.33% | 43% | -7.58% | -8.74% | -2.21 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.214% | 56% | 2.54 | +42.50% |
| bull | 687 | 28% | +0.112% | 54% | 2.66 | +111.17% |
| bear | 400 | 17% | +0.083% | 49% | 2.15 | +38.07% |
| chop | 1160 | 48% | -0.025% | 45% | -0.63 | -27.40% |

## Turnover, fees, activity

- trades: 4503 (1.86/day); active days 100%
- turnover 33.6x equity/year; fees 3.36% of equity/year ($20,198 total)
- average gross exposure 0.21; brake active 11.9% of hours
- correlation of daily returns with s3v2 baseline: 0.82
