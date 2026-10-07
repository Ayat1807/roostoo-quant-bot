# Run: b6s_b6a_A3_cusum4_c50_r4h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +182.14% | +16.91% | 1.23 | 1.88 | -14.34% | 1.18 | 1.48 |
| in_sample | 2020-02-15 → 2024-12-31 | +120.05% | +17.53% | 1.29 | 1.98 | -14.34% | 1.22 | 1.55 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +28.31% | +15.23% | 1.08 | 1.63 | -13.74% | 1.11 | 1.31 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +13.17% | +13.17% | 0.87 | 1.32 | -13.74% | 0.96 | 1.08 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.13% | 46% | -5.45% | -6.06% | -0.99 | 14 | 99% |
| out_of_sample | 628 | -0.28% | 42% | -5.45% | -5.65% | -2.01 | 14 | 100% |
| in_sample | 1768 | -0.06% | 48% | -5.08% | -6.06% | -0.61 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.338% | 55% | 5.19 | +78.84% |
| bull | 687 | 28% | +0.067% | 46% | 2.20 | +56.60% |
| bear | 400 | 17% | +0.054% | 42% | 1.60 | +22.91% |
| chop | 1160 | 48% | -0.012% | 38% | -0.30 | -15.86% |

## Turnover, fees, activity

- trades: 8207 (3.39/day); active days 100%
- turnover 70.1x equity/year; fees 7.01% of equity/year ($41,462 total)
- average gross exposure 0.16; brake active 6.6% of hours
- correlation of daily returns with s3v2 baseline: 0.75
