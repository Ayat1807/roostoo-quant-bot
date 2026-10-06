# Run: b3_s3v2e_c4h_core10

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +155.54% | +15.18% | 1.01 | 1.49 | -19.52% | 0.78 | 1.13 |
| in_sample | 2020-02-15 → 2024-12-31 | +79.99% | +12.79% | 0.88 | 1.30 | -19.52% | 0.66 | 0.98 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +42.12% | +22.13% | 1.35 | 1.98 | -12.67% | 1.75 | 1.72 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +24.57% | +24.57% | 1.34 | 1.98 | -12.67% | 1.94 | 1.77 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.19% | 45% | -6.81% | -7.11% | -1.67 | 14 | 100% |
| out_of_sample | 628 | -0.15% | 47% | -5.79% | -6.18% | -0.78 | 14 | 100% |
| in_sample | 1768 | -0.20% | 44% | -6.81% | -7.11% | -1.91 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.235% | 58% | 3.06 | +48.44% |
| bull | 687 | 28% | +0.094% | 53% | 2.82 | +87.50% |
| bear | 400 | 17% | +0.043% | 47% | 1.27 | +17.99% |
| chop | 1160 | 48% | -0.016% | 43% | -0.40 | -19.94% |

## Turnover, fees, activity

- trades: 5047 (2.08/day); active days 100%
- turnover 40.3x equity/year; fees 4.03% of equity/year ($21,234 total)
- average gross exposure 0.18; brake active 9.8% of hours
- correlation of daily returns with s3v2 baseline: 0.99
