# Run: b6s_b6a_A3_bocpd05_c50_r2h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +146.25% | +14.54% | 1.08 | 1.66 | -14.88% | 0.98 | 1.28 |
| in_sample | 2020-02-15 → 2024-12-31 | +114.02% | +16.87% | 1.24 | 1.93 | -11.83% | 1.43 | 1.57 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +15.13% | +8.35% | 0.65 | 0.98 | -14.88% | 0.56 | 0.75 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +6.40% | +6.40% | 0.48 | 0.72 | -14.88% | 0.43 | 0.56 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.15% | 45% | -4.98% | -5.52% | -1.45 | 14 | 99% |
| out_of_sample | 628 | -0.41% | 39% | -4.98% | -5.33% | -2.73 | 14 | 100% |
| in_sample | 1768 | -0.06% | 48% | -4.86% | -5.52% | -0.64 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.336% | 54% | 5.17 | +78.10% |
| bull | 687 | 28% | +0.054% | 45% | 1.72 | +43.40% |
| bear | 400 | 17% | +0.054% | 40% | 1.60 | +23.18% |
| chop | 1160 | 48% | -0.016% | 38% | -0.39 | -19.44% |

## Turnover, fees, activity

- trades: 9404 (3.88/day); active days 100%
- turnover 87.4x equity/year; fees 8.74% of equity/year ($51,675 total)
- average gross exposure 0.16; brake active 6.9% of hours
- correlation of daily returns with s3v2 baseline: 0.73
