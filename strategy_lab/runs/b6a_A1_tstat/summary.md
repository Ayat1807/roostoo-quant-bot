# Run: b6a_A1_tstat

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'signal': 'tstat', 'tstat_cap': 2.0}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +193.25% | +17.59% | 1.62 | 2.34 | -9.45% | 1.86 | 1.98 |
| in_sample | 2020-02-15 → 2024-12-31 | +161.16% | +21.73% | 1.86 | 2.69 | -9.45% | 2.30 | 2.32 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +12.34% | +6.85% | 0.83 | 1.18 | -5.30% | 1.29 | 1.11 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +14.37% | +14.37% | 1.43 | 2.06 | -5.30% | 2.71 | 2.07 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.08% | 47% | -4.41% | -5.40% | -0.95 | 14 | 100% |
| out_of_sample | 628 | -0.17% | 38% | -3.43% | -4.82% | -2.20 | 14 | 100% |
| in_sample | 1768 | +0.02% | 50% | -4.41% | -5.40% | 0.17 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.210% | 56% | 3.63 | +43.03% |
| bull | 687 | 28% | +0.097% | 57% | 3.61 | +92.40% |
| bear | 400 | 17% | +0.026% | 52% | 1.35 | +10.53% |
| chop | 1160 | 48% | -0.002% | 46% | -0.08 | -3.09% |

## Turnover, fees, activity

- trades: 3585 (1.48/day); active days 100%
- turnover 9.6x equity/year; fees 0.96% of equity/year ($6,322 total)
- average gross exposure 0.13; brake active 0.8% of hours
- correlation of daily returns with s3v2 baseline: 0.72
