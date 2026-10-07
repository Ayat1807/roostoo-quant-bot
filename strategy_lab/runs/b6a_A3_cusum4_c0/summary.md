# Run: b6a_A3_cusum4_c0

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +94.81% | +10.56% | 0.88 | 1.31 | -19.99% | 0.53 | 0.95 |
| in_sample | 2020-02-15 → 2024-12-31 | +46.44% | +8.13% | 0.70 | 1.06 | -19.99% | 0.41 | 0.76 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +33.17% | +17.70% | 1.33 | 1.97 | -11.92% | 1.48 | 1.63 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +16.62% | +16.62% | 1.13 | 1.67 | -11.92% | 1.39 | 1.43 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.20% | 44% | -7.31% | -7.93% | -1.92 | 14 | 99% |
| out_of_sample | 628 | -0.14% | 47% | -5.25% | -5.60% | -1.04 | 14 | 100% |
| in_sample | 1768 | -0.20% | 43% | -7.31% | -7.93% | -2.30 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.233% | 53% | 3.95 | +48.93% |
| bull | 687 | 28% | +0.056% | 49% | 1.98 | +45.35% |
| bear | 400 | 17% | +0.040% | 46% | 1.38 | +16.69% |
| chop | 1160 | 48% | -0.018% | 42% | -0.48 | -20.82% |

## Turnover, fees, activity

- trades: 5161 (2.13/day); active days 100%
- turnover 44.7x equity/year; fees 4.47% of equity/year ($19,655 total)
- average gross exposure 0.15; brake active 6.2% of hours
- correlation of daily returns with s3v2 baseline: 0.76
