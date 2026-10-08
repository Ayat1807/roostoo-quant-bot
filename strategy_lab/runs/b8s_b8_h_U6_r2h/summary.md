# Run: b8s_b8_h_U6_r2h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'floor_breadth': 7, 'floor_gross': 0.5}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +145.58% | +14.49% | 0.77 | 1.13 | -24.80% | 0.58 | 0.86 |
| in_sample | 2020-02-15 → 2024-12-31 | +135.12% | +19.14% | 0.95 | 1.39 | -24.80% | 0.77 | 1.07 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +5.11% | +2.88% | 0.25 | 0.36 | -17.23% | 0.17 | 0.27 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +7.59% | +7.59% | 0.48 | 0.72 | -16.46% | 0.46 | 0.57 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.70% | 42% | -5.74% | -6.71% | -2.68 | 14 | 99% |
| out_of_sample | 628 | -0.93% | 38% | -4.99% | -6.10% | -3.40 | 14 | 100% |
| in_sample | 1768 | -0.59% | 43% | -5.74% | -6.71% | -2.33 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.539% | 53% | 5.24 | +149.42% |
| bull | 687 | 28% | +0.086% | 47% | 1.67 | +74.59% |
| bear | 400 | 17% | +0.014% | 41% | 0.29 | +3.90% |
| chop | 1160 | 48% | -0.045% | 37% | -0.87 | -43.96% |

## Turnover, fees, activity

- trades: 15221 (6.28/day); active days 100%
- turnover 140.6x equity/year; fees 14.06% of equity/year ($88,879 total)
- average gross exposure 0.23; brake active 30.6% of hours
- correlation of daily returns with s3v2 baseline: 0.78
